<!-- @format -->

# Retrieving OSM data

Retrieval obtains an OSM snapshot for comparison with the imported stops. It does not edit OpenStreetMap.

## Choose an endpoint

1. Finish the [mapping profile](02-profiles.md), including both matching radii.
2. Expand **Retrieve**.
3. Enter a URL in **HTTPS Overpass-compatible endpoint**.
4. Optionally enter a custom basemap URL.
5. Select **Retrieve Candidates**.

Use an HTTPS endpoint that supports Overpass queries and browser access. The information link beside the endpoint field leads to the [OSM wiki's public Overpass instances](https://wiki.openstreetmap.org/wiki/Overpass_API#Public_Overpass_API_instances). Follow the chosen service's usage policy.

The endpoint field masks its contents. Its value is used only for the current browser session and is not restored after a reload. A masked field does not make the remote service anonymous: the service still receives the request.

## Basemap settings

Without a custom style, the map uses OpenFreeMap:

| Application theme | Default basemap |
| ----------------- | --------------- |
| Dark              | Fiord           |
| Light             | Positron        |

**Optional session-only MapLibre style URL** selects a different map style. Supply a MapLibre-compatible style URL, not an ordinary map website or an Overpass endpoint.

The style and its referenced resources must be accessible to the browser. Custom styles may use their own tile providers and access policies. The style URL is not persisted and must be entered again after a reload.

Basemap features are visual context. They are not the retrieved OSM candidate snapshot, and a feature drawn in the basemap is not necessarily available to select as a match.

## What is requested

The query covers the imported stop extent, padded by the candidate radius. It requests:

- Nodes tagged `highway=bus_stop`.
- Nodes and ways tagged `public_transport=platform`.
- Nodes carrying the selected feed-specific GTFS identity tags.

This is not an unrestricted search of every OSM object. Relations and other unsupported feature types are outside this workflow. Importing a station row does not imply that every possible station representation will be retrieved.

After the request, Orcaboros matches candidates locally. A lack of matching results is not proof that the stop is missing from OSM.

## Progress and completion

![Retrieval panel reporting four synthetic OSM candidates from one completed Overpass request](../../resources/images/orcaboros/retrieval-light.png#only-light)
![Retrieval panel reporting four synthetic OSM candidates from one completed Overpass request](../../resources/images/orcaboros/retrieval-dark.png#only-dark)

_Fictional example using an intercepted demonstration endpoint, not a public Overpass service._

Watch the request and local-matching progress, then check the resulting candidate count. Select **Continue to review** when retrieval succeeds.

**Cancel OSM Request** stops an active request. A failed or cancelled request preserves the last successful snapshot and its reviews. A successful refresh replaces that snapshot and invalidates the previous review decisions and export draft.

!!! warning "Refreshing is not a merge"

    Retrieve again only when you intend to rebuild the candidate set and redo the review. Export useful progress first; an earlier `.osm` file is a separate artifact, not a session restore point.

## Limits and failures

| Limit                            | Value      |
| -------------------------------- | ---------- |
| Requested Overpass query timeout | 60 seconds |
| Client request timeout           | 75 seconds |
| Maximum response size            | 25 MiB     |
| Maximum elements per response    | 50,000     |

Server-side limits can be stricter. An Overpass runtime-error remark, invalid response, unsupported data, HTTP/CORS problem, timeout, or exceeded limit is a failure, not a successful empty result.

For a failed request:

1. Read the displayed error.
2. Check the endpoint URL and the service's availability and browser-access policy.
3. Check whether the selected feeds cover an unexpectedly large area.
4. Retry when appropriate, or use another suitable endpoint.

Do not repeatedly send an oversized query to a busy public instance. If you need to change the feed selection or profile, account for the resulting session/review reset.

A **successful zero-result response** is different from a failure. Confirm the geographic extent, feed IDs, search radius, and supported candidate types before treating any feature as new.

**Next:** [Reviewing changes](04-review.md).
