"""Modelo del portafolio de I+D (actividad 9.5).

Sólo usa proyectos, ecuaciones y precios de la hoja de ruta de IaC
(actividad 9.1 parte C, secciones 14 a 16). Cifras en miles de dólares.
Año base 2026, tasa de descuento 9 %, horizonte 2031 (H=2033 para la
sensibilidad). Variables de entorno:
  H=2033        horizonte alternativo
  SOBRE=1.27    sobrecosto medio de Flyvbjerg y Budzier en lugar del propio
  SIGMA=0.60    media pesimista de la adopción del autoservicio
"""
import itertools
import os
import numpy as np

rng = np.random.default_rng(20261102)
M = 40000
MP = 95.0 / 12                      # miles de dólares por mes-persona
OTROS = 84.0 / 736.2                # otros conceptos sobre ingeniería (hoja de ruta)
HORIZON = int(os.environ.get("H", "2031"))
SOBRE = float(os.environ.get("SOBRE", "0"))
SIGMA_MU = float(os.environ.get("SIGMA", "0.68"))
YEARS = np.arange(2026, HORIZON + 1)
NY = len(YEARS)
X = lambda *v: np.array(v, float)[:NY]
DISC = 1.09 ** -(YEARS - 2026)

# trimestres: 0 = 2026 T4, 1 = 2027 T1, ..., 10 = 2029 T2
QLAB = ["26T4", "27T1", "27T2", "27T3", "27T4", "28T1", "28T2", "28T3",
        "28T4", "29T1", "29T2"]
Q_YEAR = np.array([2026] + [2027] * 4 + [2028] * 4 + [2029] * 2)

# EDT: (código, paquete, meses-persona, trimestres)
WBS = {
    "G": [("1.1", "Gobierno del portafolio y puertas", 1.5, list(range(11))),
          ("1.2", "Valor ganado y medición de figuras", 1.5, list(range(11)))],
    "R1": [("2.1", "Importación de la cola importable", 3, [0]),
           ("2.2", "Codificación de recursos resistentes", 2, [0, 1]),
           ("2.3", "Conciliación y medición de cobertura", 1, [1]),
           ("2.4", "P5: reconstrucción cronometrada (parte R1)", 1, [8])],
    "R3": [("3.1", "P2: módulo de referencia y contrato", 3, [1]),
           ("3.2", "Módulos de red, cómputo y datos", 7, [2, 3]),
           ("3.3", "Certificación: firma, versiones y registro", 4, [3, 4]),
           ("3.4", "Migración de consumidores", 3, [4]),
           ("3.5", "P5: reconstrucción cronometrada (parte R3)", 1, [8])],
    "R4": [("4.1", "P3: evaluación en modo aviso", 2, [4]),
           ("4.2", "Biblioteca de reglas propias", 4, [5]),
           ("4.3", "Modo bloqueo y régimen de excepciones", 3, [5, 6]),
           ("4.4", "Medición de falsos positivos", 1, [6])],
    "R7": [("5.1", "P4: portal, tres plantillas, diez equipos", 3, [6, 7]),
           ("5.2", "Plantillas sobre el catálogo", 6, [8, 9]),
           ("5.3", "Integración con petición y aprobación", 4, [9]),
           ("5.4", "Despliegue a todos los equipos", 3, [10])],
}
RESERVA = {"G": 0.10, "R1": 0.10, "R3": 0.15, "R4": 0.15, "R7": 0.20}


def trimestral(p, solo=None):
    q = np.zeros(11)
    for cod, _, mp, qs in WBS[p]:
        if solo is not None and cod not in solo:
            continue
        q[qs] += mp * MP / len(qs)
    if p != "G":
        q *= 1 + OTROS
    return q


QCOST = {p: trimestral(p) for p in WBS}
BASE = {p: QCOST[p].sum() for p in WBS}
MPS = {p: sum(w[2] for w in WBS[p]) for p in WBS}


def anual(q):
    return np.array([q[Q_YEAR == y].sum() for y in YEARS])


YCOST = {p: anual(QCOST[p]) for p in WBS}
# gasto si la puerta detiene o degrada el proyecto
YCOST_G3 = anual(trimestral("R7", solo={"5.1"}))            # R7 cancelado
YCOST_G2 = anual(trimestral("R4", solo={"4.1", "4.2", "4.4"}))  # R4 sólo aviso


def tri(a, m, b):
    return rng.triangular(a, m, b, M)


# precios unitarios de la hoja de ruta, con su incertidumbre
c_m = tri(0.28, 0.40, 0.52)        # por recurso no codificado y año
c_f = tri(1.1, 1.6, 2.1)           # por cambio fallido
h_ac = tri(1.5, 2.1, 2.7)          # horas de acompañamiento por cambio
g = tri(0.05, 0.15, 0.22)          # crecimiento anual del parque
# G1: la cobertura se estanca en el 74 %
estanca = rng.random(M) < 0.25
# G2: falsos positivos por encima del 15 %: R4 se queda en modo aviso
g2_falla = rng.random(M) < 0.20
gamma_f = np.where(g2_falla, tri(0.66, 0.70, 0.74), tri(0.85, 0.94, 0.97))
kappa_f = tri(0.60, 0.80, 0.88)
# G3: adopción del autoservicio, beta de media SIGMA_MU y d.t. 0,13
sd = 0.13
k = SIGMA_MU * (1 - SIGMA_MU) / sd**2 - 1
sigma_f = rng.beta(SIGMA_MU * k, (1 - SIGMA_MU) * k, M)
r7_sigue = sigma_f >= 0.60


def sobrecosto(med, s):
    if SOBRE:
        med = med * SOBRE / 1.10
    return med * np.exp(rng.normal(0, s, M))


OVR = {"G": sobrecosto(1.03, 0.08), "R1": sobrecosto(1.06, 0.12),
       "R3": sobrecosto(1.08, 0.15), "R4": sobrecosto(1.10, 0.18),
       "R7": sobrecosto(1.12, 0.22)}

N0 = 1200
NPARK = N0 * (1 + g[:, None]) ** (YEARS - 2026)[None, :]
NC = X(0, 500, 700, 900, 1000, 1100, 1200, 1300)   # cambios por año
F0, PI, THETA = 0.20, 0.354, 0.688
C_SIN = 0.55                       # cobertura de 2026 en la hoja de ruta
COV_OK = X(0.55, 0.62, 0.74, 0.86, 0.88, 0.88, 0.88, 0.88)
COV_EST = X(0.55, 0.62, 0.70, 0.74, 0.75, 0.75, 0.75, 0.75)


def simular(sel):
    s = set(sel)
    if "R1" in s:
        cov = np.where(estanca[:, None], COV_EST, COV_OK)
    else:
        cov = np.broadcast_to(np.minimum(COV_OK, C_SIN), (M, NY))
    B1 = NPARK * (cov - C_SIN) * c_m[:, None]

    kap = np.full((M, NY), 0.15)
    if "R3" in s:
        kap = 0.15 + (kappa_f[:, None] - 0.15) * X(0, 0.1, 0.6, 1, 1, 1, 1, 1)
    gam = np.full((M, NY), 0.62)
    if "R4" in s:
        gam = 0.62 + (gamma_f[:, None] - 0.62) * X(0, 0, 0.5, 1, 1, 1, 1, 1)
    f = F0 * (1 - PI * gam) * (1 - THETA * kap)
    B2 = NC * (0.14 - f) * c_f[:, None]

    sop = 0.4 * (kap - 0.15) / 0.65
    if "R7" in s:
        sop = sop + 0.6 * (r7_sigue * np.minimum(sigma_f, 0.9) / 0.75)[:, None] \
            * X(0, 0, 0, 0.5, 1, 1, 1, 1)
    B3 = NC * h_ac[:, None] * 0.06 * sop
    ben = B1 + B2 + B3

    cost = np.zeros((M, NY))
    for p in s:
        full = YCOST[p][None, :] * OVR[p][:, None]
        if p == "R7":
            part = YCOST_G3[None, :] * OVR[p][:, None]
            full = np.where(r7_sigue[:, None], full, part)
        if p == "R4":
            part = YCOST_G2[None, :] * OVR[p][:, None]
            full = np.where(g2_falla[:, None], part, full)
        cost += full
    van = ((ben - cost) * DISC).sum(1)
    return van, ben, cost, dict(B1=B1, B2=B2, B3=B3)


NUCLEO = ["G", "R1"]
OPC = ["R3", "R4", "R7"]
carteras = []
for r in range(len(OPC) + 1):
    for sub in itertools.combinations(OPC, r):
        if "R7" in sub and "R3" not in sub:
            continue                # R7 necesita el catálogo de R3
        sel = NUCLEO + list(sub)
        van, ben, cost, _ = simular(sel)
        base = sum(BASE[p] for p in sel)
        res = sum(BASE[p] * RESERVA[p] for p in sel)
        carteras.append(dict(sub=sub, van=van, E=van.mean(), S=van.std(),
                             pp=(van < 0).mean(), base=base, res=res))

print(f"== carteras (horizonte {HORIZON}) ==")
for c in carteras:
    dom = any(o["E"] >= c["E"] and o["S"] <= c["S"] and
              (o["E"] > c["E"] or o["S"] < c["S"]) for o in carteras)
    print(f"{'+'.join(('R1',) + c['sub']):14s} E={c['E']:7.1f} S={c['S']:6.1f}"
          f" P(VAN<0)={c['pp']:.3f} base={c['base']:6.1f}"
          f" total={c['base'] + c['res']:6.1f} {'dominada' if dom else 'frontera'}")

full = [c for c in carteras if len(c["sub"]) == 3][0]
print("\n== contribución marginal sobre el portafolio completo ==")
for p in OPC:
    rest = tuple(x for x in OPC if x != p and not (p == "R3" and x == "R7"))
    otro = [c for c in carteras if set(c["sub"]) == set(rest)][0]
    d = full["van"] - otro["van"]
    print(f"{p} (sin {'+'.join(rest) or 'nada'}): dE={d.mean():6.1f} "
          f"dS={d.std():5.1f} P(d<0)={(d < 0).mean():.3f}")
van_sin_r1, *_ = simular(["G", "R3", "R4", "R7"])
d = full["van"] - van_sin_r1
print(f"R1: dE={d.mean():6.1f} dS={d.std():5.1f} P(d<0)={(d < 0).mean():.3f}")

print("\nP(sigma<0,60) =", round((~r7_sigue).mean(), 3),
      " P(estanca) =", estanca.mean(), " P(G2 falla) =", g2_falla.mean())

print("\n== presupuesto ==")
tb = tr = tmp = 0
for p in WBS:
    tb += BASE[p]; tr += BASE[p] * RESERVA[p]; tmp += MPS[p]
    print(f"{p}: mp={MPS[p]:4.1f} base={BASE[p]:6.1f} reserva={BASE[p]*RESERVA[p]:5.1f}"
          f" total={BASE[p]*(1+RESERVA[p]):6.1f}")
print(f"TOTAL mp={tmp} base={tb:.1f} reserva={tr:.1f} ({tr/tb:.1%}) total={tb+tr:.1f}")
for p in WBS:
    for cod, nom, mp, qs in WBS[p]:
        c = mp * MP * (1 + (OTROS if p != "G" else 0))
        print(f"   {cod} {nom:46s} {mp:4.1f} mp {c:6.1f}")
print("trimestres:")
acum = 0
for i, l in enumerate(QLAB):
    t = sum(QCOST[p][i] for p in WBS)
    acum += t
    print(f"  {l} " + " ".join(f"{p}={QCOST[p][i]:5.1f}" for p in WBS)
          + f" total={t:5.1f} acum={acum:6.1f}")
print("por año:", {p: YCOST[p].round(1).tolist() for p in WBS})

van, ben, cost, parts = simular(NUCLEO + OPC)
ct = cost.sum(1)
print(f"\ncosto real con puertas: media={ct.mean():.1f} P50={np.percentile(ct,50):.1f}"
      f" P80={np.percentile(ct,80):.1f} P(supera base+reserva)={(ct > tb+tr).mean():.3f}")
sinp = sum(BASE[p] * OVR[p] for p in WBS)
print(f"sin puertas: P80={np.percentile(sinp,80):.1f} P(supera)={(sinp > tb+tr).mean():.3f}")
print("beneficio medio por año", ben.mean(0).round(1))
for k_, v in parts.items():
    print(f"  {k_}", v.mean(0).round(1))
print("costo medio por año", cost.mean(0).round(1))
print("flujo acumulado medio", np.cumsum((ben - cost).mean(0)).round(1))
print(f"VAN portafolio: E={van.mean():.1f} P5={np.percentile(van,5):.1f}"
      f" P95={np.percentile(van,95):.1f}")


# figuras de mérito deterministas en 2029 (modelo técnico de la hoja de ruta)
def tc(s, ga, ka):
    return (1 - s) * 16 + (1 - ga) * 14 + ga * 0.2 + 1.8 + (1 - ka) * 3.2 + ka * 0.7


def fallo(ga, ka):
    return F0 * (1 - PI * ga) * (1 - THETA * ka)


print("\n== figuras en 2029 (deterministas) ==")
for nom, s_, ga, ka in [("ninguno", 0, .62, .15), ("R3", 0, .62, .8),
                        ("R4", 0, .94, .15), ("R3+R4", 0, .94, .8),
                        ("R3+R7", .75, .62, .8), ("todos", .75, .94, .8)]:
    print(f"{nom:8s} Tc={tc(s_, ga, ka):5.1f} h  f={fallo(ga, ka):.3f}")
