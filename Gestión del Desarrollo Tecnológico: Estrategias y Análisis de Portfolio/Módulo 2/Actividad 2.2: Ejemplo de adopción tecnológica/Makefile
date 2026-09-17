# Actividad 2.2. Ejemplo de adopción tecnológica.
# La transición del Mac de x86 a Apple Silicon, del M1 (2020) al M5 (2025),
# leída con las figuras de mérito del módulo.
#
#   make pdf    compone main.pdf con LuaLaTeX y Biber
#   make check  verifica que la composición no dejó avisos y resume la salida
#   make clean  borra los intermedios (main.pdf NO se borra)

.PHONY: pdf check clean

pdf: main.pdf

main.pdf: main.tex referencias.bib
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	biber main
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex

check:
	@if [ -f main.log ]; then \
	  if grep -E 'Warning|undefined|Overfull|Underfull|Error' main.log; then \
	    echo "la composición dejó avisos"; exit 1; \
	  else echo "composición sin avisos"; fi; \
	else echo "sin main.log: ejecuta make clean pdf para comprobar los avisos"; fi
	@pdfinfo main.pdf | grep -E '^(Pages|Page size|File size)'

clean:
	rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml main.toc
