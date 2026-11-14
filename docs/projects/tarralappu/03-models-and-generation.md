<!-- @format -->

# Models and generation

## Choose a model

The **New Sketch** model picker loads OpenRouter's image-model catalogue and groups models by creator. Use **Filter models…** to narrow the list and the star beside a model to pin or unpin it. Pinned models appear first and remain available in their creator group. Pins are shared with the Prompt Board's **Send to…** dialog.

The picker displays available pricing and, where possible, a relative cost tier. **Pricing not listed** is not a promise that a model is free. Prices and capabilities can change; confirm current terms with OpenRouter before generating.

If the catalogue fails to load, use **Retry**. Some models are labelled **capabilities estimated** when detailed discovery is unavailable. Their controls use conservative defaults, not a guarantee of provider support. For GPT Image 2.6 Sunburst and Flare, Tarralappu checks endpoint details and blocks generation if it cannot confirm the endpoint; use **Retry endpoint discovery** when offered.

## Configure a draft

The controls on a draft depend on its model and discovered endpoint. You may see:

| Control                        | Purpose                                                                    |
| ------------------------------ | -------------------------------------------------------------------------- |
| **Aspect** and **Size**        | Choose among the model's advertised aspect ratios and size options         |
| **Quality** and **Background** | Select supported quality and background choices                            |
| **Outputs**                    | Request multiple images in one generation, up to the displayed model limit |
| **Format**                     | Choose an offered output format or the provider default                    |
| **Compression**                | Set the allowed compression value for JPEG or WebP output                  |
| **Seed**                       | Supply a supported nonnegative seed, or leave it blank for random          |
| **Reasoning**                  | Set reasoning effort when offered for the model                            |
| **Stream**                     | Show provider-supplied intermediate raster previews when supported         |

**Outputs** is the number of images in one request. It is not the fork count, and it is not the header's **Parallel** concurrency setting. Changing output count, quality, size, format, or references can change the charge.

For supported GPT Image 2.6 endpoints, **Advanced image controls** can expose **Complexity**, **Moderation**, custom **Pixel size**, GIF frame controls, or partial-preview count. Their presence depends on endpoint confirmation. **Reset advanced options to provider defaults** clears those advanced choices. The feature-availability disclosure explains controls that could not be confirmed; masks and SVG author selection are not offered.

![A refinement draft with advanced image and generation controls in the light theme](../../resources/images/tarralappu/advanced-light.png#only-light)
![A refinement draft with advanced image and generation controls in the dark theme](../../resources/images/tarralappu/advanced-dark.png#only-dark)

_The controls shown depend on the selected model and the endpoint's reported capabilities._

When custom still-image pixel sizing is available, use `auto` or `WIDTHxHEIGHT`. Both dimensions must be multiples of 16, neither edge may exceed 3840 pixels, the ratio must be between 1:3 and 3:1, and the total must be 655,360–8,294,400 pixels. Sizes above 2560 × 1440 are experimental. A custom size takes precedence over aspect and size options in the request.

## Format and streaming restrictions

- Compression applies to JPEG and WebP, not PNG or GIF.
- If an explicit format is selected for a transparent background, use PNG or WebP.
- GIF and multiple outputs use buffered completion rather than streaming. When a GPT Image 2.6 Sunburst or Flare endpoint offers SVG, that output also cannot stream, is generation-only, and requires one output.
- For GPT Image 2.6, GIF frame controls and preview counts appear only when confirmed by the endpoint. GIF frame sizing is automatic; the offered frame count is within 2–16, and frame duration is within 20–2000 milliseconds in 10-millisecond increments, subject to narrower endpoint limits. The provider may return fewer previews than requested.
- Streaming previews are temporary. Only completed output is saved, and an interrupted request can still be charged.

These are application constraints, not a promise that every listed format is available for every model. If an older saved selection is unavailable, choose an offered setting before generating. When switching from a custom still-image pixel size to GIF, reset the advanced options to clear the old size.

## Start the request

Review the prompt, selected references, output count, and budget. Select **Generate** on a root card or **Refine** on a refinement draft. A connected key, a nonempty prompt, compatible inputs, and available model capabilities are required.

Requests move through **Queued** and **Generating** to **Done** or **Error**. The header's **Parallel** setting controls how many image jobs can run at once. Creating a draft, selecting a model, and changing options do not start an image request.

The estimate can be unavailable or lower than the final cost. A local cap cannot prevent every overrun. See [Costs and budgets](07-costs-and-budgets.md) before submitting requests.

**Next:** [References and markup](04-references-and-markup.md).
