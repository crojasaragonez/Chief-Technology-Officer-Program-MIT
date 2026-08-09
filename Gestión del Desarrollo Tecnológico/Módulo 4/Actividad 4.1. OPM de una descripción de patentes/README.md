# Actividad 4.1: OPM de una descripción de patentes

Informe que acompaña al modelo conceptual construido en OPM Sandbox a partir del
fragmento de la patente estadounidense 528.671 (trampa para ratones, 1894). El
texto explica cómo se pasa de una descripción de catorce piezas numeradas, que
es una descripción de forma, a un modelo de función con objetos, estados y
procesos.

El informe está escrito en LaTeX y utiliza LuaLaTeX, la tipografía OpenType
`Source Serif Pro` y `biblatex-apa`/Biber con estilo APA localizado al español.

## Archivos

- `main.tex`: informe.
- `OPM Mouse Trap.png`: captura del diagrama de objeto-proceso (Figura 1).
- `OPL Mouse Trap.png`: captura del OPL generado por la herramienta (Figura 2).
- `referencias.bib`: bibliografía (Biber/APA).
- `context.txt`: enunciado de la actividad y fragmento de la patente.
- `Makefile`: tareas de compilación.
- `main.pdf`: documento generado.

## Contenido del informe

- Criterio de traducción del texto al modelo: sustantivos a objetos, adjetivos y
  condiciones a estados, verbos a procesos, con un corte funcional (una pieza
  entra como objeto solo si alguno de sus estados cambia durante la operación).
- Lectura del OPD: seis objetos, la agregación de la trampa en base, gatillo,
  martillo y muelle transversal, y el enlace de agente que hace del animal el
  iniciador de la secuencia.
- Lectura de las diecinueve frases del OPL agrupadas en cuatro bloques:
  espacios de estados, estructura, secuencia y cambios de estado.
- Figura 3, compuesta en TikZ: separa el proceso de carga (Armar Trampa, cuatro
  precondiciones simultáneas) de la cadena de disparo de cinco pasos, con la
  transición de estado que aporta cada paso.
- Cuadro 1: trazabilidad entre las piezas numeradas de la patente (1 a 14) y las
  entidades del modelo, incluidas las que se dejaron fuera y por qué.
- Conclusiones: el cierre como componente crítico que desacopla la energía de
  activación de la energía de captura, la concentración del riesgo en Armar
  Trampa y la lectura de reivindicaciones sobre la función y no sobre la forma.
- Límites declarados del modelo: el estado `disparada` aún sin proceso que lo
  asigne, `Animal` modelado como objeto del sistema en lugar de entidad del
  entorno, y las relaciones `relates to` entre procesos que la construcción
  canónica de OPM expresaría como enlaces de invocación.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20 en versiones
recientes de LaTeX.

## Requisitos

- LuaLaTeX con los paquetes `fontspec`, `babel`, `microtype`, `amsmath`,
  `siunitx`, `graphicx`, `tikz` y `biblatex-apa`.
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
