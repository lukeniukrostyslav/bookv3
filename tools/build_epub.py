from __future__ import annotations
import html
import re
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MANUSCRIPT=ROOT/"manuscript"
OUT=ROOT/"dist"
OUT.mkdir(exist_ok=True)

chapters=[]
for i in range(1,33):
    p=MANUSCRIPT/f"CHAPTER_{i:02d}.md"
    text=p.read_text(encoding="utf-8")
    lines=text.splitlines()
    heading=next((x for x in lines if x.startswith("# ")), f"# Глава {i}")
    title=re.sub(r"^#\s*","",heading).strip()
    body="\n".join(x for x in lines if x != heading)
    paragraphs=[]
    for block in re.split(r"\n\s*\n", body):
        block=block.strip()
        if not block: continue
        if block.startswith("# "): continue
        paragraphs.append(f"<p>{html.escape(block).replace(chr(10), '<br/>')}</p>")
    chapters.append((i,title,"\n".join(paragraphs)))

book_title="ОТЕЛЬ ПОСЛЕДНЕГО ЗАВТРА"
author="РОСТИСЛАВ ЛУКЕНЮК"
uid="hotel-last-tomorrow-rostyslav-lukeniuk"

css="""body{font-family:serif;line-height:1.5;margin:8%;}h1{text-align:center;margin-top:25%;}p{text-indent:1.2em;margin:0 0 .7em;}nav ol{list-style:none;padding:0;}nav li{margin:.5em 0;}"""

with zipfile.ZipFile(OUT/"HOTEL_LAST_TOMORROW.epub","w") as z:
    z.writestr("mimetype","application/epub+zip",compress_type=zipfile.ZIP_STORED)
    container='''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="EPUB/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>'''
    z.writestr("META-INF/container.xml",container)
    z.writestr("EPUB/style.css",css)
    manifest=[]; spine=[]
    for i,title,body in chapters:
        fn=f"chapter-{i:02d}.xhtml"
        doc=f'''<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml"><head><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head><body><h1>{html.escape(title)}</h1>{body}</body></html>'''
        z.writestr("EPUB/"+fn,doc)
        manifest.append(f'<item id="c{i}" href="{fn}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="c{i}"/>')
    nav_items="".join(f'<li><a href="chapter-{i:02d}.xhtml">{html.escape(t)}</a></li>' for i,t,_ in chapters)
    nav=f'''<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops"><head><title>Содержание</title></head><body><nav epub:type="toc"><h1>Содержание</h1><ol>{nav_items}</ol></nav></body></html>'''
    z.writestr("EPUB/nav.xhtml",nav)
    manifest.append('<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>')
    opf=f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="bookid">{uid}</dc:identifier><dc:title>{book_title}</dc:title><dc:language>ru</dc:language><dc:creator>{author}</dc:creator><meta property="dcterms:modified">2026-09-20T00:00:00Z</meta></metadata>
<manifest>{''.join(manifest)}</manifest><spine>{''.join(spine)}</spine></package>'''
    z.writestr("EPUB/content.opf",opf)
print(OUT/"HOTEL_LAST_TOMORROW.epub")
