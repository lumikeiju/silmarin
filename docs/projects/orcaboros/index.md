<!-- @format -->

# Orcaboros

Browser-based tool for comparing GTFS transit stops with OpenStreetMap and preparing reviewed changes for JOSM.

- **Website**: [lumikeiju.dev/orcaboros](https://lumikeiju.dev/orcaboros/)
- **Repository**: [github.com/lumikeiju/orcaboros](https://github.com/lumikeiju/orcaboros)

This manual covers the end-user workflow in Orcaboros **v1.0.0**: preparing inputs, configuring mappings, finding existing features, reviewing differences, and handing the result to JOSM.

!!! warning "Beta software and OSM contributions"

    Check every proposed change against the feed and current OpenStreetMap data. Confirm that each feed's licence permits contributing derived data to OSM, and follow the [OSM Automated Edits Code of Conduct](https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct). An automatic match is evidence to review, not permission to upload.

## Manual

Read the chapters in order for a first session, or use them as references.

| Chapter                                                            | Contents                                                                     |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| [Getting started](01-getting-started.md)                           | Requirements, feed IDs, ZIP import, supported rows, and diagnostics          |
| [Mapping profiles](02-profiles.md)                                 | Stock profiles, every editor setting, tag mappings, and profile files        |
| [Retrieving OSM data](03-retrieval.md)                             | Overpass endpoints, basemaps, query coverage, cancellation, and limits       |
| [Reviewing changes](04-review.md)                                  | Queue categories, automatic matches, decisions, comparisons, and map linking |
| [Exporting to JOSM](05-export.md)                                  | Partial exports, conflicts, file contents, and final inspection              |
| [Sessions and troubleshooting](06-sessions-and-troubleshooting.md) | Saving, recovery, reset, accessibility, privacy, and common problems         |
| [Profile JSON reference](07-profile-reference.md)                  | Schema fields, rule types, applicability, and a complete example             |

## The workspace

![Orcaboros desktop workspace with the workflow sidebar, linked stop on the map, review queue, decision buttons, and tag comparison](../../resources/images/orcaboros/workspace-light.png#only-light)
![Orcaboros desktop workspace with the workflow sidebar, linked stop on the map, review queue, decision buttons, and tag comparison](../../resources/images/orcaboros/workspace-dark.png#only-dark)

_Desktop overview from the Orcaboros repository, showing the application's dark theme._

The five numbered panels are **Upload**, **Profile**, **Retrieve**, **Review**, and **Export**. Expand a panel to return to its controls. The review workspace combines the map, queue, decision buttons, and comparison table; on narrower screens these areas stack vertically.

The progress indicator tracks resolved items, including automatic matches and OSM-only items kept unchanged. It is not a count of edits that will be uploaded. The Export panel separately reports the number of GTFS features ready for export.

## Important boundaries

- Only the ZIP's `stops.txt` is read. Orcaboros does not import routes, timetables, or the rest of the GTFS schedule.
- GTFS processing happens locally in the browser. OSM retrieval and basemap loading require network access.
- Candidates are a bounded selection of OSM nodes and platform ways, not a complete model of the transport network.
- The comparison table is read-only. It does not expose individual tag-resolution controls.
- Exact automatic matches can be exported even if you have not clicked **Accept match**. Reveal and inspect the **exact** queue category.
- OSM-only items labelled **removed** do not produce deletions.
- The result is a JOSM-compatible **`.osm` file**. Orcaboros does not upload to OSM, control JOSM remotely, or provide account-based/cloud session storage.

## About this manual

The documentation was checked on **2026-10-31** against the deployed v1.0.0 interface and [source revision `ec79d82`](https://github.com/lumikeiju/orcaboros/tree/ec79d82aea13100e97a96f84cf273a53d75c0669). It adapts the project's [README](https://github.com/lumikeiju/orcaboros/blob/ec79d82aea13100e97a96f84cf273a53d75c0669/README.md), [mapping-profile guide](https://github.com/lumikeiju/orcaboros/blob/ec79d82aea13100e97a96f84cf273a53d75c0669/docs/mapping-profiles.md), and verified application behavior.

The [desktop overview](https://github.com/lumikeiju/orcaboros/blob/ec79d82aea13100e97a96f84cf273a53d75c0669/src/assets/screenshot-dark.png) is an existing project image. Other screenshots use the compact browser layout and a **fictional `MANUAL-DEMO` feed with synthetic OSM responses**. Those examples illustrate controls and states; their stops, identities, and changes must not be uploaded to OpenStreetMap.
