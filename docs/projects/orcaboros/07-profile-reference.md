<!-- @format -->

# Profile JSON reference

Use **Import profile JSON** and **Export profile JSON** in the [Profile editor](02-profiles.md#managing-profile-json) to exchange configurations. A profile is data, not an executable script or an entire saved session.

## Top-level fields

| Field                   | Type   | Requirement                                                              |
| ----------------------- | ------ | ------------------------------------------------------------------------ |
| `schemaVersion`         | Number | Exactly `1`                                                              |
| `id`                    | String | Nonempty profile identifier                                              |
| `name`                  | String | Nonempty display name                                                    |
| `version`               | String | Nonempty profile version                                                 |
| `sourceFeeds`           | Array  | At least one source-feed definition, with unique IDs                     |
| `mappingRules`          | Array  | Tag rules; an empty array is allowed                                     |
| `candidateRadiusMeters` | Number | Greater than 0 and at most 10,000                                        |
| `autoIdRadiusMeters`    | Number | Greater than 0, at most 10,000, and no greater than the candidate radius |

The app's default radii are 50 m and 10 m, respectively. They are explicit fields in an exported schema-v1 profile.

## Source-feed definitions

Each entry in `sourceFeeds` describes one feed.

| Field               | Type                       | Meaning                                                                    |
| ------------------- | -------------------------- | -------------------------------------------------------------------------- |
| `id`                | String                     | Feed identity, using the same normalization and restrictions as upload IDs |
| `displayName`       | String                     | Nonempty source name                                                       |
| `enabled`           | Boolean                    | Whether the feed is enabled; every currently imported feed must be enabled |
| `geometryTarget`    | String                     | `"osm"` or `"gtfs"`; defaults to `"osm"` when absent                       |
| `streetNameCleanup` | Boolean                    | Whether to compute cleaned street names; defaults to `true` when absent    |
| `metadata`          | Object, optional           | String key/value metadata available to rules                               |
| `additionalTags`    | Array, optional            | Tag rules applied within this feed                                         |
| `removeKeys`        | Array of strings, optional | Existing OSM keys to remove; defaults to an empty array                    |

`US-WA-PSC` is not a valid configured source. A profile containing other feed IDs does not become a stock profile merely because it was imported.

The geometry setting moves matched nodes only when it is `"gtfs"`. Platform ways keep their member geometry, and new nodes always use feed coordinates.

## Rule values and applicability

Rules in `mappingRules` and per-feed `additionalTags` have:

- `key`: the output OSM tag key.
- `value`: one of the value objects below.
- `appliesTo`: an optional restriction.

| Value object                                         | Result                                            |
| ---------------------------------------------------- | ------------------------------------------------- |
| `{ "kind": "constant", "value": "platform" }`        | A literal value                                   |
| `{ "kind": "field", "field": "stop_name_expanded" }` | The value of an imported or computed field        |
| `{ "kind": "source-metadata", "key": "operator" }`   | The named value from the source feed's `metadata` |

Fields can name existing `stops.txt` headers, including `stop_id`, `stop_code`, `stop_name`, coordinates, `location_type`, and `parent_station`. Computed fields include:

| Field                | Value                                                |
| -------------------- | ---------------------------------------------------- |
| `stop_name_expanded` | The name after the feed's cleanup setting is applied |
| `source_feed_id`     | The source's feed ID                                 |
| `source_feed_name`   | The source's display name                            |

To restrict a rule, use either or both of these arrays:

```json
{
    "sourceFeedIds": ["MANUAL-DEMO"],
    "locationKinds": ["platform"]
}
```

That object is the value of `appliesTo`. Supported location kinds are `"platform"` and `"station"`. Without a restriction, the rule applies generally within its containing scope; an `additionalTags` rule still belongs to its own feed.

For example, this rule adds an operator value only to platforms in the named feed:

```json
{
    "key": "operator",
    "value": { "kind": "source-metadata", "key": "operator" },
    "appliesTo": {
        "sourceFeedIds": ["MANUAL-DEMO"],
        "locationKinds": ["platform"]
    }
}
```

The feed must supply the corresponding string in its `metadata` for that rule to have a value.

Rules cannot contain executable code, template expressions, arbitrary query filters, or Overpass QL. Empty values are omitted. Active keys/values must pass validation, and overlapping output keys for the same feature are invalid.

## Validation constraints

- OSM keys must be nonempty and at most 255 characters. Resolved values are limited to 255 characters. Control characters and invalid Unicode text are rejected.
- Field names must be nonempty, at most 255 characters, and contain no control characters. An unavailable field or metadata value resolves to an empty value and produces no tag.
- A `source-metadata` rule's lookup key must contain 1-64 ASCII letters, digits, underscores, periods, colons, or hyphens.
- Feed IDs in `appliesTo.sourceFeedIds` must exist in the profile. Within a feed's `additionalTags`, only that containing feed can be named.
- An explicitly empty applicability array matches nothing; omit the restriction to apply generally.

Identity output keys have additional requirements. A rule for `gtfs:stop_id:<FEED_ID>` must:

1. Name a feed configured in `sourceFeeds`.
2. Use `{ "kind": "field", "field": "stop_id" }` as its value.
3. Apply only to that feed. In a multi-feed profile, set `appliesTo.sourceFeedIds` to an array containing exactly that feed ID.
4. Apply to every location kind: omit `appliesTo.locationKinds`, even if the currently imported rows are all platforms.

For example:

```json
{
    "key": "gtfs:stop_id:MANUAL-DEMO",
    "value": { "kind": "field", "field": "stop_id" },
    "appliesTo": { "sourceFeedIds": ["MANUAL-DEMO"] }
}
```

This rule is optional and is not part of the stock output mappings. If you deliberately add it, its active mapped value takes precedence over a removal rule for the same key.

## Complete fictional example

This is the profile used for the manual's fictional `MANUAL-DEMO` feed. It illustrates the schema, **not approved tagging or data for a real import**.

```json
{
    "schemaVersion": 1,
    "id": "manual-demo",
    "name": "Fictional demonstration profile",
    "version": "1.0.0",
    "sourceFeeds": [
        {
            "id": "MANUAL-DEMO",
            "displayName": "Fictional manual examples",
            "enabled": true,
            "geometryTarget": "osm",
            "streetNameCleanup": true,
            "additionalTags": [
                {
                    "key": "public_transport",
                    "value": { "kind": "constant", "value": "platform" },
                    "appliesTo": { "locationKinds": ["platform"] }
                },
                {
                    "key": "highway",
                    "value": { "kind": "constant", "value": "bus_stop" },
                    "appliesTo": { "locationKinds": ["platform"] }
                }
            ],
            "removeKeys": ["gtfs:stop_id:MANUAL-DEMO"]
        }
    ],
    "mappingRules": [
        {
            "key": "name",
            "value": { "kind": "field", "field": "stop_name_expanded" }
        },
        {
            "key": "gtfs:stop_code:MANUAL-DEMO",
            "value": { "kind": "field", "field": "stop_code" }
        }
    ],
    "candidateRadiusMeters": 50,
    "autoIdRadiusMeters": 10
}
```

Here, `stop_id` helps identify a feature but is not an output mapping. The stop-code mapping is distinct from the identity key selected for removal. With multiple feeds, use appropriate feed restrictions and feed-specific tag keys rather than copying the example unchanged.

## Validation and older files

The editor omits blank/incomplete inactive rows when exporting JSON. Invalid active rules are reported before replacing the current profile or activating an import.

Older profiles missing `geometryTarget`, `streetNameCleanup`, or `removeKeys` receive the defaults described above. Legacy non-direct rules in `mappingRules` are migrated to the applicable feeds' `additionalTags`.

After importing, inspect the resulting feed sections and example outputs. Applying a compatible profile still invalidates candidates, reviews, and the draft, even when the file itself passes validation.

**Return to:** [Mapping profiles](02-profiles.md) or the [Orcaboros manual](index.md).
