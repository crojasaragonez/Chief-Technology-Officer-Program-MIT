# Actividad 4.1. Teach-back: ingeniería de prompts. Diapositivas.
#
#   make pdf       compone diapositivas.pdf y diapositivas-con-notas.pdf
#   make png       exporta cada diapositiva a PNG (para revisarlas)
#   make check     verifica avisos, rayas (U+2014 o tres guiones) y páginas
#   make clean     borra los intermedios (los PDF NO se borran)

.PHONY: pdf png check clean

LUALATEX = lualatex -interaction=nonstopmode -halt-on-error

pdf: diapositivas.pdf diapositivas-con-notas.pdf

diapositivas.pdf: diapositivas.tex
	$(LUALATEX) diapositivas.tex
	$(LUALATEX) diapositivas.tex

# El mismo fuente, con las notas debajo de cada diapositiva.
diapositivas-con-notas.pdf: diapositivas.tex
	$(LUALATEX) -jobname=diapositivas-con-notas '\def\connotas{1}\input{diapositivas.tex}'
	$(LUALATEX) -jobname=diapositivas-con-notas '\def\connotas{1}\input{diapositivas.tex}'

png: diapositivas.pdf
	mkdir -p png
	pdftoppm -r 120 -png diapositivas.pdf png/diapositiva

check:
	@if grep -n -e "$$(printf '\342\200\224')" -e '-\{3\}' diapositivas.tex; then echo "hay rayas"; else echo "sin rayas"; fi
	@if grep -E 'Warning|undefined|Overfull|Error' diapositivas.log diapositivas-con-notas.log; then \
	  echo "la composición dejó avisos"; else echo "composición sin avisos"; fi
	@pdfinfo diapositivas.pdf | grep -E '^(Pages|Page size)'
	@pdfinfo diapositivas-con-notas.pdf | grep -E '^(Pages|Page size)'

clean:
	rm -f *.aux *.log *.out *.toc *.nav *.snm *.vrb
	rm -rf png
