# Actividad 9.3. Estima la huella de carbono por pasajero de un vuelo
#
#   make pdf    compone main.pdf con LuaLaTeX y Biber
#   make check  verifica que la composición no dejó avisos y resume la salida
#   make all    las dos anteriores
#   make clean  borra los intermedios (main.pdf NO se borra)

FUENTE = main.tex
PDF    = main.pdf

.PHONY: all pdf check clean

all: pdf

pdf: $(PDF)

$(PDF): $(FUENTE) referencias.bib
	lualatex -interaction=nonstopmode -halt-on-error $(FUENTE)
	biber main
	lualatex -interaction=nonstopmode -halt-on-error $(FUENTE)
	lualatex -interaction=nonstopmode -halt-on-error $(FUENTE)

check:
	@if [ -f main.log ]; then \
	  if grep -E 'Warning|undefined|Overfull|Underfull|Error' main.log; then \
	    echo "la composición dejó avisos"; exit 1; \
	  else echo "composición sin avisos"; fi; \
	else echo "sin main.log: ejecuta make clean pdf para comprobar los avisos"; fi
	@pdfinfo $(PDF) | grep -E '^(Pages|Page size|File size)'

clean:
	rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml \
	      main.toc
