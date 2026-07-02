# Small Systems Lab Repository Audit

Maintained by: Aderin (acting as SSL steward for this pass, per the ecosystem-wide
repository-restoration standard also applied to UMADA). Last full pass: 2026-07-02.

This audit documents current structure, navigation, and gaps for the Small Systems Lab
(SSL) hub repository. It does not invent facts, features, or partnerships not already
present in this repository or the sibling repositories checked out alongside it.

## Repository purpose

Small Systems Lab is the ecosystem hub: a public-interest studio for tender systems
(civic tools, editorial intelligence, accessibility infrastructure, food memory,
environmental sensing, speculative storytelling, AI literacy), and the static site that
links out to every SSL branch project. See `README.md` and `SCHEMA_CARD.md`.

## Current structure

A small static site, no build step, no framework:

- `index.html` — the live GitHub Pages homepage.
- `site.css` — layout glue (max-width wrapper, header/footer, grid, dividers).
- `variables.css` — the locked SSL visual system: design tokens (paper #efece2, ink
  #1a1a1a, line #d0cdc6, muted #6f6f6f; Helvetica Neue / Georgia / Courier Prime) and
  shared components (`.btn`, `.card`, text utilities, focus states, print styles).
- `docs/` — six method/practice documents (`ssl-method.md`, `operations.md`,
  `rule-based-intelligence.md`, `ancient-geometry.md`, `accessibility.md`,
  `branches.md`).
- `claude/CLAUDE_HANDOFF.md` — the original build brief for this site.
- `.nojekyll` — disables Jekyll processing on GitHub Pages.
- `README.md` — project overview.

No `assets/` directory exists, despite being listed in the pre-restoration
`README.md`'s repository-structure block. **Fixed this pass** — see "Duplicated or
outdated files" below.

## Homepage / entry point

`index.html` is the homepage and the only page on the live site (single-page hub with
in-page sections: What this is, Method, Branches, System Questions). `README.md` is the
GitHub-facing entry point for anyone browsing the repository instead of the live site.

## Important pages

`index.html` is the only HTML page. All six `docs/*.md` files and `claude/
CLAUDE_HANDOFF.md` are supporting documentation, not separate site pages (this repo has
`.nojekyll`, so Markdown files are not rendered as HTML by GitHub Pages — they are only
readable via the GitHub repository UI or as raw text).

## Orphan pages (fixed this pass)

Before this pass, all six `docs/*.md` files were listed in `README.md`'s repository-tree
code block but not hyperlinked from anywhere, and were not referenced from `index.html`
at all. **Fixed:**

- Added a "Documentation" section to `README.md` with real links to every `docs/*.md`
  file, `INDEX.md`, and `SCHEMA_CARD.md`.
- Added a "Documentation" link in `index.html`'s footer, pointing to the `docs/` folder
  on GitHub (`https://github.com/ukadike/Small-Systems-Lab/tree/main/docs`), since the
  Markdown files are not rendered pages on the live Pages site.
- Created `INDEX.md` (repo sitemap + ecosystem directory) and `SCHEMA_CARD.md`
  (orientation card), neither of which existed before.

`claude/CLAUDE_HANDOFF.md` remains intentionally unlinked from the public site (it is a
build brief for agents, not visitor-facing content); it is now indexed from `INDEX.md`.

## Broken links / navigation gaps (fixed this pass)

- **Missing sibling link**: `index.html`'s "Accessible by Design" card had no link at
  all (text-only "In development — no site yet"), even though the real repository
  (`github.com/ukadike/accessible-by-design-prototyping`) exists and contains a
  substantial, real WCAG 2.2+ auditing toolkit — it simply has no GitHub Pages
  deployment (no `CNAME`, no `gh-pages`/Pages workflow found in that repo). **Fixed:**
  added a `.btn` link to the GitHub repository itself, matching the task's fallback
  convention (Pages URL not available → link to `github.com/ukadike/<repo>`), and kept
  an honest "No live site yet" meta note rather than inventing a Pages URL.
- **Casing inconsistency**: `index.html` linked Umada as
  `https://ukadike.github.io/Umada/` (capital U), while every other branch link in this
  file (Omoluabi, Earth Sensors Lab, Echo) had already been deliberately lowercased in
  prior commits — see `git log`: "Fix branch link casing to match canonical lowercase
  repo URLs" (commit `1eb3be0`). No sibling repository currently cross-links to Umada's
  Pages site to confirm casing directly, but an unmerged sibling branch on this same
  repository, `claude/github-pages-navigation-links-6t45r6` (see below), independently
  made the same lowercase fix. **Fixed:** changed the link to
  `https://ukadike.github.io/umada/` for consistency with the rest of this file's
  established convention.
- **Ounjẹ**: remains unlinked, "In development — no site yet." No public repository for
  Ounjẹ was found among the sibling repositories checked during this pass. Left
  unchanged — not fabricating a URL. **Needs Kemi review** if a repo exists elsewhere.

No other broken links found. Internal anchors (`#main`, `#about-h`, etc.) all resolve;
external `https://ukadike.github.io/*` and `https://github.com/*` URL patterns are
internally consistent after the fixes above.

## Cross-repository coherence (verified this pass)

Checked out sibling repositories directly (`Umada`, `Echo`, `Earth-Sensors-Lab`,
`omoluabi`, `accessible-by-design-prototyping`) and confirmed each live one already
links back to this hub via its own site footer, using the lowercase form
`https://ukadike.github.io/small-systems-lab/` (Earth Sensors Lab's footer link is the
one exception, still using `Small-Systems-Lab` with capital letters — **Needs Kemi
review**: that fix belongs in the Earth Sensors Lab repository, out of scope for this
pass, but is noted here for the ecosystem-wide effort). `accessible-by-design-
prototyping` has no footer link back to the hub since it has no live site to put a
footer on.

## Missing navigation

None found beyond the items already fixed above. `index.html`'s in-page sections (What
this is, Method, Branches, System Questions) are all reachable by normal scrolling; no
in-page table of contents exists, which is reasonable for a single-page hub of this
length.

## Missing documentation

- No `docs/` file dedicated to "Public Knowledge Stewardship," the fifth of SSL's five
  method practices named in `README.md` and `index.html` (the other four —
  Operations of Care, Rule-Based Intelligence, Ancient Geometry, Accessibility — each
  have one). **Needs Kemi review**: whether to add `docs/public-knowledge-stewardship.md`
  or fold the concept into an existing file. Not created this pass — would require
  drafting new content, which is Kemi's call, not a restoration-scope fix.
- `README.md`'s "Suggested GitHub Pages Tagline" section is a leftover instruction from
  `claude/CLAUDE_HANDOFF.md`'s brief, not content for visitors. Left in place (not
  incorrect, just internal-process framing) — **Needs Kemi review** on whether to trim.

## Duplicated or outdated files (fixed this pass)

- `README.md`'s repository-structure code block listed a nonexistent `assets/`
  directory and omitted `INDEX.md`, `SCHEMA_CARD.md`, `site.css`, `variables.css`, and
  `.nojekyll`. **Fixed:** rewrote the block to match the actual repository contents and
  added a note explaining the removal of `assets/`.
- `README.md`'s "Branches" section and `index.html`'s "Branches" section had drifted:
  `index.html` included live links and repo-status framing (`unlinked` styling, "no site
  yet") that `README.md` did not. **Fixed:** `README.md`'s branch entries now include the
  same live-site links and repository links as `index.html`, so a visitor reading either
  file gets a coherent picture.

## Accessibility issues

Baseline already solid: skip link (`.skip-link`), semantic sectioning with
`aria-labelledby` on every `<section>`, single `<h1>`, logical `h2`→`h3` heading order,
visible focus states defined globally in `variables.css` (`*:focus`, plus explicit rules
for links/buttons/inputs), no color-only meaning (the `.unlinked`/muted card style is
paired with explicit "no site yet" text, not color alone), `lang="en"` set, no images
present so no outstanding alt-text gaps. No new violations introduced by this pass's
edits (all new links use the same `.btn`/plain-link patterns already in the file).

**Needs Kemi review**: `--color-muted: #6f6f6f` on `--color-paper: #efece2` — a WCAG
contrast check was not run in this pass. The unmerged `claude/github-pages-navigation-
links-6t45r6` branch (see below) already darkens this token to `#5c5c5c` specifically
for AA text contrast; worth reviewing and merging separately rather than redoing here,
since `variables.css` is the locked visual system and any token change should be a
deliberate, reviewed decision.

## Code quality issues

None found. The site has no build step, no JavaScript, and a small, consistent CSS
split (`variables.css` = tokens/components, `site.css` = layout only), matching its own
stated convention in `site.css`'s header comment.

## External-link convention (checked, not changed)

This file's pre-existing convention is plain `<a href>` with no `target="_blank"` /
`rel` attributes anywhere, including for external links (e.g. the footer's
`github.com/ukadike` link). All links added in this pass (Accessible by Design's GitHub
link, the footer Documentation link, and the Umada casing fix) match that convention —
no `target="_blank"` introduced, to avoid a new, inconsistently-applied pattern. Note
that the unmerged `claude/github-pages-navigation-links-6t45r6` branch does add
`target="_blank" rel="noopener noreferrer"`, but only to the single footer GitHub link,
not to the new sibling nav links it adds — an inconsistency in that branch, flagged here
rather than inherited.

## A parallel unmerged branch (found, not merged — Needs Kemi review)

`git branch -a` / `git fetch` surfaced `origin/claude/github-pages-navigation-links-
6t45r6`, three commits ahead of the same base as this repo's `main`:

1. "Add consistent ecosystem navigation and a sitemap page" — adds a `<nav class="wrap
   primary">` header linking Home/Omoluabi/Earth Sensors Lab/Echo/Umada/Sitemap, a new
   `/sitemap/index.html` page, a `.footer-nav`, and supporting `site.css`/`variables.css`
   additions (`.sr-only`, `.breadcrumb`, `nav.primary` styling).
2. "Add basic SEO: canonical URLs, Open Graph/Twitter tags, robots.txt, sitemap.xml" —
   adds `<link rel="canonical">`, OG/Twitter meta tags, `robots.txt`, `sitemap.xml`.
3. "Darken muted gray for WCAG AA text contrast" — changes `--color-muted` from
   `#6f6f6f` to `#5c5c5c`.

This branch already does substantial, relevant, good-quality work that overlaps with
this restoration pass's goals (navigation, casing, accessibility) and already contains
the lowercase Umada fix independently arrived at here. It was not merged into this pass
because: (a) it wasn't part of the assigned task scope, (b) it introduces new nav/sitemap
UI surface beyond "add missing links," which is a design decision for Kemi rather than
an unattended merge, and (c) it has the `target="_blank"` inconsistency noted above.
**Recommended**: Kemi reviews and either merges it (fixing the `target="_blank"`
inconsistency first) or extracts the useful pieces (contrast fix, SEO meta).

## Recommended changes (not made this pass — flagged for Kemi review)

- Whether to add a `docs/public-knowledge-stewardship.md` file (see "Missing
  documentation" above).
- Whether to run/merge the `claude/github-pages-navigation-links-6t45r6` branch.
- Whether Earth Sensors Lab's own footer link back to this hub should be lowercased to
  match the rest of the ecosystem (fix belongs in that repo).
- Whether Ounjẹ has a repository anywhere that should be linked.
- Whether to run a formal WCAG contrast check on `--color-muted` before deciding to
  change the locked visual-system token.

## Completed changes (this pass)

- Fixed the Umada Pages link casing in `index.html` to lowercase
  (`https://ukadike.github.io/umada/`), matching the established convention for
  Omoluabi/Earth Sensors Lab/Echo.
- Added a working link (to the GitHub repository) for Accessible by Design in
  `index.html`, replacing the previously unlinked card.
- Added a "Documentation" link in `index.html`'s footer.
- Added a "Documentation" section and synced "Branches" section (with live links) to
  `README.md`.
- Rewrote `README.md`'s repository-structure block to match reality (removed the
  nonexistent `assets/` directory, added `INDEX.md`, `SCHEMA_CARD.md`, `site.css`,
  `variables.css`, `.nojekyll`).
- Created root `INDEX.md` (repo sitemap + full ecosystem directory table).
- Created root `SCHEMA_CARD.md` (orientation card for contributors/code agents).
- This audit file.
