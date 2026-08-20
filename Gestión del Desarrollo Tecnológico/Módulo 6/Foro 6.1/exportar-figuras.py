#!/usr/bin/env python3
"""Exporta las figuras de main.tex a PNG e incrusta el resultado en el HTML.

Extrae los entornos tikzpicture de main.tex, los compila con la clase
`standalone` (una página por figura), los convierte a PNG, los optimiza y
genera `foro-6.1-tinymce.html` con las imágenes en base64, listo para
seleccionar todo, copiar y pegar en un editor TinyMCE.

De este modo las imágenes del HTML no pueden desincronizarse del informe:
se regeneran siempre desde la misma fuente.

Uso: make html
"""

import base64
import pathlib
import re
import shutil
import subprocess
import sys

AQUI = pathlib.Path(__file__).resolve().parent
FIGDIR = AQUI / "figuras"
HTML_MAESTRO = "foro-6.1.html"
HTML_SALIDA = "foro-6.1-tinymce.html"
DPI = "190"

PREAMBULO = r"""\documentclass[tikz,border=6pt]{standalone}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage{fontspec}
\setmainfont{Source Serif Pro}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage{xcolor}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,patterns}
\sisetup{output-decimal-marker={,},group-separator={.},group-minimum-digits=4,detect-all}
\definecolor{cADS}{RGB}{31,78,121}
\definecolor{cHum}{RGB}{191,110,30}
\definecolor{cReg}{RGB}{40,124,70}
\definecolor{cUSA}{RGB}{116,66,150}
\definecolor{cRiesgo}{RGB}{176,42,42}
\newcommand{\barrarot}[6]{%
  \node[left, text width=3.7cm, align=right, font=\scriptsize] at (-0.15,#1) {#4};%
  \fill[#3] (0,#1-0.17) rectangle (#2,#1+0.17);%
  \node[right, font=\scriptsize] at (#6,#1) {#5};%
}
\begin{document}
"""


def ejecutar(orden, **kwargs):
    resultado = subprocess.run(orden, cwd=AQUI, capture_output=True, text=True, **kwargs)
    if resultado.returncode != 0:
        sys.exit(f"falló: {' '.join(orden)}\n{resultado.stdout[-2500:]}{resultado.stderr[-800:]}")
    return resultado


def main():
    fuente = (AQUI / "main.tex").read_text(encoding="utf-8")
    figuras = re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", fuente, re.S)
    if not figuras:
        sys.exit("no se encontró ningún entorno tikzpicture en main.tex")
    print(f"figuras encontradas en main.tex: {len(figuras)}")

    (AQUI / "figuras.tex").write_text(
        PREAMBULO + "\n".join(figuras) + "\n\\end{document}\n", encoding="utf-8"
    )
    ejecutar(["lualatex", "-interaction=nonstopmode", "-halt-on-error", "figuras.tex"])

    FIGDIR.mkdir(exist_ok=True)
    for viejo in FIGDIR.glob("figura-*.png"):
        viejo.unlink()
    ejecutar(["pdftoppm", "-png", "-r", DPI, "figuras.pdf", "figuras/fig"])

    generadas = sorted(FIGDIR.glob("fig-*.png"))
    if len(generadas) != len(figuras):
        sys.exit(f"se esperaban {len(figuras)} páginas y se obtuvieron {len(generadas)}")
    for indice, origen in enumerate(generadas, 1):
        origen.rename(FIGDIR / f"figura-{indice}.png")

    if shutil.which("pngquant") and shutil.which("optipng"):
        for png in sorted(FIGDIR.glob("figura-*.png")):
            subprocess.run(["pngquant", "--quality=80-98", "--speed", "1",
                            "--force", "--output", str(png), str(png)],
                           capture_output=True)
            subprocess.run(["optipng", "-quiet", "-o5", str(png)], capture_output=True)
    else:
        print("aviso: sin pngquant/optipng, las imágenes quedan sin optimizar")

    pesos = {p.name: p.stat().st_size for p in sorted(FIGDIR.glob("figura-*.png"))}
    for nombre, peso in pesos.items():
        print(f"  {nombre}: {peso / 1024:.0f} KB")

    html = (AQUI / HTML_MAESTRO).read_text(encoding="utf-8")

    def incrustar(coincidencia):
        datos = (FIGDIR / coincidencia.group(1)).read_bytes()
        return "data:image/png;base64," + base64.b64encode(datos).decode("ascii")

    salida, sustituciones = re.subn(r"figuras/(figura-\d+\.png)", incrustar, html)
    if sustituciones != len(figuras):
        sys.exit(f"el HTML referencia {sustituciones} imágenes y hay {len(figuras)} figuras")
    (AQUI / HTML_SALIDA).write_text(salida, encoding="utf-8")
    print(f"{HTML_SALIDA}: {len(salida.encode('utf-8')) / 1024:.0f} KB, "
          f"{sustituciones} imágenes incrustadas")


if __name__ == "__main__":
    main()
