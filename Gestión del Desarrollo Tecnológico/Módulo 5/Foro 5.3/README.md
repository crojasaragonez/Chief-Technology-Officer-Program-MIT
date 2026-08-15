# Foro 5.3: ¿Siempre gana la mejor tecnología?

Caso de estudio sobre **IPv6**, especificado en diciembre de 1995 y elevado a
norma de Internet (STD 86) en julio de 2017, que treinta años después alcanza al
47 por ciento de los usuarios sin haber sustituido a IPv4 en ningún momento.

El informe responde a las dos preguntas del enunciado, cuándo y por qué ocurrió,
con figuras de mérito y curvas en S de los dos protocolos.

## Tesis

IPv6 es superior a IPv4 en casi todas las figuras de mérito medibles, pero valía
cero en la única que gobierna la adopción de un protocolo de red: la
compatibilidad con la base instalada. Mientras tanto, el titular no compitió en
el terreno del invasor, mejoró en el suyo. CIDR (1993), NAT (1994) y CGNAT (2012)
convirtieron el techo de direcciones de IPv4 de rígido en elástico, y **NAT se
publicó diecinueve meses antes que IPv6**.

## Contenido gráfico

Las cuatro figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: las dos curvas en S sobre un mismo FOM (fracción de usuarios que
  puede usar el protocolo de forma nativa). IPv4 sube de 0 a 100 por ciento en un
  día, el 1 de enero de 1983 sobre unos 400 servidores; IPv6 lleva desde 2008
  midiéndose y no llega al 50. Incluye las dos series de medición independientes
  (Google y APNIC Labs) y las dos extrapolaciones. Es el diagrama que pide el
  enunciado.
- **Figura 2**: el contrainvasor. Panel A, cronología comparada de las normas del
  IETF, que muestra el adelanto del remiendo sobre el sucesor. Panel B, precio de
  mercado de una dirección IPv4, que cae desde 2021.
- **Figura 3**: perfil de figuras de mérito expresado como razón entre IPv6 e
  IPv4, en dos paneles porque la ventaja en espacio de direcciones (29 órdenes de
  magnitud) no cabe en el mismo eje que las demás.
- **Figura 4**: adopción de IPv6 por región, que muestra que la media mundial del
  43 por ciento no describe a ninguna región concreta.

Los dos cuadros recogen la cronología verificada y la matriz completa de FOM.

## Verificación de datos

Las series de adopción **no se tomaron de fuentes secundarias**, que resultaron
contradictorias entre sí, sino descargando los datos crudos de las dos
mediciones públicas el 15 de agosto de 2026:

- Google: `www.google.com/intl/en_ALL/ipv6/statistics/data/adoption.js`,
  6.552 datos diarios desde el 4 de septiembre de 2008.
- APNIC Labs: `data1.labs.apnic.net/v6stats/v6region/XA.json`,
  4.639 datos con suavizado de 30 días desde el 7 de octubre de 2013.
- Tabla de rutas global: `bgp.potaroo.net`, AS6447.

Cuatro comprobaciones cambiaron el contenido:

- Las fuentes secundarias daban el cruce del 50 por ciento el 28 de marzo, el 13
  de abril y el 23 de abril de 2026, con valores distintos. El dato crudo
  confirma el **28 de marzo de 2026 con 50,10 por ciento**, que además fue
  **sábado**: los quince días en que la serie supera el 50 son todos fines de
  semana, y la media móvil de 30 días nunca lo ha alcanzado.
- El ajuste logístico y la extrapolación lineal se contradicen (asíntota en el
  47,6 por ciento frente a llegada al 100 en 2045). Se comprobó cuál ajusta mejor
  los últimos cinco años y se declara la contradicción en lugar de elegir.
- El artículo de The Register sobre los treinta años de IPv6 lo firma **Simon
  Sharwood**, no el autor que sugería la búsqueda.
- El número de campos de la cabecera IPv4 (doce antes de las opciones) y la
  longitud mínima (20 octetos) se contrastaron con la RFC 791 original, no con
  resúmenes.

Los precios del mercado de direcciones IPv4 se declaran como orden de magnitud y
tendencia, no como serie de precio único, porque las fuentes disponibles son
informes de intermediarios con dispersión alta según el tamaño del bloque.

## Archivos

- `main.tex`: informe.
- `referencias.bib`: bibliografía (Biber/APA), 38 entradas, todas citadas.
- `context.txt`: enunciado de la actividad.
- `Makefile`: tareas de compilación.
- `main.pdf`: documento generado, 11 páginas.

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
