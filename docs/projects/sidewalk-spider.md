<!-- @format -->

# Sidewalk Spider

!!! example "Sidewalk Spider is currently under construction!"

An interactive "web" tool <small>(see what I did there?)</small> for associating sidewalks and crossings with streets in OpenStreetMap.

- **Website**: [lumikeiju.dev/sidewalk-spider](https://lumikeiju.dev/sidewalk-spider)
- **Repository**: [github.com/lumikeiju/sidewalk-spider](https://github.com/lumikeiju/sidewalk-spider)

## Overview

Sidewalk Spider weaves associations between footways and the streets they accompany, turning a tedious tagging chore into a visual, low-friction, slightly gamified interaction.

## Workflow

1. Fetch nearby data via the Overpass API
2. Visually associate sidewalks and crossings with their parent streets
3. Auto-save progress to `localStorage`
4. Export the resulting changeset as an OSM file ready for upload
