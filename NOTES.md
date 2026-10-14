# LabelCraft – development notes

How LabelCraft is built and what to keep in mind when changing it. For what it does and how to use it, see [README.md](README.md).

## How it is built

- **Source:** `labelcraft.src.html` (HTML, CSS and JavaScript in one file). Run `python build.py` after every change.
- **`build.py`** writes:
  - `index.html`: points the library tags at `lib/` and the fonts at `fonts/fonts.css`, so it works offline.
  - `dist/artifact.html`: a single page that loads the libraries from cdnjs.
- **Libraries** (in `lib/`): Fabric.js 5.3.1 (the canvas), JsBarcode 3.11.6 (barcodes), qrcode-generator 1.4.4 (QR codes, UTF-8).
- **Fonts:** `fetch_fonts.py` downloads the Google fonts (Latin and Latin Extended only) into `fonts/` and writes `fonts/fonts.css`. Variable fonts share files, so 26 `@font-face` rules use 16 files.

## Model

- The canvas works in **pixels at 300 DPI**; the interface shows millimetres or inches.
- **Barcodes are rebuilt as exact-size vector paths** whenever their size or value changes. They are never stretched, which would make them unreadable.
- **Label file format:** JSON `{ app: 'LabelCraft', version, label, canvas }`, where `canvas` is Fabric's JSON.
- **Stock catalogue** (`STOCK`): about 70 sizes covering Dymo LabelWriter, Dymo D1 tape, Brother DK, Brother TZe, Zebra/thermal, and Avery US Letter and A4. Shapes: rounded or square corners, round/oval, or continuous tape with a length.
- **Export:** PNG, JPG or SVG at 203, 300 or 600 DPI. 203 and 300 match most thermal label printers.

## Decisions

- **"Turn label 90°" turns the whole label,** content and all. Rotating an object only turns that object.
- **Fit-to-window zoom is skipped while the workspace is hidden** (under 40 px), so it doesn't calculate a zoom of zero.
- The grid column uses `minmax(0, 1fr)`, so a wide canvas cannot push the side panels off screen.

## History

| Version | Changes |
| --- | --- |
| 2026-10-13 | First version: stock catalogue, text, barcodes, QR codes, shapes, images, rotation, save/open, export |
| 2026-10-13 | Fonts made offline (`fetch_fonts.py`, `fonts/`) |

## Ideas for later

- Batch and serial printing: numbered labels, or one label per row of a CSV file.
- Print several labels per sheet for Avery stock.
