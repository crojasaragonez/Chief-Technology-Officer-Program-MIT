# Foro 5.4: las tecnologías «obsoletas» se siguen utilizando

Caso de estudio sobre la primera generación de plaguicidas orgánicos de síntesis
(1944-1974) y su persistencia en la agricultura de Costa Rica, medida con los
datos oficiales de uso aparente del Servicio Fitosanitario del Estado
correspondientes a 2022.

El comentario responde a las cuatro preguntas del enunciado: qué tecnología es y
cómo la encontré, cuál es la tecnología nueva llamada a reemplazarla, por qué los
usuarios no la han abandonado y por qué además ha renacido.

## Tesis

Costa Rica no tiene una ley que prohíba importar moléculas nuevas. Tiene un
régimen de registro asimétrico que no le pide nada al producto viejo y se lo pide
todo al producto nuevo:

- Los decretos 17557 (1986) y 24337 (1995) inscribieron plaguicidas sin fecha de
  vencimiento.
- El decreto 33495 (2006) exige el paquete completo de datos de riesgo, pero solo
  a los registros nuevos.
- La Ley 8702 (2009) registró más de 400 plaguicidas sin evaluación ambiental ni
  sanitaria y concedió diez años de protección de datos de prueba.

Resultado: 1.884 formulados siguen en el mercado con registro vencido o sin
vencimiento y sin reválida de eficacia biológica, mientras el país pasó veintiún
años sin poder registrar moléculas nuevas.

La segunda respuesta, la del renacimiento, es agronómica: el mancozeb es
multisitio (FRAC M03) y sirve hoy como socio de mezcla que protege de la
resistencia a las moléculas modernas de sitio único.

## Contenido gráfico

- **Figura 1**: uso aparente de diecisiete ingredientes activos en 2022 sobre un
  eje logarítmico de 10² a 10⁷ kg, separados en la generación anterior a 1975 y
  la posterior a 1995. Compuesta en TikZ dentro de `main.tex`, sin imágenes
  externas.
- **Cuadro 1**: comparación de las dos generaciones en nueve figuras de mérito.

## Verificación de datos

Las cifras por molécula se tomaron del cuadro 2 del informe AE-REG-INF-001 del
SFE, extraído del PDF original, no de fuentes secundarias de prensa. Las
comprobaciones que cambiaron el contenido:

- La suma de las once moléculas antiguas es de **6,44 millones de kg ia**, el
  70 % del uso aparente nacional. Una versión previa del cuadro decía 5,6.
- Las tres cifras de kg/ha que circulan (8,84 del SFE, 34,45 del PNUD y 23,4 de
  FAOSTAT) usan denominadores distintos. Se citan las tres con su metodología en
  lugar de escoger la más llamativa.
- La razón de 6.344 a 1 entre mancozeb y clorantraniliprol es de masa, no de
  superficie tratada. La corrección por dosis de etiqueta se declara
  explícitamente como estimación de orden de magnitud.

Los años de introducción de cada molécula se declaran en la leyenda de la figura
con una incertidumbre de uno o dos años.

## Versión para el foro (TinyMCE)

La plataforma del foro usa un editor WYSIWYG TinyMCE, que acepta contenido
pegado desde el portapapeles con formato e imágenes incrustadas. El flujo es el
mismo del Foro 5.3:

```bash
make html
```

`exportar-figuras.py` extrae los entornos `tikzpicture` de `main.tex`, los
compila con la clase `standalone`, los convierte a PNG a 190 ppp, los optimiza
con `pngquant` y `optipng` e incrusta el resultado en base64 dentro de
`foro-5.4-tinymce.html`. Las imágenes del HTML no pueden desincronizarse del
informe porque se regeneran siempre desde la misma fuente.

Para publicar: abrir `foro-5.4-tinymce.html` en el navegador, seleccionar todo
(Ctrl+A), copiar (Ctrl+C) y pegar en el editor del foro. La imagen viaja dentro
del HTML, así que no hace falta subirla por separado.

`foro-5.4.html` es la fuente editable, con la imagen referenciada como archivo.
`foro-5.4-tinymce.html` es el artefacto generado y no debe editarse a mano.

Diferencias respecto al PDF: las citas van resueltas en texto al estilo APA en
lugar de generarse con Biber, y los estilos son inline en el `<head>` para que
TinyMCE los conserve al pegar.

## Archivos

- `main.tex`: comentario del foro.
- `referencias.bib`: bibliografía (Biber/APA), 18 entradas.
- `foro-5.4.html`: versión HTML editable, con la figura como archivo externo.
- `foro-5.4-tinymce.html`: generado por `make html`, con la figura en base64.
- `exportar-figuras.py`: exportador de figuras y ensamblador del HTML.
- `figuras/figura-1.png`: figura exportada desde `main.tex`.
- `notas-investigacion.md`: cifras verificadas con su fuente, base de redacción.
- `context.txt`: enunciado del foro.
- `Makefile`: tareas de compilación.
- `main.pdf`: documento generado, 7 páginas.

## Requisitos

- LuaLaTeX con `fontspec`, `babel`, `microtype`, `amsmath`, `siunitx`, `tikz` y
  `biblatex-apa`.
- Biber.
- La tipografía `Source Serif Pro` disponible para `fontconfig`:

```bash
fc-match "Source Serif Pro"
```

- `make`, `grep` y `poppler-tools` (`pdfinfo`, `pdftoppm`) para las tareas
  automatizadas.
- Para `make html`: Python 3 y, de forma opcional, `pngquant` y `optipng`. Sin
  ellos el HTML se genera igual, con las imágenes sin optimizar.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa`.

## Compilación

```bash
make pdf
make check
make html
```

El primer comando ejecuta la secuencia completa de LuaLaTeX y Biber. El segundo
falla si el registro contiene advertencias, referencias sin resolver o problemas
de composición. El tercero regenera la figura y el HTML para el foro. Para
eliminar solo los archivos auxiliares:

```bash
make clean
```
