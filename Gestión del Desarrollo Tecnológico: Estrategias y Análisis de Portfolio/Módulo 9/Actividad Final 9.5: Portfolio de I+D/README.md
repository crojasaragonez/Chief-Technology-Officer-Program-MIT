# Actividad final 9.5: Portfolio de I+D

**Cuatro proyectos, cuatro puertas.** Portafolio de I+D de la plataforma de
infraestructura como código para 2026-2029, construido sólo con proyectos de la
hoja de ruta tecnológica del primer programa (actividad 9.1 parte C).

## Resumen

- Proyectos: R1 (la mitad que falta), R3, R4 y R7. R2 está cerrado; R5, R6 y R8
  pasan al presupuesto de operación porque no tienen prototipo.
- **547,4 miles de dólares comprometidos**: 473,6 de base y 73,8 de reserva
  (15,6 %), 54 meses-persona.
- VAN esperado a 2031: **727,3**. El máximo sería R1 + R3 (776,8); R4 y R7 se
  incluyen por los compromisos de tiempo de ciclo y cumplimiento, a un precio
  de 49,5.
- Puertas G1 a G4 de la hoja de ruta. Con ellas, la probabilidad de pasarse
  del presupuesto es del 19,6 %; sin ellas, del 30 %.

## Correspondencia con la consigna

| Elemento pedido | Sección |
|---|---|
| Elegir proyectos de la hoja de ruta | 2. De la hoja de ruta al portafolio |
| Objetivos y propuesta de valor por FOM | 3. Objetivos y propuesta de valor |
| Estructura de división del trabajo | 4 |
| Calendario | 5 |
| Presupuesto | 6 |
| Matriz de riesgo | 7 |
| Valoración del portafolio | 8 |
| Contraste con el sector | 9 |
| Por qué vale la pena | 10 |

## Compilar

```
make pdf     # LuaLaTeX + Biber
make check   # debe decir "composición sin avisos"
```

## Modelo

`modelo/portafolio.py` (NumPy) reproduce todas las cifras con semilla fija:

```
python3 modelo/portafolio.py             # caso base, horizonte 2031
H=2033 python3 modelo/portafolio.py      # horizonte 2033
SOBRE=1.27 python3 modelo/portafolio.py  # sobrecosto medio de Flyvbjerg
SIGMA=0.60 python3 modelo/portafolio.py  # adopción del portal pesimista
```
