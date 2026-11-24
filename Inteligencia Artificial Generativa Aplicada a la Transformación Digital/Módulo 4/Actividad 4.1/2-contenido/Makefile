# Actividad 4.1. Teach-back: ingeniería de prompts.
#
#   make pdf       compone main.pdf con LuaLaTeX
#   make palabras  cuenta las palabras de cada sección (la nota va de 100 a 150)
#   make check     verifica avisos, rayas y páginas
#   make clean     borra los intermedios (main.pdf NO se borra)

.PHONY: pdf palabras check clean

pdf: main.pdf

main.pdf: main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex
	lualatex -interaction=nonstopmode -halt-on-error main.tex

# Sección 1 (nota de contextualización): 100 a 150 palabras.
palabras:
	@texcount -sub=section -utf8 main.tex | grep -E 'Section|Words in text'

check:
	@if grep -n -e '—' -e '---' main.tex; then echo "hay rayas"; else echo "sin rayas"; fi
	@if grep -E 'Warning|undefined|Overfull|Error' main.log; then \
	  echo "la composición dejó avisos"; else echo "composición sin avisos"; fi
	@pdfinfo main.pdf | grep -E '^(Pages|File size)'

clean:
	rm -f main.aux main.log main.out main.toc
