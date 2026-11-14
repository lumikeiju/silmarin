---
description: Project-wide instructions for Silmärin
applyTo: "**"
---

<!-- @format -->

# Silmärin

Silmärin is Lumikeiju’s documentation source for project user manuals and tutorials, built with Zensical (`zensical.toml`).

- Edit source Markdown under `docs/`; follow nearby project/topic structure and link new pages from the relevant index.
- Write accurate, task-oriented guidance. Verify product behavior, prerequisites, UI labels, and outcomes; never invent details.
- Match nearby Markdown conventions: concise headings, language-tagged code fences, relative links, and useful frontmatter.
- Use descriptive alt text and captions for images; follow existing asset paths and light/dark image patterns.
- Keep changes focused. Never edit generated output in `site/`.
- `main` holds source; `beta`/`stable` hold built files only. Never merge source into them; deploy only via `.github/workflows/promote.yml`.
- Validate documentation changes with `.\.venv\Scripts\zensical.exe build --clean`.
