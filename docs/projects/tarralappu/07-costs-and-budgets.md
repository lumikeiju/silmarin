<!-- @format -->

# Costs and budgets

Image generation and Random text generation use OpenRouter. Review current model pricing, account access, and provider billing information before sending requests.

!!! warning "Local caps are not hard billing limits"

    Estimates can be unavailable or lower than the final charge. Requests with unknown estimates can exceed a local cap, and interrupted or failed requests may still be billed. Set an OpenRouter spending limit for provider-enforced protection and check OpenRouter for the authoritative charges.

## Read costs

The header's **Session** total includes known image-generation charges on retained sketch cards and known Random text costs. A chain header shows that row's known total; a completed card can show its known charge. The **Incomplete** indicator or an unreported-cost warning means some charges may be missing.

The model picker may show price components and approximate `$` tiers. Those tiers are rough hints across different billing schemes, not exact request quotes. An unavailable estimate or **pricing not listed** does not mean zero cost.

Tarralappu records reported cost when available and may look up a generation's usage afterward. Known charges from repeated attempts are accumulated. An error, cancellation, lost response, or storage problem can leave a charge unknown, so compare against OpenRouter rather than treating the local total as a bill.

## Set local caps

- **Session cost cap ($):** expand **Style & References**, enter a positive amount, and leave the field to save it. This covers the board's known image and Random text costs.
- **Chain cost cap:** enter a positive amount in the **Cap $** field at the right of that row's header and leave the field to save it. It applies to image requests in that chain.
- Clear a cap by leaving its field blank or entering a nonpositive value.

The app includes known in-flight estimates when checking budgets. It blocks a request if a cap is already reached, or if a known estimate would exceed the relevant cap. An unknown estimate is not zero: the request can proceed while the cap has room and still cost more than the remaining amount. Random uses the session cap, not a chain cap.

A new fork starts without a chain cap; set one on the new row if desired. Copied history in a fork does not represent a new request or charge. Deleting a sketch removes its image-generation cost from local totals, while Random text costs remain. These totals therefore do not necessarily equal your complete provider account history.

## Parallel jobs

The header's **Parallel** control sets image-job concurrency; the interface offers values from 1 to 8, with 2 as the initial default. It does not change the number of outputs in a single request or the number of forks. Multiple jobs may be in flight, so known estimates are reserved when checking caps.

Random text uses its own one-at-a-time guard. Starting or cancelling Random does not start or cancel an image-generation job.

**Next:** [Storage and troubleshooting](08-storage-and-troubleshooting.md).
