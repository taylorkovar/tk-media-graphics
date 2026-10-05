"""Taylor Kovar brand media cards (1080x1350, 4:5) in the TK palette with Josefin Sans.

Usage: python3 brand_cards.py spec.json out.jpg

Every spec needs "layout" and "publication". Layouts and their fields:
  statement   kicker (small caps line), lines [..], accent [..]          dark Oxford, big type
  number      number ("$2M", "43%"), sub [..]                            light Mist, giant figure
  question    lines [..], accent [..], answer                            Glacier top / Oxford band
  quote       quote (Taylor's own words from the article, <= 25 words)   Mist, oversized quote mark
  photo       photo (path), focus [x,y], lines [..], accent [..]         photo top, Oxford panel below
  photo_full  photo (path), focus [x,y], lines [..], accent [..]         full-bleed photo, gradient, text bottom
Optional: "theme_flip": true swaps light/dark on statement/number/quote for variety.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "..", "fonts", "Josefin{}.ttf")
W, H = 1080, 1350
M = 96
OXFORD = (54, 65, 87)      # #364157
GLACIER = (97, 119, 156)   # #61779C
HAZE = (171, 180, 183)     # #ABB4B7
WHITE = (255, 255, 255)
MIST = (238, 240, 242)
CREDIT_Y = H - 160


def font(weight, size):
    return ImageFont.truetype(F.format(weight), size)


def fit(draw, lines, weight, max_w, max_h, leading=1.02, start=260, min_size=36):
    """Largest size where every line fits max_w and the stack fits max_h."""
    for s in range(start, min_size, -2):
        f = font(weight, s)
        if all(draw.textlength(t, font=f) <= max_w for t in lines) and s * leading * len(lines) <= max_h:
            return f, s
    return font(weight, min_size), min_size


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def tracked(draw, xy, text, f, fill, tr):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + f.size * tr
    return x


def tracked_len(draw, text, f, tr):
    return sum(draw.textlength(c, font=f) for c in text) + f.size * tr * (len(text) - 1)


def stack(draw, x, y, lines, f, fill, leading=1.02, accent=(), accent_fill=None):
    for t in lines:
        top = f.getbbox(t)[1]
        draw.text((x, y - top), t, font=f, fill=accent_fill if t in accent else fill)
        y += int(f.size * leading)
    return y


def credit(draw, pub, fg, rule):
    draw.line([M, CREDIT_Y, W - M, CREDIT_Y], fill=rule, width=2)
    f = font(600, 26)
    tracked(draw, (M, CREDIT_Y + 34), "TAYLOR KOVAR, CFP®", f, fg, 0.12)
    right = f"AS QUOTED IN {pub.upper()}"
    # shrink if a long publication name would collide
    while tracked_len(draw, right, f, 0.12) > (W - 2 * M) * 0.55 and f.size > 18:
        f = font(600, f.size - 1)
    tracked(draw, (W - M - tracked_len(draw, right, f, 0.12), CREDIT_Y + 34), right, f, fg, 0.12)


def palette(spec, dark_default):
    dark = dark_default != bool(spec.get("theme_flip"))
    return (OXFORD, WHITE, HAZE, GLACIER) if dark else (MIST, OXFORD, GLACIER, HAZE)


def statement(spec):
    bg, fg, acc, rule = palette(spec, True)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    top = 300
    if spec.get("kicker"):
        tracked(d, (M, 120), spec["kicker"].upper(), font(600, 28), acc, 0.2)
        d.rectangle([M, 175, M + 90, 181], fill=rule if bg == OXFORD else GLACIER)
    else:
        top = 200
    avail = CREDIT_Y - 80 - top
    f, s = fit(d, spec["lines"], 700, W - 2 * M, avail, start=230)
    y = top + (avail - int(s * 1.02 * len(spec["lines"]))) // 2
    stack(d, M, y, spec["lines"], f, fg, accent=spec.get("accent", []), accent_fill=acc)
    credit(d, spec["publication"], fg, rule)
    return img


def number(spec):
    bg, fg, acc, rule = palette(spec, False)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    big = spec["number"]
    f, s = fit(d, [big], 700, W - 2 * M, 520, start=520)
    bb = f.getbbox(big)
    d.text((M - 8, 170 - bb[1]), big, font=f, fill=fg)
    y = 170 + (bb[3] - bb[1]) + 50
    d.rectangle([M, y, M + 160, y + 10], fill=GLACIER if bg == MIST else HAZE)
    y += 70
    f2, _ = fit(d, spec["sub"], 300, W - 2 * M, CREDIT_Y - 60 - y, leading=1.15, start=96)
    stack(d, M, y, spec["sub"], f2, fg, leading=1.15)
    credit(d, spec["publication"], fg, rule)
    return img


def question(spec):
    img = Image.new("RGB", (W, H), GLACIER)
    d = ImageDraw.Draw(img)
    band = int(H * 0.68)
    d.rectangle([0, band, W, H], fill=OXFORD)
    f, s = fit(d, spec["lines"], 700, W - 2 * M, band - 160, leading=1.0, start=200)
    y = (band - int(s * len(spec["lines"]))) // 2 + 20
    stack(d, M, y, spec["lines"], f, WHITE, leading=1.0, accent=spec.get("accent", []), accent_fill=OXFORD)
    if spec.get("answer"):
        d.text((M, band + 70), spec["answer"], font=font(300, 52), fill=WHITE)
    credit(d, spec["publication"], HAZE, GLACIER)
    return img


def quote(spec):
    bg, fg, acc, rule = palette(spec, False)
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    d.text((M - 10, 40), "“", font=font(700, 420), fill=GLACIER)
    box_top, box_h = 400, CREDIT_Y - 120 - 400
    for s in range(96, 40, -2):
        f = font(400, s)
        lines = wrap(d, spec["quote"], f, W - 2 * M)
        if s * 1.25 * len(lines) <= box_h:
            break
    stack(d, M, box_top, lines, f, fg, leading=1.25)
    tracked(d, (M, CREDIT_Y - 70), "— TAYLOR KOVAR", font(600, 30), acc, 0.15)
    credit(d, spec["publication"], fg, rule)
    return img


def place_photo(spec, w, h):
    src = Image.open(spec["photo"]).convert("RGB")
    fx, fy = spec.get("focus", [0.5, 0.4])
    scale = max(w / src.width, h / src.height)
    src = src.resize((int(src.width * scale) + 1, int(src.height * scale) + 1), Image.LANCZOS)
    left = min(max(int(src.width * fx - w / 2), 0), src.width - w)
    top = min(max(int(src.height * fy - h / 2), 0), src.height - h)
    return src.crop((left, top, left + w, top + h))


def photo(spec):
    img = Image.new("RGB", (W, H), OXFORD)
    d = ImageDraw.Draw(img)
    ph_h = int(H * spec.get("photo_share", 0.5))
    img.paste(place_photo(spec, W, ph_h), (0, 0))
    d.rectangle([0, ph_h, W, ph_h + 10], fill=GLACIER)
    avail = CREDIT_Y - 60 - (ph_h + 70)
    f, s = fit(d, spec["lines"], 700, W - 2 * M, avail, start=150)
    y = ph_h + 70 + (avail - int(s * 1.02 * len(spec["lines"]))) // 2
    stack(d, M, y, spec["lines"], f, WHITE, accent=spec.get("accent", []), accent_fill=HAZE)
    credit(d, spec["publication"], WHITE, GLACIER)
    return img


def photo_full(spec):
    img = place_photo(spec, W, H)
    grad = Image.new("L", (1, H))
    start = int(H * 0.38)
    for y in range(H):
        grad.putpixel((0, y), 0 if y < start else min(235, int(235 * (y - start) / (H * 0.32))))
    overlay = Image.new("RGB", (W, H), OXFORD)
    img = Image.composite(overlay, img, grad.resize((W, H)))
    d = ImageDraw.Draw(img)
    avail = 420
    f, s = fit(d, spec["lines"], 700, W - 2 * M, avail, start=140)
    y = CREDIT_Y - 60 - int(s * 1.02 * len(spec["lines"]))
    stack(d, M, y, spec["lines"], f, WHITE, accent=spec.get("accent", []), accent_fill=HAZE)
    credit(d, spec["publication"], WHITE, HAZE)
    return img


LAYOUTS = {"statement": statement, "number": number, "question": question,
           "quote": quote, "photo": photo, "photo_full": photo_full}

if __name__ == "__main__":
    spec = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    im = LAYOUTS[spec["layout"]](spec).convert("RGB")
    if out.lower().endswith((".jpg", ".jpeg")):
        im.save(out, quality=88, optimize=True, progressive=True)
    else:
        im.save(out)
    print("saved", out)
