<!-- @format -->

# Prompts and shared style

Tarralappu separates a sketch's subject prompt from reusable board-level style guidance. You can write both yourself; generated suggestions are optional.

## Write a Style Guide

Expand **Style & References** and enter shared visual direction in **Style Guide**, for example, colors, lighting, texture, or medium. The text is saved as you edit.

A Style Guide is not automatically sent with every request. On a sketch, select **Attach Style Description** to include the current guide. New root drafts initially check this option when a guide is present; ordinary refinements start with shared attachments unchecked. Check the actual card before generating.

The guide can work alongside a **Style Reference** image and a **Layout Reference** image, but each attachment has its own checkbox. See [References and markup](04-references-and-markup.md).

## Use the Prompt Board

1. Expand **Prompt Board** and select **Add Note**.
2. Optionally name the note and enter its prompt text. Edits save after a short pause.
3. Use the note's copy control to copy the text, or **Send to…** to create drafts from it.
4. Use the remove control to delete a note you no longer need.

Removing a note removes it from the board; it does not delete drafts previously created from it. A note can be blank while you work, but a nonempty prompt is needed for selection and sending.

![Prompt Board with example notes and controls for copying, selecting, and sending prompts in the light theme](../../resources/images/tarralappu/prompts-light.png#only-light)
![Prompt Board with example notes and controls for copying, selecting, and sending prompts in the dark theme](../../resources/images/tarralappu/prompts-dark.png#only-dark)

_Example notes are scratchpad content. Sending them creates drafts, not image requests._

### Send to one or more models

Use the send control on a note, or select the checkboxes on several nonempty notes and select **Send to…**. In the dialog:

1. Filter the catalogue if useful and check the models to compare.
2. Use the star controls to pin or unpin models without losing the selection.
3. Confirm **Send to** or **Create … drafts**.

Each selected prompt/model combination creates a separate root draft. For example, two prompts and three models create six drafts. Inspect and generate each draft deliberately; the send action does not start image generation. If an error reports that some drafts may already have been created, check the board before repeating the action.

## Random suggestions

**Random** appears on the Style Guide, Prompt Board notes, and editable sketch prompts. It uses DeepSeek Flash through OpenRouter, not the sketch's image model. It needs a connected key, uses API credits, and replaces the target text rather than appending to it. On a note without a name, it can also supply a short name; an existing name is preserved.

Only one Random text request runs at a time. **Cancel** stops waiting for that request and leaves the existing text unchanged, but OpenRouter may still charge for processed tokens. A failed request also leaves the prior text in place; read the displayed error and cost status before retrying.

Random does not start image generation or change attachment selections. Existing board text and reference images are not sent as context for the Random request. Review the returned suggestion before using it.

**Next:** [Models and generation](03-models-and-generation.md).
