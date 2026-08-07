# Foro 4.3: patentes como indicador de globalización

Artículo breve para el foro 4.3. Responde a las dos preguntas del enunciado
(qué opino de la tendencia y cuáles son sus ventajas e inconvenientes)
separando dos fenómenos que suelen confundirse en la misma estadística: la
co-invención internacional, que es colaboración, y el control transfronterizo
de la titularidad, que es propiedad.

La postura personal que sostiene el texto es que la patente es un mal
necesario: sus beneficios son reales, pero el costo del proceso en dinero y en
tiempo no los justifica, y la internacionalización multiplica precisamente ese
defecto.

El informe está escrito en LaTeX y utiliza LuaLaTeX, la tipografía OpenType
`Source Serif Pro` y `biblatex-apa`/Biber con estilo APA localizado al español.

## Archivos

- `main.tex`: artículo.
- `referencias.bib`: bibliografía (Biber/APA).
- `context.txt`: enunciado de la actividad y opinión personal de partida.
- `Makefile`: tareas de compilación.
- `main.pdf`: documento generado.

Las dos figuras están compuestas en TikZ, por lo que no hay imágenes externas:

- Figura 1: serie de solicitudes PCT (2000-2024), con el aplanamiento posterior
  a 2020. Valores verificados contra fuentes de la OMPI: 90.948 en 2000
  (comunicado UPD/2001/124), unas 134.000 en 2005 (*The International Patent
  System in 2005*), y 164.355 en 2010, 218.000 en 2015, 274.889 en 2020 y
  273.900 en 2024 (*PCT Yearly Review 2025*, cuadros S3 y A1). La propia OMPI
  describe 2020-2024 como una meseta de cinco años, con una variación media del
  -0,1 % anual.
- Figura 2: matriz de cuatro cuadrantes que cruza el lugar de la invención con
  la titularidad del derecho, según la taxonomía de Archibugi y Michie (1995).

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
