"""Builds LabelCraft from labelcraft.src.html.

  index.html          standalone app, loads the libraries from lib/ and the fonts from fonts/
                      (works offline; run fetch_fonts.py once to download the fonts)
  dist/artifact.html  page fragment for publishing as a Claude artifact (libraries from cdnjs)

Run:  python build.py
"""
import pathlib
import re

root = pathlib.Path(__file__).parent
page = (root / "labelcraft.src.html").read_text(encoding="utf-8")

CDN = "https://cdnjs.cloudflare.com/ajax/libs/"
LOCAL = {
    CDN + "fabric.js/5.3.1/fabric.min.js": "lib/fabric.min.js",
    CDN + "jsbarcode/3.11.6/JsBarcode.all.min.js": "lib/JsBarcode.all.min.js",
    CDN + "qrcode-generator/1.4.4/qrcode.min.js": "lib/qrcode.min.js",
}
standalone_body = page
for cdn, local in LOCAL.items():
    assert cdn in page, f"missing script tag: {cdn}"
    assert (root / local).exists(), f"missing library file: {local}"
    standalone_body = standalone_body.replace(cdn, local)

# Swap the two Google Fonts <link> tags for the local stylesheet.
GOOGLE_FONTS = re.compile(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\n'
                          r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]+">')
assert GOOGLE_FONTS.search(standalone_body), "Google Fonts links not found"
assert (root / "fonts" / "fonts.css").exists(), "fonts/fonts.css is missing: run python fetch_fonts.py"
standalone_body = GOOGLE_FONTS.sub('<link rel="stylesheet" href="fonts/fonts.css">', standalone_body, count=1)

head, body = standalone_body.split('<div class="app">', 1)
standalone = (
    '<!doctype html>\n<html lang="en">\n<head>\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    + head.strip() + '\n</head>\n<body>\n<div class="app">' + body + '</body>\n</html>\n'
)
(root / "index.html").write_text(standalone, encoding="utf-8")
(root / "dist").mkdir(exist_ok=True)
(root / "dist" / "artifact.html").write_text(page, encoding="utf-8")
print("Built index.html and dist/artifact.html")
