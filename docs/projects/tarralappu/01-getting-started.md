<!-- @format -->

# Getting started

[Tarralappu](https://lumikeiju.dev/tarralappu/) is a browser workspace for generating images through OpenRouter. You do not need to install Tarralappu to use the hosted application.

## Before you begin

Have a modern browser with JavaScript and browser storage enabled, an internet connection, and an [OpenRouter](https://openrouter.ai/) account and API key. Check your account's available credits, model access, and provider-side spending limit before making paid requests.

The model catalogue can load without a key, and you can prepare drafts without generating. **Generate**, a draft's **Refine** button, **Retry**, and **Random** can send requests that use credits. A local session cap is useful for tracking, but it is not a guaranteed maximum charge.

## Connect your key

1. Select **API Key** in the header.
2. Enter your OpenRouter API key in **OpenRouter API key**.
3. Optionally select **Remember on this device** on a trusted personal device.
4. Select **Connect**. The panel shows **Key ✓** when a key is set.

Connecting stores the entered key; it does not verify that the account has credits or access to a particular model. A request can still fail because of authentication, account, model, or provider restrictions.

Without **Remember on this device**, the key is kept in memory and browser session storage. Remembering it also stores it in local storage, where JavaScript running on that page can access it. Avoid this option on shared devices. **Change key** clears the stored key and lets you enter another one.

Never put an API key in a prompt, screenshot, issue report, or shared request log. The key is not stored in the board's IndexedDB records or included in the request-source viewer.

## Set a budget and inspect the workspace

Expand **Style & References**. In **Session cost cap ($)**, enter a positive amount and move focus out of the field to save it. A blank or nonpositive value removes the cap. Read **How this cap works** and the [budget guide](07-costs-and-budgets.md): unknown or underestimated requests can exceed a local cap.

The same panel contains the shared **Style Guide**, **Style Reference**, and **Layout Reference**. They are optional. **Prompt Board** is a separate shelf for reusable notes. The header displays the session total and **Parallel** job setting.

## Create your first sketch

1. Select **New Sketch**.
2. Filter the model list if needed and select an image model. Review its displayed pricing and any capability warning.
3. Optionally enter a prompt, then select **Create Draft**.
4. In the new card, enter a nonempty **Generation prompt** if you did not already provide one.
5. Review the attachment checkboxes and the model's available settings.
6. When you are ready to make a paid request, select **Generate**.

![New Sketch composer showing a selected image model, a filtered catalogue, and an example prompt in the light theme](../../resources/images/tarralappu/composer-light.png#only-light)
![New Sketch composer showing a selected image model, a filtered catalogue, and an example prompt in the dark theme](../../resources/images/tarralappu/composer-dark.png#only-dark)

_Example model selection and prompt. Available models and prices can change._

Creating the draft does not start generation. A model is required to create it; a nonempty prompt is required to generate. The row stays associated with the selected model, so create another sketch or send a Prompt Board note to another model to compare.

Watch the card move through **Queued** and **Generating** to **Done** or **Error**. When the result is ready, open it with the magnifying-glass control or use its **Download** link. See [Results and media](06-results-and-media.md) before relying on a browser-stored image as your only copy.

**Next:** [Prompts and shared style](02-prompts-and-style.md).
