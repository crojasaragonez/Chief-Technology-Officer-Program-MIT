# Hoja de ruta tecnológica de la infraestructura como código

Documento único y acumulativo (`main.tex`) de la hoja de ruta tecnológica de
la **infraestructura como código** (IaC). Cada entrega del curso se inserta
como una sección más, en el lugar que le corresponde por el índice de doce
elementos de una hoja de ruta, no al final.

Esta versión incorpora la **Actividad 9.1, Parte C: figuras de mérito y
evolución tecnológica**, y con ella **el documento completa los doce elementos
del índice**. Antes de esta entrega quedaban ausentes el 5, el 7, el 10, el 11
y el 12, el 8 estaba declarado fuera de alcance y el 4 y el 9 estaban
atendidos sólo en parte.

## Qué aporta esta entrega

**Elemento 4, la parte que faltaba.** Las figuras de mérito ya tenían unidad y
procedimiento de medida, pero no evolución temporal ni tasa de mejora. Se
añade:

- Sección 10, apartados 02 y 03: los cuatro criterios de admisión de una
  figura de mérito, la separación entre figuras de entrega y de
  infraestructura, y las anclas de normalización con el valor de 2026 y el
  objetivo de 2029.
- Sección 11 completa: los tres modelos de evolución. Curva S de la cobertura
  (inflexión en 2012, 92 % del límite recorrido) y del tiempo de
  reconstrucción (asíntota de 3,6 h); ajuste log-lineal al modo de la ley de
  Moore sobre la superficie declarable (duplicación cada 1,8 a 2,2 años); y
  frente de Pareto de las seis posiciones, en el que Terraform gestionado y la
  plataforma de 2026 resultan dominados.

**Los seis elementos que faltaban**, en secciones nuevas: 12 (motivaciones
estratégicas), 14 (modelo técnico), 15 (modelo financiero), 16 (cartera y
prototipos), 17 (publicaciones y patentes), 18 (declaración de estrategia) y
19 (evaluación de madurez).

**Dos correcciones a lo ya entregado**, detectadas al construir el frente de
Pareto:

- El apartado 08 de la sección 13 afirmaba que, bajo el escenario multinube,
  el jugador B quedaba «dominado por la ruta propia en ambos ejes». No lo
  está: con un $\Delta C$ de $-4$ frente a $-1$, B conserva tres puntos de
  ventaja en coste y sigue formalmente en la frontera. El texto se rehace con
  el argumento correcto, que es la tasa de canje: esos tres puntos de coste
  cuestan 34,1 puntos de valor.
- El elemento 8 ya no se declara fuera de alcance, y las tres remisiones que
  lo hacían apuntan ahora a la sección 15.

## Qué falta por hacer

Las capturas del modelo hechas con la herramienta oficial (OPCloud,
<https://opcloud-sandbox.web.app/>, u OPCAT) quedan pendientes y se entregan
aparte. El documento no las incorpora ni depende de ellas.

## Estructura del informe

| Sección | Elemento ATRA | Contenido |
|---|---|---|
| 1 | | Objeto, frontera del sistema y correspondencia con los doce elementos |
| 2 | 1 | Principio de funcionamiento: estado deseado, registrado y real |
| 3 | 1 | Ciclo de operación en siete pasos; comparación a tres bandas |
| 4 | 1 | Las siete capas, de L0 (sustrato) a L6 (plataforma) |
| 5 | 1 | Los seis módulos transversales |
| 6 | 1 | Modos de operación: empuje/arrastre, mutable/inmutable, declarativo/imperativo |
| 7 | 1 | El módulo como unidad de composición |
| 8 | 2 | DSM de arquitectura y DSM de cartera, particionado y secuencia |
| 9 | 3 | Modelo OPM: SD, SD2, SD1 y el OPL de los tres |
| **10** | **4** | **Ocho figuras de mérito: criterios de admisión, unidad, medida y anclas** |
| **11** | **4** | **Evolución: curva S, tasa de mejora al modo de Moore y frente de Pareto** |
| **12** | **5** | **Seis motivaciones estratégicas y trazabilidad hasta los proyectos** |
| 13 | 6 | Posicionamiento frente a la competencia: gráfico vectorial |
| **14** | **7** | **Modelo técnico: cuatro ecuaciones calibradas y su sensibilidad** |
| **15** | **8** | **Modelo financiero: flujo, VAN, TIR y siete escenarios** |
| **16** | **9** | **Cartera: madurez de partida, cinco prototipos y cuatro puertas** |
| **17** | **10** | **Publicaciones fundacionales, literatura empírica y tres patentes** |
| **18** | **11** | **Declaración de estrategia: postura, compromisos y renuncias** |
| **19** | **12** | **Evaluación de madurez en dos dimensiones** |
| 20 | | Conclusiones |

### La sección 11 (evolución) en detalle

| Apartado | Contenido |
|---|---|
| 01 | La frontera de la tecnología frente a la posición de la empresa |
| 02 | Trece hitos documentados que anclan la serie, de 1993 a 2026 |
| 03 | Curva S de la cobertura: $L=100$ %, $k=0{,}171$, $t_0=2012{,}0$, $R^2=0{,}991$ |
| 04 | Curva S del tiempo de reconstrucción: asíntota de 3,6 h, $R^2=0{,}9998$ |
| 05 | Ley de Moore: la superficie declarable se duplica cada 1,8 a 2,2 años |
| 06 | Tasa de mejora de las ocho figuras, con el $T_2$ de dos intervalos |
| 07 | Frente de Pareto: dos posiciones dominadas y las tasas de canje |
| 08 | El diagnóstico en dos regímenes simultáneos |
| 09 | Los cuatro límites de los ajustes |

El hallazgo de la sección: los tres modelos divergen, y su divergencia es el
resultado. Lo que la tecnología **entrega**, medido como razón o como tiempo,
satura; lo que **abarca**, medido como recuento, sigue duplicándose cada dos
años. No hay contradicción, porque la superficie declarable y la superficie a
declarar crecen al mismo ritmo y la razón entre ambas es la cobertura.

### Trazabilidad de las cifras

Todas las cifras nuevas son reproducibles. Los ajustes logísticos, las tasas
de duplicación, el frente de Pareto, las cuatro ecuaciones del modelo técnico
y el flujo de caja se calcularon con SciPy antes de redactar, y las cuatro
ecuaciones del modelo técnico reproducen exactamente los valores de 2026 y de
2029 del cuadro de anclas, que se habían estimado por separado en la entrega
anterior.

Las publicaciones y las tres patentes del elemento 10 se verificaron una a una
en el registro, con número, titular y fecha. Las patentes son
US 11.372.626 B2 (JPMorgan Chase), US 11.349.958 B1 (Salesforce) y
WO 2024/023685 A1 (Dazz).

## Contenido de la carpeta

- `main.tex`: informe (70 páginas, con índice general). Las veinticuatro
  figuras son TikZ y pgfplots generadas desde el propio fuente; el documento
  no depende de ningún archivo de imagen.
- `referencias.bib`: 54 entradas, sólo con metadatos verificados de forma
  independiente.
- `context.txt`: el enunciado de la actividad y los doce elementos
  recomendados para el índice de una hoja de ruta tecnológica.

## Requisitos

- LuaLaTeX con `fontspec`, `babel`, `microtype`, `amsmath`, `tikz`
  (bibliotecas `arrows.meta`, `positioning`, `shapes.geometric`, `calc`,
  `fit`, `backgrounds`, `shadows`), `pgfplots`, `placeins`, `tocloft` y
  `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` disponible para `fontconfig`.
- `make`, `grep` y `poppler-tools` (`pdfinfo`) para las tareas automatizadas.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20.

Con 36 cuadros y 24 figuras, la cola de flotantes de LaTeX se desborda con los
parámetros por omisión y las tablas se acumulan al final del documento. El
preámbulo relaja `topfraction`, `bottomfraction`, `textfraction` y
`floatpagefraction`, sube los contadores `topnumber`, `bottomnumber` y
`totalnumber`, y carga `placeins` con la opción `section` para que ningún
flotante cruce de sección.

Puede comprobarse la disponibilidad de la tipografía con:

```bash
fc-match "Source Serif Pro"
```

## Compilación

```bash
make pdf
make check
```

El primer comando ejecuta la secuencia completa de LaTeX y Biber. El segundo
falla si el registro final contiene advertencias, referencias sin resolver o
problemas de composición. Para eliminar sólo los auxiliares, `make clean`.
