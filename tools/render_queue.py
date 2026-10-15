"""Render queued card specs into JPEGs. Run by .github/workflows/render-cards.yml.

Each queue/*.json is a brand_cards.py spec plus:
  "out": "media-mentions/<YYYY-MM-DD_pub_topic>.jpg"   (required)
  "photo_drive_id": "<Google Drive file id>"            (photo layouts only; the file
                                                          must be shared "Anyone with the link")
Rendered images are written to "out" and the spec is deleted.

Content Mill scheduler jobs (a different robot) are queue/cm_*.json files shaped:
  {"fetch_url": "https://export-download.canva.com/...",
   "out": "media-mentions/content-mill/cm_<Post ID>_<YYYYMMDDHH>.png"}
They are handled first and separately: the Canva PNG is saved to "out" as-is and the job is
deleted. A failed Content Mill job is reported and deleted but NEVER fails the run, so it can't
block media-mention cards.
"""
import glob, json, os, re, subprocess, sys, tempfile, urllib.parse, urllib.request
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
done = []
specs = sorted(glob.glob(os.path.join(ROOT, "queue", "*.json")))

# --- Content Mill fetch jobs (isolated; never exit) ---
media_specs = []
for path in specs:
    try:
        spec = json.load(open(path))
    except Exception:
        spec = None
    if not (isinstance(spec, dict) and "fetch_url" in spec):
        media_specs.append(path)
        continue
    try:
        url, out = spec["fetch_url"], spec["out"]
        if urllib.parse.urlparse(url).hostname != "export-download.canva.com":
            raise ValueError("fetch_url must be a Canva export link")
        if not re.fullmatch(r"media-mentions/content-mill/cm_[A-Za-z0-9._-]+\.png", out):
            raise ValueError(f"bad out path {out!r}")
        data = urllib.request.urlopen(url, timeout=60).read()
        if not data.startswith(b"\x89PNG\r\n\x1a\n"):
            raise ValueError("Canva link did not return a PNG (expired?)")
        dest = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(data)
        done.append(out)
    except Exception as e:
        print(f"CONTENT MILL FETCH FAILED {os.path.basename(path)}: {e}")
    os.remove(path)

# --- Media-mention cards (unchanged behavior) ---
for path in media_specs:
    spec = json.load(open(path))
    out = spec.pop("out")
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
