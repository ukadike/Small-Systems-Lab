# WCAG 2.1 AA Accessibility Audit

Scope: all web content in this repository — `index.html`, `site.css`,
`variables.css`. (No other HTML/JS/template files exist; `README.md`, `INDEX.md`,
`SCHEMA_CARD.md`, and `docs/*.md` are plain Markdown, not rendered as HTML pages on
this site — `.nojekyll` disables Jekyll/GitHub Pages rendering of them — and contain
no raw HTML, so they are out of scope for this pass.)

Contrast ratios below were computed directly from the hex values in `variables.css`
using the WCAG relative-luminance formula, not estimated.

## Summary

| Severity | Found | Fixed | Left open |
|---|---|---|---|
| Serious  | 1 | 1 | 0 |
| Moderate | 0 | 0 | 0 |
| Minor / advisory | 2 | 0 | 2 |
| **Total** | **3** | **1** | **2** |

Everything else in scope (heading structure, landmarks, list markup, skip link,
`lang`, page title, link-text quality, focus visibility, keyboard reachability,
color-alone meaning, motion, ARIA, non-text content/alt text) was checked and found
already compliant — see "Checked, no issues found" below.

## Issues found

### 1. `--color-muted` fails 4.5:1 text contrast against `--color-paper` — FIXED

- **Location:** `variables.css:12` (token), consumed by `.text-meta` (used in
  `index.html:16,19` header and `index.html:149` footer) and `.card.unlinked`
  (`index.html:100-105`).
- **WCAG:** 1.4.3 Contrast (Minimum) — AA.
- **Severity:** Serious (confirmed real failure, not a guess).
- **Measured:** `#6f6f6f` on `#efece2` (paper) = **4.25:1** — fails the 4.5:1 minimum
  for normal-size text. (`.text-meta` text is 0.85rem / ~13.6px, weight 400 — normal
  text, not large text, so 4.5:1 applies.) Every place `.text-meta` is used in this
  page sits on the `--color-paper` background (header, footer), so this was a live,
  user-facing failure, not a theoretical one.
- **Also checked:** `#6f6f6f` on `--color-soft` (`.card.unlinked`) = 4.77:1 (passes)
  and on `--color-white` = 5.03:1 (passes) — only the paper-background usage failed.
- **Fix (shared token — affects Echo, omoluabi, Umada, Earth-Sensors-Lab, which all
  consume this file):** darkened `--color-muted` from `#6f6f6f` to `#666666` in
  `variables.css:12-16`. New ratios: **4.86:1 on paper**, 5.45:1 on soft, 5.74:1 on
  white — clears 4.5:1 with margin on every background it's actually used against in
  this repo. Hue is unchanged (neutral gray); the change is an 8% luminance shift
  (111→102 per channel), the smallest adjustment that clears the threshold with a
  safety margin (the bare-minimum value, `#6b6b6b`, only reaches 4.51:1 — too close to
  the line to be safe against rounding/rendering differences across browsers).
  A prior repo audit (`docs/REPO_AUDIT.md`) had already flagged this exact failure and
  deferred it for review, noting an unmerged sibling branch that independently darkens
  the same token to `#5c5c5c` for the same reason; this fix addresses the same root
  cause with a smaller delta from the original value.

**This token change ripples to every sibling repo that includes `variables.css`**
(Echo, omoluabi, Umada, Earth-Sensors-Lab) — flagging per the task's ground rules.
No other token values were touched.

### 2. `--color-line` has very low contrast against `--color-paper` — LEFT OPEN (advisory)

- **Location:** `variables.css:11` (token), used via `--border-thin` for `.divider`
  (`site.css:46-50`) and `.card` borders (`variables.css:190-195`).
- **WCAG:** 1.4.11 Non-text Contrast (AA) — applies to UI components and graphical
  objects required to understand content; arguably does not apply here.
- **Severity:** Minor / advisory, not treated as a confirmed violation.
- **Measured:** `#d0cdc6` on `#efece2` (paper) = **1.34:1**.
- **Why left open:** `.divider` and `.card` borders are decorative visual separators
  between static content blocks, not interactive UI components (no form controls, no
  custom widgets use this border) and not graphical objects whose meaning is lost
  without the border — the grouping is redundant with layout/spacing and heading
  structure. Because `--color-line` is used pervasively for the whole visual system's
  "quiet line" aesthetic across sibling repos, and because this doesn't meet the
  criterion's actual applicability threshold with the confidence the task requires
  before touching a shared token, it was left unchanged. **Flagging for Kemi review**
  if any sibling repo later uses `--color-line` as a boundary for an actual
  interactive control (e.g., an input outline) — that usage would need a real fix.

### 3. Footer "Documentation" link text is short out of context — LEFT OPEN (advisory)

- **Location:** `index.html:150`.
- **WCAG:** 2.4.4 Link Purpose (In Context) — AA.
- **Severity:** Minor / advisory.
- **Detail:** The link text is just "Documentation," which is acceptable under 2.4.4
  because the surrounding footer sentence ("Small Systems Lab treats documentation...
  as infrastructure" plus the adjacent `github.com/ukadike` link) supplies context
  identifying whose documentation it is and where it goes. Not a bare "click here" /
  "read more" pattern. Left as-is; noted here rather than silently passed over.

## Checked, no issues found

- **1.1.1 Non-text content:** No `<img>`, icon fonts, or inline SVGs exist anywhere in
  the repo's HTML/CSS. Nothing to fix; nothing to leave as `AWAITING FRAGMENT`.
- **1.3.1 Info & relationships:** Single `<h1>` (`index.html:17`); `h2` used for every
  section (`about-h`, `method-h`, `branches-h`, `questions-h`), `h3` only nested inside
  those sections (card titles) — no skipped levels. Landmarks present: `<header>`,
  `<main id="main">`, `<footer>`. The "System Questions" list is real `<ul>/<li>`
  markup (`index.html:128-139`). No forms/inputs exist, so no label-association issue.
- **1.4.1 Use of color:** `.card.unlinked` styling (muted text + soft background) is
  always paired with explicit text ("In development — no site yet"); links are always
  underlined by default (`site.css:12-15`), not distinguished by color alone.
- **1.4.3 / 1.4.11 Contrast (everything else measured):** `--color-ink` on
  `--color-paper` = 14.72:1; on `--color-white` = 17.40:1; on `--color-soft` =
  16.51:1 — all headings/body text pass with very large margin. `.btn` border/text
  (ink on paper, 2px border) and focus outline (`--focus-outline: 2px solid
  --color-ink`) measure the same 14.72:1+ against every background they appear on,
  clearing the 3:1 non-text minimum easily.
- **2.1.1 / 2.4.7 Keyboard & focus:** No `outline: none` (or `outline: 0`) anywhere in
  `site.css` or `variables.css` — confirmed by direct search. `*:focus`,
  `a:focus`, `button:focus`, `input:focus`, `textarea:focus`, and `.btn:focus` all
  explicitly set a visible 2px ink outline with offset. Every interactive element
  (skip link, nav-style links, `.btn` links) is a real `<a>`, reachable and operable
  by keyboard with no custom widgets/`tabindex` tricks to get wrong.
- **2.4.1 Bypass blocks:** `.skip-link` present (`index.html:12`), targets
  `#main` (`index.html:23`), and is a real focusable link with a visible focus state
  (`site.css:18-28`). This is a single-page site with no repeated nav, so this is the
  right level of bypass support.
- **2.4.2 Page titled:** `<title>Small Systems Lab</title>` present and descriptive.
- **2.4.4 Link purpose:** All branch links read "Visit Omoluabi," "Visit Earth Sensors
  Lab," etc. — no bare "click here"/"read more" anywhere (footer link addressed as
  item 3 above).
- **3.1.1 Language of page:** `<html lang="en">` set.
- **4.1.2 Name, role, value:** No custom widgets/ARIA roles are used at all — only
  native `<a>`, headings, `<ul>/<li>`, `<section>`, `<article>` — nothing to get wrong.
  `aria-labelledby` on every `<section>` correctly references an existing heading `id`.
- **Motion:** `--transition: none` globally (`variables.css:60`), and `.btn`'s
  `transition: var(--transition)` resolves to `none` — there are no CSS
  animations/transitions anywhere in the repository for `prefers-reduced-motion` to
  need to override. Nothing to fix.
- **Inline SVGs:** None exist in the repository.

## Files changed this pass

- `variables.css` — `--color-muted` token value (see item 1). **Shared-token change —
  affects sibling repos that include this file.**
- `WCAG_AUDIT.md` — this file (new).

No changes were made to `index.html`, `site.css`, or any Markdown file.
