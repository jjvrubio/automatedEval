#!/usr/bin/env /usr/bin/python3
"""Export the macOS SF Symbols used by callouts as coloured PNG assets."""

from pathlib import Path
import sys

import AppKit


ASSETS = {
    "note": ("pencil.circle", "2563EB"),
    "info": ("info.circle", "0284C7"),
    "tip": ("lightbulb", "16A34A"),
    "success": ("checkmark.circle", "16A34A"),
    "question": ("questionmark.circle", "D97706"),
    "warning": ("exclamationmark.triangle", "D97706"),
    "danger": ("xmark.octagon", "DC2626"),
    "example": ("list.bullet.rectangle", "9333EA"),
    "quote": ("quote.bubble", "6B7280"),
}


def nscolor(hex_color: str):
    values = [int(hex_color[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    return AppKit.NSColor.colorWithCalibratedRed_green_blue_alpha_(*values, 1)


def export_symbol(output: Path, symbol_name: str, color: str) -> None:
    image = AppKit.NSImage.imageWithSystemSymbolName_accessibilityDescription_(
        symbol_name, output.stem
    )
    if image is None:
        raise RuntimeError(f"SF Symbol no disponible: {symbol_name}")

    size_config = AppKit.NSImageSymbolConfiguration.configurationWithPointSize_weight_(
        96, AppKit.NSFontWeightSemibold
    )
    palette_config = AppKit.NSImageSymbolConfiguration.configurationWithPaletteColors_(
        [nscolor(color)]
    )
    image = image.imageWithSymbolConfiguration_(size_config)
    image = image.imageWithSymbolConfiguration_(palette_config)

    canvas = AppKit.NSImage.alloc().initWithSize_((128, 128))
    canvas.lockFocus()
    AppKit.NSGraphicsContext.currentContext().setImageInterpolation_(
        AppKit.NSImageInterpolationHigh
    )
    image.drawInRect_fromRect_operation_fraction_(
        ((8, 8), (112, 112)),
        AppKit.NSZeroRect,
        AppKit.NSCompositingOperationSourceOver,
        1,
    )
    canvas.unlockFocus()

    bitmap = AppKit.NSBitmapImageRep.imageRepWithData_(canvas.TIFFRepresentation())
    png = bitmap.representationUsingType_properties_(AppKit.NSBitmapImageFileTypePNG, {})
    if not png.writeToFile_atomically_(str(output), True):
        raise RuntimeError(f"No se pudo escribir {output}")


def main() -> int:
    default_output = Path(__file__).resolve().parents[1] / "assets/icons/sf-symbols"
    output_dir = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else default_output
    output_dir.mkdir(parents=True, exist_ok=True)
    for filename, (symbol_name, color) in ASSETS.items():
        export_symbol(output_dir / f"{filename}.png", symbol_name, color)
        print(f"Generado {filename}.png ← {symbol_name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
