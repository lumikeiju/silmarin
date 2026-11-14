<!-- @format -->

# Exporting to JOSM

Orcaboros exports a **JOSM-compatible `.osm` file**. It does not upload changes to OpenStreetMap or send them to JOSM through Remote Control.

## Check what will be included

Export supports partial progress:

- **auto-matched**, **match-selected**, and **create-selected** stops are eligible.
- **unreviewed** and **skipped** stops are excluded.
- OSM-only items kept unchanged do not produce deletions.

Queue filters affect visibility, not export eligibility. In particular, hiding the exact category does not exclude its automatic matches.

Before downloading:

1. Reveal **exact** in the review filters and inspect automatic matches.
2. Check every selected candidate and every proposed new node.
3. Confirm geometry settings, tag additions, preserved values, and removals.
4. Resolve conflicting decisions.
5. Verify that the ready-to-export count agrees with the decisions you intend to include.

## Download the file

1. Expand **Export**.
2. Read the number of features ready to export.
3. Select **Download JOSM OSM File**.
4. Save the downloaded `.osm` file.

![Export panel showing three of four fictional GTFS features ready and the Download JOSM OSM File button](../../resources/images/orcaboros/export-light.png#only-light)
![Export panel showing three of four fictional GTFS features ready and the Download JOSM OSM File button](../../resources/images/orcaboros/export-dark.png#only-dark)

_Fictional partial export: one automatic match, one accepted match, and one new node; the remaining unreviewed stop is excluded. Never upload this demonstration data._

The button is disabled while work is in progress, before OSM retrieval, or when there are no exportable decisions. The application validates and saves the draft before initiating the browser download. A storage or validation failure must be resolved rather than treated as a successful export.

The overall progress indicator can differ from the export count because it also includes OSM-only items reviewed unchanged.

## What the file contains

The file can contain:

- New nodes at GTFS coordinates, with profile-generated tags.
- Selected existing nodes with their retained IDs and versions.
- Selected platform ways with their retained IDs, versions, and member references.

The profile's geometry target controls matched-node coordinates. Way members are not moved by the GTFS geometry option. No element deletions are exported.

The file includes the default changeset metadata:

| Key       | Default value                                                  |
| --------- | -------------------------------------------------------------- |
| `comment` | `Edit public transport features using GTFS data \| #Orcaboros` |
| `host`    | `https://lumikeiju.dev/orcaboros/`                             |

Inspect and complete the changeset information in JOSM for the actual contribution. An error may use the generic phrase "OSM Change export"; that does not make the downloaded format an `.osc` file.

An export is an editing artifact, **not a full session backup**. Orcaboros does not import it to restore the review queue.

## Conflicts that block export

Two stops from the **same feed** cannot claim the same OSM element. Different feeds may share one element only when their geometry and tag decisions agree.

Export can therefore be blocked by:

- Duplicate claims within one source feed.
- Conflicting tags proposed for a shared OSM element.
- Different required coordinates for a shared element.
- Invalid coordinates, tags, element data, or inconsistent draft state.

Read the validation details. Where the interface links to affected review items, follow those links and reconcile the decisions. Verify which stop actually belongs to the element; do not create a duplicate node merely to bypass the conflict.

If correcting the profile is necessary, remember that applying it invalidates the existing candidates and reviews.

## Inspect in JOSM

Open the downloaded file in JOSM and inspect it against current OSM data before considering an upload.

- Check for duplicate stops or platforms.
- Check each changed or created object's position.
- Verify names, mode-specific tagging, added stop codes, retained tags, and proposed removals.
- Confirm that platform ways still have the intended members and geometry.
- Resolve stale-data or upload conflicts using current OSM information.
- Review JOSM's validation messages and the final upload summary.
- Confirm the feed's permitted use, the applicable community process, and the actual changeset description.

No JOSM screenshot is included here: the illustrated workflow ends at Orcaboros's export controls. For JOSM's own interface, use the [JOSM help](https://josm.openstreetmap.de/wiki/Help).

**Next:** [Sessions and troubleshooting](06-sessions-and-troubleshooting.md).
