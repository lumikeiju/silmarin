<!-- @format -->

# Changelog

Changes to Silmärin are documented here.

This project adheres to [Semantic Versioning](https://semver.org/) and [Conventional Commits](https://www.conventionalcommits.org/).

## v2.1.0 (2026-11-14)

### Features

- Add an illustrated Tarralappu v2.1.0 manual covering setup, prompts, models, generation, references, refinements, media, costs, and troubleshooting.
- Update the project catalogue to link readers to the detailed Tarralappu guide.
- Enable GLightbox for enlarging documentation images, with separate galleries for light and dark themes.

## v2.0.0 (2026-10-31)

### Features

- Refresh the project catalogue to cover all nine public GitHub repositories, adding lumikeiju.dev, Saarelai, Orcaboros, and Tarralappu.
- Add an illustrated Orcaboros v1.0.0 user manual covering setup, mapping profiles, OSM retrieval, review, JOSM export, sessions, troubleshooting, and profile JSON.
- Add 14 themed screenshot assets and update the homepage and catalogue to introduce user manuals and reference material.

### Fixes

- Correct Orcaboros documentation for skipped-stop identities, automatic-match export, read-only tag comparisons, and profile validation restrictions.
- Clarify Python 3.11+ setup, virtual-environment recovery, dependency updates, and screenshot capture and processing instructions.
- Remove the standalone ArkkiSnappi and ImproveNode pages; their project overviews are now included in Saarelai.

### Dependencies

- Pin Zensical to 0.1.1 and Pillow to 13.0.0.
- Use the shared requirements manifest for CI and site builds.

### Deployment

- Add CI builds for pushes and pull requests, and replace automatic deployment with manual `main` → `beta` → `stable` promotion. Stable publishes the tested beta artifact without rebuilding.
- Attach site ZIPs, checksums, manifests, and provenance to beta and stable releases.

## v1.0.0 (2026-04-19)

### Features

- Initial refresh
