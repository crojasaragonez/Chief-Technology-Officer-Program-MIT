# Hoja de ruta tecnológica de la infraestructura como código

Documento único y acumulativo (`main.tex`) de la hoja de ruta tecnológica de
la **infraestructura como código** (IaC). Cada entrega del curso se inserta
como una sección más, en el lugar que le corresponde por el índice de doce
elementos de una hoja de ruta, no al final.

Esta versión incorpora las correcciones pedidas por el profesor sobre la
Actividad Final Integrada, Parte A:

- **Elemento 2, matriz de estructura de dependencia (DSM)**: faltaba por
  completo. Se añade como sección 8, con dos matrices, su particionado y la
  secuencia de implantación que se deriva de él.
- **Elemento 3, OPM**: se reconstruye entero. Se corrigen los errores de
  sintaxis del OPD anterior y se separa el modelo en los tres diagramas que
  prevé la norma (SD, despliegue SD2 y ampliación SD1), cada uno con su OPL.

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
| **8** | **2** | **DSM de arquitectura y DSM de cartera, particionado y secuencia** |
| **9** | **3** | **Modelo OPM: SD, SD2, SD1 y el OPL de los tres** |
| 10 | 4 | Ocho figuras de mérito con unidad y procedimiento de medida |
| 11 | 6 | Posicionamiento frente a la competencia: gráfico vectorial |
| 12 | | Conclusiones |

### La sección 8 (DSM) en detalle

| Apartado | Contenido |
|---|---|
| 01 | Convención de lectura: marca en (i, j) significa que i necesita algo de j |
| 02 | DSM de arquitectura sobre los trece componentes (Figura 8) |
| 03 | Lectura de las sumas: concentradores de riesgo y puntos de arranque |
| 04 | Particionado en ocho olas y el bloque acoplado L1-M4 (Figura 9) |
| 05 | DSM de la cartera de ocho proyectos, con dos intensidades (Figura 10) |
| 06 | Secuenciación en seis olas; la cartera no tiene ciclos (Figura 11) |
| 07 | Riesgos que la estructura hace visibles |
| 08 | Límites de las dos matrices |

El hallazgo que enlaza los elementos 2 y 3: la DSM detecta un único bloque
acoplado, el del motor de aprovisionamiento con la política como código, y la
ampliación en detalle del modelo OPM lo rompe al partir el proceso en
planificación, validación y aplicación.

### La sección 9 (OPM) en detalle

| Apartado | Contenido |
|---|---|
| 01 | Por qué OPM y cómo se ha construido el modelo |
| 02 | Vocabulario cerrado de la norma y frase OPL que genera cada símbolo |
| 03 | Diagrama de sistema (SD) y sus entidades |
| 04 | OPL del SD |
| 05 | Despliegue de la especificación (SD2) y su OPL |
| 06 | Ampliación en detalle del proceso principal (SD1) |
| 07 | OPL de la ampliación |
| 08 | Qué hace explícito el modelo |

Errores del OPD anterior que quedan corregidos: las flechas entre subprocesos
de la ampliación, que en OPM serían enlaces de invocación y no precedencia;
la falta de distinción de las cosas físicas y ambientales; el uso de «puede
ser» (que declara estados) para una generalización; los cambios de estado
declarados en el OPL pero dibujados como enlace de efecto al objeto entero; la
orientación del triángulo de exhibición; y el «consta de» de la ampliación,
que es la frase de la agregación y no la del despliegue del proceso.

### La sección 11 (competencia) en detalle

| Apartado | Contenido |
|---|---|
| 01 | Quién es el cliente, quién el productor y cuál el producto de referencia |
| 02 | Caracterización de los tres jugadores |
| 03 | Construcción de los dos ejes: utilidad multiatributo e índice de coste |
| 04 | Figuras de mérito estimadas a 2029 y perfil comparado |
| 05 | Descomposición de cada trayectoria en vectores tecnológicos |
| 06 | El gráfico vectorial |
| 07 | Lectura del gráfico |
| 08 | Sensibilidad al supuesto de cartera de nube |
| 09 | Límites del análisis |

## Contenido de la carpeta

- `main.tex`: informe (35 páginas, con índice general). Las dieciséis figuras
  son TikZ y pgfplots generadas desde el propio fuente; el documento no
  depende de ningún archivo de imagen.
- `referencias.bib`: sólo entradas con metadatos verificados de forma
  independiente.
- `context.txt`: los doce elementos recomendados para el índice de una hoja de
  ruta tecnológica.

## Requisitos

- LuaLaTeX con `fontspec`, `babel`, `microtype`, `amsmath`, `tikz`
  (bibliotecas `arrows.meta`, `positioning`, `shapes.geometric`, `calc`,
  `fit`, `backgrounds`, `shadows`), `pgfplots`, `tocloft` y `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` disponible para `fontconfig`.
- `make`, `grep` y `poppler-tools` (`pdfinfo`) para las tareas automatizadas.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20.

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
