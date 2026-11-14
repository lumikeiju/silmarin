<!-- @format -->

# Reviewing changes

The review workspace connects three panes: **Review Queue**, **Decision**, and **Comparison**, alongside the map. Open **Review**, then use **Open Review Queue** if needed.

## Matching and automatic decisions

Candidates are ordered by:

1. Exact feed-specific identity.
2. Normalized, expanded-name agreement.
3. Distance.
4. Element ID as a tie-breaker.

An automatic match requires **exactly one** exact-identity candidate within the auto-match radius. Matching names or short distances alone never auto-select a candidate.

!!! warning "Inspect automatic matches before export"

    The **exact** category is hidden by default, but its **auto-matched** stops can already be included in an export. Open **Filters**, enable **exact**, and check them individually. You do not have to click **Accept match** for an automatic match to become exportable.

## Queue categories and filters

Categories describe the relationship to retrieved identity evidence. They do not determine what you should edit.

| Category    | Meaning                                                                         | What not to assume                                                                                 |
| ----------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| **new**     | No exact-identity candidate was found                                           | An existing untagged or differently tagged OSM stop may still be the right match                   |
| **moved**   | Exact identity exists beyond the auto-match radius                              | The feed coordinates are not automatically more accurate                                           |
| **exact**   | Exact identity exists within the auto-match radius                              | The tags, coordinates, and identity still need checking; ambiguity can prevent automatic selection |
| **removed** | A retrieved OSM identity is absent from all valid stop IDs in the imported feed | The physical feature has not necessarily disappeared                                               |

**Filters** independently toggles new, removed, moved, and exact results. New, removed, and moved are enabled initially; exact is initially disabled. Changing a filter hides or reveals items but does not discard their decisions or exclude them from export.

![Review queue with category filters open and the exact category enabled, exposing an automatically matched fictional stop](../../resources/images/orcaboros/filters-light.png#only-light)
![Review queue with category filters open and the exact category enabled, exposing an automatically matched fictional stop](../../resources/images/orcaboros/filters-dark.png#only-dark)

_Fictional examples show an automatic match, an accepted match, and an unreviewed stop. Category counts and decision states are separate._

The queue shows ten results per page. When more than one page is needed, use **First**, **Previous**, **Next**, and **Last**. The result range describes the filtered list; the queue's total can be larger. If nothing is shown, use **Check filters?** or reopen Filters before concluding that review is finished.

## Make a decision

Select a queue item or its map-focus control. Check the candidate, tags, and coordinates before using the Decision pane.

| Action                   | Result                                                                                 |
| ------------------------ | -------------------------------------------------------------------------------------- |
| **Accept match**         | Records the selected candidate as the OSM element for this stop                        |
| **Skip feature**         | Leaves the stop out of the export                                                      |
| **Create separate node** | Proposes a new node at the GTFS coordinates instead of modifying an existing candidate |

Accept match requires a candidate. Creating a separate node is an explicit choice, not the required action for every item labelled new. Check for existing features before creating duplicates.

Decision-pane actions advance to the next visible item. You can revisit a stop and change its decision. For a different existing candidate, use the [map's link controls](#using-the-map).

The state labels record your progress:

| State               | Export treatment                                |
| ------------------- | ----------------------------------------------- |
| **unreviewed**      | Excluded                                        |
| **auto-matched**    | Included without an additional acceptance click |
| **match-selected**  | Included as a selected existing element         |
| **create-selected** | Included as a new node                          |
| **skipped**         | Excluded                                        |

These are decision states, not the new/moved/exact categories. A new-category stop can become match-selected after you identify an existing OSM feature.

## Read the comparison

![Decision buttons above the read-only comparison for a fictional moved stop, with GTFS and OSM tags and a 20 metre match distance](../../resources/images/orcaboros/comparison-light.png#only-light)
![Decision buttons above the read-only comparison for a fictional moved stop, with GTFS and OSM tags and a 20 metre match distance](../../resources/images/orcaboros/comparison-dark.png#only-dark)

_Fictional moved stop. The comparison proposes a stop-code tag and shows an existing identity tag; location metadata is separate from OSM tags._

The left side shows **profile-mapped GTFS tags**, not every raw CSV field. The right side shows the selected OSM element's tags. Coordinates and calculated match distance appear in a separate metadata table below.

Addition and removal/replacement highlighting draws attention to differences. **The table is read-only:** there are no per-tag checkboxes, value editors, or accept/reject controls in this interface. Highlighting is not a promise that every differing GTFS value will overwrite OSM.

## What happens to tags

For a selected match, the default proposal behaves as follows:

| Situation                                                                   | Default result                                       |
| --------------------------------------------------------------------------- | ---------------------------------------------------- |
| A mapped key is missing from OSM                                            | Add the proposed value                               |
| An existing OSM key has no mapping or removal rule                          | Preserve it                                          |
| A mapped value differs from the existing value                              | Normally keep the current OSM value                  |
| Existing and proposed `name` values are equivalent after name normalization | Accept the proposed name form                        |
| An existing key is configured for removal                                   | Remove it unless an active mapping supplies that key |

New nodes receive the profile's resolved tags and have no existing OSM tags to preserve.

If these defaults are not the desired result, either revise the profile and retrieve/review again, or make the necessary final changes in JOSM. Do not assume that clicking a highlighted comparison cell changes the export.

## OSM-only items

An item labelled **removed** has an identity absent from all valid stop IDs in the imported feed, not just the eligible stops. A row with a valid `stop_id` remains in that identity set even if its coordinates or location type prevent it from being reviewed. A feed change, omitted row, or invalid `stop_id` can still leave an OSM identity absent; this is not proof that the physical feature disappeared.

Inspect it, then use **Keep OSM element unchanged** to record that review. Orcaboros does not propose or export an element deletion. An item kept unchanged contributes to review progress, but it is not an additional edited GTFS feature in the export count.

## Using the map

Use the queue's focus controls to locate a feature. Map and queue focus are synchronized. Pan and zoom to inspect the surroundings, and open feature popups to distinguish mapped GTFS tags from existing OSM tags.

The expandable **Map Legend** explains match-found, moved, unmatched, removed, pending, reviewed, candidate, and connection symbols. Focused and alternative candidates have distinct indicators.

Individual feature detail appears at **zoom 11 and above**. At lower zooms, **Zoom in to view data** explains why detail is hidden; established connections remain visible. A hidden point at low zoom is not a failed import.

To link a stop to another retrieved candidate:

1. Open the GTFS stop's popup.
2. Select **Change Link**.
3. Preview the connection and choose the intended retrieved OSM candidate.
4. Commit the new target by selecting it on the map.

The original connection remains until a replacement is committed. Use **Cancel Link** or **Escape** to cancel without replacing it. Proximity alone does not establish a valid match, and basemap-only features are not selectable retrieved candidates.

If WebGL2 or map initialization fails, use **Retry map**. The review queue remains available, but do not approve uncertain geometry simply because the map is unavailable.

**Next:** [Exporting to JOSM](05-export.md).
