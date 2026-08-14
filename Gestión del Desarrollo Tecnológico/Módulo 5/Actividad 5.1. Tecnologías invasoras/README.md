# Actividad 5.1: tecnologías invasoras

Caso de estudio sobre la sustitución de la enciclopedia impresa
(*Encyclopædia Britannica*, 1768-2012) y la cadena de cuatro generaciones
tecnológicas que la reemplazaron: papel, CD-ROM (Microsoft Encarta, 1993-2009),
wiki (Wikipedia, 2001 hasta hoy) y modelos de lenguaje (2022 hasta hoy).

El informe responde a las dos preguntas del enunciado, cuándo y por qué ocurrió,
e incluye el diagrama pedido con un eje de tiempo y un eje de figura de mérito.

## Contenido gráfico

Las cinco figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: curvas en S de las cuatro generaciones sobre el FOM de cobertura
  (artículos accesibles, escala logarítmica) entre 1889 y 2026, con el eje de
  tiempo comprimido antes de 1990. Marca el cruce de curvas en 2002. Es el
  diagrama que pide el enunciado.
- **Figuras 2 a 5**: una ficha de figuras de mérito por generación
  (enciclopedia impresa, Encarta, Wikipedia y modelos de lenguaje) sobre un eje
  logarítmico común de 10⁻³ a 10⁹, con cinco FOM comparables: cobertura,
  profundidad, latencia de actualización, latencia de acceso y coste marginal.
  Las líneas punteadas indican la posición de las generaciones anteriores.
  La Figura 5 añade un segundo panel con el FOM que empeora, la fiabilidad de
  las respuestas.

Los dos cuadros recogen la cronología verificada y la matriz completa de FOM.

## Verificación de datos

Todas las cifras del documento se contrastaron con la fuente antes de escribirse.
Dos comprobaciones cambiaron el contenido:

- El hito de siete millones de artículos de la Wikipedia en inglés es del
  **28 de mayo de 2025**, no de 2022 como afirmaba una fuente secundaria.
- El recuento actual de artículos se tomó en directo de la API de Wikipedia
  (`action=query&meta=siteinfo&siprop=statistics`), no de una cifra citada.

Los valores que no son datos medidos se declaran como tales en las leyendas y en
la sección de precisiones y limitaciones: la latencia de acceso de la
enciclopedia impresa es un supuesto de orden de magnitud, y dos tramos de la
Figura 1 se dibujan de forma esquemática por falta de una serie anual pública.

## Archivos

- `main.tex`: informe.
- `referencias.bib`: bibliografía (Biber/APA), 32 entradas.
- `context.txt`: enunciado de la actividad.
- `Makefile`: tareas de compilación.
- `main.pdf`: documento generado, 12 páginas.

## Requisitos

- LuaLaTeX con `fontspec`, `babel`, `microtype`, `amsmath`, `siunitx`, `tikz`
  (bibliotecas `arrows.meta` y `patterns`) y `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` disponible para `fontconfig`:

```bash
fc-match "Source Serif Pro"
```

- `make`, `grep` y `poppler-tools` (`pdfinfo`) para las tareas automatizadas.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa`.

## Compilación

```bash
make pdf
make check
```

El primer comando ejecuta la secuencia completa de LuaLaTeX y Biber. El segundo
falla si el registro contiene advertencias, referencias sin resolver o problemas
de composición. Para eliminar solo los archivos auxiliares:

```bash
make clean
```
