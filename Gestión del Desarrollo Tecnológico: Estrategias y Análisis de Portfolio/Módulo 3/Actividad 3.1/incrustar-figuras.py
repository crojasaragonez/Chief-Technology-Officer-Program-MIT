#!/usr/bin/env python3
"""Produce el entregable autocontenido para el editor WYSIWYG de la plataforma.

Lee actividad-3.1.html (el maestro, que referencia las imágenes por ruta) y
escribe actividad-3.1-tinymce.html con cada <img src="..."> sustituido por los
datos de la imagen en base64, de modo que el fichero no dependa de nada externo
al pegarlo: se abre en el navegador, se selecciona todo y se copia.

El gráfico se incrusta como PNG y no como SVG en línea porque los editores
WYSIWYG suelen descartar el SVG al pegar.
"""

import base64
import mimetypes
import pathlib
import re

RAIZ = pathlib.Path(__file__).parent
MAESTRO = RAIZ / "actividad-3.1.html"
FINAL = RAIZ / "actividad-3.1-tinymce.html"


def incrustar(coincidencia: re.Match) -> str:
    ruta = RAIZ / coincidencia.group(1)
    if not ruta.exists():
        raise SystemExit(f"falta la imagen referenciada: {coincidencia.group(1)}")
    tipo = mimetypes.guess_type(ruta.name)[0] or "image/png"
    datos = base64.b64encode(ruta.read_bytes()).decode("ascii")
    return f'src="data:{tipo};base64,{datos}"'


html = MAESTRO.read_text(encoding="utf-8")
html, n = re.subn(r'src="([^"]+\.(?:png|jpg|jpeg))"', incrustar, html)
FINAL.write_text(html, encoding="utf-8")
print(f"{FINAL.name}: {FINAL.stat().st_size // 1024} kB, {n} imágenes incrustadas")
