<!-- @format -->

# References and markup

References provide visual context for a request. They are distinct from the text in the Style Guide and from the prompt itself. The model may interpret them differently from what you intended, so inspect the result.

## Shared style and layout images

Expand **Style & References** and use the two slots under **Reference Images**:

| Slot                 | Intended guidance          |
| -------------------- | -------------------------- |
| **Style Reference**  | Palette, texture, and mood |
| **Layout Reference** | Composition and placement  |

Use **Upload style ref** or **Upload layout ref** to choose a PNG, JPEG, or WebP file smaller than 50 MiB. The remove button beside an occupied slot removes that shared reference. To use it in a request, check **Attach Style Reference** or **Attach Layout Reference** on the sketch. The two checkboxes and **Attach Style Description** are independent.

New root drafts initially select shared context that is present when the draft is created. Ordinary new refinements start with those three attachments off. Check the flags on each card rather than assuming a reference is always sent. A conversational refinement may still include earlier context in its retained history.

Inputs count against the model's total image limit. The limit includes previous outputs, subject references, and checked global images. Tarralappu shows warnings when a model cannot accept images or the selected inputs do not fit. Upload validation and the upstream encoded-request limit are separate: an image accepted for storage can still be too large to send.

## Subject references and the edit source

For a supported dedicated image endpoint, expand **Subject references and edit source** on the editable card.

1. Use **Upload subject references** to add PNG, JPEG, or WebP images smaller than 50 MiB each.
2. Use **Earlier** and **Later** to change their order, or **Remove** to detach one.
3. If editing an existing image, choose a **Primary edit source** from the previous outputs or subject references.
4. Review the input count and any checked shared references before generating.

![Refinement draft showing a selected previous output, an uploaded subject reference, and attachment checkboxes in the light theme](../../resources/images/tarralappu/references-light.png#only-light)
![Refinement draft showing a selected previous output, an uploaded subject reference, and attachment checkboxes in the dark theme](../../resources/images/tarralappu/references-dark.png#only-dark)

_The example selects the previous result as the primary edit source and keeps a separate subject reference._

The chosen edit source is sent first; other subject references follow in their selected order, then checked shared reference images. Choosing a source does not automatically remove the other subject references. With **Use previous outputs in order (legacy)**, previous outputs are used in order instead of selecting one primary source.

Changing the primary source clears any saved markup tied to the old source. Removing the selected subject source also clears its markup. Set the source first, then prepare annotations.

## Use GIF or SVG results as edit inputs

Edit inputs must be raster PNG, JPEG, or WebP. Generated GIF and SVG files remain available in their original formats, but they must be explicitly converted before use as an edit source.

In the refinement's **Previous output** disclosure, choose **Use first frame as PNG** for a GIF or **Rasterize to PNG reference** for an SVG. This creates a separate PNG subject reference, selects it as the primary source, and leaves the original unchanged. Check the resulting reference and output settings before sending the edit.

## Markup-guided edits

**Markup-guided edit** is available only when the selected endpoint confirms markup support. It uses a separate transparent PNG overlay aligned with the selected raster source; it is guidance for the model, not an exact mask.

1. Select a primary PNG, JPEG, or WebP edit source.
2. Open **Markup-guided edit** and select **Add annotation**.
3. Choose a circle, rectangle, or arrow, then enter its `x`, `y`, `width`, and `height` values in image pixels. Keep the shape within the source bounds.
4. Use **Undo**, **Redo**, or **Clear annotations** as needed, then select **Save transparent markup**.
5. In the prompt, describe the desired change and what should remain unchanged.

Alternatively, use **Upload matching transparent PNG**. It must be smaller than 50 MiB, match the oriented source dimensions, and contain transparent pixels. The markup and its base may contain at most 16,777,216 pixels. **Remove saved markup** detaches the overlay. If support is not confirmed or endpoint discovery fails, follow the displayed message rather than assuming markup will be sent.

**Next:** [Chains and forks](05-chains-and-forks.md).
