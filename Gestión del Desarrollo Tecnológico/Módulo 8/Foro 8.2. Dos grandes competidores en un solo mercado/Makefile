# Foro 8.2. Anthropic y OpenAI: dos ofensivas tecnológicas sobre el mismo
# mercado.
#
#   make pdf    compone main.pdf con LuaLaTeX y Biber
#   make html   regenera figuras/*.png desde main.tex y produce el HTML con
#               las imágenes incrustadas en base64, listo para pegar en el
#               editor WYSIWYG del foro
#   make check  verifica que la composición no dejó avisos y resume las salidas
#   make all    las dos anteriores
#   make clean  borra los intermedios (main.pdf y el HTML final NO se borran)

FUENTE      = main.tex
PDF         = main.pdf
HTML_FUENTE = foro-8.2.html
HTML_FINAL  = foro-8.2-tinymce.html
FIGURAS     = figuras

.PHONY: all pdf html check clean

all: pdf html

pdf: $(PDF)

$(PDF): $(FUENTE) referencias.bib
	lualatex -interaction=nonstopmode -halt-on-error $(FUENTE)
	biber main
	lualatex -interaction=nonstopmode -halt-on-error $(FUENTE)
	lualatex -interaction=nonstopmode -halt-on-error $(FUENTE)

# Las figuras del HTML se extraen de los entornos tikzpicture de main.tex, de
# modo que no pueden desincronizarse del informe: se regeneran siempre desde
# la misma fuente.
html: $(HTML_FINAL)

$(HTML_FINAL): $(FUENTE) $(HTML_FUENTE) exportar-figuras.py
	python3 exportar-figuras.py

check:
	@if [ -f main.log ]; then \
	  if grep -E 'Warning|undefined|Overfull|Underfull|Error' main.log; then \
	    echo "la composición dejó avisos"; exit 1; \
	  else echo "composición sin avisos"; fi; \
	else echo "sin main.log: ejecuta make clean pdf para comprobar los avisos"; fi
	@pdfinfo $(PDF) | grep -E '^(Pages|Page size|File size)'
	@test -f $(HTML_FINAL) || { echo "falta $(HTML_FINAL): ejecuta make html"; exit 1; }
	@echo "$(HTML_FINAL): $$(du -h $(HTML_FINAL) | cut -f1), \
$$(grep -c 'data:image/png;base64' $(HTML_FINAL)) imágenes incrustadas"
	@test $$(grep -c 'data:image/png;base64' $(HTML_FINAL)) -eq \
	  $$(grep -c 'begin{tikzpicture}' $(FUENTE)) \
	  || { echo "el HTML y main.tex no tienen el mismo número de figuras"; exit 1; }

clean:
	rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml
	rm -f figuras.aux figuras.log figuras.pdf figuras.tex
