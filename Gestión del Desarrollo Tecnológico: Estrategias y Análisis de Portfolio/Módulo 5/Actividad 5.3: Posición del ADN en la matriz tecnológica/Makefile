# Actividad 5.3. Posición del ADN en la matriz tecnológica.
# Ubicación de la secuenciación del ADN en la matriz 5x5 y tasa anual de
# mejora del coste por genoma desde el año 2000.
#
#   make pdf    compone main.pdf con LuaLaTeX y Biber
#   make check  verifica que la composición no dejó avisos y resume la salida
#   make clean  borra los intermedios (main.pdf NO se borra)
#
# Los datos de las figuras están en datos/. Los .dat del gráfico del módulo
# salen de digitalizar M5.3.png; nhgri-genoma.dat sale de nhgri-costes.csv.
# calculos.py recalcula todas las tasas que cita el texto.

.PHONY: pdf check clean calculos

pdf: main.pdf

main.pdf: main.tex referencias.bib $(wildcard datos/*.dat)
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	biber main
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex

calculos:
	python3 calculos.py

check:
	@if [ -f main.log ]; then \
	  if grep -E 'Warning|undefined|Overfull|Underfull|Error' main.log; then \
	    echo "la composición dejó avisos"; exit 1; \
	  else echo "composición sin avisos"; fi; \
	else echo "sin main.log: ejecuta make clean pdf para comprobar los avisos"; fi
	@pdfinfo main.pdf | grep -E '^(Pages|Page size|File size)'

clean:
	rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml main.toc
