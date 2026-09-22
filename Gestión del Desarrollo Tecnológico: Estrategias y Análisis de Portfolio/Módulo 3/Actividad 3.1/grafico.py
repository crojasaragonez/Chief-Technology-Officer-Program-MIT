#!/usr/bin/env python3
"""Genera la Figura 2 del documento a partir de muestras.csv.

Lee las medidas del propio fichero de datos, ajusta por mínimos cuadrados el
modelo de pérdida logarítmica P(d) = A - 10 n log10(d) sobre los puntos con
d > 0 (el de 0 m queda fuera: log(0) no está definido y a esa distancia no se
cumplen las condiciones de campo lejano) y escribe figuras/grafico.svg y su
versión en PNG. Como la figura se deriva del CSV y no de valores copiados a
mano, no puede desincronizarse de las medidas.

Además imprime el ajuste, de modo que las cifras del apartado 6 del documento
se pueden comprobar ejecutando este guion.
"""

import csv
import math
import pathlib
import subprocess

RAIZ = pathlib.Path(__file__).parent
DATOS = RAIZ / "muestras.csv"
FIGURAS = RAIZ / "figuras"
SVG = FIGURAS / "grafico.svg"
PNG = FIGURAS / "grafico.png"

SERIE = "#603e94"   # morado del documento, la serie medida
MODELO = "#8a8a8a"  # gris neutro, la curva de referencia ajustada
TINTA = "#1a1a1a"
SECUNDARIA = "#555"
EJES = "#b8b8b8"
REJILLA = "#e2e0dc"

W, H = 700, 320
IZQ, DER, ARR, ABA = 56, 24, 18, 44
YMIN, YMAX, XMAX = -70.0, -38.0, 11.0


def leer():
    with DATOS.open(encoding="utf-8") as f:
        return [(float(fila[0]), float(fila[1]))
                for fila in csv.reader(f) if fila and fila[0][0].isdigit()]


def ajustar(puntos):
    """Mínimos cuadrados de dBm frente a log10(d) sobre los puntos con d > 0."""
    x = [math.log10(d) for d, _ in puntos if d > 0]
    y = [v for d, v in puntos if d > 0]
    n = len(x)
    mx, my = sum(x) / n, sum(y) / n
    pendiente = (sum((a - mx) * (b - my) for a, b in zip(x, y))
                 / sum((a - mx) ** 2 for a in x))
    corte = my - pendiente * mx
    sst = sum((b - my) ** 2 for b in y)
    ssr = sum((corte + pendiente * a - b) ** 2 for a, b in zip(x, y))
    return corte, pendiente, 1 - ssr / sst, math.sqrt(ssr / n)


def X(d):
    return IZQ + (d / XMAX) * (W - IZQ - DER)


def Y(v):
    return ARR + ((YMAX - v) / (YMAX - YMIN)) * (H - ARR - ABA)


def dibujar(puntos, corte, pendiente):
    o = [f'<svg viewBox="0 0 {W} {H}" width="100%" role="img"'
         f' aria-labelledby="g1t g1d" style="max-width:{W}px;'
         'font-family:Georgia,\'Times New Roman\',serif">',
         '<title id="g1t">Potencia recibida frente a distancia al'
         ' rúter</title>',
         '<desc id="g1d">' + '; '.join(
             f'{v:.0f} dBm a {d:.0f} m' for d, v in puntos)
         + '. La curva discontinua es el modelo logarítmico ajustado a los'
           ' puntos con distancia mayor que cero.</desc>']

    # rejilla recesiva y etiquetas del eje vertical
    for v in range(int(YMIN), int(YMAX) + 1, 5):
        y = Y(v)
        o.append(f'<line x1="{IZQ}" y1="{y:.1f}" x2="{W-DER}" y2="{y:.1f}"'
                 f' stroke="{REJILLA}" stroke-width="1"/>')
        o.append(f'<text x="{IZQ-10}" y="{y+4:.1f}" text-anchor="end"'
                 f' font-size="12" fill="#666">&#8722;{abs(v)}</text>')
    o.append(f'<text x="{IZQ-10}" y="{Y(YMAX)-10:.1f}" text-anchor="end"'
             ' font-size="11.5" fill="#666">dBm</text>')

    # eje horizontal
    o.append(f'<line x1="{IZQ}" y1="{Y(YMIN):.1f}" x2="{W-DER}"'
             f' y2="{Y(YMIN):.1f}" stroke="{EJES}" stroke-width="1"/>')
    for d in (0, 2, 4, 6, 8, 10):
        x = X(d)
        o.append(f'<line x1="{x:.1f}" y1="{Y(YMIN):.1f}" x2="{x:.1f}"'
                 f' y2="{Y(YMIN)+5:.1f}" stroke="{EJES}" stroke-width="1"/>')
        o.append(f'<text x="{x:.1f}" y="{Y(YMIN)+20:.1f}"'
                 f' text-anchor="middle" font-size="12" fill="#666">{d}</text>')
    o.append(f'<text x="{(IZQ+W-DER)/2:.1f}" y="{H-6}" text-anchor="middle"'
             ' font-size="12" fill="#666">distancia al rúter'
             ' (metros)</text>')

    # curva del modelo, prolongada hasta el borde del marco
    curva, d = [], 1.6
    while d <= XMAX + 1e-9:
        curva.append(f'{X(d):.1f},{Y(corte + pendiente * math.log10(d)):.1f}')
        d += 0.1
    o.append(f'<polyline fill="none" stroke="{MODELO}" stroke-width="2"'
             f' stroke-dasharray="6 4" points="{" ".join(curva)}"/>')

    # serie medida, con anillo blanco para que los puntos no se peguen a la línea
    o.append(f'<polyline fill="none" stroke="{SERIE}" stroke-width="2"'
             ' points="'
             + ' '.join(f'{X(d):.1f},{Y(v):.1f}' for d, v in puntos) + '"/>')
    for d, v in puntos:
        o.append(f'<circle cx="{X(d):.1f}" cy="{Y(v):.1f}" r="5"'
                 f' fill="{SERIE}" stroke="#ffffff" stroke-width="2"/>')

    # etiquetas directas, desplazadas a mano para que no se solapen
    desplazamiento = {0: (12, -6), 3: (10, -12), 6: (8, -13), 10: (-6, 19)}
    for d, v in puntos:
        dx, dy = desplazamiento[int(d)]
        o.append(f'<text x="{X(d)+dx:.1f}" y="{Y(v)+dy:.1f}"'
                 f' text-anchor="{"start" if dx >= 0 else "middle"}"'
                 f' font-size="12.5" fill="{TINTA}">'
                 f'&#8722;{abs(int(v))} dBm</text>')

    # leyenda dentro del marco, en el hueco que deja la curva
    o.append(f'<circle cx="{X(6.15):.1f}" cy="{Y(-42.6):.1f}" r="5"'
             f' fill="{SERIE}" stroke="#ffffff" stroke-width="2"/>')
    o.append(f'<text x="{X(6.4):.1f}" y="{Y(-42.6)+4:.1f}" font-size="12.5"'
             f' fill="{TINTA}">medida con <tspan font-style="italic">iw</tspan>'
             '</text>')
    o.append(f'<line x1="{X(6.0):.1f}" y1="{Y(-45.2):.1f}" x2="{X(6.3):.1f}"'
             f' y2="{Y(-45.2):.1f}" stroke="{MODELO}" stroke-width="2"'
             ' stroke-dasharray="6 4"/>')
    o.append(f'<text x="{X(6.4):.1f}" y="{Y(-45.2)+4:.1f}" font-size="12.5"'
             f' fill="{SECUNDARIA}">modelo log-distancia,'
             ' <tspan font-style="italic">n</tspan> = '
             f'{-pendiente/10:.2f}'.replace('.', ',') + '</text>')
    o.append('</svg>')
    return '\n'.join(o)


puntos = leer()
corte, pendiente, r2, rmse = ajustar(puntos)
FIGURAS.mkdir(exist_ok=True)
SVG.write_text(dibujar(puntos, corte, pendiente), encoding="utf-8")
subprocess.run(["rsvg-convert", "-w", "1400", "-b", "white",
                str(SVG), "-o", str(PNG)], check=True)

print(f"ajuste sobre {sum(1 for d, _ in puntos if d > 0)} puntos con d > 0:")
print(f"  P(d) = {corte:.2f} - {-pendiente:.2f} log10(d)   ->   "
      f"n = {-pendiente/10:.3f}")
print(f"  R2 = {r2:.4f}, RMSE = {rmse:.2f} dB")
for d, v in puntos:
    if d > 0:
        p = corte + pendiente * math.log10(d)
        print(f"  d = {d:4.1f} m   medido {v:.0f}   modelo {p:6.1f}   "
              f"residuo {v-p:+.1f}")
for d, v in puntos:
    print(f"  d = {d:4.1f} m   {v:.0f} dBm = {10**(v/10)*1e6:.2f} nW")
print(f"escrito {SVG.name} y {PNG.name}")
