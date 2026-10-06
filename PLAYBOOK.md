# TK Media Mentions — Daily Playbook

Daily job that turns Taylor Kovar's press mentions into social posts for human approval.
Every run does two things:
1. **New mentions:** anything on https://choose11.com/in-the-press/ that isn't in the tracker yet (may be zero).
2. **One throwback:** the next older mention in the tracker that hasn't been posted.

Posts go to GoHighLevel as *in review* for Claudia. Nothing publishes without her approval.

---

## Systems and IDs

| What | Value |
|---|---|
| Tracker | Google Sheet `11ciDQwCe5M3Z_lotkvX49N91e0Y8NEdoCy-RCiJYmfI`, tab **Media Mentions** (row 1 = headers, newest at top) |
| GHL location | TaylorKovar.com `CoD1jBJnfOnS8iAmntku` |
| GHL userId (creator) | Taylor Kovar `0owaLTQF7YTV3EFV8N9c` |
| GHL approver | Claudia Valladares `3nS0t3FsisxjJ3uDiKhI` |
| Image hosting | this repo; public URL = `https://raw.githubusercontent.com/taylorkovar/tk-media-graphics/main/<path>` |
| Graphic builder | `tools/brand_cards.py` (fonts in `fonts/`) |
| Run history | `log.json` in this repo (layouts, photos, rows done). Read it first, append to it, push it. |

**GHL account IDs**
- Facebook page: `67055050817f4e032ecbff41_CoD1jBJnfOnS8iAmntku_415562988306103_page`
- Instagram: `67a6783b6bb1fdb083e36b8d_CoD1jBJnfOnS8iAmntku_17841402976402496`
- LinkedIn profile: `67a678600c011c4450eb74a3_CoD1jBJnfOnS8iAmntku_OlhS_xldVM_profile`
- LinkedIn page: `67055081e689400600e949a9_CoD1jBJnfOnS8iAmntku_107872485_page`
- Threads: `6aac4159cd1cd4d29e3dec4d_CoD1jBJnfOnS8iAmntku_28733261506363980_profile`
- TikTok and YouTube are video-only. Skip them. X is not connected.

**Tracker columns: always find them by header name, never by letter.** The team rearranges this sheet. At the start of every run, read row 1 and map each header to its column letter. If a header below is missing, stop and report it instead of guessing.

Layout as of 10/5/2026, for reference only:
A Article Date (MM/DD/YYYY) · B Publication · C Title · D Link · E Author · F Author FB · G Author Insta · H Author X · I Author LinkedIn · **J Status** · K FB/Insta/LinkedIn Caption · L Threads/X Caption · M Reel Script · N Graphic Link · O Video Link · P Date Image Posted · Q Date Reel Posted.

- Never touch Video Link, Date Image Posted, or Date Reel Posted. The team fills those.
- **Never overwrite a cell that already has content.** The team or other tools may have filled captions, scripts, or handles. If a caption cell is already filled, use that text for the post as-is (lightly fix only obvious typos). Fill only empty cells.
- In the text below, "Status", "Main caption" (FB/Insta/LinkedIn Caption), "Threads caption", "Reel Script", and "Graphic Link" refer to those headers.

**Photo folders (Google Drive)** — image files only (ignore videos). Prefer files under ~6 MB.
- TK Solo Pics `1bFJydk2E3CEZl8IUzysdT6FhvBDvgdcD` (main source)
- Event Pictures `1oYEqGqYFq8EOnh3nK7cQJuLBCoGcgulX` (speaking, stage)
- Tay & Meg Pics `1-PMuvxkO8JrE2Tw9gOzNj9li-mjNSo4Q` (only for couples / marriage-and-money topics)
- Other subfolders of `TK.com Pics & Vids` (parent `190Up7yXQFmWGilkZtwXY3yIIid_gJNhK`) such as BTS, Kovar Travels and Old Biz Pics are fine. Casual, behind-the-scenes shots are welcome. **Never use Kovar Kids or Fam Pics.**

---

## Step 1 — New mentions
1. Fetch the press page. Each entry shows `logo-alt-text - MM/DD/YYYY Title` linking to the article.
2. Compare links against the Link column. Anything new gets a **new row inserted at row 2** (keep newest at top), filling Article Date, Publication (clean name: "AOL", "GOBankingRates", "Yahoo Finance"...), Title, and Link.
3. Process it (Step 3). Schedule it for **9:00 AM America/Chicago the next day**.

## Step 2 — One throwback
1. Find the topmost row (row 3 and down) where **Status is empty**.
2. Open the link.
   - Dead (404, removed, paywalled to nothing): set Status = `Skipped - dead link` and try the next row.
   - Too dated to repost (a specific past tax year, stimulus checks, a past election, an expired rule, prices or rates that are clearly stale): set Status = `Skipped - dated` and try the next row.
   - Taylor is not actually quoted: set Status = `Skipped - no TK quote` and try the next row.
   - Give up after 8 tries and say so in the summary.
3. Process it (Step 3). Schedule it for **12:00 PM America/Chicago the next day**. Captions can say "a while back" or "still true today". Never present an old article as brand-new.

## Step 3 — Process one mention
**Read the article.** Find what Taylor actually said. If Author is empty, fill the byline (add the outlet if syndicated, e.g. "Chris Adam (MoneyLion, syndicated on AOL)"). For the Author FB / Insta / X / LinkedIn columns, fill an empty one only with a handle or profile URL you actually found on the article page or the author's bio page. Otherwise leave it empty. Never guess a handle.

**Write copy (Main caption, Threads caption, Reel Script). Only for cells that are empty.** Voice: Taylor, first person, plain and casual, professional but human.
- No buzzwords or AI-sounding phrasing. Avoid "the good news is", "here's the thing", "game-changer", rule-of-three flourishes, emoji walls and hashtag stuffing (0–3 hashtags max).
- Compliance (Taylor is a CFP at an RIA): no guarantees. Use "may", "could", "can". Don't recommend specific products or vehicles (e.g., 529 plans, named funds, insurance products). Keep advice general. Don't default to "talk to a financial advisor" as the call to action.
- Never sound like bragging about Taylor's own money or success.
- Keep his quotes accurate. Paraphrase rather than invent.
- **Main caption (FB/IG/LinkedIn):** 60–130 words. Hook line from the article's idea, one or two short paragraphs, then credit the outlet (and author if known). End with "The article is in the first comment."
- **Threads caption:** under 450 characters, includes the article link.
- **Reel Script:** 25–45 seconds spoken. Start with `HOOK (on screen: "...")`, then a story-led script in Taylor's voice (a relatable moment, then the point, then a question or simple takeaway). End with "(About N seconds)". Don't script the outlet as an endorsement.

**Build the graphic.**
1. Pick a layout that fits the content *and* differs from the last 3 runs in `log.json`. Over time aim for roughly half with a photo (`photo`, `photo_full`) and half type-only (`statement`, `number`, `question`, `quote`). Use `number` only with a real figure from the article. Use `quote` only with Taylor's exact words (25 words or fewer). Use `theme_flip` sometimes for variety.
2. **Photo layouts:** search one of the folders above, choose an image not used in the last 30 entries of `log.json`, download it, decode to a file, and **look at it**. It must be clearly Taylor, decent quality, and appropriate. Set `focus` to where his face or upper body is.
3. **Headline rule:** speak to the reader (a question, a reframe, or a short takeaway) in 2–4 lines of up to ~16 characters each. When a photo of Taylor is on the card, the headline must not read as a statement about Taylor's own life (no "I have $2M..." readings).
4. Render, then **open the image and check it**: no text overflow or overlap with the credit line, and nothing awkward next to the photo. Fix and re-render if needed.
5. Save as `media-mentions/YYYY-MM-DD_<publication-slug>_<short-topic>.jpg` (article date). Commit and push (see "Pushing" below), then confirm the public URL returns HTTP 200 before using it.

**Create two GHL posts** (`create-post`, status `in_review`):
- Main: accountIds = FB page, Instagram, LinkedIn profile, LinkedIn page; `summary` = Main caption; media = [{url, type: "image/jpeg", altText}]; `followUpComment` = "Read the full article here: <link>"; `facebookPostDetails: {type: "post"}`, `instagramPostDetails: {type: "post"}`.
- Threads: accountIds = Threads; `summary` = Threads caption; same media.
- Both: `type: "post"`, `userId` (creator), `scheduleDate` (ISO UTC converted from the Chicago time above, minding daylight saving), `postApprovalDetails: {approver: <Claudia>, approvalStatus: "pending", requesterNote: "Media mention: <Publication>, <date>. Auto-drafted by Claude. Check tags before approving."}`.
- Use an idempotency key like `tk-media-<YYYYMMDD>-<slug>-main` / `-threads` so retries never double-post.

**Update the tracker:** Status = `In GHL review (Claudia) - sched M/D h:mm` and Graphic Link = the image URL. Then append to `log.json`: `{date_run, row_link, kind: "new"|"throwback", layout, photo_file_id or null, image_path}`.

---

## Pushing to GitHub
The token comes from the task prompt. Never write it to any file in this repo, any tracker cell or any message.
```bash
git -c credential.helper= -c http.extraHeader="Authorization: Basic $(printf 'x-access-token:%s' "$TOKEN" | base64 -w0)" push -q https://github.com/taylorkovar/tk-media-graphics.git main
```
Harmless warnings like "expected 'acknowledgments'" / "push negotiation failed" can appear. Verify with `curl -s -o /dev/null -w "%{http_code}" <raw url>` (wait a few seconds; retry up to 3 times).

## Setup each run
```bash
git clone -q https://github.com/taylorkovar/tk-media-graphics.git && cd tk-media-graphics
git config user.name "TK Media Bot" && git config user.email "team@growviagroup.com"
python3 -c "import PIL" || pip install --break-system-packages pillow
```

## Finish
Send a short summary (if you stopped early for any reason, say exactly why and at which step): what was added, which rows were skipped and why, and anything that needs a human (an unverified handle, a run that failed). If GHL, Sheets, or GitHub fails, don't half-post. Leave Status empty for that row so the next run retries, and report the error.
