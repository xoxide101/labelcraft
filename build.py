"""Builds LabelCraft from labelcraft.src.html.

  index.html          standalone app, loads the libraries from the lib/ folder (works offline,
                      apart from the Google fonts, which fall back to system fonts)
  dist/artifact.html  page fragment for publishing as a Claude artifact (libraries from cdnjs)

Run:  python build.py
"""
import pathlib

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
