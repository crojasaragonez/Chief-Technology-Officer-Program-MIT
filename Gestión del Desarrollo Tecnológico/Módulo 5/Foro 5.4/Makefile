.PHONY: pdf check clean

pdf:
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	biber main
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex

check:
	@! grep -E 'Warning|undefined|Overfull|Underfull|Error' main.log
	@pdfinfo main.pdf | grep -E '^(Pages|Page size|File size)'

clean:
	rm -f main.aux main.bbl main.bcf main.blg main.log main.out main.run.xml
