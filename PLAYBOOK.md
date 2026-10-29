# TK Media Mentions — Daily Playbook

Weekday job (Mon–Fri) that turns Taylor Kovar's press mentions into social posts for human approval.
Every run does three things:
0. **Rejections:** fix or reopen any post Claudia rejected (Step 0).
1. **New mentions:** anything on https://choose11.com/in-the-press/ that isn't in the tracker yet (may be zero).
2. **Throwbacks:** older mentions from the tracker, so that every calendar day (weekends included) has one throwback post. Usually one per run; the Thursday run covers the weekend.

Posts are scheduled **two business days ahead** so Claudia has a working day to review. See "Scheduling" below.

Posts go to GoHighLevel as *in review* for Claudia. Nothing publishes without her approval.

---

## Systems and IDs

| What | Value |
|---|---|
| Tracker | Google Sheet `11ciDQwCe5M3Z_lotkvX49N91e0Y8NEdoCy-RCiJYmfI`, tab **Media Mentions** (row 1 = headers, newest at top) |
| GHL location | TaylorKovar.com `CoD1jBJnfOnS8iAmntku` |
| GHL userId (creator) | Taylor Kovar `0owaLTQF7YTV3EFV8N9c` |
| GHL approver | Claudia Valladares `HVPbKziWl5cst6jueTAL` (Claudia@Choose11.com, her main login; don't use her old claudia@taylorkovar.com login `3nS0t3FsisxjJ3uDiKhI`) |
| Image hosting | this repo; public URL = `https://raw.githubusercontent.com/taylorkovar/tk-media-graphics/main/<path>`. Images are rendered **by a GitHub Action** from a spec you queue (see "Publishing images") |
| Graphic builder | `tools/brand_cards.py` (fonts in `fonts/`) |
| Run history | `log.json` in this repo (layouts, photos, rows done). Read it first, append to it, save it with the GitHub connector. |
| Repo writes | **GitHub connector only** (`push_files` / `create_or_update_file`). Never `git push`, never use or ask for a token. |

**GHL account IDs**
- Facebook page: `67055050817f4e032ecbff41_CoD1jBJnfOnS8iAmntku_415562988306103_page`
- Instagram: `67a6783b6bb1fdb083e36b8d_CoD1jBJnfOnS8iAmntku_17841402976402496`
- LinkedIn profile: `67a678600c011c4450eb74a3_CoD1jBJnfOnS8iAmntku_OlhS_xldVM_profile`
- LinkedIn page: `67055081e689400600e949a9_CoD1jBJnfOnS8iAmntku_107872485_page`
- Threads: `6aac4159cd1cd4d29e3dec4d_CoD1jBJnfOnS8iAmntku_28733261506363980_profile`
- Bluesky (taylorkovar.bsky.social): `6ac3936857e651b3b0f33191_CoD1jBJnfOnS8iAmntku_did:plc:irkcha2fdua6pubdl7aap5dc_profile`
- TikTok and YouTube are video-only. Skip them. X is not connected.

**Tracker columns: always find them by header name, never by letter.** The team rearranges this sheet. At the start of every run, read row 1 and map each header to its column letter. If a header below is missing, stop and report it instead of guessing.

Layout as of 10/8/2026, for reference only:
A Article Date (MM/DD/YYYY) · B Publication · C Title · D Link · E Author · F Author FB · G Author Insta · H Author X · I Author LinkedIn · **J Status** · K FB/Insta/LinkedIn Caption · L Threads/X Caption · M BlueSky Caption · N Reel Script · O Graphic Link · P Video Link · Q Date Image Posted · R Date Reel Posted.

- Never touch Video Link, Date Image Posted, or Date Reel Posted. The team fills those.
- **Captions (including BlueSky Caption) and Reel Script: always write your own** for the row you're processing (as long as its Status is empty), replacing whatever is there. Another tool pre-filled many rows with templated copy ("Here is one place to start...", "Save this for your next money conversation", "Thanks to X for including me") that Taylor does NOT want. Never reuse those phrases or that structure.
- **Everything else: never overwrite a cell that already has content** (author, handles, links, dates). Fill only empty cells.
- In the text below, "Status", "Main caption" (FB/Insta/LinkedIn Caption), "Threads caption", "Bluesky caption" (BlueSky Caption), "Reel Script", and "Graphic Link" refer to those headers.

**Photo folders (Google Drive)** — image files only (ignore videos). Prefer files under ~6 MB.
- TK Solo Pics `1bFJydk2E3CEZl8IUzysdT6FhvBDvgdcD` (main source)
- Event Pictures `1oYEqGqYFq8EOnh3nK7cQJuLBCoGcgulX` (speaking, stage)
- Tay & Meg Pics `1-PMuvxkO8JrE2Tw9gOzNj9li-mjNSo4Q` (only for couples / marriage-and-money topics)
- Other subfolders of `TK.com Pics & Vids` (parent `190Up7yXQFmWGilkZtwXY3yIIid_gJNhK`) such as BTS, Kovar Travels and Old Biz Pics are fine. Casual, behind-the-scenes shots are welcome. **Never use Kovar Kids or Fam Pics.**

---

## Scheduling
The team works Mon–Fri, so the task runs only on weekdays. Posts still go out 7 days a week.
- **Target date** = 2 business days after the run date: Mon→Wed, Tue→Thu, Wed→Fri, Thu→Mon, Fri→Tue. (Holidays are not skipped.)
- **New mentions:** 9:00 AM America/Chicago on the target date.
- **Throwbacks:** exactly one per calendar day, at 12:00 PM America/Chicago. A date is *covered* when some tracker row's Status reads `... sched M/D 12:00` for that date. Each run, check every date from **tomorrow through the target date**, and schedule one throwback for each date that isn't covered, earliest date first, at most 4 per run. In a normal week that means one per run, and the Thursday run fills Sat, Sun and Mon. If a run gets missed, the next run fills the gap automatically.
- If several cards are made in one run, give each a different layout (and a different photo).
- **No back-to-back topics.** Before scheduling anything, look at what is already scheduled the day before, the same day and the day after (tracker Status dates plus `log.json` `scheduled_for`). Never put two posts on the same topic (e.g. two Social Security posts) within a day of each other. For a throwback, skip to the next empty-Status row on a different topic. For a new mention, move it to the nearest day without a same-topic post; a weekend 9:00 AM slot is fine since new mentions never land there otherwise. Note the move in `log.json`. (Team feedback 10/21/2026: an SS new mention and an SS throwback on the same Friday.)
- Convert to UTC minding daylight saving: CDT is UTC−5 until Sun Nov 1 2026 (2 AM), then CST is UTC−6 until Sun Mar 14 2027.

## Step 0 — Handle rejected posts
Do this first, every run, before Step 1. (Confirmed against a real rejection 10/29/2026.)
1. In `log.json`, take every entry whose `scheduled_for` is tomorrow or later and call `get-post` (params `{"path": {"id": ...}}`) on each ID in its `ghl_post_ids`.
2. Read `postApprovalDetails.approvalStatus`. `pending` or `approved`: nothing to do. `rejected`: the post's `status` also turns `failed`, and Claudia's reason is in `postApprovalDetails.approverNote`.
3. A rejection on one platform applies to the whole set (Main, Threads, Bluesky) when they share the card, so revise all three together.
   - **The note asks for something specific** (new photo, softer wording, shorter card): make the change. If the card changes, render it as `<same name>-v2.jpg` and publish and check it as usual. Then call `edit-post` on each post in place, keeping the same IDs and `scheduleDate`, with the full body (accountIds, summary, media, type, userId, platform details) plus `status: "in_review"` and `postApprovalDetails: {approver: <Claudia>, approvalStatus: "pending", requesterNote: "Revised per your note: <one line on what changed>. ..."}`. Use idempotency keys ending in `-rev1` (`-rev2` and so on after that). Call `get-post` again to confirm it reads `in_review` / `pending`. Update the row's captions, Reel Script and Graphic Link, but keep its Status.
   - **The note is empty or unclear, or says to drop the post:** don't revise or delete anything. Set the row's Status to `Rejected - <her note, or "no note">`. That reopens the date (the coverage check only counts `sched M/D`), so Step 2 fills it with another row, and the rejected row is never picked again.
   - **The post goes out within 24 hours of this run:** don't revise. Report it so a human can handle it.
   - **The set already has a `revision` entry in `log.json` and was rejected again:** treat it as unclear.
4. After a revision the old `approverNote` stays on the post. Decide only by `approvalStatus`, and never revise a post that reads `pending`.
5. Add a `log.json` entry with `kind: "revision"`, `approver_note`, what changed, and any standing rule the note implies. Read past `revision` entries before writing new copy or choosing photos.
6. Put every rejection, and what you did about it, in the run summary. If `get-post` fails, report it and continue.

## Step 1 — New mentions
1. Fetch the press page. Each entry shows `logo-alt-text - MM/DD/YYYY Title` linking to the article.
2. Compare links against the Link column. Anything new gets a **new row inserted at row 2** (keep newest at top), filling Article Date, Publication (clean name: "AOL", "GOBankingRates", "Yahoo Finance"...), Title, and Link.
3. Process it (Step 3). Schedule it for **9:00 AM America/Chicago on the target date** (see Scheduling).

## Step 2 — Throwbacks
Work out which dates need a throwback (see Scheduling). For each one, earliest first:
1. Find the topmost row (row 3 and down) where **Status is empty** (and that you haven't already picked this run).
2. Open the link.
   - Dead (404, removed, paywalled to nothing): set Status = `Skipped - dead link` and try the next row.
   - Too dated to repost (a specific past tax year, stimulus checks, a past election, an expired rule, prices or rates that are clearly stale): set Status = `Skipped - dated` and try the next row.
   - Taylor is not actually quoted: set Status = `Skipped - no TK quote` and try the next row.
   - Give up after 8 tries and say so in the summary.
3. Process it (Step 3). Schedule it for **12:00 PM America/Chicago on that date**. Captions can say "a while back" or "still true today". Never present an old article as brand-new.

## Step 3 — Process one mention
**Read the article.** Find what Taylor actually said. If Author is empty, fill the byline (add the outlet if syndicated, e.g. "Chris Adam (MoneyLion, syndicated on AOL)"). For the Author FB / Insta / X / LinkedIn columns, fill an empty one only with a handle or profile URL you actually found on the article page or the author's bio page. Otherwise leave it empty. Never guess a handle.

**Write copy (Main caption, Threads caption, Bluesky caption, Reel Script).** Voice: Taylor, first person, writing the way he writes his own Facebook posts (reference posts from the team, 10/21/2026, below). **Taylor helps people build a life they actually want to live.**
How his posts sound:
- **Open with a sharp, observational hook line**, often a little wry: "Kinda chic to drive the car with 140,000 miles on it." / "The finished copy of The 5 Money Personalities fits in one hand, and it took years to get it there." Not "Picture someone..." scene-setting.
- **Full, natural, conversational sentences**, the way people actually talk, often joined with "and", "but", "so" or a comma: "It doesn't always look like the newest and the best, it can look like the older Jeep model." Short paragraphs are fine, but **don't chop thoughts into strings of short sentences or fragments.** Staccato copy ("Bigger check. Bigger number. Done.") reads as AI (team feedback 10/21/2026). At most one short list of fragments per post, and only when it lands, like his "The reinvested dividend. The car you kept two extra years. The raise you didn't spend."
- **Concrete, everyday details** (an older Jeep, a raise you didn't spend, a paid-off house, fifteen years of boring decisions) over abstractions.
- **Contrast lines** that flip the usual story: "You see the couple with the paid-off house. You don't see the fifteen years of boring decisions and old cars that got them there."
- **Name the idea when there is one** (delayed gratification, survivorship bias), then explain it in plain words.
- **Confident and direct, not soft or therapeutic.** Warmth comes from being on the reader's side ("I know how discouraging it is..."), not from reassurance padding. Skip "go easy on yourself" style filler unless it really fits.
- **End on a crisp closer or one concrete action**: "Kinda chic to be quietly ahead and never mention it." / "Keep doing the boring thing this month, and write down one piece of progress so you can see your own process." (The main caption still ends with the fixed line below.)
Reference post 1: "Kinda chic to drive the car with 140,000 miles on it. Kinda chic to keep the 401k contribution the same after the raise instead of upgrading the truck. / People are using the trend to justify all the new purses and skincare. I want to use it to show the truth behind wealth building. It doesn't always look like the newest and the best, it can look like the older Jeep model. / ... Nobody claps for the boring version of wealth. The reinvested dividend. The car you kept two extra years. The raise you didn't spend. / It doesn't post well because there's no reveal. No before and after. Just a slow, unglamorous climb that only shows up on a statement years later. / Kinda chic to be quietly ahead and never mention it."
Reference post 2: "... If you're in the middle of something slow right now, like a debt payoff or a business that hasn't turned the corner, I know how discouraging it is to scroll past everyone's finished product. / When we only see what made it to the end, we forget the drafts and the failed tries, and we start to believe the finish came easy. Survivorship bias is the formal name for it, and it messes with money as much as anything. / You see the couple with the paid-off house. You don't see the fifteen years of boring decisions and old cars that got them there. / Comparing your middle to someone else's finish line will make you feel behind every time. / Keep doing the boring thing this month, and write down one piece of progress so you can see your own process."
(Supersedes the 10/20/2026 "old man wisdom" note. All rules below still apply, including compliance and no client references.)
- **Never reference clients or the people Taylor works with** ("families I sit down with", "what I see with clients", "I hear this a lot from people"). Clients shouldn't wonder whether a post is about them. Use "a lot of us" or speak to the reader directly instead.

The job of the copy is to **connect the article to the reader's life**. Not "I was quoted in X." Build it like this:
1. Open with a hook line about the reader's situation or a common belief, in Taylor's observational style (see above). Specific beats generic.
2. Bring in what Taylor actually said in the article, in his words or a close paraphrase, as the insight for that moment.
3. Give them one gentle thing to think about or try, framed as a suggestion, ideally tied back to building a life they actually want.
4. Mention the outlet naturally ("I talked about this with GOBankingRates...") near the end. The press mention adds credibility; it isn't the headline.
Every caption should read differently from the last few. Vary the opening move (a wry observation, a common belief flipped, a question, a small confession); the main caption's last line is fixed (see below). Read the last 5 rows that have Status filled to avoid repeating yourself.
- No buzzwords or AI-sounding phrasing. Avoid "the good news is", "here's the thing", "game-changer", rule-of-three flourishes, emoji walls and hashtag stuffing (0–3 hashtags max).
- Never write "I got into this/it with <outlet>" (Taylor finds it weird). Use plain wording like "I talked about this with <outlet>" or "I shared this with <outlet>".
- Compliance (Taylor is a CFP at an RIA): no guarantees. Use "may", "could", "can". Don't recommend specific products or vehicles (e.g., 529 plans, named funds, insurance products). Keep advice general. Don't default to "talk to a financial advisor" as the call to action. On investing topics, never say what "works best" or "holds up best", and include a plain risk line (e.g. "Investing always carries risk") (Claudia's rejection 10/29/2026).
- Never sound like bragging about Taylor's own money or success.
- Keep his quotes accurate. Paraphrase rather than invent.
- **Main caption (FB/IG/LinkedIn):** 50–90 words following the structure above. Don't paste Taylor's full quote into the caption, especially when it's already on the card: give the gist in one plain sentence. Always end with exactly: "Check out the full article in the comments."
- **Threads caption:** under 450 characters, includes the article link.
- **Bluesky caption:** 300 characters max *including* the article link (Bluesky's hard limit; long links count in full). Usually a tighter cut of the Threads caption. Bluesky has no follow-up comment, so the link goes in the caption. Save it in the BlueSky Caption column.
- **Reel Script:** 25–45 seconds spoken. Start with `HOOK (on screen: "...")`, then a story-led script in Taylor's voice (story, story, information, story, story): a relatable moment or a real-feeling scenario, what he told the outlet, then a crisp closer or one simple takeaway. Same natural, conversational sentences as his posts (no choppy one-liners). Light humor is welcome; never bragging, never referencing clients. End with "(About N seconds)". Don't script the outlet as an endorsement.

**Build the graphic.**
0. **Make the press mention obvious.** Every card shows the outlet prominently: all layouts get an "AS QUOTED IN <OUTLET>" masthead band by default, and `quote_forward` puts "TAYLOR KOVAR, CFP®, TOLD <OUTLET>" as the header. Use the outlet's name as text only. **Never use publication logo files.** If the publication name is long, add `"outlet_display"` with a recognizable short form (e.g. "U.S. NEWS", "YAHOO FINANCE", "GOBANKINGRATES"). Don't set `"masthead": false` unless Taylor asks.
   Use `quote_forward` only when the article has a short, strong line from Taylor (his exact words, **15 words or fewer**; an exact shorter excerpt of a longer quote is fine). Otherwise use a headline card.
   **Keep card text short.** Someone scrolling should get the card in about two seconds. Headline cards: about 10 words max. Quote cards: 15 words max. (Taylor's feedback 10/19/2026: a 26-word quote card was too much text for one graphic. The replacement that worked was a statement card reading "Your retirement could last 30 years.")
1. Pick a layout that fits the content *and* differs from the last 3 runs in `log.json`. Over time aim for roughly half with a photo (`photo`, `photo_full`) and half type-only (`statement`, `number`, `question`, `quote`, `quote_forward`). Use `number` only with a real figure from the article. Use `quote` and `quote_forward` only with Taylor's exact words (15 words max on the card). Use `theme_flip` sometimes for variety.
2. **Photo layouts:** search one of the folders above, choose an image not used in the last 30 entries of `log.json`, download it, decode to a file, and **look at it**. It must be clearly Taylor, decent quality, and appropriate. **The photo has to make sense with the headline.** A generic smiling headshot next to a worry or question headline ("Will it keep up?") does not; go type-only instead (team feedback 10/21/2026). When nothing in the folders fits the topic, type-only is the right call. Set `focus` to where his face or upper body is. For the local preview, apply `ImageOps.exif_transpose` first (the Action does the same). Note the Drive file id for the spec.
3. **Headline rule:** speak to the reader (a question, a reframe, or a short takeaway) in 2–4 lines of up to ~16 characters each. When a photo of Taylor is on the card, the headline must not read as a statement about Taylor's own life (no "I have $2M..." readings).
4. Render, then **open the image and check it**: no text overflow or overlap with the credit line, and nothing awkward next to the photo. Fix and re-render if needed.
5. Name it `media-mentions/YYYY-MM-DD_<publication-slug>_<short-topic>.jpg` (article date) and publish it through the Action (see "Publishing images" below). Confirm the public URL returns HTTP 200 **and** open the downloaded copy before using it.

**Create three GHL posts** (`create-post`, status `in_review`):
- Main: accountIds = FB page, Instagram, LinkedIn profile, LinkedIn page; `summary` = Main caption; media = [{url, type: "image/jpeg", altText}]; `followUpComment` = "Read the full article here: <link>"; `facebookPostDetails: {type: "post"}`, `instagramPostDetails: {type: "post"}`.
- Threads: accountIds = Threads; `summary` = Threads caption; same media.
- Bluesky: accountIds = Bluesky; `summary` = Bluesky caption (check it is 300 characters or fewer); same media; no `followUpComment`.
- All three: `type: "post"`, `userId` (creator), `scheduleDate` (ISO UTC converted from the Chicago time above, minding daylight saving), `postApprovalDetails: {approver: <Claudia>, approvalStatus: "pending", requesterNote: "Media mention: <Publication>, <date>. Auto-drafted by Claude. Check tags before approving."}`.
- Use an idempotency key like `tk-media-<YYYYMMDD>-<slug>-main` / `-threads` / `-bluesky` so retries never double-post.

**Update the tracker:** Status = `In GHL review (Claudia) - sched M/D h:mm` (exactly this format, e.g. `sched 10/17 12:00` or `sched 10/19 9:00`; the throwback coverage check reads it), the three captions and Reel Script, and Graphic Link = the image URL. Then append to `log.json`: `{date_run, row_link, kind: "new"|"throwback", layout, masthead: true|false, photo_file_id or null, image_path, ghl_post_ids: [..], scheduled_for}`. The post IDs and layout are kept so engagement can be compared by card style later.

---

## Publishing images (no token)
Binary images can't go through the GitHub connector, so a GitHub Action renders them in the repo (`.github/workflows/render-cards.yml` runs `tools/render_queue.py`, which runs the same `tools/brand_cards.py`).
1. Render locally first and check it (Step 3.4). The Action produces the same image from the same spec.
2. With the GitHub connector (`push_files`, branch `main`), add `queue/<image-name>.json` containing the exact spec you rendered, minus the local `photo` path, plus:
   - `"out": "media-mentions/<image-name>.jpg"`
   - for photo layouts: `"photo_drive_id": "<Drive file id>"` (photo folders are shared "Anyone with the link", so the Action can download it).
   You can queue several specs in one `push_files` call.
3. Wait about 60 seconds, then poll `curl -s -o /dev/null -w "%{http_code}" <raw url>` every 20 seconds, up to 5 minutes.
4. On 200, download the raw URL and **open it** to confirm it matches your local render. Only then create GHL posts.
5. If it never appears, the Action failed (the spec stays in `queue/`). Don't post; leave that row's Status empty and report it. Remove the stale spec with `delete_file` so the next run starts clean.

**Shared with another robot:** the Content Mill scheduler also uses this queue. Its jobs are `queue/cm_*.json` files (a `fetch_url` that downloads a Canva PNG) and its images live in `media-mentions/content-mill/`. They are handled separately and can't fail your renders. Never edit or delete `cm_*` queue files or anything in `media-mentions/content-mill/`, and don't count them as media-mention images.

**log.json:** read it with `get_file_contents` (that gives the current SHA), append your entries, and save the whole file with `create_or_update_file` (include the SHA). The Action also commits to `main`, so if the save fails on a SHA mismatch, re-read and retry.

## Setup each run
```bash
git clone -q https://github.com/taylorkovar/tk-media-graphics.git && cd tk-media-graphics
python3 -c "import PIL" || pip install --break-system-packages pillow
```

## Finish
Send a short summary (if you stopped early for any reason, say exactly why and at which step): what was added and the date and time each post is scheduled for, which rows were skipped and why, and anything that needs a human (an unverified handle, a run that failed). If GHL, Sheets, the GitHub connector or the render Action fails, don't half-post. Leave Status empty for that row so the next run retries, and report the error.
