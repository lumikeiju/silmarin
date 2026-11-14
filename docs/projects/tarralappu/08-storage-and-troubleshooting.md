<!-- @format -->

# Storage and troubleshooting

## What is saved

Tarralappu saves its board, prompts, model pins, sketch chains, settings, image records, and available cost information in the browser's IndexedDB. Reopen the same application origin in the same browser profile to use that stored board.

The API key is separate: by default it is held in memory and session storage; **Remember on this device** opts into local storage. Neither the board database nor a request-source snapshot contains the key.

Browser storage can be cleared, evicted, unavailable, or tied to a different browser profile or origin. There is no account-based board synchronization or full-board backup/export control in v2.1.0. Download important images and keep copies of important prompt text separately. An individual image download does not restore a chain, its settings, or its history.

If the page is closed or reloaded while a sketch is queued or generating, the card is restored as an **Error** and can be retried. A request interrupted after it started may still have been charged. Check OpenRouter before retrying.

## Privacy and network access

The application has no Tarralappu backend. Model discovery and generation use network requests to OpenRouter; the selected model provider may process the prompt and images included in a request. Hosting the application and any provider service are separate from local board storage.

Only send material you are allowed to share. Be especially careful with private reference images, prompts, raw errors, and copied request source. The Random text requests do not send your existing board text or reference images, but they still use OpenRouter and can cost credits.

## Layout and keyboard access

- Use **Skip to main content** to bypass the header.
- Expand or collapse **Style & References** and **Prompt Board** to make room for the board.
- Rows extend horizontally; scroll the row to reach later sketches and the **+ Refine** card.
- Use the header's theme button to switch between light and dark.
- Reference-order buttons, annotation fields, dialogs, and card actions are keyboard accessible. **Escape** closes the image viewer.

## Common problems

| Symptom                                 | Checks and next steps                                                                                                                              |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Saved data will not load                | Check browser storage permissions and available space, then select **Try again**. Avoid clearing site data unless you intend to discard the board. |
| The model list is empty or fails        | Check the connection, clear the filter, and use **Retry**. Catalogue and endpoint availability can change.                                         |
| A model or option is missing            | Check the selected model and endpoint. Some capabilities are estimated or require endpoint confirmation; use the offered discovery retry.          |
| A draft cannot generate                 | Enter a prompt, connect a key, and check model capabilities, endpoint errors, input limits, and incompatible options.                              |
| The key is set but a request fails      | Check the displayed error, OpenRouter account access, credits, and model availability. **Connect** alone does not validate the key.                |
| A reference cannot be uploaded or sent  | Use PNG, JPEG, or WebP; check file and model input limits. A file can pass upload validation but exceed the encoded request limit.                 |
| A GIF or SVG cannot be used for an edit | Convert the previous output to a PNG reference explicitly; retain the original download.                                                           |
| Markup is unavailable or rejected       | Confirm endpoint support, choose a primary raster source, and use a transparent PNG matching its dimensions.                                       |
| A request is blocked by a cap           | Check both the session and chain cap, including other known in-flight estimates. Do not treat unknown estimates as free.                           |
| A card is interrupted or fails          | Read the error and any known or unreported charge. Correct the cause and retry only after checking possible provider charges.                      |
| The local total seems too low           | Deleted sketches no longer contribute their image charges; some costs can be unreported. Check OpenRouter for the complete bill.                   |
| Expected work is missing                | Check the browser profile and application origin, whether site data was cleared, and whether the card or its ancestor was deleted.                 |

If a problem persists, use the [Tarralappu issue tracker](https://github.com/lumikeiju/tarralappu/issues). Include the app version, browser, visible error, and reproducible steps. Remove API keys, private prompts, images, and sensitive response details before sharing.

**Return to:** [Tarralappu manual](../tarralappu.md).
