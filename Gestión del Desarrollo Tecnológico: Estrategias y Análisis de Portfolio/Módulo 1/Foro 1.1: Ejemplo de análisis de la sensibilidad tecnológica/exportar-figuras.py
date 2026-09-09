#!/usr/bin/env python3
"""Exporta las figuras de main.tex a PNG e incrusta el resultado en el HTML.

Extrae los entornos tikzpicture de main.tex, los compila con la clase
`standalone` a 11 pt, el mismo cuerpo que main.tex para que el salto de línea
de los rótulos coincida, los convierte a PNG, los optimiza y
genera `foro-1.1-tinymce.html` con las imágenes en base64, listo para
seleccionar todo, copiar y pegar en un editor TinyMCE.

El preámbulo de las figuras no se duplica aquí: se extrae del propio main.tex,
entre la marca de inicio de los colores y el \\title. Así las imágenes del HTML
no pueden desincronizarse del informe ni por el contenido ni por el estilo.

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
HTML_MAESTRO = "foro-1.1.html"
HTML_SALIDA = "foro-1.1-tinymce.html"
DPI = "190"

CABECERA = r"""\documentclass[tikz,border=6pt,11pt]{standalone}
\usepackage[spanish,es-noshorthands]{babel}
\usepackage{fontspec}
\setmainfont{Source Serif Pro}
\usepackage{amsmath}
\usepackage{siunitx}
\usepackage[version=4]{mhchem}
\usepackage{xcolor}
\usetikzlibrary{arrows.meta,positioning,shapes.geometric,fit,backgrounds,patterns,decorations.pathreplacing}
\sisetup{output-decimal-marker={,},group-separator={.},group-minimum-digits=4,detect-all}
"""

INICIO_MACROS = "% Colores:"
FIN_MACROS = r"\title{"


def ejecutar(orden, **kwargs):
    resultado = subprocess.run(orden, cwd=AQUI, capture_output=True, text=True, **kwargs)
    if resultado.returncode != 0:
        sys.exit(f"falló: {' '.join(orden)}\n{resultado.stdout[-2500:]}{resultado.stderr[-800:]}")
    return resultado


def macros_de(fuente):
    """Devuelve los colores y las macros de figura definidos en main.tex."""
    inicio = fuente.find(INICIO_MACROS)
    fin = fuente.find(FIN_MACROS)
    if inicio == -1 or fin == -1 or fin < inicio:
        sys.exit("no se localizó el bloque de macros de figura en main.tex")
    return fuente[inicio:fin]


def main():
    fuente = (AQUI / "main.tex").read_text(encoding="utf-8")
    figuras = re.findall(r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", fuente, re.S)
    if not figuras:
        sys.exit("no se encontró ningún entorno tikzpicture en main.tex")
    print(f"figuras encontradas en main.tex: {len(figuras)}")

    (AQUI / "figuras.tex").write_text(
        CABECERA + macros_de(fuente) + "\\begin{document}\n"
        + "\n".join(figuras) + "\n\\end{document}\n",
        encoding="utf-8",
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

    for png in sorted(FIGDIR.glob("figura-*.png")):
        print(f"  {png.name}: {png.stat().st_size / 1024:.0f} KB")

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
