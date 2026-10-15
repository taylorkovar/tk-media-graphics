"""Download queued Canva exports into permanent repo files. Run by .github/workflows/fetch-images.yml.

Each fetch-queue/*.json is:
  {"url": "https://export-download.canva.com/...", "out": "content-mill/<Post ID>.png"}
The image is saved to "out" and the queue file is deleted. Served at
https://raw.githubusercontent.com/taylorkovar/tk-media-graphics/main/<out>
"""
import glob, json, os, re, sys, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PNG = b"\x89PNG\r\n\x1a\n"
failed = False
for path in sorted(glob.glob(os.path.join(ROOT, "fetch-queue", "*.json"))):
    try:
        job = json.load(open(path))
        url, out = job["url"], job["out"]
        if urllib.parse.urlparse(url).hostname != "export-download.canva.com":
            raise ValueError(f"url must be a Canva export link: {url[:80]}")
        if not re.fullmatch(r"content-mill/[A-Za-z0-9._-]+\.png", out):
            raise ValueError(f"bad out path {out!r}")
        data = urllib.request.urlopen(url, timeout=60).read()
        if not data.startswith(PNG):
            raise ValueError("download is not a PNG (link expired?)")
        dest = os.path.join(ROOT, out)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(data)
        print("saved", out, len(data), "bytes")
    except Exception as e:
        failed = True
        print(f"FAILED {os.path.basename(path)}: {e}")
    os.remove(path)
sys.exit(1 if failed else 0)
