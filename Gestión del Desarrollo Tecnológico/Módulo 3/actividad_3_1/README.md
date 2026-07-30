# Actividad 3.1: fundición del acero en un horno de arco eléctrico

Cálculo del límite teórico de consumo eléctrico para fundir una tonelada de
acero (≈ 268 kWh/ton) y comparación con el desempeño del horno de arco
eléctrico en el año 2000 (375 kWh/ton).

El informe está escrito en LaTeX y utiliza LuaLaTeX, la tipografía OpenType
`Source Serif Pro` y `biblatex-apa`/Biber con estilo APA localizado al español.

## Archivos

- `main.tex`: informe.
- `referencias.bib`: bibliografía (Biber/APA).
- `chart.png`: gráfico del curso con las tres figuras de mérito (1970-2000).
  Es la Figura 1 del informe.
- `context.txt`: enunciado de la actividad.
- `Makefile`: tareas de compilación.
- `main.pdf`: documento generado.

Las fórmulas del cuadro del enunciado están compuestas directamente en LaTeX,
por lo que no se conserva ninguna imagen para ellas.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20 en versiones
recientes de LaTeX.

## Requisitos

- LuaLaTeX con los paquetes `fontspec`, `babel`, `microtype`, `amsmath`,
  `siunitx`, `tikz` y `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` instalada y disponible para `fontconfig`.
- `make`, `ripgrep` (`rg`) y `poppler-tools` (`pdfinfo`) para utilizar las
  tareas automatizadas.

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
