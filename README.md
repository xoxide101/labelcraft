<img src="docs/logo.svg" width="64" height="64" alt="LabelCraft logo">

# LabelCraft

**A label maker that runs in your browser: Dymo, Brother, Zebra and Avery labels with barcodes and QR codes.**

Pick your label stock, add text, barcodes, QR codes, shapes and logos, rotate them any way you need, then print at real size or export a sharp image. Everything works offline from this folder.

![LabelCraft designing a Dymo 30334 shelf label with rotated text and a Code 128 barcode](docs/editor.png)

## Getting started

1. Download this repository (green **Code** button › **Download ZIP**) or clone it.
2. Double-click `index.html`. It opens in Chrome or Edge.
3. Pick your **label stock** on the left (search by name, code or size), or type a **custom size**.
4. Add text, a barcode or a QR code from the toolbar, then **File › Print** or **Export**.

Your label also autosaves in the browser.

## Finding your way

| Where | What is there |
| --- | --- |
| **LabelCraft logo** (top left) | Every command in classic menus: File, Edit, Insert, View, Help (also F10) |
| **Top bar** | Quick buttons (save, undo, redo, export, print; customize them with ⌄), the label name, **Search commands (Alt+Q)**, label stock and size, theme, help |
| **Ribbon tabs** | **Home** (clipboard, label), **Insert** (text, barcode, QR code, shapes, image), **Arrange** (rotate, order), **View** (zoom, guides, units, theme), **Output** (export, print, save) |

## What it does

### Label stock (100+ sizes built in)
- **Dymo LabelWriter** (30252 address, 30334 multipurpose, 30256 shipping…)
- **Dymo D1** tape
- **Brother DK** rolls and **Brother TZe** tape
- **Zebra / thermal** labels
- **Avery** sheets for laser and inkjet printers, with their real sheet layouts: 22 US Letter templates (5160, 5161, 5162, 5163, 5164, 5167, 5195, 5366, 5395, 5371, round and square labels…) and 20 A4 templates (L7160/J8160, L7163, L7165, L7651…). **Search for any compatible code**: 8160, 5960, 18160 and 40 other codes all find 5160.
- **Laser and inkjet forms**: full, half, quarter and sixth sheets on Letter, A4 (A5, A6, A7) and Legal, plus two 4 × 6 in shipping labels per page.
- **CD and DVD labels**: discs with the centre hole cut out: Avery 8931 (5931, 5692, 8692) and L7676 / J8676, full-face labels (small hole) on Letter and A4, inkjet-printable discs and mini CDs. The hole stays blank when printing.
- **CD and DVD case inserts** on Letter and A4: jewel case front cover, folded booklet, tray card with both spines, spine strips, and DVD (14 mm spine), slim DVD (7 mm) and Blu-ray covers. Blue dashed **fold lines** show the spines on screen (not printed), and inserts print with **cut marks and fold marks**.
- **Custom sheet** for any other sheet: label size, page (Letter, A4, Legal), labels across and down, gaps.
- **Custom size** in mm or inches: rounded or square corners, round / oval, or continuous tape (set the tape length).
- **Turn label 90°** turns the whole label sideways, content and all.

### Design
- **Text, formatted like a word processor** (Text tab, Format menu or the panel on the right): 29 fonts (Barlow Condensed, Oswald, Roboto Mono and Archivo Black bundled, plus common Windows and Mac fonts), size with bigger / smaller, **bold, italic, underline, strikethrough, overline, superscript, subscript**, text colour, **highlight**, text **outline**, change case (UPPERCASE, lowercase, Title Case, Sentence case), clear formatting, align left / centre / right / **justify**, **bullets and numbering**, letter spacing and line height.
- **Format just some words**: double-click the text on the label, select the words, then pick the formatting (Ctrl+B, Ctrl+I, Ctrl+U, Ctrl+] and Ctrl+[ work too).
- **Wrap text in a box** of a set width, **Fit to label** width, and insert today's date, the time or symbols (© ® ™ ° ± € ✓ ★ ⚠ …).
- **Tables**: type into a grid in the side panel (double-click the table to start), add or delete rows and columns, heading row, font, size, alignment, grid lines, padding; resize by dragging and text shrinks to fit each cell.
- **Shapes**: box, ellipse, line. **Images and logos** from your computer.
- **Rotate** anything **90° left, 90° right or 180°**, or type any angle.
- **Align** to the label edges and centre; **snap to centre**; bring to front / send to back.
- **Safe print area** guide, zoom, fit to window, actual size (100%).
- Undo / redo, cut / copy / paste / duplicate, select all, nudge with the arrow keys.

### Barcodes and QR codes
Barcodes are drawn as exact vector bars at the size you set, so they never get blurry or stretched.

| Type | Use |
| --- | --- |
| Code 128 | Letters and numbers (most common) |
| Code 39 | Capitals, numbers, `- . $ / + %` |
| EAN-13 / EAN-8 | Retail products |
| UPC-A | US retail |
| ITF-14 / Interleaved 2 of 5 | Shipping cartons |
| Codabar | Libraries, blood banks |
| MSI | Shelf labels |
| Pharmacode | Pharmaceutical packaging |
| QR code | Links, text, Wi-Fi details… (full Unicode) |
| PDF417 | Lots of data in a small space: ID cards, shipping, boarding passes (set the columns to change its shape) |
| Micro PDF417 | Small items |
| Data Matrix | Electronics, healthcare, small parts |
| Aztec | Tickets and transport |

### Save, print and export
- **Save / Open** label files (`.json`), so you can reuse and edit labels later.
- **Print** at the label's real size.
- **Print sheets** for laser and inkjet: full sheets, or just some labels **starting at any position** (click the spot on the sheet picture), so partly used sheets are not wasted. Optional label outlines for a test on plain paper, and a **printer adjustment** (move right / down) that is remembered. Sheets can also be saved as 300 DPI PNG pages.
- **Full colour or black & white**: thermal printer labels start in black & white and the preview shows what prints (colours become black, white or a fine dot pattern; text and barcodes stay crisp). Sheet labels start in full colour; pick any colour for text, fills and outlines, and set a label colour for coloured stock.

![Printing a sheet of Avery 5160 labels, starting at label 8](docs/sheet-print.png)

- **Export** as **PNG**, **JPG** or **SVG** at **203, 300 or 600 DPI** (203 and 300 match most label printers).
- Light and dark mode for the editor (the theme never changes what prints).

## Keyboard shortcuts

| Action | Keys |
| --- | --- |
| Open a label | Ctrl+O |
| Save / Save as | Ctrl+S / Ctrl+Shift+S |
| Export image | Ctrl+E |
| Print | Ctrl+P |
| Undo / Redo | Ctrl+Z / Ctrl+Y |
| Cut / Copy / Paste | Ctrl+X / Ctrl+C / Ctrl+V |
| Duplicate | Ctrl+D |
| Select all | Ctrl+A |
| Delete selection | Delete |
| Rotate 90° right / left | R / Shift+R |
| Nudge 0.5 mm / 5 mm | Arrows / Shift+Arrows |
| Zoom in / out / fit | + / − / 0 |

## For developers

The app is written in `labelcraft.src.html`. After changing it, run:

```
python build.py
```

This writes:
- `index.html`: the offline app, using `lib/` (libraries) and `fonts/` from this folder
- `dist/artifact.html`: a single-file version that loads the libraries and fonts online

`python fetch_fonts.py` downloads the fonts into `fonts/` again if they are ever missing.

## Requirements

Chrome or Edge (recent versions). Firefox and Safari work too, but download files instead of saving straight into a folder.

## Credits

- [Fabric.js](http://fabricjs.com/) 5.3.1, [JsBarcode](https://github.com/lindell/JsBarcode) 3.11.6, [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) 1.4.4 (all MIT)
- Fonts: Archivo Black, Barlow Condensed, Instrument Sans, JetBrains Mono, Oswald, Roboto Mono (SIL Open Font License)

## Development notes

How the app is built, the decisions behind it, and known pitfalls: see [NOTES.md](NOTES.md).
