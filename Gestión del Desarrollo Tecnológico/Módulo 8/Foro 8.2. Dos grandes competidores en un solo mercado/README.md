# Foro 8.2: Anthropic y OpenAI, dos grandes competidores en un solo mercado

Respuesta al enunciado del foro (elegir un sector condicionado por el desarrollo
tecnológico de dos grandes competidores, clasificarlos según las categorías del
módulo, dibujar una gráfica vectorial y explicar cómo se reparten el mercado)
con datos verificados al **1 de septiembre de 2026**, fecha en la que Anthropic
publicó Claude Fable 5.1 y Mythos 5.1.

La comparación cubre las cuatro dimensiones pedidas: **benchmarks públicos,
innovación, precios y equipo técnico**. No busca un ganador: con los datos
disponibles ninguna de las dos compañías domina a la otra, y la frontera de
eficiencia del gráfico vectorial tiene cuatro puntos repartidos dos a dos.

## Tesis

**No se reparten un mercado, se reparten dos.** Anthropic tiene el 40 por ciento
del gasto empresarial en interfaces de programación de modelos y el 54 por
ciento de la codificación; OpenAI tiene el 46,4 por ciento de la audiencia de
asistentes de consumo. Ese reparto no es casualidad: está inscrito en las dos
arquitecturas de precio.

- **Anthropic** cobra la ventana de un millón de tokens a tarifa plana y ha
  llevado la lectura de caché al 2,5 por ciento de la tarifa de entrada, lo que
  la hace más barata en sesiones de agente largas.
- **OpenAI** aplica un tramo de precio por encima de los 272.000 tokens, lo que
  la hace más barata en interacciones cortas y de alto volumen.
- El **ranking de precio cambia de signo** según el perfil de uso: en el perfil
  de agente, Claude Opus 5 cuesta un 29 por ciento menos que GPT-5.6 Sol; en el
  perfil de conversación, un 26 por ciento más.
- La cadencia de lanzamiento es casi idéntica (nueve frente a siete eventos en
  ocho meses). **La diferencia no está en el ritmo, está en la dirección**:
  ofensiva de profundidad y estándar abierto (MCP) frente a ofensiva de
  amplitud y propiedad del canal (aplicación, navegador, publicidad, comercio y
  dispositivo).

## Contenido gráfico

Las cinco figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: origen común y separación de trayectorias. Panel A, cronología
  2021 a 2026 en dos pistas. Panel B, cadencia de lanzamiento de modelos entre
  enero y septiembre de 2026, que es el indicador de innovación más limpio del
  trabajo.
- **Figura 2**: tres evaluaciones públicas con tres resultados distintos. Panel
  A, Artificial Analysis Intelligence Index. Panel B, ARC-AGI-3. Panel C,
  Terminal-Bench 2.1 con la escala ampliada.
- **Figura 3**: precios. Panel A, tarifas oficiales por millón de tokens. Panel
  B, coste calculado de una tarea tipo en dos perfiles de uso, que es donde se
  ve que no hay un proveedor barato y otro caro.
- **Figura 4**: **el gráfico vectorial**, la pieza central. Origen en el
  producto de referencia del 28 de mayo de 2026, siete vectores fechados y una
  frontera de eficiencia de cuatro puntos con dos puntos dominados.
- **Figura 5**: reparto del mercado. Panel A, cuota por segmento. Panel B, tres
  razones de monetización, incluida la de ingreso por punto de cuota de
  audiencia de consumo (7,3 a 1 a favor de Anthropic).

## Cuadros

1. Clasificación de los dos jugadores según cuatro juegos de categorías
   (Freeman y Soete, de Weck, Teece, Shapiro y Varian).
2. Construcción de las dos coordenadas y de los siete vectores tecnológicos.
3. Ficha comparativa a 1 de septiembre de 2026.

## Cómo se construye

```
make pdf     # main.pdf con LuaLaTeX y Biber
make html    # regenera figuras/*.png desde main.tex y produce el HTML final
make check   # verifica que no hay avisos y que el HTML tiene todas las figuras
make all     # pdf + html
make clean   # borra los intermedios
```

El entregable para el foro es **`foro-8.2-tinymce.html`**: se abre en el
navegador, se selecciona todo, se copia y se pega en el editor WYSIWYG. Lleva
las cinco imágenes incrustadas en base64, de modo que no depende de ningún
fichero externo.

`foro-8.2.html` es el maestro editable a mano; `exportar-figuras.py` extrae los
entornos `tikzpicture` de `main.tex`, los compila con la clase `standalone`, los
convierte a PNG y sustituye las referencias `figuras/figura-N.png` por los datos
en base64. **Las imágenes del HTML no pueden desincronizarse del informe**
porque se regeneran siempre desde `main.tex`.

## Sobre las fuentes

Se ha priorizado la evaluación independiente sobre la declarada por el
fabricante:

- **Capacidad**: Artificial Analysis (índice compuesto de veinticuatro
  evaluaciones), ARC Prize Foundation y BenchLM. Solo Terminal-Bench 2.1 procede
  de los datos de lanzamiento de cada proveedor, y así se indica.
- **Precios**: las páginas oficiales de tarifas de las dos compañías. Los costes
  por tarea son cálculo propio a partir de ellas, con los dos perfiles
  publicados en el texto para que el lector pueda rehacerlos.
- **Mercado**: encuesta de Menlo Ventures a 495 responsables de decisión
  (diciembre de 2025) y Sensor Tower (mayo de 2026).
- **Ingresos y talento**: TechCrunch, Bloomberg, The Next Web, CNBC y SignalFire.

La sección 10 del documento recoge nueve limitaciones explícitas, entre ellas
que el resultado del gráfico vectorial depende del perfil de tarea elegido, que
los costes están calculados en tokens y no en trabajo, que las versiones del
índice compuesto no son comparables entre sí y que el mercado tiene un tercer
jugador (Google) que el enunciado no contempla.
