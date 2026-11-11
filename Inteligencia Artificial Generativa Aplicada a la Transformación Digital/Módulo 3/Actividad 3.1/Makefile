# Actividad 3.1. Su prompt en la práctica.
#
#   make pdf       compone main.pdf con LuaLaTeX
#   make palabras  cuenta las palabras de cada sección (límites de la actividad)
#   make check     verifica avisos, pendientes y rayas
#   make clean     borra los intermedios (main.pdf NO se borra)

.PHONY: pdf palabras check clean

pdf: main.pdf

main.pdf: main.tex $(wildcard capturas/*)
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex

# Paso 1: 80 a 120. Paso 3: 150 a 200. Total sin la biblioteca: 400 a 500.
palabras:
	@texcount -sub=section -utf8 main.tex | grep -E 'Section|Words in text'

check:
	@if grep -n 'pendiente{' main.tex | grep -v -e newcommand -e '#1'; then \
	  echo "quedan pendientes por escribir"; else echo "sin pendientes"; fi
	@if grep -n -e '—' -e '---' main.tex; then echo "hay rayas"; else echo "sin rayas"; fi
	@if grep -E 'Warning|undefined|Overfull|Error' main.log; then \
	  echo "la composición dejó avisos"; else echo "composición sin avisos"; fi
	@pdfinfo main.pdf | grep -E '^(Pages|File size)'

clean:
	rm -f main.aux main.log main.out main.toc
