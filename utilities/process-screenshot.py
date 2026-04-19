#!/usr/bin/env python3
"""
process-screenshot.py

Generate themed screenshot variants with borders and drop shadows for
Silmärin. Produces two variants per input image for Zensical light/dark
theme support:

  {name}-light.png  ->  light theme pages (#only-light): dark border + shadow
  {name}-dark.png   ->  dark theme pages  (#only-dark):  light border + glow

Usage:
  python process-screenshot.py <input> [options]

Examples:
  python process-screenshot.py screenshot.png
  python process-screenshot.py path/to/images/*.png --output-dir ./processed
  python process-screenshot.py crop.png --variants light --border-width 3
  python process-screenshot.py docs/resources/images/ --recurse
  python process-screenshot.py screenshot.png --profile uw-purple

Run with --help for full options.
"""

# @format

# region Imports

import argparse
import copy
import glob
import sys
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:
    print(
        "Error: Pillow is required. Install with: pip install pillow",
        file=sys.stderr,
    )
    sys.exit(1)

# endregion


# region Configuration

# =============================================================================
# Configuration
# =============================================================================
# Adjust these values to change the visual appearance of generated images.
# All sizes are in pixels. Colors are RGBA tuples (0-255).
# After editing, re-run the script to regenerate images with the new settings.

# Border width around the screenshot content.
BORDER_WIDTH = 2

# Transparent padding around the bordered image to contain the drop shadow.
# Increase if shadow appears clipped at the edges.
SHADOW_PADDING = 32

# -----------------------------------------------------------------------------
# Light-theme variant
# -----------------------------------------------------------------------------
# Displayed on light pages via #only-light.
# Uses a dark border and dark drop shadow to stand out against light backgrounds
LIGHT_PROFILE = {
    "border_color": (34, 34, 34, 255),  # #222222 - very dark gray
    # Ambient shadow: large, soft, centered - creates overall depth
    "ambient": {
        "color": (0, 0, 0, 32),  # ~12.5% opacity black
        "blur": 12,  # Max is 12 for 32 padding and 255 opacity
        "offset": (0, 0),
    },
    # Key shadow: smaller, offset downward - creates directional light effect
    "key": {
        "color": (0, 0, 0, 64),  # ~25% opacity black
        "blur": 2,
        "offset": (0, 4),
    },
}

# -----------------------------------------------------------------------------
# Dark-theme variant
# -----------------------------------------------------------------------------
# Displayed on dark pages via #only-dark.
# Uses a light border and subtle glow to stand out against dark backgrounds
DARK_PROFILE = {
    "border_color": (85, 85, 85, 255),  # #555555 - light gray
    # Ambient glow: large, soft, centered - creates subtle edge definition
    "ambient": {
        "color": (221, 221, 221, 32),  # ~12.5% opacity near-white
        "blur": 4,  # Narrower ambient for dark theme to reduce banding
        "offset": (0, 0),
    },
    # Key glow: smaller, offset downward - adds subtle directional light
    "key": {
        "color": (221, 221, 221, 51),  # ~20% opacity near-white
        "blur": 2,
        "offset": (0, 4),
    },
}

# Supported image extensions for directory scanning.
# Can be added: ".bmp", ".gif", ".tiff", ".tif", ".webp"
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}

# endregion

# region Custom Profiles

# =============================================================================
# Custom Profiles
# =============================================================================
# Named presets that override default settings. Select with --profile <name>.
# Each profile can override any combination of: border_width, shadow_padding,
# light (theme profile), and dark (theme profile). Omitted keys fall through
# to the script-level defaults above. CLI arguments override profile values.
#
# Silmärin Palette Reference:
#   Midnight Blue:     #1A1A2E  (26,26,46)    — deep night sky
#   Twilight Indigo:   #2C2C54  (44,44,84)    — dusky blue-violet
#   Moonlit Silver:    #B0C4DE  (176,196,222)  — pale moonlight
#   Starlight White:   #D6E4F0  (214,228,240)  — soft silvery white
#   Ethereal Blue:     #4A6FA5  (74,111,165)   — tranquil blue
#   Archive Gold:      #C9A96E  (201,169,110)  — warm antique gold
#
# =============================================================================

CUSTOM_PROFILES: dict[str, dict[str, Any]] = {
    # Ethereal Blue borders with moonlit-tinted shadows for both themes.
    "moonlight": {
        "light": {
            "border_color": (74, 111, 165, 255),  # #4A6FA5 — Ethereal Blue
            "ambient": {
                "color": (74, 111, 165, 32),  # Blue-tinted ambient
                "blur": 12,
                "offset": (0, 0),
            },
            "key": {
                "color": (74, 111, 165, 64),  # Blue-tinted key
                "blur": 2,
                "offset": (0, 4),
            },
        },
        "dark": {
            "border_color": (176, 196, 222, 255),  # #B0C4DE — Moonlit Silver
            "ambient": {
                "color": (176, 196, 222, 32),  # Silver-tinted ambient
                "blur": 4,
                "offset": (0, 0),
            },
            "key": {
                "color": (176, 196, 222, 48),  # Silver-tinted key
                "blur": 2,
                "offset": (0, 4),
            },
        },
    },
    # Twilight Indigo (light) / Archive Gold (dark) borders with matching shadows.
    "archive": {
        "light": {
            "border_color": (44, 44, 84, 255),  # #2C2C54 — Twilight Indigo
            "ambient": {
                "color": (44, 44, 84, 32),  # Indigo-tinted ambient
                "blur": 12,
                "offset": (0, 0),
            },
            "key": {
                "color": (44, 44, 84, 64),  # Indigo-tinted key
                "blur": 2,
                "offset": (0, 4),
            },
        },
        "dark": {
            "border_color": (201, 169, 110, 255),  # #C9A96E — Archive Gold
            "ambient": {
                "color": (201, 169, 110, 32),  # Gold-tinted ambient
                "blur": 4,
                "offset": (0, 0),
            },
            "key": {
                "color": (201, 169, 110, 48),  # Gold-tinted key
                "blur": 2,
                "offset": (0, 4),
            },
        },
    },
}

# endregion

# region Utility Functions


def is_output_file(p: Path) -> bool:
    """Return True if a file matches the output naming pattern (-light/-dark).

    Output files use a dash suffix: example-light.png, example-dark.png.
    Source files use a dot suffix: example.light.png, example.dark.png.
    This prevents re-processing previously generated output files.
    """
    s = p.stem
    return s.endswith("-light") or s.endswith("-dark")


def create_shadow_layer(
    canvas_size: tuple[int, int],
    rect: tuple[int, int, int, int],
    color: tuple[int, int, int, int],
    blur_radius: int,
    offset: tuple[int, int],
) -> Image.Image:
    """Create a single shadow/glow layer with Gaussian blur.

    Args:
        canvas_size: (width, height) of the output layer.
        rect: (x0, y0, x1, y1) base rectangle position (before offset).
        color: RGBA fill color for the shadow rectangle.
        blur_radius: Gaussian blur radius. 0 for no blur.
        offset: (dx, dy) pixel offset for the shadow rectangle.

    Returns:
        RGBA Image with the blurred shadow.
    """
    layer = Image.new("RGBA", canvas_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    x0 = rect[0] + offset[0]
    y0 = rect[1] + offset[1]
    x1 = rect[2] + offset[0]
    y1 = rect[3] + offset[1]

    draw.rectangle([x0, y0, x1, y1], fill=color)

    if blur_radius > 0:
        layer = layer.filter(ImageFilter.GaussianBlur(radius=blur_radius))

    return layer


def process_image(
    img: Image.Image,
    profile: dict,
    border_width: int,
    shadow_padding: int,
) -> Image.Image:
    """Add border and two-layer drop shadow to an image.

    Args:
        img: Source image.
        profile: Shadow/border profile dict (LIGHT_PROFILE or DARK_PROFILE).
        border_width: Border width in pixels.
        shadow_padding: Padding around bordered image for shadow space.

    Returns:
        RGBA Image with border and shadow applied.
    """
    img = img.convert("RGBA")

    # Bordered image dimensions
    bordered_w = img.width + 2 * border_width
    bordered_h = img.height + 2 * border_width

    # Total canvas = bordered image + shadow padding on all sides
    canvas_w = bordered_w + 2 * shadow_padding
    canvas_h = bordered_h + 2 * shadow_padding

    # Position of bordered image on the canvas (centered)
    img_x = shadow_padding
    img_y = shadow_padding

    # Shadow source rectangle (matches bordered image bounds)
    shadow_rect = (img_x, img_y, img_x + bordered_w -
                   1, img_y + bordered_h - 1)

    # Layer 1: Ambient shadow (large, soft, centered)
    ambient = create_shadow_layer(
        (canvas_w, canvas_h),
        shadow_rect,
        profile["ambient"]["color"],
        profile["ambient"]["blur"],
        profile["ambient"]["offset"],
    )

    # Layer 2: Key shadow (smaller, directional)
    key = create_shadow_layer(
        (canvas_w, canvas_h),
        shadow_rect,
        profile["key"]["color"],
        profile["key"]["blur"],
        profile["key"]["offset"],
    )

    # Composite shadows: ambient → key
    result = Image.alpha_composite(ambient, key)

    # Create bordered image (border color fill + source image inset)
    bordered = Image.new("RGBA", (bordered_w, bordered_h),
                         profile["border_color"])
    bordered.paste(img, (border_width, border_width))

    # Place bordered image on top of shadow layers
    result.paste(bordered, (img_x, img_y), bordered)

    return result


def parse_rgba(value: str) -> tuple[int, int, int, int]:
    """Parse an RGBA color from a comma-separated string.

    Args:
        value: String like "43,43,43,255" or "0,0,0,15".

    Returns:
        Tuple of (R, G, B, A) integers 0-255.

    Raises:
        argparse.ArgumentTypeError: If the format is invalid.
    """
    try:
        parts = [int(x.strip()) for x in value.split(",")]
        if len(parts) != 4 or not all(0 <= p <= 255 for p in parts):
            raise ValueError
        return (parts[0], parts[1], parts[2], parts[3])
    except (ValueError, IndexError):
        raise argparse.ArgumentTypeError(
            f"Invalid RGBA color '{value}'. Expected format: R,G,B,A (0-255 each)."
        )


def parse_offset(value: str) -> tuple[int, int]:
    """Parse an x,y offset from a comma-separated string.

    Args:
        value: String like "0,2" or "-1,3".

    Returns:
        Tuple of (x, y) integers.

    Raises:
        argparse.ArgumentTypeError: If the format is invalid.
    """
    try:
        parts = [int(x.strip()) for x in value.split(",")]
        if len(parts) != 2:
            raise ValueError
        return (parts[0], parts[1])
    except (ValueError, IndexError):
        raise argparse.ArgumentTypeError(
            f"Invalid offset '{value}'. Expected format: X,Y (integers)."
        )


def resolve_profile(
    base: dict,
    custom: dict | None,
    prefix: str,
    args: argparse.Namespace,
) -> dict:
    """Build a resolved theme profile by layering: base → custom → CLI overrides.

    Args:
        base: Script-level default profile (LIGHT_PROFILE or DARK_PROFILE).
        custom: Optional named custom profile dict for this theme, or None.
        prefix: CLI argument prefix ("light" or "dark").
        args: Parsed argparse namespace.

    Returns:
        New profile dict with all applicable overrides applied.
    """
    # Start with script defaults
    p = copy.deepcopy(base)

    # Layer named custom profile on top (if provided)
    if custom is not None:
        if "border_color" in custom:
            p["border_color"] = custom["border_color"]
        for layer in ("ambient", "key"):
            if layer in custom:
                for key in ("color", "blur", "offset"):
                    if key in custom[layer]:
                        p[layer][key] = custom[layer][key]

    # Layer CLI overrides on top (highest priority)
    border = getattr(args, f"{prefix}_border_color", None)
    if border is not None:
        p["border_color"] = border

    for layer in ("ambient", "key"):
        color = getattr(args, f"{prefix}_{layer}_color", None)
        if color is not None:
            p[layer]["color"] = color

        blur = getattr(args, f"{prefix}_{layer}_blur", None)
        if blur is not None:
            p[layer]["blur"] = blur

        offset = getattr(args, f"{prefix}_{layer}_offset", None)
        if offset is not None:
            p[layer]["offset"] = offset

    return p


def process_file(
    input_path: Path,
    output_dir: Path | None,
    variants: str,
    border_width: int,
    shadow_padding: int,
    light_profile: dict,
    dark_profile: dict,
    overwrite: bool = False,
) -> list[Path]:
    """Process a single image file and write output variant(s).

    Mode-tag detection:
      If the source filename contains a `.light` or `.dark` segment before the
      extension (e.g. `example.light.png`), only the matching variant is
      generated and the dot-tag is replaced with a dash-suffix in the output:
        example.light.png  ->  example-light.png
        example.dark.png   ->  example-dark.png

      Untagged files (e.g. `example.png`) generate both variants as usual:
        example.png  ->  example-light.png + example-dark.png

    The --variants CLI flag further constrains output. For example, a
    `.light`-tagged file with --variants dark produces no output.

    Args:
        input_path: Path to the source image.
        output_dir: Output directory. None = same directory as input.
        variants: "both", "light", or "dark".
        border_width: Border width in pixels.
        shadow_padding: Shadow padding in pixels.
        light_profile: Resolved light-theme profile dict.
        dark_profile: Resolved dark-theme profile dict.
        overwrite: If False, raise FileExistsError when output files exist.

    Returns:
        List of output file paths written.

    Raises:
        FileExistsError: If an output file already exists and overwrite is False.
    """
    img = Image.open(input_path)
    stem = input_path.stem
    out_dir = output_dir or input_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # Detect mode tag: "example.light" -> stem="example", mode_tag="light"
    mode_tag: str | None = None
    if stem.endswith(".light"):
        mode_tag = "light"
        stem = stem[: -len(".light")]
    elif stem.endswith(".dark"):
        mode_tag = "dark"
        stem = stem[: -len(".dark")]

    # Build the set of variants to generate
    requested = set()
    if variants in ("both", "light"):
        requested.add("light")
    if variants in ("both", "dark"):
        requested.add("dark")

    # If mode-tagged, restrict to only that variant
    if mode_tag is not None:
        requested &= {mode_tag}

    profiles = {}
    if "light" in requested:
        profiles["light"] = light_profile
    if "dark" in requested:
        profiles["dark"] = dark_profile

    if not profiles and mode_tag:
        print(
            f"  Skipped: .{mode_tag} source excluded by --variants {variants}",
        )

    outputs = []
    for variant_name, profile in profiles.items():
        result = process_image(img, profile, border_width, shadow_padding)
        out_path = out_dir / f"{stem}-{variant_name}.png"

        if out_path.exists() and not overwrite:
            raise FileExistsError(
                f"Output file already exists: {out_path}\n"
                f"  Re-run with --overwrite to replace existing files."
            )

        # Save as maximally-compressed lossless PNG with no metadata.
        # compress_level=9 applies maximum zlib deflate compression.
        # Pillow writes no text chunks, no gamma, no ICC profile —
        # only the mandatory IHDR, IDAT, and IEND chunks.
        result.save(out_path, "PNG", compress_level=9)
        outputs.append(out_path)
        print(f"  -> {out_path}")

    return outputs

# endregion

# region Main


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Generate themed screenshot variants with borders and drop shadows "
            "for Zensical light/dark theme support."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Output naming:
  Untagged source (generates both variants):
    input.png        ->  input-light.png  +  input-dark.png

  Mode-tagged source (generates only the matching variant):
    input.light.png  ->  input-light.png   (light only)
    input.dark.png   ->  input-dark.png    (dark only)

  The dot-separator (.light/.dark) marks the SOURCE file's intended theme.
  The dash-separator (-light/-dark) marks the OUTPUT file for Zensical.
  Source files are never overwritten.

  Sibling detection:
    If img.dark.png and img.png coexist, img.png produces only -light.
    If both img.light.png and img.dark.png exist, img.png is skipped.
    The --variants flag further constrains which outputs are generated.

Markdown usage:
  ![Alt text](path/to/image-light.png#only-light){{ width="300" }}
  ![Alt text](path/to/image-dark.png#only-dark){{ width="300" }}

Configuration:
  Edit the LIGHT_PROFILE, DARK_PROFILE, BORDER_WIDTH, and SHADOW_PADDING
  constants at the top of this script to change defaults permanently.
  Use CLI arguments below to override any setting for a single run.
  Use --profile <name> to apply a named custom profile preset.
  Priority: script defaults < --profile < CLI overrides.

Custom profiles:  {profiles_list}

Color format:  R,G,B,A   (0-255 each, e.g. "43,43,43,255")
Offset format: X,Y       (pixels, e.g. "0,2")
""".format(
            profiles_list=(
                ", ".join(CUSTOM_PROFILES.keys()
                          ) if CUSTOM_PROFILES else "(none)"
            )
        ),
    )

    # -------------------------------------------------------------------------
    # General options
    # -------------------------------------------------------------------------
    parser.add_argument(
        "input",
        nargs="+",
        help=(
            "Input image path(s), directory path(s), or glob patterns. "
            "Directories are scanned for image files (use --recurse for subdirs)."
        ),
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory (default: same directory as each input file).",
    )
    parser.add_argument(
        "--recurse",
        action="store_true",
        default=False,
        help="Recursively scan directories for image files (default: off).",
    )
    parser.add_argument(
        "--variants",
        choices=["both", "light", "dark"],
        default="both",
        help="Which variant(s) to generate (default: both).",
    )
    parser.add_argument(
        "--border-width",
        type=int,
        default=BORDER_WIDTH,
        help=f"Border width in pixels (default: {BORDER_WIDTH}).",
    )
    parser.add_argument(
        "--shadow-padding",
        type=int,
        default=SHADOW_PADDING,
        help=f"Shadow padding in pixels (default: {SHADOW_PADDING}).",
    )
    parser.add_argument(
        "--profile",
        type=str,
        default=None,
        choices=list(CUSTOM_PROFILES.keys()),
        help="Apply a named custom profile preset. CLI overrides still take priority.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="Overwrite existing output files (default: error if they exist).",
    )

    # -------------------------------------------------------------------------
    # Light-theme profile overrides
    # -------------------------------------------------------------------------
    light_group = parser.add_argument_group(
        "light-theme overrides",
        "Override light-theme profile settings for this run.",
    )
    light_group.add_argument(
        "--light-border-color",
        type=parse_rgba,
        default=None,
        dest="light_border_color",
        metavar="R,G,B,A",
        help=f"Border color (default: {','.join(str(c) for c in LIGHT_PROFILE['border_color'])}).",
    )
    light_group.add_argument(
        "--light-ambient-color",
        type=parse_rgba,
        default=None,
        dest="light_ambient_color",
        metavar="R,G,B,A",
        help=f"Ambient shadow color (default: {','.join(str(c) for c in LIGHT_PROFILE['ambient']['color'])}).",
    )
    light_group.add_argument(
        "--light-ambient-blur",
        type=int,
        default=None,
        dest="light_ambient_blur",
        help=f"Ambient shadow blur radius (default: {LIGHT_PROFILE['ambient']['blur']}).",
    )
    light_group.add_argument(
        "--light-ambient-offset",
        type=parse_offset,
        default=None,
        dest="light_ambient_offset",
        metavar="X,Y",
        help=f"Ambient shadow offset (default: {','.join(str(c) for c in LIGHT_PROFILE['ambient']['offset'])}).",
    )
    light_group.add_argument(
        "--light-key-color",
        type=parse_rgba,
        default=None,
        dest="light_key_color",
        metavar="R,G,B,A",
        help=f"Key shadow color (default: {','.join(str(c) for c in LIGHT_PROFILE['key']['color'])}).",
    )
    light_group.add_argument(
        "--light-key-blur",
        type=int,
        default=None,
        dest="light_key_blur",
        help=f"Key shadow blur radius (default: {LIGHT_PROFILE['key']['blur']}).",
    )
    light_group.add_argument(
        "--light-key-offset",
        type=parse_offset,
        default=None,
        dest="light_key_offset",
        metavar="X,Y",
        help=f"Key shadow offset (default: {','.join(str(c) for c in LIGHT_PROFILE['key']['offset'])}).",
    )

    # -------------------------------------------------------------------------
    # Dark-theme profile overrides
    # -------------------------------------------------------------------------
    dark_group = parser.add_argument_group(
        "dark-theme overrides",
        "Override dark-theme profile settings for this run.",
    )
    dark_group.add_argument(
        "--dark-border-color",
        type=parse_rgba,
        default=None,
        dest="dark_border_color",
        metavar="R,G,B,A",
        help=f"Border color (default: {','.join(str(c) for c in DARK_PROFILE['border_color'])}).",
    )
    dark_group.add_argument(
        "--dark-ambient-color",
        type=parse_rgba,
        default=None,
        dest="dark_ambient_color",
        metavar="R,G,B,A",
        help=f"Ambient glow color (default: {','.join(str(c) for c in DARK_PROFILE['ambient']['color'])}).",
    )
    dark_group.add_argument(
        "--dark-ambient-blur",
        type=int,
        default=None,
        dest="dark_ambient_blur",
        help=f"Ambient glow blur radius (default: {DARK_PROFILE['ambient']['blur']}).",
    )
    dark_group.add_argument(
        "--dark-ambient-offset",
        type=parse_offset,
        default=None,
        dest="dark_ambient_offset",
        metavar="X,Y",
        help=f"Ambient glow offset (default: {','.join(str(c) for c in DARK_PROFILE['ambient']['offset'])}).",
    )
    dark_group.add_argument(
        "--dark-key-color",
        type=parse_rgba,
        default=None,
        dest="dark_key_color",
        metavar="R,G,B,A",
        help=f"Key glow color (default: {','.join(str(c) for c in DARK_PROFILE['key']['color'])}).",
    )
    dark_group.add_argument(
        "--dark-key-blur",
        type=int,
        default=None,
        dest="dark_key_blur",
        help=f"Key glow blur radius (default: {DARK_PROFILE['key']['blur']}).",
    )
    dark_group.add_argument(
        "--dark-key-offset",
        type=parse_offset,
        default=None,
        dest="dark_key_offset",
        metavar="X,Y",
        help=f"Key glow offset (default: {','.join(str(c) for c in DARK_PROFILE['key']['offset'])}).",
    )

    args = parser.parse_args()

    # Resolve named custom profile (if any).
    # argparse choices= constraint validates the name; .get() is a safety net.
    custom = CUSTOM_PROFILES.get(args.profile) if args.profile else None

    # Resolve final profiles: script defaults → custom profile → CLI overrides
    custom_light = custom.get("light") if custom else None
    custom_dark = custom.get("dark") if custom else None

    light_profile = resolve_profile(LIGHT_PROFILE, custom_light, "light", args)
    dark_profile = resolve_profile(DARK_PROFILE, custom_dark, "dark", args)

    # Resolve border_width and shadow_padding: custom profile → CLI
    border_width = args.border_width
    shadow_padding = args.shadow_padding
    if custom:
        if "border_width" in custom and args.border_width == BORDER_WIDTH:
            border_width = int(custom["border_width"])
        if "shadow_padding" in custom and args.shadow_padding == SHADOW_PADDING:
            shadow_padding = int(custom["shadow_padding"])

    if args.profile:
        print(f"Using profile: {args.profile}")

    # Expand glob patterns, directories, and direct paths into a file list
    input_files: list[Path] = []
    for pattern in args.input:
        path = Path(pattern)

        if path.is_dir():
            # Directory: collect image files (optionally recursive)
            if args.recurse:
                found = sorted(path.rglob("*"))
            else:
                found = sorted(path.iterdir())
            dir_images = [
                f for f in found
                if f.is_file()
                and f.suffix.lower() in IMAGE_EXTENSIONS
                and not is_output_file(f)
            ]
            if not dir_images:
                print(
                    f"Warning: No image files in '{path}'"
                    f"{' (recursive)' if args.recurse else ''}, skipping.",
                    file=sys.stderr,
                )
            input_files.extend(dir_images)
        else:
            # Glob pattern or direct file path
            expanded = glob.glob(pattern, recursive=args.recurse)
            if expanded:
                input_files.extend(
                    Path(p) for p in expanded
                    if Path(p).is_file()
                    and Path(p).suffix.lower() in IMAGE_EXTENSIONS
                    and not is_output_file(Path(p))
                )
            elif path.is_file():
                if is_output_file(path):
                    print(
                        f"Warning: '{path}' looks like an output file "
                        f"(ends with -light/-dark), skipping.",
                        file=sys.stderr,
                    )
                else:
                    input_files.append(path)
            else:
                print(
                    f"Warning: '{pattern}' not found, skipping.", file=sys.stderr)

    if not input_files:
        print("Error: No input files found.", file=sys.stderr)
        sys.exit(1)

    # Deduplicate while preserving order (overlapping globs/directories).
    seen: set[Path] = set()
    unique_files: list[Path] = []
    for f in input_files:
        resolved = f.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique_files.append(f)
    input_files = unique_files

    # Skip untagged files when both .light and .dark tagged siblings exist.
    # When only one tagged sibling exists, restrict the untagged file to the
    # uncovered variant instead of skipping it entirely.
    # e.g. accessmap.png + accessmap.dark.png → accessmap.png produces -light only.
    input_set = {f.resolve() for f in input_files}
    work_items: list[tuple[Path, str]] = []  # (path, variants_override)
    for f in input_files:
        stem = f.stem
        # Only check files that are NOT mode-tagged themselves
        if not (stem.endswith(".light") or stem.endswith(".dark")):
            light_sibling = f.with_name(f"{stem}.light{f.suffix}")
            dark_sibling = f.with_name(f"{stem}.dark{f.suffix}")
            has_light = light_sibling.resolve() in input_set
            has_dark = dark_sibling.resolve() in input_set
            if has_light and has_dark:
                print(
                    f"Skipping '{f.name}': mode-tagged variants "
                    f"'{light_sibling.name}' and '{dark_sibling.name}' "
                    f"already cover both themes."
                )
                continue
            elif has_light or has_dark:
                sibling = light_sibling if has_light else dark_sibling
                covered = "light" if has_light else "dark"
                other = "dark" if has_light else "light"
                # Check if the uncovered variant is allowed by --variants
                if args.variants != "both" and args.variants != other:
                    print(
                        f"Skipping '{f.name}': '{sibling.name}' covers "
                        f"{covered} theme; {other} theme excluded by "
                        f"--variants {args.variants}."
                    )
                    continue
                print(
                    f"Note: '{sibling.name}' covers {covered} theme; "
                    f"'{f.name}' will produce only the {other} variant."
                )
                work_items.append((f, other))
                continue
        work_items.append((f, args.variants))

    if not work_items:
        print("Error: No input files to process after filtering.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(work_items)} image(s) to process.")

    total_outputs: list[Path] = []
    for input_path, file_variants in work_items:
        print(f"Processing: {input_path}")
        try:
            outputs = process_file(
                input_path,
                args.output_dir,
                file_variants,
                border_width,
                shadow_padding,
                light_profile,
                dark_profile,
                args.overwrite,
            )
            total_outputs.extend(outputs)
        except Exception as e:
            print(f"  Error: {e}", file=sys.stderr)

    print(f"\nDone. Generated {len(total_outputs)} file(s).")

# endregion


if __name__ == "__main__":
    main()
