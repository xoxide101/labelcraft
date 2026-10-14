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

## Title bar and ribbon (shared)

All four Craft apps use the same `craft-titlebar.js` code: in SiteCraft and DataCraft as a file, pasted into the single-file apps (LabelCraft as its own `<script>`, ShiftCraft inside its main script, so the emailable copy keeps working). It provides:

- **`CraftTitlebar`:**
  - logo button that opens every classic menu side by side (F10)
  - quick buttons that people can hide or extend with any command (⌄; right-click a quick button to remove it; kept in localStorage `<app>-quick`)
  - file name and save state
  - **Search commands (Alt+Q)** over menus and ribbon, with recently used commands
  - info chips, theme and help
- **`CraftRibbon`:** tabs of labelled buttons in named groups, one color per tab, collapse with ⌃ or a double-click; remembers the last tab.
- **`CraftIcons`:** the shared icon set.

Ribbon buttons reuse the apps' own menu commands (looked up by label), so a button and its menu item always do the same thing. Each app has a matching logo in `docs/logo.svg` (also used as the browser-tab icon).

## Title bar

The Office-style strip at the very top is the shared `CraftTitlebar` component, pasted into `labelcraft.src.html` as its own `<script>` (so the single-file build keeps working).

- **Quick buttons:** save, undo, redo, export, print.
- **Info chips:** label stock and size.
- **Search:** Alt+Q searches every menu command.

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
