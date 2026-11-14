<!-- @format -->

# Tarralappu

Sticky-note-themed browser interface for AI image generation through OpenRouter.

- **Website**: [lumikeiju.dev/tarralappu](https://lumikeiju.dev/tarralappu/)
- **Repository**: [github.com/lumikeiju/tarralappu](https://github.com/lumikeiju/tarralappu)

This manual covers **v2.1.0**: connecting OpenRouter, composing prompts, generating images, developing refinements, and managing the resulting media.

!!! warning "Generation can cost money"

    **Generate**, a refinement draft's **Refine** button, **Retry**, and **Random** send requests to OpenRouter and may incur charges. Tarralappu's local cost caps are estimates, not provider billing limits. Set a spending limit in OpenRouter if you need a provider-enforced limit.

## Manual

| Chapter                                                                     | Contents                                                            |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| [Getting started](tarralappu/01-getting-started.md)                         | Requirements, API key, workspace, and first sketch                  |
| [Prompts and shared style](tarralappu/02-prompts-and-style.md)              | Style Guide, Prompt Board, model comparisons, and Random            |
| [Models and generation](tarralappu/03-models-and-generation.md)             | Model selection, supported settings, output formats, and generation |
| [References and markup](tarralappu/04-references-and-markup.md)             | Shared and per-sketch images, edit sources, and annotations         |
| [Chains and forks](tarralappu/05-chains-and-forks.md)                       | Refinements, branches, retries, deletion, and cancellation          |
| [Results and media](tarralappu/06-results-and-media.md)                     | Viewing, downloading, animation, descriptions, and request source   |
| [Costs and budgets](tarralappu/07-costs-and-budgets.md)                     | Estimates, reported costs, local caps, and concurrency              |
| [Storage and troubleshooting](tarralappu/08-storage-and-troubleshooting.md) | Persistence, privacy, accessibility, and recovery                   |

## The workspace

![Tarralappu workspace with shared style controls, a session cap, and a chain of lighthouse sketches in the light theme](../resources/images/tarralappu/workspace-light.png#only-light)
![Tarralappu workspace with shared style controls, a session cap, and a chain of lighthouse sketches in the dark theme](../resources/images/tarralappu/workspace-dark.png#only-dark)

_Example workspace. The lighthouse images and prompts were created for this manual; displayed prices and costs are examples._

The header contains the API key panel, session cost, **Parallel** setting, and theme toggle. Expand **Style & References** for the shared Style Guide, two reference-image slots, and session cap. **Prompt Board** holds reusable prompt notes. Below them, each horizontal sketch chain is locked to one image model.

Drafting and organizing content do not themselves generate images. Completed cards show the returned media; refinements continue a row, while forks create separate rows.

## Important boundaries

- Tarralappu runs in the browser and sends generation requests directly to OpenRouter. It does not have a Tarralappu application backend.
- The model catalogue, capabilities, availability, and pricing are supplied by OpenRouter and can change. A control shown for one model or endpoint may not appear for another.
- Boards and media are stored in the browser. Download important results separately; browser storage is not a durable backup.
- Reference images and prompts included in a request leave the browser for the selected service. Use only material you are permitted to share.

## About this manual

The guide was checked on **2026-11-14** against the v2.1.0 interface and [source revision `15c4e7e`](https://github.com/lumikeiju/tarralappu/tree/15c4e7e9986f5a054782648a1249de628a32b8e4).
