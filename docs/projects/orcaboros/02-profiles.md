<!-- @format -->

# Mapping profiles

A profile defines how imported stops become proposed OSM tags, which existing tags to remove, which coordinates to retain, and how far away to search for matches. Inspect it before retrieving candidates.

!!! warning "Profile changes invalidate review work"

    Applying a compatible profile change reprocesses the imported stops and clears the candidate results, reviews, and export draft. Retrieve OSM data again afterward. Export any useful work before changing mappings or radii mid-session.

## Stock profiles

The upload feed ID must match one of these IDs to select its stock profile.

| Feed ID     | Agency                   |
| ----------- | ------------------------ |
| `US-WA-CT`  | Community Transit        |
| `US-WA-ET`  | Everett Transit          |
| `US-WA-IT`  | Intercity Transit        |
| `US-WA-KCM` | King County Metro        |
| `US-WA-KT`  | Kitsap Transit           |
| `US-WA-PT`  | Pierce Transit           |
| `US-WA-SCM` | Seattle Center Monorail  |
| `US-WA-ST`  | Sound Transit            |
| `US-WA-WSF` | Washington State Ferries |

When **every** imported feed has a stock profile, Orcaboros combines them. Their sections initially collapse and display **Auto-matched**; expand each one to inspect its settings. This profile-selection label is separate from an automatically matched OSM feature.

If any feed ID is unknown, the application creates a blank custom profile for all selected feeds. It has no field mappings, additional tags, or removal keys. Configure it yourself or import a compatible profile; do not assume the other feeds kept their stock rules. Custom feed IDs are not added to the stock registry.

Stock profiles:

- Map `stop_name_expanded` to `name`.
- Map `stop_code` to `gtfs:stop_code:<FEED_ID>`.
- Do **not** map `stop_id` to an output tag.
- Propose `public_transport=platform` and `highway=bus_stop` for platform rows.
- Propose removing `gtfs:stop_id`, `gtfs:stop_id:<FEED_ID>`, and `gtfs:feed` from matched elements.

These are the supplied defaults, not a guarantee that every resulting tag suits every transport mode or feature. Station rows do not receive the platform-only constants.

## Matching radii

![Profile editor showing the fictional feed's candidate and auto-match radii, OSM geometry target, name cleanup, and field mapping table](../../resources/images/orcaboros/profile-light.png#only-light)
![Profile editor showing the fictional feed's candidate and auto-match radii, OSM geometry target, name cleanup, and field mapping table](../../resources/images/orcaboros/profile-dark.png#only-dark)

_Fictional profile with 50 m candidate and 10 m auto-match radii. More mapping rows continue below the visible area._

| Setting                  | Default | Effect                                                                              |
| ------------------------ | ------- | ----------------------------------------------------------------------------------- |
| **Candidate radius (m)** | 50      | Controls the nearby candidate search and the retrieval padding                      |
| **Auto-match radius**    | 10      | Maximum distance for a unique exact-identity candidate to be automatically selected |

Both values must be greater than zero and at most 10,000 m. The auto-match radius cannot exceed the candidate radius.

Increasing a radius does not make proximity reliable evidence of identity. Name similarity and distance alone never produce an automatic match; see [matching behavior](04-review.md#matching-and-automatic-decisions).

## Geometry target

Each feed has a **Geometry target** switch:

- **OSM**, the default, preserves the selected existing OSM element's position.
- **GTFS** uses the feed coordinates for matched **nodes**.

Platform ways retain their member geometry with either setting. Their center is used for matching, not as a replacement for the way's shape. New nodes use GTFS coordinates regardless of this switch.

Check locations against the actual stop or platform. Choosing GTFS does not establish that the feed coordinates are more accurate.

## Street name cleanup

**Street name cleanup** is enabled by default. It cleans all-uppercase names and expands supported US street abbreviations and directions.

The cleaned value is available as `stop_name_expanded`. The original `stop_name` remains available, so a mapping can deliberately use the raw name instead. This is name processing, not translation or a general international address-normalization service.

Review the example outputs and the final comparison, especially when working outside the stock profiles' region.

## GTFS fields to OSM tags

The **GTFS fields to OSM tags** table pairs an imported or computed field with an OSM key. Enter the destination key beside the field you want to use.

- A blank OSM key means **ignore this field**.
- Examples show how values from the imported feed map to the chosen key.
- A field's presence in the CSV does not mean it should be copied into OSM.
- Empty resolved values do not produce tags.
- Active mappings must use valid keys and values; duplicate output keys applying to the same feature are invalid.

Useful computed fields are `stop_name_expanded`, `source_feed_id`, and `source_feed_name`. The [JSON reference](07-profile-reference.md) also describes feed- and location-specific rules.

## Additional OSM tags

Use **Add OSM tag** to add a constant key/value rule under **Additional OSM tags**. These rules belong to the feed section containing them.

Existing rules may instead take a value from a GTFS field or the feed's metadata. The editor identifies that source; it is not a free-text constant value. Use [profile JSON](07-profile-reference.md#rule-values-and-applicability) for those rule types and explicit applicability restrictions.

A partially filled editor row is inactive. Complete it before expecting an output tag, or clear/remove it if it was accidental. Inactive rows are omitted from exported profile JSON.

## OSM keys to remove

Use **Add OSM key to remove** under **OSM keys to remove** to name an existing tag key that should be removed from matched elements.

- Removal rules apply to matched OSM elements, not new nodes.
- An active mapping for the same key takes precedence over removal.
- Unmapped keys not selected for removal are preserved.
- Matching legacy generic GTFS identities can also produce identity-tag removal proposals.

Feed-specific `gtfs:stop_id:<FEED_ID>` tags can therefore help identify a match even when the profile proposes removing them from the result. Identification and output tagging are separate operations.

The [comparison defaults](04-review.md#what-happens-to-tags) explain which values are retained. The current UI does not provide a separate accept/reject control for each tag removal.

## Managing profile JSON

- **Export profile JSON** saves the active mapping configuration for reuse. It does not back up the entire session.
- **Import profile JSON** loads and validates a profile file.
- **Reset stock profile** returns to the combined stock configuration, subject to compatibility with the currently imported feeds.

An imported profile must enable **every imported feed**. Invalid active rules or an incompatible feed selection are rejected rather than replacing the working profile.

Resetting to stock cannot supply a stock definition for an unknown custom feed. If your session includes such a feed, the reset may be rejected; use or edit a compatible custom profile instead.

When the profile is ready, select **Continue to OSM retrieval**.

**Next:** [Retrieving OSM data](03-retrieval.md).
