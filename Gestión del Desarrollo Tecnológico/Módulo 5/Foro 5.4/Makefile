.PHONY: pdf html check clean

pdf:
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	biber main
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex

# Regenera las figuras desde main.tex y produce el HTML para pegar en TinyMCE.
html:
	python3 exportar-figuras.py

check:
	@! grep -E 'Warning|undefined|Overfull|Underfull|Error' main.log
	@pdfinfo main.pdf | grep -E '^(Pages|Page size|File size)'

clean:
	rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml
	rm -f figuras.aux figuras.log figuras.pdf figuras.tex
