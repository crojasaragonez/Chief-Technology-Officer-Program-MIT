# Foro 6.3: ¿Un mundo sin automóviles?

Respuesta al enunciado del foro (¿conduce?, ¿puede imaginarse una vida sin
vehículo privado?) tratada como un problema de gestión tecnológica: si el mismo
artefacto produce cuotas de uso que van del **20 al 71 por ciento** según dónde
se mida, la variable explicativa no es el artefacto.

## Tesis

La pregunta «¿puede vivir sin coche?» no es una pregunta tecnológica sino de
accesibilidad: cuántos destinos caben dentro del presupuesto diario de tiempo de
viaje sin usar un automóvil. La figura de mérito que decide es del sistema
(densidad, mezcla de usos y reparto del espacio), no del vehículo, de modo que
electrificarlo o automatizarlo no mueve el resultado. En la Gran Área
Metropolitana de Costa Rica la respuesta hoy es «no puedo», y la fecha más
temprana en que podría cambiar la fija el calendario del tren eléctrico de la
GAM, no la industria del automóvil.

## Contenido gráfico

Las cuatro figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: la escalera del 20,3 al 71,2 por ciento. Cuota del vehículo
  privado en nueve ámbitos, incluidas las cuatro ciudades que menciona el
  enunciado. Las dos métricas disponibles (todos los viajes frente a
  desplazamientos al trabajo) se distinguen con color.
- **Figura 2**: el experimento natural de Madrid. Panel A, reparto modal por
  corona de residencia; Panel B, hogares sin ningún turismo. Mismo país, misma
  flota, mismo precio del combustible, cuatro resultados distintos.
- **Figura 3**: las dos restricciones que ninguna mejora del vehículo levanta.
  Panel A, el área alcanzable en treinta minutos crece con el cuadrado de la
  velocidad; Panel B, personas por hora que mueve un carril según a qué modo se
  dedique (NACTO).
- **Figura 4**: Costa Rica. Panel A, la flota crece un 150 por ciento mientras
  el uso del autobús cae un 42; Panel B, el calendario del Tren Eléctrico de
  Pasajeros de la GAM, de la ley firmada en mayo de 2026 a la operación completa
  en 2031.

## Verificación de datos

Las cifras no se tomaron de resúmenes de prensa cuando existía la fuente
primaria:

- **Madrid**: encuesta domiciliaria de movilidad de 2018 del Consorcio Regional
  de Transportes, PDF de síntesis. De ahí salen el reparto modal por corona
  (tabla 4) y la distribución de hogares por número de turismos (tabla 2).
- **Nueva York y Los Ángeles**: tablas B08301 y B25044 de la American Community
  Survey de 2024, consultadas por API el 19 de agosto de 2026. Los porcentajes
  se calcularon a partir de los conteos, no de fuentes secundarias.
- **Adelaida**: QuickStats del censo australiano de 2021 para Greater Adelaide.
- **Costa Rica**: boletín técnico del LanammeUCR (2024) para el reparto modal y
  el gasto de los hogares, con la Contraloría General de la República como
  origen del dato.

Tres comprobaciones cambiaron el contenido:

- La cifra de «segundo peor tránsito del mundo» de San José procede de
  **Numbeo**, un índice construido con respuestas voluntarias, y el índice de
  TomTom no cubre la ciudad. Se descartó y se declara por qué.
- El censo australiano de 2021 se levantó durante confinamientos, pero **Australia
  del Sur no estaba confinada** el día del censo, de modo que el dato de Adelaida
  es de los menos afectados. Se advierte igualmente.
- La flota costarricense se publica de tres maneras (1.879.790 derechos de
  circulación, más de 3,1 millones de automotores registrados y unos 2,1
  millones según LanammeUCR). Se usa la serie de derechos de circulación y se
  explica la diferencia.

## Versión para el foro (TinyMCE)

El foro se edita con TinyMCE, que acepta HTML pegado desde el navegador.

1. Abrir **`foro-6.3-tinymce.html`** en el navegador.
2. Seleccionar todo (`Ctrl+A`) y copiar (`Ctrl+C`).
3. Pegar en el cuadro de texto del foro (`Ctrl+V`).

Las cuatro figuras van incrustadas en base64 dentro del propio HTML, de modo que
viajan con el portapapeles y no hay que subirlas por separado. Si la instalación
concreta de TinyMCE filtra las imágenes en base64, están también sueltas en
`figuras/figura-1.png` a `figura-4.png` para insertarlas con el botón de imagen
del editor.

Los dos HTML **no se editan a mano**. `foro-6.3.html` es el maestro legible, con
rutas relativas a las imágenes, y el que se pega se genera con:

```bash
make html
```

Esa orden extrae los entornos `tikzpicture` de `main.tex`, los compila con la
clase `standalone`, los convierte a PNG, los optimiza con `pngquant` y `optipng`
y los incrusta en `foro-6.3-tinymce.html`. Las figuras del foro no pueden, por
tanto, desincronizarse de las del informe.

## Archivos

- `main.tex`: informe.
- `referencias.bib`: bibliografía (Biber/APA), 29 entradas, todas citadas.
- `contexto.txt`: enunciado de la actividad.
- `Makefile`: tareas de compilación (`pdf`, `html`, `check`, `clean`).
- `main.pdf`: documento generado, 10 páginas.
- `foro-6.3.html`: versión HTML del informe (maestro, con rutas relativas).
- `foro-6.3-tinymce.html`: versión generada, con las imágenes incrustadas, para
  copiar y pegar en el foro.
- `exportar-figuras.py`: genera las dos cosas anteriores desde `main.tex`.
- `figuras/`: las cuatro figuras en PNG, por si hay que subirlas a mano.

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
