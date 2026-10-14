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

## Title bar and ribbon (this app's own copy)

The title bar and ribbon code (`CraftTitlebar`, `CraftRibbon`, `CraftIcons`) started as one file shared by the Craft apps. **Each app now keeps its own copy and changes it on its own**: here it is its own <script> in labelcraft.src.html. Changes are not copied to the other apps, so the apps can be refined separately until it is clear how unified they should be. It provides:

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

- **Shapes, text boxes and shadows (same features in every Craft app that places objects):** box, circle/oval, triangle, diamond, pentagon, hexagon, octagon, star and arrow (plus lines), with corners from sharp to round (`shapePath`: 100% rounds each corner to half the shortest side), words inside, text boxes with wrapping, border, background, corners and padding, a drop shadow and opacity. Each app has its own copy of the shape geometry.

- **Print colour is part of the label** (`label.mode`: `'bw'` or `'color'`, plus `label.bg`). Picking stock sets it: sheets → colour, everything else → black & white; custom sizes keep the current mode. Black & white output goes through `toBlackWhite` (Atkinson dithering: solid black and white stay solid). The on-screen preview is a CSS grayscale filter on the lower canvas only, so selection handles stay coloured.
- **Sheets**: each sheet stock has `sheet: {page, pw, ph, cols, rows, lw, lh, left, top, hp, vp, approx}` in mm (built by `sheets()` from rows in inches or mm). Rows without margins are centred on the page and marked `approx`; the print dialog then suggests a test page with outlines. `also` lists other product codes with the same layout (searchable).
- **"Turn label 90°" on a sheet** stores `label.turn`; `cellImage` turns the picture back so it lands the right way on the sheet.
- **Discs** are shape `'disc'` with `label.hole` (mm): the canvas clip is an even-odd path (outer circle minus hole) and `#hole` covers the hole on screen. **Fold lines** are `label.folds` (`{x}` or `{y}` in mm, as designed); they are a DOM overlay (`#folds`), so they never print, and `turnFolds` turns them with the label. Case inserts that sit sideways on the page have `turn: 270` in the catalogue; `sheet.cut` turns on cut and fold marks by default.
- **Text formatting** works on the selected characters while editing (`range(o)`), otherwise on the whole text (`removeStyle` then `set`). `styleOf` reads a style over the range and returns undefined when mixed. Panel buttons `preventDefault` on mousedown so the text stays in editing mode. After changing text from code while editing, `syncEditing` copies it into fabric's hidden textarea (otherwise the next keystroke would undo it). Converting to a wrapped `Textbox` copies `o.styles` directly, because `toObject` writes styles in array form.
- **Curved text** is `kind: 'arc'`, a group of single-letter texts rebuilt from `o.arc` (text, `r` mm from the label centre, `pos` degrees with 0 at the top and clockwise, `dir` up/down, `span`, font, size, weight, style, fill, spacing, stroke, sw, shadow) by `buildArc`. In `object:modified`, moving changes `pos` and `r` (angle and distance of the group centre from the label centre, compared with a fresh build), the rotate handle adds to `pos`, scaling changes the size; then `replaceInPlace` rebuilds it on the circle. Font formatting reaches it through `arcStyleOf` / `arcPatch`, so the Text tab works on normal and curved text alike (`TX()`). Turning the label adds 90° to `pos`.
- **Tables** are `kind: 'table'` groups rebuilt from `o.tb` (cells, column widths and row heights in mm, font, lines) by `buildTable`; `swapObject` replaces the group in place. Scaling a table stretches columns and rows instead of scaling text.
- **PDF417, Micro PDF417, Data Matrix and Aztec** come from bwip-js 4.10.2 (`lib/bwip-js-min.js`, MIT): `toSVG` with scale 1, the path is placed in a group and scaled to the width; height follows the code's own shape.
- Sheet pages are drawn at 300 DPI with image smoothing off, so black & white dots stay pure. The printer adjustment is kept in localStorage `labelcraft-sheet-adjust`.

- **"Turn label 90°" turns the whole label,** content and all. Rotating an object only turns that object.
- **Fit-to-window zoom is skipped while the workspace is hidden** (under 40 px), so it doesn't calculate a zoom of zero.
- The grid column uses `minmax(0, 1fr)`, so a wide canvas cannot push the side panels off screen.

## History

| Version | Changes |
| --- | --- |
| 2026-10-13 | First version: stock catalogue, text, barcodes, QR codes, shapes, images, rotation, save/open, export |
| 2026-10-13 | Fonts made offline (`fetch_fonts.py`, `fonts/`) |
| 2026-10-14 | Ribbon, logo menu, customizable quick buttons |
| 2026-10-14 | Text tab redone with Office-style icon-only buttons in two rows (shared ribbon now supports `row` and `iconOnly`) |
| 2026-10-14 | v0.4: curved text (up / down around the label centre, drag in/out and around, spread), Word-style Text tab with colour palettes, effects, line and letter spacing |
| 2026-10-14 | v0.3: word-processor text formatting (per-word styles, highlight, outline, case, lists, justify, wrap, fit), tables, PDF417 / Micro PDF417 / Data Matrix / Aztec (bwip-js) |
| 2026-10-14 | CD/DVD disc labels with centre hole, spine strips, jewel case / booklet / tray card / DVD / slim DVD / Blu-ray inserts, fold lines, cut and fold marks |
| 2026-10-14 | v0.2: full colour or black & white, Avery US and A4 sheet layouts with compatible codes, laser/inkjet forms, custom sheets, sheet printing from any position, any colour for shapes; fixed an error when selecting a single shape |

## Ideas for later

- Batch and serial printing: numbered labels, or one label per row of a CSV file.
- Different labels on one sheet (mail merge from CSV, serial numbers per position).
- Check the centred (approximate) sheet layouts against Avery's published templates.

**2026-10-14:** Rotation angle box for curved text; shapes, text boxes, drop shadow and opacity.
