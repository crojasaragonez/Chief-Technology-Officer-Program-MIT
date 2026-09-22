# Actividad 3.1. Medición del RSSI de un ordenador portátil con iw.
#
#   make figura  regenera figuras/grafico.svg y .png desde muestras.csv, y
#                escribe por pantalla el ajuste del modelo log-distancia
#   make html    figura + actividad-3.1-tinymce.html con las imágenes
#                incrustadas en base64, listo para pegar en el editor de la
#                plataforma
#   make pdf     compone vista.pdf desde el HTML maestro con Chrome headless
#   make check   verifica que el entregable no depende de ficheros externos
#   make clean   borra lo generado (el HTML maestro NO se borra)

MAESTRO  = actividad-3.1.html
FINAL    = actividad-3.1-tinymce.html
DATOS    = muestras.csv
FIGURAS  = figuras
PDF      = vista.pdf

.PHONY: all figura html pdf check clean

all: html

figura: $(FIGURAS)/grafico.png

# La figura se deriva del CSV, de modo que no puede desincronizarse de las
# medidas: cambiar una muestra y ejecutar make basta para rehacer el gráfico.
$(FIGURAS)/grafico.png: $(DATOS) grafico.py
	python3 grafico.py

html: $(FINAL)

$(FINAL): $(MAESTRO) $(FIGURAS)/grafico.png output.png incrustar-figuras.py
	python3 incrustar-figuras.py

pdf: $(PDF)

$(PDF): $(MAESTRO) $(FIGURAS)/grafico.png output.png
	google-chrome --headless=new --disable-gpu --no-pdf-header-footer \
	  --print-to-pdf=$(PDF) $(MAESTRO)

check:
	@test -f $(FINAL) || { echo "falta $(FINAL): ejecuta make html"; exit 1; }
	@echo "$(FINAL): $$(du -h $(FINAL) | cut -f1), \
$$(grep -c 'base64' $(FINAL)) imágenes incrustadas"
	@grep -q 'src="[^d]' $(FINAL) \
	  && { echo "el entregable aún referencia ficheros externos"; exit 1; } \
	  || echo "entregable autocontenido: ninguna imagen por ruta"
	@test $$(grep -c 'base64' $(FINAL)) -eq \
	  $$(grep -c '<img ' $(MAESTRO)) \
	  || { echo "faltan imágenes por incrustar"; exit 1; }

clean:
	rm -f $(FINAL) $(PDF) $(FIGURAS)/grafico.svg $(FIGURAS)/grafico.png
