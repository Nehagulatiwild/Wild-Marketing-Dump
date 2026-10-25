# Wild Marketing Dump: weekly workflow

Live site: https://nehagulatiwild.github.io/Wild-Marketing-Dump/
New issue every Monday, ready by **Sunday 6 pm IST**. Curated by Neha Gulati (@neharunswild).

## How the site works
- `index.html` reads `issues.json` and shows the newest issue (highest `no`) on top; every issue is listed in the archive with a PDF download.
- Each issue is one file `issues/NN.html` of 13 sheets (1080×1350) styled by `mag.css`, plus `issues/NN.pdf`.
- Images live in `img/`. Name new ones with the issue number, e.g. `img/02-godrej.jpg` (JPG, max ~1400 px).
- Render with `python3 tools/render.py issues/NN.html /tmp/out` (Playwright; fonts are local in `fonts/`). Fix any overflow it reports, then copy `/tmp/out/issue.pdf` to `issues/NN.pdf`.
- Add the new entry to `issues.json`: `{ "no": "02", "week": "26 Oct–1 Nov 2026", "date": "2026-11-02", "headline": "...", "html": "issues/02.html", "pdf": "issues/02.pdf" }`.

## The 13 pages (copy the previous issue as the template)
| # | Page | Colour |
|---|---|---|
| 1 | Cover: 3 witty, fun cover lines (not a summary) + ₹0 sticker | Hot pink |
| 2 | Contents | Off-white |
| 3 | The Big One: story of the week + image + "My take" | Cobalt |
| 4–5 | The Dump: 6 stories, each with Neha's one-liner (no label) | Yellow / Orange |
| 6–7 | Campaign of the Week: best campaign anywhere in the world that Neha picks; image, what they did, insight, how it works, "Why I picked it" | Purple |
| 8–9 | Wild Brand Idea: that week's Wild Idea reel (from her Content Calendar). Category → White space → Brand idea → Positioning, range, launch. Use her script words. Two images. | Yellow (match images) |
| 10 | Number of the Week + "My take" | Neon green |
| 11 | Indian Brand Watch: 5 image tiles + "The pattern" | Orange |
| 12 | Steal This × Wild Gyaan (merged): one move + concept + 3 steps + image | Cobalt |
| 13 | Back page: marketing weather + Follow "Wild Brand Ideas & Stories for you!" | Hot pink |

Palette: yellow #FFD23F, hot pink #FF4F9A, cobalt #2D5BFF, orange #FF7A1A, purple #7B3FF2, neon green #B6FF3B, off-white #FFF8EE, near-black #141414.
Fonts: Anton (headlines), Instrument Serif italic (sub-lines), DM Sans (body).

## Rules
- Anything that is Neha's take must sound spoken, in her own voice (Hinglish fine), never AI-sounding. Draft it, then she approves or rewrites.
- "My take" and "Why I picked it" boxes are neon green (`take hot`).
- No swipe buttons. No "No. 01" in footers. Footer = sources (left) only.
- Every story credits its source. No brand logos as decoration; brand images only from Neha.
- Facts come from the week's Morning Marketing Brief editions (Mon–Sun) and their linked sources.

## Sunday routine
1. Morning: draft the issue from the week's briefs, with draft takes, 3 Campaign-of-the-Week options and the image list; send to Neha.
2. Neha replies with picks, take edits and images.
3. Build, render, check every page, push to `main`, confirm the live site loads.
4. Report last week's Instagram bio link taps (Windsor.ai, instagram connector).
5. Monday: Neha posts a Story with a link sticker and adds the CTA to that day's reel caption.
