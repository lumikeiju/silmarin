<!-- @format -->

# Getting started

Orcaboros runs at [lumikeiju.dev/orcaboros](https://lumikeiju.dev/orcaboros/). Using the hosted application does not require installing Orcaboros or its development tools.

## Before you begin

Have the following ready:

- A modern browser. The map requires WebGL2; the review queue remains available if map initialization fails.
- One or more local GTFS ZIP files, with permission to use their data for the intended OSM contribution.
- An appropriate HTTPS Overpass endpoint for [retrieving OSM data](03-retrieval.md).
- [JOSM](https://josm.openstreetmap.de/) for inspecting the exported file. Any eventual OSM upload happens there, not in Orcaboros.

Read and acknowledge the beta warning. Keep the original archives outside the application: its saved session does not retain the ZIP bytes.

## Select archives and identify feeds

1. Expand **Upload**.
2. Use **Choose or drop GTFS ZIPs**, or drop the archives onto the upload area.
3. Check the **GTFS Feed ID** beside every selected ZIP.
4. Remove any accidentally selected archive before processing.
5. Select **Process selected GTFS ZIPs**.

A feed ID defaults to the filename without `.zip`, trimmed and uppercased. It is **not** inferred from `agency.txt` or other feed metadata. For example, a stock King County Metro feed needs the ID `US-WA-KCM`, even if the downloaded archive has a different name.

Feed IDs:

- Use letters and digits, optionally separated by single hyphens.
- Must be unique among the selected archives.
- Have a maximum length of 242 characters.
- Cannot be the consolidated feed ID `US-WA-PSC`, which Orcaboros explicitly rejects.

See the [stock feed table](02-profiles.md#stock-profiles) before importing. If even one selected feed lacks a stock profile, the application starts with a blank custom profile for **all** selected feeds.

## Check the import result

![Upload panel showing the fictional MANUAL-DEMO archive and four eligible stops with no skipped rows](../../resources/images/orcaboros/upload-light.png#only-light)
![Upload panel showing the fictional MANUAL-DEMO archive and four eligible stops with no skipped rows](../../resources/images/orcaboros/upload-dark.png#only-dark)

_Fictional example: four eligible stops were imported from one source feed._

During processing, **Cancel import** stops the operation. An import is staged before becoming active: a failed or cancelled replacement leaves the previous active session intact. Merely selecting new ZIP files does not replace the session either.

After processing:

1. Confirm the imported feed IDs and eligible-stop count.
2. Read each feed's diagnostics, including skipped and unsupported-location counts.
3. Investigate unexpected omissions before continuing. The interface shows the first five diagnostic details per feed, not necessarily every problematic row.
4. Select **Continue to profile mapping**.

A successful replacement activates the newly imported session. Export any useful earlier work before deliberately replacing it.

## Supported ZIP contents

Orcaboros reads the exact ZIP-root entry **`stops.txt`**. A nested file such as `feed/stops.txt` is not the required entry. Other GTFS files are not processed.

The file must be valid UTF-8 CSV with these columns:

| Column      | Requirement                                                                          |
| ----------- | ------------------------------------------------------------------------------------ |
| `stop_id`   | Nonempty, at most 255 characters, with no control characters; unique within the feed |
| `stop_name` | Nonempty and at most 255 characters                                                  |
| `stop_lat`  | Finite WGS84 latitude, between -90 and 90                                            |
| `stop_lon`  | Finite WGS84 longitude, between -180 and 180                                         |

Duplicate stop IDs fail that feed's import; they are not silently merged. The same stop ID in different feeds has a different source identity.

`location_type` determines which rows are eligible:

| Value                  | Treatment              |
| ---------------------- | ---------------------- |
| Missing, blank, or `0` | Platform               |
| `1`                    | Station                |
| Other values           | Skipped as unsupported |

Columns such as `stop_code` and `parent_station` can be used in mappings, as can other existing CSV headers. Reading a field does not itself create an OSM tag or relationship; the profile decides what to propose.

## Import failures and skipped rows

A corrupt archive, missing or duplicate root `stops.txt`, invalid encoding or CSV structure, missing required columns, or duplicate stop IDs can prevent import. Invalid individual rows are otherwise skipped with diagnostics.

Check the archive and source data rather than treating a smaller eligible-stop count as a complete feed. Orcaboros retains every valid `stop_id` for identity checks, even when that row is skipped for invalid coordinates, another invalid value, or an unsupported location type. Such a row does not make its OSM identity appear **removed**. A missing or invalid `stop_id` cannot provide that protection.

For recovery advice, see [Sessions and troubleshooting](06-sessions-and-troubleshooting.md#common-problems).

**Next:** [Mapping profiles](02-profiles.md).
