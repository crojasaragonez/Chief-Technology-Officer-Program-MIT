# Actividad 8.1, parte B: análisis de la competencia

Continuación de la actividad 7.4, parte A. Al informe sobre el alcance de la
**infraestructura como código** (IaC) se le añade el análisis competitivo que
pide la segunda entrega: un **gráfico vectorial** que sitúa a tres
competidores (Terraform, Bicep y Pulumi) y a la trayectoria propuesta para la
empresa en un plano de variación de valor para el cliente y variación de coste
para el productor.

Ese análisis corresponde al **elemento 6** del índice de una hoja de ruta
tecnológica ATRA, el posicionamiento de la empresa con respecto a la
competencia mediante diagramas de figuras de mérito, y ocupa la sección 9 del
informe. Se apoya en las ocho figuras de mérito ya definidas en la sección 8,
de modo que las dos entregas forman un solo documento y no dos informes
separados.

El informe está escrito en LaTeX y utiliza LuaLaTeX, la tipografía OpenType
`Source Serif Pro` y `biblatex-apa`/Biber con estilo APA localizado al español.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20 en versiones
recientes de LaTeX.

## Contenido

- `main.tex`: informe (25 páginas, con índice general). Las doce figuras son TikZ y pgfplots
  generadas desde el propio fuente; el documento no depende de ningún archivo
  de imagen.
- `referencias.bib`: sólo entradas con metadatos verificados de forma
  independiente (Crossref y las páginas oficiales de cada norma o proyecto).
- `context.txt`: los doce elementos recomendados para el índice de una hoja de
  ruta tecnológica, conservados como contexto del módulo.
- `grafico_vectorial.png`: la plantilla genérica de gráfico vectorial
  facilitada con el enunciado. No la usa el documento: la Figura 9 es de
  elaboración propia.

## Estructura del informe

El índice general está en la página 2 y llega al nivel de apartado. Los
apartados van sin numerar en el cuerpo del texto, así que se registran en el
índice con el comando `\subsec`, definido en el preámbulo, que además de
componer el título añade la entrada correspondiente.

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
| **9** | **Posicionamiento frente a la competencia: competidores, construcción de los dos índices, gráfico vectorial, sensibilidad y límites** |
| 10 | Modelo OPM: entidades, diagrama de sistema y su OPL, enlaces estructurales, ampliación SD1 y su OPL |
| 11 | Conclusiones |

## La sección 9 en detalle

| Apartado | Contenido |
|---|---|
| 01 | Quién es el cliente, quién el productor y cuál el producto de referencia |
| 02 | Caracterización de los tres jugadores (Cuadro 5) |
| 03 | Construcción de los dos ejes: utilidad multiatributo e índice de coste de propiedad |
| 04 | Figuras de mérito estimadas a 2029 (Cuadros 6 y 7) y perfil comparado (Figura 8) |
| 05 | Descomposición de cada trayectoria en vectores tecnológicos (Cuadro 8) |
| 06 | El gráfico vectorial (Figura 9) |
| 07 | Lectura del gráfico: frontera de eficiencia, origen real del valor, trampa del cuadrante inferior izquierdo |
| 08 | Sensibilidad al supuesto de cartera de nube (Cuadro 9) |
| 09 | Límites del análisis |

Las coordenadas del gráfico son índices construidos, no magnitudes
observables, y el documento declara su procedimiento de cálculo: las cuatro
figuras de mérito orientadas al cliente se normalizan a una utilidad de 0 a
100 entre anclas explícitas y se agregan con pesos declarados; el eje de coste
es un índice de coste anual de propiedad por cada cien recursos gestionados,
con la plataforma actual normalizada a 100 puntos.

## Diagrama en OPM Sandbox

El modelo de objetos y procesos está en la sección 10 del informe: el diagrama
de sistema, los enlaces estructurales, la ampliación en detalle y el OPL de
ambos niveles.

El diagrama construido en <https://opcloud-sandbox.web.app/> se entrega aparte.
El entorno no guarda el trabajo entre sesiones ni permite descargarlo, de modo
que la captura de pantalla es el único registro posible; el informe no la
incorpora ni depende de ella.

## Requisitos

- LuaLaTeX con los paquetes `fontspec`, `babel`, `microtype`, `amsmath`,
  `tikz`, `pgfplots`, `tocloft` y `biblatex-apa`.
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
