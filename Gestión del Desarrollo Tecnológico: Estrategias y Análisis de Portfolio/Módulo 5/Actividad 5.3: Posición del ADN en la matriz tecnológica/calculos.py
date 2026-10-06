#!/usr/bin/env python3
"""Recalcula las tasas de mejora que cita main.tex.

Lee la curva de coste digitalizada del gráfico del módulo
(datos/grafico-coste.dat), la de producción (datos/grafico-produccion.dat) y la
serie oficial del NHGRI (datos/nhgri-genoma.dat), y aplica la ecuación de la
tasa anual entre dos lecturas:

    r = (C0 / C1) ** (1 / (t1 - t0)) - 1     mejora anual
    d = 1 - (C1 / C0) ** (1 / (t1 - t0))     caída anual del coste
    T = ln 2 / ln(1 + r)                     semivida del coste

Uso: make calculos
"""

import math
import pathlib

import numpy as np

DATOS = pathlib.Path(__file__).resolve().parent / "datos"


def leer(nombre):
    return np.loadtxt(DATOS / nombre, skiprows=1)


def en(serie, anio):
    """Valor de la serie en el año más cercano a `anio`."""
    return serie[np.argmin(abs(serie[:, 0] - anio))]


def informe(rotulo, t0, c0, t1, c1):
    f = (c0 / c1) ** (1 / (t1 - t0))
    print(f"{rotulo:<28} factor {c0 / c1:>10.4g}  {t1 - t0:5.2f} años  "
          f"r = {100 * (f - 1):6.1f} %  d = {100 * (1 - 1 / f):5.1f} %  "
          f"T = {12 * math.log(2) / math.log(f):5.1f} meses")


coste = leer("grafico-coste.dat")
print("Gráfico del módulo, curva de coste")
for a, b in ((2000, 2019), (2000, 2004), (2004, 2010), (2010, 2019)):
    (t0, c0), (t1, c1) = en(coste, a), en(coste, b)
    informe(f"  {a}-{b}", t0, c0, t1, c1)
m = coste[:, 0] >= 2000
k = np.polyfit(coste[m, 0], np.log(coste[m, 1]), 1)[0]
print(f"  ajuste logarítmico 2000-2019: r = {100 * (math.exp(-k) - 1):.1f} %")
informe("  ley de Moore", 1995, 1e9, 2019, 10 ** 5.49)

nhgri = leer("nhgri-genoma.dat")
print("\nNHGRI, coste por genoma")
for a, b in ((2001.7, 2022.4), (2001.7, 2019.1), (2001.7, 2007.8),
             (2007.8, 2011.8), (2011.8, 2022.4)):
    (t0, c0, _), (t1, c1, _) = en(nhgri, a), en(nhgri, b)
    informe(f"  {t0:.1f}-{t1:.1f}", t0, c0, t1, c1)
t0, c0, _ = nhgri[0]
print(f"  con la ley de Moore desde 2001 costaría en 2022: "
      f"{c0 * 0.5 ** ((nhgri[-1, 0] - t0) / 2):,.0f} dólares")

prod = leer("grafico-produccion.dat")
(t0, p0), (t1, p1) = en(prod, 2000), en(prod, 2014)
f = (p1 / p0) ** (1 / (t1 - t0))
print(f"\nProducción 2000-2014: mejora {100 * (f - 1):.0f} % anual, "
      f"se duplica cada {12 * math.log(2) / math.log(f):.1f} meses")
cp = leer("coste-vs-produccion.dat")
b, a = np.polyfit(np.log10(cp[:, 1]), np.log10(cp[:, 2]), 1)
r2 = np.corrcoef(np.log10(cp[:, 1]), np.log10(cp[:, 2]))[0, 1] ** 2
print(f"Coste frente a producción: pendiente {b:.3f}, R² = {r2:.3f}, "
      f"producción x10 divide el coste por {10 ** -b:.1f}")
