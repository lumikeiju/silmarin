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

The version number is stored in the `CHANGELOG.md` file.

### Conventional Commits

Commits follow [Conventional Commits](https://www.conventionalcommits.org/) with scoping:

- `feat: description` - Core features or Docs content
- `fix: description` - Core patches or Docs corrections

Examples:

```
feat: add abbreviations plugin
feat: add user manual page
fix: fix nav generator logic
fix: fix typo
```

### Branch Naming

Follow GitHub flow with structured branch names:

**Format**: `type/scope/short-description`

**Examples**:

```
feat/add-abbreviations-plugin
feat/add-user-manual-page
fix/fix-nav-generator-logic
fix/fix-typo
```

### Pull Request & Release Process

1. Create a feature branch following the naming convention
2. Make commits using conventional commit format
3. Open a pull request to `main`
4. Upon merge to `main`, releases are automated

## Getting Started (Windows 10/11)

This section of the guide explains how to set up a Windows environment for contributing to Silmärin for the first time.

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
        1. Size: `810`x`1440`

        2. Device Pixel Ratio: `1`

        3. User Agent String: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0`

    2. Name: `[Screenshot] Web - Landscape`
        1. Size: `1440`x`810`

        2. Device Pixel Ratio: `1`

        3. User Agent String: `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:140.0) Gecko/20100101 Firefox/140.0`

3. It is recommended to remove all embedded metadata, such as with the use of [ExifToolGUI](https://exiftool.org/gui/).

4. Process screenshots with the `process-screenshot.py` utility to generate themed light/dark variants with borders and drop shadows:

    ```powershell
    # Ensure venv is activated first!
    ..\.venv\Scripts\Activate.ps1

    # Process a single screenshot
    python .\utilities\process-screenshot.py docs\resources\images\example\screenshot.png

    # Process all images in a directory
    python .\utilities\process-screenshot.py docs\resources\images\example\

    # Process recursively with a custom profile
    python .\utilities\process-screenshot.py docs\resources\images\ --recurse --profile moonlight

    # Regenerate existing output files
    python .\utilities\process-screenshot.py screenshot.png --overwrite
    ```

    The script produces two variants per input image, saved as maximally-compressed lossless PNGs:
    - `{name}-light.png` — dark border + drop shadow for light theme pages
    - `{name}-dark.png` — light border + glow for dark theme pages

    Reference them in Markdown with Zensical's theme-switching fragments:

    ```markdown
    ![Alt text](path/to/image-light.png#only-light)
    ![Alt text](path/to/image-dark.png#only-dark)
    ```

    Mode-tagged source files (e.g., `image.light.png`, `image.dark.png`) generate only the matching variant. Run with `--help` for all options including per-variant color/shadow overrides.


#### QR Codes

1. Create QR codes using [Project Nayuki's QR Code generator library](https://github.com/nayuki/QR-Code-generator).
