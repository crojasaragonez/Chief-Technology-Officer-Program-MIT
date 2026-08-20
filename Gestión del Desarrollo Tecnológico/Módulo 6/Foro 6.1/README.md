# Foro 6.1: Vehículos autónomos

Respuesta a las cuatro preguntas del enunciado (certificación, tránsito mixto,
responsabilidad legal y empleo) con los datos disponibles en agosto de 2026:
**220,6 millones de millas sin conductor a bordo** acumuladas por el mayor
operador hasta marzo de 2026, la primera exención de despliegue comercial de la
NHTSA a un vehículo sin volante (31 de julio de 2026) y la norma china
obligatoria GB 44721-2026 (4 de agosto de 2026).

## Tesis

**Lo que hay que certificar no es un vehículo, es un proceso.** El umbral
estadístico que haría creíble una certificación por kilometraje está fuera de
alcance: 275 millones de millas sin una sola muerte para acreditar la tasa de
mortalidad al 95 por ciento y 8.800 millones para demostrar una mejora del 20
por ciento (Kalra y Paddock, 2016), y cada actualización de software reinicia la
cuenta. De ahí se derivan las otras tres respuestas:

- **Tránsito mixto**, con el dominio de diseño operativo (ODD) como valla: es una
  restricción real, auditable, ampliable por tramos y revocable, a diferencia de
  la infraestructura dedicada.
- **La responsabilidad se traslada** del conductor al operador y al fabricante,
  con pago en primera instancia por el seguro y repetición posterior, que es el
  diseño británico. Entre dos autónomos deciden los registros de datos, no los
  testimonios.
- **El empleo pierde y gana a distinto ritmo**: poco en el agregado y en treinta
  años, mucho en unas pocas ciudades y en dos o tres años, lo que ya se está
  midiendo.

## Contenido gráfico

Las cinco figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: el límite estadístico de la certificación por millas. Panel A,
  los dos umbrales de Kalra y Paddock frente a lo acumulado por Waymo y frente a
  la exposición anual de los conductores humanos de EE. UU. ($3{,}3\times10^{12}$
  millas). Panel B, la serie de millas acumuladas sin conductor, de 7,1 millones
  a finales de 2023 a 220,6 millones en marzo de 2026, con el cruce del primer
  umbral hacia julio de 2026.
- **Figura 2**: los dos regímenes de autorización. Panel A, cronología comparada
  de la homologación de tipo con auditoría (UNECE, UE, Alemania, Reino Unido,
  China) frente a la autocertificación estadounidense con exenciones. Panel B, la
  autorización por capas que propongo, de la norma del vehículo a la vigilancia
  continua.
- **Figura 3**: la evidencia del tránsito mixto. Panel A, reducciones del 94, 82
  y 93 por ciento frente al conductor humano de la misma zona. Panel B, los 78
  siniestros con lesión o airbag comunicados a la NHTSA: 72 originados por otro
  conductor y 48 alcances por detrás.
- **Figura 4**: quién responde en cada régimen, con las tres cadenas de
  responsabilidad (EE. UU., Reino Unido, UE y Alemania) y el escenario de dos
  autónomos entre sí.
- **Figura 5**: empleo expuesto (15,5 y 3,8 millones de trabajadores) y efectos
  ya medidos en los mercados con robotaxi en el cuarto trimestre de 2025.

Los dos cuadros recogen la cronología verificada y la matriz de responsabilidad
por escenario y por jurisdicción.

## Verificación de datos

Los datos se tomaron de fuentes primarias siempre que existían:

- Millas y reducciones de siniestralidad: página de impacto de seguridad de Waymo
  (datos a 31 de marzo de 2026) y la actualización del 24 de junio de 2026,
  contrastadas con el estudio revisado por pares de *Traffic Injury Prevention*
  (56,7 millones de millas) y con el análisis de reclamaciones de Swiss Re (25,3
  millones de millas), que es independiente del operador.
- Siniestralidad humana de referencia: `DOT HS 813 829` de la NHTSA, julio de
  2026, que da 36.640 muertes estimadas en 2025 y una tasa de 1,10 por cada 100
  millones de millas. La exposición anual de $3{,}3\times10^{12}$ millas es un
  cálculo propio a partir de esas dos cifras.
- Regulación: textos y publicaciones oficiales (Reglamento UNECE 157, Reglamento
  de Ejecución (UE) 2022/1426, Directiva (UE) 2024/2853, leyes británicas de 2018
  y 2024, *Federal Register* del 31 de julio de 2026).
- Empleo: *Occupational Outlook Handbook* del BLS y los dos estudios académicos
  de referencia (Beede et al., 2017; Groshen et al., 2018).

Tres comprobaciones cambiaron el contenido:

- La cifra de 220,6 millones de millas corresponde a **marzo de 2026** y a cinco
  áreas metropolitanas, no al total histórico de la empresa en todas sus
  operaciones. La serie de la Figura 1 usa solo puntos con fuente identificable
  y descarta los hitos que solo aparecían en agregadores.
- Los dos fallecimientos con vehículos sin conductor implicados (San Francisco,
  enero de 2025, y Dallas, 2026) **no se atribuyeron al sistema**: la
  reconstrucción sitúa la causa en terceros. Se declara así en las limitaciones.
- El reparto de culpa de los 78 siniestros es una **lectura de los relatos** hecha
  por un analista externo, no una resolución oficial: los informes de la orden
  general de la NHTSA acreditan que hubo choque, no quién tuvo la culpa.

Los datos de ingresos de los conductores de plataforma proceden de un panel
privado y se declaran como dirección, no como magnitud. Los dos hitos chinos se
apoyan en prensa especializada porque no hay versión oficial verificable.

## Versión para el foro (TinyMCE)

El foro se edita con TinyMCE, que acepta HTML pegado desde el navegador.

1. Abrir **`foro-6.1-tinymce.html`** en el navegador.
2. Seleccionar todo (`Ctrl+A`) y copiar (`Ctrl+C`).
3. Pegar en el cuadro de texto del foro (`Ctrl+V`).

Las cinco figuras van incrustadas en base64 dentro del propio HTML, de modo que
viajan con el portapapeles y no hay que subirlas por separado. Si la instalación
concreta de TinyMCE filtra las imágenes en base64, están también sueltas en
`figuras/figura-1.png` a `figura-5.png` para insertarlas con el botón de imagen
del editor.

Los dos HTML **no se editan a mano**. `foro-6.1.html` es el maestro legible, con
rutas relativas a las imágenes, y el que se pega se genera con:

```bash
make html
```

Esa orden extrae los entornos `tikzpicture` de `main.tex`, los compila con la
clase `standalone`, los convierte a PNG, los optimiza con `pngquant` y `optipng`
y los incrusta en `foro-6.1-tinymce.html`. Las figuras del foro no pueden, por
tanto, desincronizarse de las del informe.

## Archivos

- `main.tex`: informe.
- `referencias.bib`: bibliografía (Biber/APA), 40 entradas, todas citadas.
- `contexto.txt`: enunciado de la actividad.
- `Makefile`: tareas de compilación (`pdf`, `html`, `check`, `clean`).
- `main.pdf`: documento generado, 14 páginas.
- `foro-6.1.html`: versión HTML del informe (maestro, con rutas relativas).
- `foro-6.1-tinymce.html`: versión generada, con las imágenes incrustadas, para
  copiar y pegar en el foro.
- `exportar-figuras.py`: genera las dos cosas anteriores desde `main.tex`.
- `figuras/`: las cinco figuras en PNG, por si hay que subirlas a mano.

## Requisitos

- LuaLaTeX con `fontspec`, `babel`, `microtype`, `amsmath`, `siunitx`, `tikz`
  (bibliotecas `arrows.meta` y `patterns`) y `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` disponible para `fontconfig`:

```bash
fc-match "Source Serif Pro"
```

- `make`, `grep` y `poppler-tools` (`pdfinfo`, `pdftoppm`) para las tareas
  automatizadas.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa`. Por la misma razón
los porcentajes de las figuras se escriben en modo texto (`+4\,\%`) y no en modo
matemático: `babel-spanish` redefine `\%` y la versión en modo matemático rompe la
compilación de las figuras con la clase `standalone`.

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
