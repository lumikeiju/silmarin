<!-- @format -->

# Results and media

## Inspect and download

A **Done** card shows its prompt and each returned image. Expand the prompt summary to read the full text. Select a result's magnifying-glass control to open **Image viewer**; close it with the close button, **Escape**, or the backdrop.

![Image viewer showing a generated watercolor lighthouse and its download and description controls in the light theme](../../resources/images/tarralappu/viewer-light.png#only-light)
![Image viewer showing a generated watercolor lighthouse and its download and description controls in the dark theme](../../resources/images/tarralappu/viewer-dark.png#only-dark)

_Example output in the image viewer. The generated image is illustrative, not a promise of a particular result._

Use **Download PNG**, **Download JPEG**, **Download WEBP**, **Download GIF**, or **Download SVG**, as offered for the returned file. Tarralappu downloads the original stored media rather than a screenshot of the preview. Save important files outside the browser.

The card reports the number of outputs received and, where available, dimensions, format, animation metadata, provider settings, and known cost. The provider may return different metadata or fewer outputs than requested; read any warning on the card.

## Animation and vector output

An animated GIF initially shows a still poster. Use **Play animation** to play it and **Pause animation** to stop. The original GIF download remains animated. Frame count and duration are displayed when available.

SVG results are displayed as images rather than inserted as page markup. If a later edit needs a GIF or SVG as its input, explicitly create a PNG still or raster reference first; the original download is not replaced. See [References and markup](04-references-and-markup.md#use-gif-or-svg-results-as-edit-inputs).

## Add an image description

Open **Image description** beneath a result or reference and enter a description of the visible content. Move focus out of the field to save it. The description can contain up to 500 characters and is used as the image's alternative text in Tarralappu. Clearing the field removes the saved description.

Descriptions are stored with the browser's image record. They are not a substitute for describing an image where you publish it, and they are not embedded into the original download by this control.

## Inspect the request

On a completed card or a card with a recorded request, select **View request source** (`</>`). The panel shows the recorded request shape and offers **Copy**. Image data is elided and the key is not included, but the source can still contain prompts and other information you may not want to share.

An error card may separately offer **View raw response**. Treat raw responses as potentially sensitive: review and redact them before sharing. Neither panel is a complete backup of the board or image files.

**Next:** [Costs and budgets](07-costs-and-budgets.md).
