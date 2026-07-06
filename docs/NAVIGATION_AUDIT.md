# Ecosystem Navigation Audit

Pass: `claude/ukadike-github-nav-audit-9yq9ft`, across all 8 repos in scope:
`ukadike/ukadike`, `ukadike/Small-Systems-Lab`, `ukadike/omoluabi`,
`ukadike/Earth-Sensors-Lab`, `ukadike/Echo`, `ukadike/Umada`,
`ukadike/accessible-by-design-prototyping`, `ukadike/alt-text-wiki.lnc`.

See `SITE_MAP.md` (this repo) for the resulting ecosystem sitemap.

## Problem found

Navigation across the ecosystem was fragmented: some repos linked forward to
siblings, almost none linked back consistently, one live site was described as
non-existent, and casing/consistency drifted between repos that were built at
different times.

## Fixes made this pass, by repo

### Small Systems Lab (hub)

- **Stale "No live site yet" for Accessible by Design**, fixed in `README.md`,
  `index.html`, `INDEX.md`, and `SCHEMA_CARD.md` — all now link
  `https://ukadike.github.io/accessible-by-design-prototyping/`.
- Merged in a previously-flagged, unmerged parallel branch
  (`claude/github-pages-navigation-links-6t45r6`) that had already built a primary
  nav header, `/sitemap/` page, SEO meta tags, `robots.txt`/`sitemap.xml`, and a
  WCAG AA contrast fix — extended its nav and sitemap page to include Accessible by
  Design, which didn't exist yet when that branch was written.
- Added `SITE_MAP.md` (this file's sibling) and this audit document.

### ukadike (profile README)

- The profile's "Featured Projects" section already linked each branch's live site
  except its own hub and Accessible by Design — added both
  (`ukadike.github.io/small-systems-lab/`, `ukadike.github.io/accessible-by-design-prototyping/`).
- Lowercased the Umada Pages URL (was `.../Umada/`) to match the ecosystem
  convention.
- Confirmed (via the prior restoration pass's own audit trail in
  `docs/REPO_AUDIT.md`) that the "Repository in development" stale labels for
  Earth Sensors Lab and Accessible by Design had already been corrected; no
  remaining stale-status language found in this pass.

### Omoluabi

- Added the shared ecosystem nav + breadcrumb to `index.html`,
  `ufo-connection/index.html`, `ufo-connection/offline.html`, and
  `world-layer-sandbox/p5-coastal-relay/index.html`.
- **Orphaned pages found**: `ufo-connection/offline.html` and
  `world-layer-sandbox/p5-coastal-relay/index.html` had no `<header>`, no skip
  link, and (for `offline.html`) no stylesheet at all — neither page could get
  back to the hub or even to Omoluabi's own home page. Both now have a skip link,
  ecosystem nav, and a three-level breadcrumb.
- Added `## Related SSL Projects` to `README.md`.

### Umada

- Added the ecosystem nav + breadcrumb to `index.html` and all 20
  `sections/*.html` pages, without disturbing the existing internal
  `primary-nav` (the details/summary "Browse the archive" menu).
- Confirmed `PUBLIC_README.md` already serves as the public "Begin Here" entry
  point distinct from the contributor `README.md` and canon files — no duplicate
  page created.
- Added `## Related SSL Projects` to `README.md`.

### Earth Sensors Lab

- Added the ecosystem nav + breadcrumb to `index.html`.
- The homepage's existing repo-local nav already linked `INDEX.md`; relabeled its
  landmark to `aria-label="Repository sections"` (since "Primary" is now the new
  ecosystem nav) and renamed the link text to "Full site index" for clarity, plus
  a second sitemap link in the footer.
- Added `## Related SSL Projects` to `README.md`.

### Echo

- Added the ecosystem nav + breadcrumb to `index.html`.
- Added a "Lesson roadmap: seven starter lessons" section listing the seven
  starter-lesson titles already named in `README.md`, each as a linked,
  numbered item.
- **Gap, not fabricated**: none of the seven lessons has its own page or
  in-page anchor yet. Each roadmap item currently links to the same shared
  `README.md#starter-lessons` anchor on GitHub rather than a page that doesn't
  exist. Flagged in `Echo/INDEX.md` and `Echo/docs/REPO_AUDIT.md` as
  `AWAITING FRAGMENT` — building the seven lesson pages is a follow-up, not
  done in this pass.
- Added `## Related SSL Projects` to `README.md`.

### Accessible by Design (Accessibility Audit Lab)

- Added the ecosystem nav + breadcrumb to all 5 pages that are actually part of
  the deployed public site (`src/site/index.html`, `about.html`,
  `website-check.html`, `pdf-check.html`, `p5-check.html`), confirmed against
  `vite.site.config.ts` and the `deploy-pages.yml` build step.
- Confirmed `src/web/index.html` (dev-only React UI, built by a separate,
  non-deployed script) and `examples/*/index.html` (test fixtures) are correctly
  **not** part of the public site and were left untouched.
- Already linked back to Small Systems Lab from `README.md`; added
  `## Related SSL Projects` alongside it.
- **Gap**: the project's own self-audit tool (`npm run audit`, Playwright +
  axe-core) could not be run against the changed pages in this sandbox — the
  network proxy blocks the Playwright Chromium download. Unit tests
  (`npm run test`, 23 tests) and a full `npm run build:site` both passed; a
  manual structural check (single `<h1>`, skip link, tag balance) was done as a
  substitute. **Recommend running the real axe-core audit** against the 5
  changed pages before treating this repo's accessibility posture as fully
  verified.

### Alt Text Wiki (`alt-text-wiki.lnc`)

- No README previously existed. Added one, explicitly marking the repo
  **legacy/archive** and pointing to Accessible by Design and the Small Systems
  Lab hub for current work.
- Added a small, visible archive-status banner to `index.html` linking to both,
  without redesigning the legacy pages themselves (per the mission's own
  instruction to treat this as legacy unless actively revived).
- This repo predates the shared SSL visual system (`variables.css`/`site.css`)
  and was intentionally **not** brought onto it, to avoid implying active
  investment in a repo that isn't being revived.

## Orphaned / out-of-scope items found, not fixed in this pass

- **Ounjẹ** — named as a sixth SSL branch in the hub's `README.md`/`index.html`,
  but has no repository or site. Left unlinked; inventing a URL would violate
  the ecosystem's own no-fabrication norms (explicit in the `Umada` and
  `Earth-Sensors-Lab` `CLAUDE.md` files, and implicit everywhere else).
- **[omoluabi-news](https://github.com/ukadike/omoluabi-news)** — a stub repo
  (only a `README.md` and empty `docs/`) for a future "portable newsroom"
  implementation of Omoluabi. It already links back to Omoluabi and Small
  Systems Lab correctly, and its own README already flags "Needs Kemi review:
  confirm scope." It wasn't in the 8-repo scope this pass was chartered to
  cover, so it's noted here rather than changed.

## Recommended next steps

1. Run the Accessible by Design project's real `npm run audit` (axe-core) against
   the 5 changed site pages in an environment where the Playwright browser
   download isn't blocked, to confirm no accessibility regressions were
   introduced by the new nav/breadcrumb markup.
2. Build the seven individual Echo lesson pages (or at least per-lesson anchors
   in `README.md`) so the lesson roadmap can link to real destinations instead
   of one shared anchor.
3. Decide Ounjẹ's status: either scaffold a minimal repo/site, or change its
   framing from "In development" to something more explicit like "Not yet
   started" if it's not actually in progress.
4. Decide whether `omoluabi-news` should be folded into the canonical ecosystem
   sitemap (`SITE_MAP.md`) once it has real content, or left as an internal
   Omoluabi satellite.
5. Consider adding a breadcrumb strip to Small Systems Lab's own homepage for
   strict consistency with every other repo, even though — as the hub itself —
   its primary nav already marks "Home" as the current page.
