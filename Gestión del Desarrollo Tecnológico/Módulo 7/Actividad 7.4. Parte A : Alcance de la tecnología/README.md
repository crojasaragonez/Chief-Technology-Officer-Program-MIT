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

- `main.tex` — informe (17 páginas). Las doce figuras son TikZ generadas desde
  el propio fuente; las dos últimas son marcos reservados para las capturas de
  pantalla de OPM Sandbox.
- `referencias.bib` — sólo entradas con metadatos verificados de forma
  independiente (Crossref y las páginas oficiales de cada norma o proyecto).
- `images/` — destino de las capturas de pantalla de OPM Sandbox.
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
| 9 | Modelo OPM: diagrama de sistema, enlaces estructurales, ampliación SD1 y OPL |
| 10 | Procedimiento de construcción en OPM Sandbox y capturas |
| 11 | Conclusiones |

## Capturas de OPM Sandbox

El entorno <https://opcloud-sandbox.web.app/> no guarda el trabajo entre
sesiones ni permite descargarlo. El procedimiento de construcción, paso a paso,
está en la sección 10 del informe. Una vez tomadas las capturas, guardarlas
como:

```
images/opcloud-sd.png     # diagrama de sistema (SD)
images/opcloud-sd1.png    # ampliación en detalle (SD1)
```

y recompilar. Las figuras 11 y 12 las insertan automáticamente; mientras no
existan, el informe compila mostrando un marco reservado en su lugar.

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
