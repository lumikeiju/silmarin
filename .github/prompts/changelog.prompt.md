---
description: Generate a changelog entry from recent commits and prepend it to CHANGELOG.md
---

<!-- @format -->

# Generate Changelog Entry

You are generating a new changelog entry for the TCAT Wiki from recent git commit history. This project follows [Conventional Commits](https://www.conventionalcommits.org/) and [Semantic Versioning](https://semver.org/).

## Step 1 — Collect commit history

Run the following command to get all commits since the last version tag:

```powershell
git log $(git describe --tags --abbrev=0)..HEAD --pretty=format:"%s" 2>$null
# If no tags exist yet, use: git log --pretty=format:"%s"
```

Read `CHANGELOG.md` to find the most recent version number (the last `## vX.Y.Z` heading), and read `pyproject.toml` or any other version source if present.

## Step 2 — Determine the new version

Apply Semantic Versioning rules to the collected commits, starting from the current version:

- Any commit with a `BREAKING CHANGE` footer or a `!` suffix (e.g. `feat!:`) → **major** bump
- Any `feat(...):` commit → **minor** bump
- Only `fix`, `chore`, `docs`, `style`, `refactor`, `perf`, `test`, etc. → **patch** bump

Use the highest applicable rule. State the resulting new version explicitly.

## Step 3 — Build the changelog entry

From the commit list, produce a changelog section using the template below.

**Inclusion rules:**

- `feat(...):` → **Features**
- `fix(...):` → **Fixes**
- All other types (`chore`, `docs`, `style`, `refactor`, `ci`, version-bump commits, merge commits) → **omit**

**Writing rules:**

- Rewrite terse or cryptic subjects into plain English
- Keep the scope in parentheses if it adds useful context, e.g. `(docs-workspaces)`
- Group closely related commits into a single bullet rather than listing each individually
- Omit the section heading entirely if it would be empty

**Template:**

```markdown
## vX.Y.Z (YYYY-MM-DD)

### Features

- Description of feature one
- Description of feature two

### Fixes

- Description of fix one
```

## Step 4 — Prepend to CHANGELOG.md

Insert the new entry immediately after the header block in `CHANGELOG.md` (below the last line of introductory prose, before the first existing `## v` entry or the end of the file).

Do not modify any existing entries.

## Step 5 — Report back

After editing `CHANGELOG.md`, respond with:

1. The new version number
2. The full text of the entry you inserted
3. Any commits you omitted due to the inclusion rules (one-line summary is fine)
4. Any commits that looked potentially miscategorized — where the `feat`/`fix` type seemed inconsistent with the actual change described
