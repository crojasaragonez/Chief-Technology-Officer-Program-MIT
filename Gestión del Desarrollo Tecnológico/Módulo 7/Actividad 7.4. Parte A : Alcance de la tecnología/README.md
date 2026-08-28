# Actividad 7.4, parte A — Alcance de la tecnología

Resumen del funcionamiento de un sistema completo de **infraestructura como
código** (IaC), con los diagramas de sus capas y módulos principales, y modelo
de objetos y procesos según la metodología OPM.

El informe está escrito en LaTeX y utiliza LuaLaTeX, la tipografía OpenType
`Source Serif Pro` y `biblatex-apa`/Biber con estilo APA localizado al español.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20 en versiones
recientes de LaTeX.

## Contenido

- `main.tex` — informe (16 páginas). Las diez figuras son TikZ generadas desde
  el propio fuente; el documento no depende de ningún archivo de imagen.
- `referencias.bib` — sólo entradas con metadatos verificados de forma
  independiente (Crossref y las páginas oficiales de cada norma o proyecto).
- `context.txt` — los doce elementos recomendados para el índice de una hoja de
  ruta tecnológica, conservados como contexto del módulo.

## Estructura del informe

| Sección | Contenido |
|---|---|
| 1 | Objeto y frontera del sistema; las cuatro propiedades que definen un sistema completo |
| 2 | Principio de funcionamiento: estado deseado, registrado y real; bucle de conciliación |
| 3 | Ciclo de operación en siete pasos; comparación a tres bandas |
| 4 | Las siete capas, de L0 (sustrato) a L6 (plataforma) |
| 5 | Los seis módulos transversales |
| 6 | Modos de operación: empuje/arrastre, mutable/inmutable, declarativo/imperativo |
| 7 | El módulo como unidad de composición |
| 8 | Ocho figuras de mérito con unidad y procedimiento de medida |
| 9 | Modelo OPM: entidades, diagrama de sistema y su OPL, enlaces estructurales, ampliación SD1 y su OPL |
| 10 | Conclusiones |

## Diagrama en OPM Sandbox

El modelo de objetos y procesos está en la sección 9 del informe: el diagrama
de sistema, los enlaces estructurales, la ampliación en detalle y el OPL de
ambos niveles.

El diagrama construido en <https://opcloud-sandbox.web.app/> se entrega aparte.
El entorno no guarda el trabajo entre sesiones ni permite descargarlo, de modo
que la captura de pantalla es el único registro posible; el informe no la
incorpora ni depende de ella.

## Requisitos

- LuaLaTeX con los paquetes `fontspec`, `babel`, `microtype`, `amsmath`,
  `tikz`, `pgfplots` y `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` instalada y disponible para `fontconfig`.
- `make`, `grep` y `poppler-tools` (`pdfinfo`) para utilizar las tareas
  automatizadas.

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
problemas de composición.

La secuencia equivalente ejecutada manualmente es:

```bash
lualatex main.tex
biber main
lualatex main.tex
lualatex main.tex
```

Para eliminar únicamente los archivos auxiliares generados:

```bash
make clean
```
