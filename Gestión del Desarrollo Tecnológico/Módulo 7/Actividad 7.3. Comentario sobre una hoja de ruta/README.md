# Actividad 7.3 — Comentario sobre una hoja de ruta

Comentario crítico sobre la hoja de ruta tecnológica `quantum_ml_technology_overview_2.pdf`
(*Quantum Machine Learning*, 16.887/EM.427, otoño de 2023), con énfasis en si
el documento contiene material suficiente para proyectar una fecha de
disponibilidad de la tecnología.

El informe está escrito en LaTeX y utiliza LuaLaTeX, la tipografía OpenType
`Source Serif Pro` y `biblatex-apa`/Biber con estilo APA localizado al español.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20 en versiones
recientes de LaTeX.

## Contenido

- `main.tex` — informe (18 páginas). Todas las figuras son TikZ/pgfplots
  generadas desde el propio fuente; no depende de la carpeta `images/`, que
  contiene material de una actividad anterior.
- `referencias.bib` — sólo entradas con metadatos verificados de forma
  independiente (Crossref para artículos, Google Patents para las patentes).
- `quantum_ml_technology_overview_2.pdf` — hoja de ruta analizada.
- `context.txt` — los doce elementos recomendados para el índice de una hoja
  de ruta, usados como rejilla de evaluación.

## Método

Las cifras del comentario provienen de tres fuentes, siempre distinguidas en el
texto:

1. Transcripción de la hoja de ruta, incluidas las figuras que en la
   presentación aparecen reducidas (DSM, OPM, matriz morfológica, análisis de
   sensibilidad y tablas financieras), leídas a alta resolución.
2. Cálculo propio: reproducción del modelo de volumen cuántico, de las
   derivadas tecnológicas normalizadas y del flujo de caja descontado completo,
   más los ajustes de tendencia sobre la tabla competitiva.
3. Corroboración externa de toda afirmación que no procede del archivo.

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

La forma recomendada es:

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
