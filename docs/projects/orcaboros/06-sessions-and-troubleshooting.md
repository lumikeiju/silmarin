<!-- @format -->

# Sessions and troubleshooting

## Saved sessions

Orcaboros stores its active session in the browser's IndexedDB. The stored data includes the profile, imported stops, OSM snapshot, review decisions, and export draft. Raw ZIP bytes are not retained.

Reopen the same application origin in the same browser profile to resume. Restoration rebuilds candidate evidence before exposing the saved reviews. There is no account or cloud synchronization, and a different browser, browser profile, or site origin has separate storage.

Do not treat browser storage as a durable backup. Keep the original archives and export useful profiles and `.osm` work separately. Those two export formats are not interchangeable, and neither restores an entire session.

The Overpass endpoint and custom style URL are **not persisted**. Re-enter them after a reload. Do not rely on theme choice or resized panel dimensions being restored either.

## Operations that affect progress

| Operation                                  | Effect                                                           |
| ------------------------------------------ | ---------------------------------------------------------------- |
| Select replacement ZIP files               | Does not yet replace the active session                          |
| Successfully process a new import          | Activates the newly imported session                             |
| Fail or cancel an import                   | Preserves the previous active session                            |
| Apply a compatible profile change          | Reprocesses stops and invalidates candidates, reviews, and draft |
| Successfully retrieve a fresh OSM snapshot | Replaces candidates and invalidates earlier reviews and draft    |
| Fail or cancel retrieval                   | Preserves the last successful snapshot and reviews               |
| Change a queue filter                      | Changes visibility, not decisions or export eligibility          |
| Download an export                         | Produces an editing file, not a session restore point            |
| Confirm session reset                      | Clears the active imported/retrieved/reviewed work               |

## Storage errors and multiple tabs

If IndexedDB is entirely unavailable, the application can operate with memory-only storage. That work does not survive closing or reloading the page. A failure to save to an existing database is a separate problem: save errors are surfaced and should not be ignored.

When another tab changes the active session, Orcaboros can report:

> The active session changed in another tab. Reload before continuing.

Continue in one tab and reload the stale one. Do not assume simultaneous tabs merge their decisions.

For a storage error, preserve any files already exported, check browser storage permissions and available space, and avoid clearing site data until you have decided to discard the saved session. Clearing site data is destructive, not a routine first troubleshooting step.

## Reset the session

1. Expand **Upload**.
2. Select **Reset current session**.
3. Choose **Keep current session** to cancel, or **Reset session** to confirm.

Confirmation clears imported data, candidates, reviews, and the active draft, along with the endpoint and custom style values. It is not an undo operation.

Resetting a session is also not the same control as **Reset stock profile**. Inspect the resulting profile rather than assuming session reset restores every profile default.

## Layout and keyboard access

- Use the header's **Light mode** / **Dark mode** button to switch appearance.
- Use the skip-to-workspace link to bypass repeated header content.
- Expand or collapse numbered workflow panels and the map legend as needed.
- On wider screens, resize the sidebar and review area with their separators.
- Focus a separator and use arrow keys for one-point adjustments, **Shift+Arrow** for five-point adjustments, or **Home** / **End** for its minimum/maximum.
- The initial sidebar width is 25% of the viewport; the initial review area height is 46% of the viewport.
- Narrow layouts stack the workspace vertically, so controls may be below the current view.
- **Escape** cancels an active map-link change.

The application provides visible keyboard focus and reduced-motion support. Keep the textual state labels and legend in view rather than relying only on map colors.

## Privacy and network access

GTFS ZIP parsing and matching occur in the browser. Imported stops and the other session data are saved locally, rather than uploaded to an Orcaboros application backend.

Network activity is still part of using the hosted application:

- The hosting service delivers the application and its resources.
- The default or custom basemap loads external styles and map resources.
- Starting retrieval sends a geographically bounded query to your selected Overpass endpoint, including the relevant feed-identity keys.

Do not interpret "local processing" as "no third-party requests." The deployed host may also load its own analytics resources. Endpoint and custom-style settings are session-only, but the services receiving requests still have their own privacy policies.

## Common problems

| Symptom                                          | Checks and next steps                                                                                                                                                                        |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A stock profile did not load                     | Check the ZIP's editable feed ID against the stock table. One unknown ID causes a blank custom profile for all selected feeds.                                                               |
| A feed ID is rejected                            | Check hyphens, unsupported characters, duplicate IDs, length, and the prohibited `US-WA-PSC` ID.                                                                                             |
| `stops.txt` cannot be found                      | Check that it is the exact ZIP-root entry, not nested in another directory.                                                                                                                  |
| Fewer stops were imported than expected          | Read diagnostics; check required values, coordinates, duplicate IDs, and unsupported location types.                                                                                         |
| Profile import or editing fails                  | Read the reported field/rule error. Check enabled feeds, radii, active key/value validity, and overlapping output keys.                                                                      |
| Reset stock profile fails for a custom feed      | Use a compatible custom profile; the stock registry cannot define that feed.                                                                                                                 |
| Overpass retrieval fails                         | Check HTTPS, endpoint availability, CORS, request size, timeouts, and the displayed error. A failed request is not an empty successful snapshot.                                             |
| No candidates were returned                      | Check the imported extent, feed IDs, radius, and supported OSM types. Do not immediately create new nodes.                                                                                   |
| The queue looks empty or too short               | Check category filters, especially exact, and pagination.                                                                                                                                    |
| Review progress exceeds the export count         | OSM-only unchanged items count toward progress; skipped/unreviewed stops do not export.                                                                                                      |
| An automatic match appeared in the export        | Auto-matched stops are eligible even when exact results are hidden. Inspect or change their decisions before exporting again.                                                                |
| An item says removed                             | Its identity is absent from all valid imported stop IDs, not confirmed physically removed. Skipped rows with valid IDs still count as present. Review it unchanged; no deletion is exported. |
| A map feature cannot be selected as a candidate  | It may exist only in the basemap, not in the retrieved OSM snapshot.                                                                                                                         |
| Points are missing at a broad map zoom           | Zoom to level 11 or above or use the focus controls.                                                                                                                                         |
| The map fails to initialize                      | Check WebGL2/browser support and use Retry map. The queue remains available.                                                                                                                 |
| Tags did not change to the displayed GTFS values | The comparison is read-only; differing existing values normally stay. Check profile/default behavior and make final edits in JOSM.                                                           |
| Download is disabled                             | Finish retrieval, wait for current work, and confirm at least one eligible decision.                                                                                                         |
| Export reports a conflict                        | Reconcile duplicate element claims, tags, or coordinates using the affected review items.                                                                                                    |
| No file appears after a valid export             | Check the browser's download UI and permissions, and distinguish a blocked download from an application validation/storage error.                                                            |
| Work is missing after reopening                  | Check browser profile/origin, cleared or unavailable storage, another tab replacing the session, and whether a new import/reset occurred.                                                    |

If a problem persists, report it in the [Orcaboros issue tracker](https://github.com/lumikeiju/orcaboros/issues). Include the app version, browser, exact visible error, and reproducible steps. Remove credentials, private endpoint/style URLs, and any feed data you cannot share.

**Reference:** [Profile JSON](07-profile-reference.md). **Return to:** [Orcaboros manual](index.md).
