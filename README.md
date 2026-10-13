# LabelCraft

A label maker that runs in the browser, for Dymo, Brother, Zebra and Avery label sizes.

- Text, shapes, images, barcodes and QR codes
- Rotate by 90° / 180° in either direction
- Save and open label files
- Export PNG, JPG or SVG
- Light/dark toggle

## Use it
Open `index.html` in Chrome or Edge. Works offline: the libraries are in `lib/` and the fonts in `fonts/` (`python fetch_fonts.py` downloads them again if needed).

## Change it
Edit `labelcraft.src.html`, then run:

```
python build.py
```

This writes `index.html` and `dist/artifact.html` (single file).

## Third-party
Fabric.js 5.3.1, JsBarcode 3.11.6, qrcode-generator 1.4.4 (all MIT). Fonts: Archivo Black, Barlow Condensed, Instrument Sans, JetBrains Mono, Oswald, Roboto Mono (SIL Open Font License).
