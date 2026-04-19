---
title: Contributing
---

<!-- @format -->

# Contributing

This guide explains how to contribute to Silmärin.

Silmärin does not accept external contributions. This guide is exclusively intended for use by Lumikeiju and the Moonlight Librarian.

---

## Version Control & Workflow

This project follows standardized version control conventions:

### Semantic Versioning

Silmärin uses [Semantic Versioning](https://semver.org/) (MAJOR.MINOR.PATCH):

- **Major (X.0.0)**:
    - Core: New major features or upgrades
    - Docs: Changes to structure/navigation that break external links
- **Minor (0.X.0)**:
    - Core: Significant changes to core features
    - Docs: New documentation or major reworks
- **Patch (0.0.X)**:
    - Core: Minor fixes, fixing typos, completing chores
    - Docs: Small updates, fixing typos, adding images

The version number is stored in the `version` field in `zensical.toml`.

### Conventional Commits

Commits follow [Conventional Commits](https://www.conventionalcommits.org/) with scoping:

- `feat(scope): description` - Core features or Docs content
- `fix(scope): description` - Core patches or Docs corrections

Examples:

```
feat(core-plugins): add abbreviations plugin
feat(docs-accessmap): add user manual page
fix(core-util): fix nav generator logic
fix(docs-walksheds): fix typo
```

### Branch Naming

Follow GitHub flow with structured branch names:

**Format**: `type/scope/short-description`

**Examples**:

```
feat/core-plugins/add-abbreviations-plugin
feat/docs-accessmap/add-user-manual-page
fix/core-util/fix-nav-generator-logic
fix/docs-walksheds/fix-typo
```

### Pull Request & Release Process

1. Create a feature branch following the naming convention
2. Make commits using conventional commit format
3. Open a pull request to `main`
4. Upon merge to `main`, releases are automated

## Getting Started (Windows 10/11)

This section of the guide explains how to set up a Windows environment for contributing to Silmärin for the first time.

### Legend

1. Keyboard shortcut to press | Action

    (`Shift`+`C`) | Copy

2. Command to enter into terminal

    [`someCommand --arguments \<path>`]

### Installation and Setup

1. Install [Visual Studio Code](https://code.visualstudio.com/)
    1. Install VS Code Extensions
        1. [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)

        2. [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)

        3. [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

        4. [YAML](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)

        5. [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml)

2. Clone the repository

    ```powershell
    git clone https://github.com/Lumikeiju/silmarin
    cd silmarin
    ```

3. Install [Python](https://www.python.org/downloads/)

4. Set up Python virtual environment
    1. Create the virtual environment

        ```powershell
        python3 -m venv .venv
        ```

    2. Activate the virtual environment

        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```

5. Install requirements

    ```powershell
    pip install -r requirements.txt
    ```

## Editing Instructions

Refer to the documentation for [Zensical](https://zensical.org/docs/).

### Images

Where possible, follow these guidelines for images:

1. Format: 24-bit `.png`

2. Resizing: Scale images using `{ width="123" }`:

    ```markdown
    ![alt text](image.png){ width="300" }
    ```

Refer to [Zensical: Images](https://zensical.org/docs/authoring/images/) for more information.

#### Screenshots

For creating screenshots with a consistent style, Firefox DevTools is to be used.

1. Open Firefox DevTools

    (`F12`)

2. Open Responsive Design View

    (`Ctrl`+`Shift`+`M`)

3. Add custom device profiles:
    1. Name: `[Screenshot] Web - Portrait`
        1. Size: `671`x`1196`

        2. Device Pixel Ratio: `1`

        3. User Agent String: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0`

    2. Name: `[Screenshot] Web - Landscape`
        1. Size: `1196`x`671`

        2. Device Pixel Ratio: `1`

        3. User Agent String: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0`

4. Resulting screenshots will fit exactly within the 2px outside border present in the following screenshot templates:
    1. [Screenshot (Landscape)](images/templates/screenshot-landscape.png)

    2. [Screenshot (Portrait)](images/templates/screenshot-portrait.png)

5. It is recommended to remove all embedded metadata, such as with the use of [ExifToolGUI](https://exiftool.org/gui/).

#### Image Annotations

For creating image annotations with a consistent style, follow these guidelines.

1. Highlight box
    2. Use: Indicating an area of focus in an image.

    3. Style
        1. Padding: `2px` distance from highlighted selection

        2. Outline
            1. Width: `1px`

            2. Color: `#007FFF`

        3. Fill
            1. Color: `#FF7F00`

            2. Opacity: `0.5`

    4. Example:

        ![example](example){ loading=lazy }

    5. Naming convention: For images with highlights, append `-h-$highlightedFeature`
        1. Example: `login.png` → `login-h-forgot-password.png`

#### QR Codes

1. Create QR codes using [Project Nayuki's QR Code generator library](https://github.com/nayuki/QR-Code-generator).
