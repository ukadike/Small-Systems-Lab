# SCHEMA CARD — Small Systems Lab

A quick-orientation card for future code agents and contributors. For fuller detail, do
not rely on this card alone — go to the files it points to.

## Project name

Small Systems Lab (SSL)

## Purpose

Small Systems Lab is the ecosystem hub: a public-interest studio for tender systems —
civic tools, editorial intelligence, accessibility infrastructure, food memory,
environmental sensing, speculative storytelling, and AI literacy. It treats care,
documentation, rule-based intelligence, and accessibility as infrastructure, not
decoration. This repository is the static-site hub that ties together every SSL branch
project and hosts SSL's own method documentation. Founded by Adekemi (Kemi) Sijuwade
Ukadike.

## Audience

- **Visitors / the public** — entry point: `index.html` (the live GitHub Pages site).
- **Contributors** — entry point: `README.md`.
- **Future code/steward agents** — entry point: this file, `INDEX.md`, `claude/CLAUDE_HANDOFF.md`.

## Core concepts

SSL builds systems around five linked practices, documented in `docs/`:

- **SSL Method** (`docs/ssl-method.md`) — a care-centered systems method: operations
  before aesthetics, rules before automation, accessibility before scale, context before
  publication, geometry before interface clutter, public memory before extraction. SSL
  does not treat AI as magic; it treats intelligence as a governed system of rules,
  roles, checks, consent, and review.
- **Operations of Care** (`docs/operations.md`) — the hidden structure of SSL: intake,
  consent, documentation, review, escalation, publishing, archiving, correction, access
  support, community feedback, maintenance. An SSL project should always be able to
  explain who decides, who reviews, who can pause publication, and what happens when
  harm is possible.
- **Rule-Based Intelligence** (`docs/rule-based-intelligence.md`) — the SSL approach to
  AI and automation: consent rules, source rules, access rules, risk rules, translation
  rules, evidence rules, accessibility rules, publishing rules, override rules, archival
  rules. The intelligence lives in the structure — the questions, constraints, review
  loops, and human authority around the tool — not in the model deciding alone.
- **Ancient Geometry as Interface Logic** (`docs/ancient-geometry.md`) — geometry as a
  way to organize knowledge, movement, memory, and decision-making, not decoration:
  circle (consent, return, review, community, continuity), triangle (source, witness,
  context; or care, rule, evidence), grid (archive, taxonomy, navigation, editorial
  order), spiral (memory, recurrence, learning, time, repair), golden ratio/rectangle
  (calm proportions, interface hierarchy, visual balance), threshold (publish / do not
  publish, safe / unsafe, verified / incomplete), crossroads (ethical decision points).
- **Accessibility as Architecture** (`docs/accessibility.md`) — a founding constraint,
  not an add-on: keyboard-only operation, screen reader compatibility, high contrast,
  captions, transcripts, alt text, plain-language summaries, multimodal outputs,
  tactile/printable options where possible, low-bandwidth and offline-first thinking.
- **Public Knowledge Stewardship** — preserving memory, context, local testimony, and
  civic information for communities and future histories (described in `README.md` and
  `index.html`; no dedicated `docs/` file yet — see `docs/REPO_AUDIT.md`).
- **Branches** (`docs/branches.md`) — one-paragraph descriptions of each SSL project.

## Interfaces

- **Public site** — `index.html`, framework-free static HTML. `variables.css` is the
  locked SSL visual system (design tokens: colors, type, spacing, borders, focus states,
  print and dark-mode notes, and shared components like `.btn` and `.card`). `site.css`
  adds only page layout (max-width wrapper, header/footer, grid, dividers) and does not
  redefine tokens. No build step, no JavaScript.
- **Documentation layer** — plain Markdown in `docs/`, `README.md`, `INDEX.md`,
  `SCHEMA_CARD.md`, read by humans and by code/steward agents.

## Inputs / Outputs

- **Inputs**: none beyond source edits to the Markdown/HTML/CSS files in this repo.
- **Outputs**: the public static site, served via GitHub Pages (`.nojekyll` present at
  root, so Jekyll processing is disabled and files are served as-is).

## Dependencies

None beyond a static-file host. No package.json, no build tooling — by design, matching
the rest of the SSL ecosystem's framework-free static sites.

## Related repos (SSL ecosystem)

- **[Omoluabi](https://github.com/ukadike/omoluabi)** — editorial intelligence for civic
  documentation, consent-aware reporting, provenance, accessibility, human-governed
  publishing. Live site: <https://ukadike.github.io/omoluabi/>.
- **[Earth Sensors Lab](https://github.com/ukadike/Earth-Sensors-Lab)** — accessible
  STEAM observatory for young people, families, educators, gardens, climate sensing.
  Live site: <https://ukadike.github.io/earth-sensors-lab/>.
- **[Echo](https://github.com/ukadike/Echo)** — AI literacy, creative technology
  education, prompts, workshops, public learning. Live site:
  <https://ukadike.github.io/echo/>.
- **[Umada](https://github.com/ukadike/Umada)** — speculative worldbuilding, future
  history, systems collapse, language memory, civic signs, the Omoluabi device as
  narrative artifact. Live site: <https://ukadike.github.io/umada/>.
- **[Accessible by Design / Accessibility Audit Lab](https://github.com/ukadike/accessible-by-design-prototyping)**
  — WCAG 2.2+ auditing toolkit for websites, p5.js sketches, and PDFs. No GitHub Pages
  deployment found at time of this audit (see `docs/REPO_AUDIT.md`).
- **Ounjẹ** — food memory, healing recipes, cultural documentation, cooking as archive.
  In development; no public repository found at time of this audit.

Every branch above with a live site links back to this hub
(`https://ukadike.github.io/small-systems-lab/`) from its own site footer.

## Accessibility considerations

Accessibility is treated as infrastructure, matching `docs/accessibility.md`: semantic
HTML, skip link, visible focus states (from `variables.css`), keyboard access, no
color-only meaning, logical heading order (single `h1`, then `h2` sections, `h3` cards).
No images currently in the site, so no outstanding alt-text gaps. See
`docs/REPO_AUDIT.md` for the accessibility pass done during this restoration.

## Future implementation notes

- `docs/` has no dedicated file for "Public Knowledge Stewardship" (the fifth method
  practice named in `README.md`/`index.html`) — flagged in `docs/REPO_AUDIT.md`, needs
  Kemi review on whether to add one.
- Ounjẹ and Accessible by Design have no live GitHub Pages sites yet; their `index.html`
  cards should be updated to `.btn` links once sites exist.
- A parallel, unmerged branch on this repo (`claude/github-pages-navigation-links-6t45r6`)
  already adds a primary nav header, a `/sitemap/` page, SEO meta tags, `robots.txt`,
  `sitemap.xml`, and a WCAG-AA contrast fix to `--color-muted`. Not merged as part of
  this pass — flagged for Kemi review in `docs/REPO_AUDIT.md`.
