# Actividad 2.2 — diseños inspirados en la biología

El borrador está escrito en LaTeX y utiliza `biblatex-apa`/Biber con estilo
APA localizado al español.

La opción `es-noshorthands` de Babel evita una incompatibilidad conocida entre
los caracteres abreviados de `babel-spanish` y `biblatex-apa` 9.20 en versiones
recientes de LaTeX.

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
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

Para eliminar únicamente los archivos auxiliares generados:

```bash
make clean
```

Antes de entregar, sustituya en `main.tex` los marcadores del nombre y la fecha.
Las secciones comentadas al final del archivo sirven como estructura para los
otros diseños bioinspirados.
