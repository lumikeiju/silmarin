<!-- @format -->

# Chains and forks

A chain is a horizontal row of sketches using the same model. Each completed sketch can produce media; an editable draft records the next request before it is sent.

## Continue a chain

1. Wait until the latest card in the row is **Done**.
2. Select the ghost **+ Refine** card at the end of the row.
3. Enter a **Refinement prompt** describing the change.
4. Review the inherited settings, previous output, references, and local caps.
5. Select the draft's **Refine** button when ready to submit.

![A completed lighthouse image followed by a refinement draft in the light theme](../../resources/images/tarralappu/refinement-light.png#only-light)
![A completed lighthouse image followed by a refinement draft in the dark theme](../../resources/images/tarralappu/refinement-dark.png#only-dark)

_The second card is an editable draft; creating it does not send the refinement._

The **+ Refine** card adds a draft only after the latest sketch is complete. It inherits generation settings and starts with an empty prompt. Shared Style Guide and global-image attachments start unchecked; inspect them if you want to send them again. If a parent has multiple outputs, the edit-source controls can select a particular output when supported.

An image-only model uses image-to-image for refinements rather than conversational history. Conversational models can include earlier prompts and images, subject to input limits; older context may be truncated to fit. Neither approach guarantees that the model will preserve every detail.

## Create alternative rows

Use the count selector and fork controls on a card to create **1–10** independent draft rows. The available action depends on the card:

| Action               | Available from                                      | What it creates                                                                       |
| -------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Initial-run fork** | A root draft or errored root                        | A new root draft with the model, prompt, and settings copied                          |
| **Re-run fork**      | A completed card                                    | A new draft for that prompt, with the completed path before it copied when applicable |
| **Refinement fork**  | A completed card, or an editable/errored refinement | A new row with a copied completed path and an editable refinement draft               |

Forks are drafts, not automatic generation requests. They keep the source row's model. Copied completed images are reused without a new generation charge, while each eventual new request can cost money. A new fork has no chain cap until you set one; the session cap still applies.

Use **+ Refine** to continue the existing row. Use a refinement fork to explore alternatives in separate rows. A forked refinement carries a copied prompt and settings, so review them rather than assuming it is blank.

## Retry, delete, or cancel

An **Error** card shows the problem and offers **Retry**. Retrying sends another request; check the error, settings, and any known or unreported charges first.

The trash control marks that card and all later cards in its row for deletion. Review the displayed count, then choose **Delete … cards** or **Cancel**. Deleting the first card removes the row. This is also the way to cancel a queued or generating image job: confirm deletion of that card. There is no separate image-generation cancel button.

Deletion is not an undoable backup. Download anything you need first. Other forked rows retain their own references to shared images, but deleting a card removes its image-generation charge from the local total. Cancellation or an interrupted request can still incur an OpenRouter charge.

**Next:** [Results and media](06-results-and-media.md).
