"""Render queued card specs into JPEGs. Run by .github/workflows/render-cards.yml.

Each queue/*.json is a brand_cards.py spec plus:
  "out": "media-mentions/<YYYY-MM-DD_pub_topic>.jpg"   (required)
  "photo_drive_id": "<Google Drive file id>"            (photo layouts only; the file
                                                          must be shared "Anyone with the link")
Rendered images are written to "out" and the spec is deleted.

Content Mill scheduler jobs are instead:
  {"fetch_url": "https://export-download.canva.com/...", "out": "media-mentions/cm_<Post ID>.png"}
The Canva export is downloaded as-is to "out" (a permanent link for HighLevel) and the job is deleted.
"""
import glob, json, os, re, subprocess, sys, tempfile, urllib.parse, urllib.request
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
done = []
for path in sorted(glob.glob(os.path.join(ROOT, "queue", "*.json"))):
    spec = json.load(open(path))
    out = spec.pop("out")
    if "fetch_url" in spec:
        url = spec["fetch_url"]
        if urllib.parse.urlparse(url).hostname != "export-download.canva.com":
            sys.exit(f"{path}: fetch_url must be a Canva export link")
        if not re.fullmatch(r"media-mentions/cm_[A-Za-z0-9._-]+\.png", out):
            sys.exit(f"{path}: bad out path {out!r}")
        data = urllib.request.urlopen(url, timeout=60).read()
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            sys.exit(f"{path}: Canva link did not return a PNG (expired?)")
        open(os.path.join(ROOT, out), "wb").write(data)
        os.remove(path)
        done.append(out)
        continue
    if not re.fullmatch(r"media-mentions/[A-Za-z0-9._-]+\.jpg", out):
        sys.exit(f"{path}: bad out path {out!r}")
    fid = spec.pop("photo_drive_id", None)
    if fid:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", fid):
            sys.exit(f"{path}: bad photo_drive_id")
        raw = tempfile.mktemp(suffix=".img")
        urllib.request.urlretrieve(
            f"https://drive.usercontent.google.com/download?id={fid}&export=download&confirm=t", raw)
        try:
            im = ImageOps.exif_transpose(Image.open(raw)).convert("RGB")
        except Exception:
            sys.exit(f"{path}: Drive file {fid} did not download as an image (is it shared 'Anyone with the link'?)")
        spec["photo"] = raw + ".jpg"
        im.save(spec["photo"], quality=95)
    elif spec.get("layout", "").startswith("photo"):
        sys.exit(f"{path}: photo layout needs photo_drive_id")
    tmp_spec = tempfile.mktemp(suffix=".json")
    json.dump(spec, open(tmp_spec, "w"))
    subprocess.run([sys.executable, os.path.join(ROOT, "tools", "brand_cards.py"), tmp_spec,
                    os.path.join(ROOT, out)], check=True)
    os.remove(path)
    done.append(out)
print("rendered:", *done, sep="\n  ")
