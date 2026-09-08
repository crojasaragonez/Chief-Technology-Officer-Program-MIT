# Foro 9.2: Su experiencia volando

Respuesta a las seis preguntas del foro sobre la experiencia personal de volar,
contestadas como lo que son (personales) y leídas después con el instrumento
del módulo 9: la **figura de mérito**, la medida cuantitativa del desempeño de
una tecnología en la función que presta, independiente de la implementación
(de Weck, 2022).

## Tesis

**En tres de las seis respuestas la figura de mérito que yo tenía en la cabeza
no era la que de verdad me importa.** Declararla bien cambia la respuesta:

- Pedí **velocidad** cuando lo que me molesta es el **tiempo sentado**. No es lo
  mismo, y el cálculo lo demuestra: duplicar la velocidad de crucero reduce el
  viaje San José–Los Ángeles un 24 por ciento, no un 50, porque cuatro horas y
  media del viaje están en tierra y son indiferentes a la velocidad. Es la ley
  de Amdahl aplicada a un viaje. Pero Mach 1,7 sí baja el tiempo en cabina de
  5,5 a 3,1 horas, que es exactamente lo que yo quería.
- Llamé **«mejores»** a dos aeropuertos midiendo dos cosas distintas sin darme
  cuenta: Atlanta por tránsito, Panamá por conectividad de red. Cuatro figuras
  de mérito legítimas producen cuatro podios sin un nombre en común.
- Llamé **preferencia** a lo que era topología de red: los dos destinos que más
  frecuento son, exactamente, los dos que tienen vuelo directo desde San José.

Y un resultado que obliga a matizar mi propia postura sobre la vergüenza de
volar: **seis vuelos de trabajo pesan entre 1,4 y 1,9 veces lo que emite un
costarricense medio en un año entero**. La decisión no cambia; el argumento de
que la contribución es despreciable, sí.

## Contenido gráfico

Las cuatro figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: la figura de mérito que se saturó. Panel A, velocidad de
  crucero de 1936 a 2030, con la meseta desde 1958 (0,7 por ciento de mejora en
  sesenta y ocho años), el Concorde como único punto que la rompió y el
  Overture como intento de volver. Panel B, la figura de mérito a la que se
  desvió el esfuerzo: energía por pasajero-kilómetro, un factor de cuatro en el
  mismo periodo.
- **Figura 2**: el viaje San José–Los Ángeles descompuesto de puerta a puerta
  en cuatro escenarios de velocidad. Es la pieza central: enseña que la
  fracción en tierra gobierna el total.
- **Figura 3**: la aritmética de la huella. Panel A, mis seis tramos frente a
  la media anual costarricense y la mundial. Panel B, eficiencia (−2 por ciento
  anual) contra tráfico (+3,6 por ciento anual) y la línea de emisiones que
  resulta del producto.
- **Figura 4**: mi red de vuelos desde San José, que explica por sí sola cuáles
  son mis tres aeropuertos.

## Cuadros

1. Las seis preguntas, mi respuesta y la figura de mérito implícita en cada una.
2. Mis rutas habituales: distancia de círculo máximo, tiempo de bloque y
   emisiones por tramo.
3. Cuatro figuras de mérito de aeropuerto, cuatro podios distintos.

## Cómo se construye

```
make pdf     # main.pdf con LuaLaTeX y Biber
make html    # regenera figuras/*.png desde main.tex y produce el HTML final
make check   # verifica que no hay avisos y que el HTML tiene todas las figuras
make all     # pdf + html
make clean   # borra los intermedios
```

El entregable para el foro es **`foro-9.2-tinymce.html`**: se abre en el
navegador, se selecciona todo, se copia y se pega en el editor WYSIWYG. Lleva
las cuatro imágenes incrustadas en base64, de modo que no depende de ningún
fichero externo.

`foro-9.2.html` es el maestro editable a mano; `exportar-figuras.py` extrae los
entornos `tikzpicture` de `main.tex`, **junto con los colores y las macros de
figura del propio preámbulo**, los compila con la clase `standalone`, los
convierte a PNG y sustituye las referencias `figuras/figura-N.png` por los datos
en base64. Como el preámbulo de las figuras no se duplica en el script sino que
se lee de `main.tex`, las imágenes del HTML no pueden desincronizarse del
informe ni por el contenido ni por el estilo.

## Sobre las fuentes

Los datos personales (seis vuelos, rutas, umbral de cinco horas, aeropuertos)
son míos. Todo lo demás está verificado el 7 de septiembre de 2026:

- **Aeropuertos**: Airports Council International para tránsito y movimientos de
  2025, la ciudad de Chicago para el dato de O'Hare, Skytrax para el ranking de
  experiencia de 2026, Copa Airlines para la conectividad de Tocumen y AERIS
  para las cifras de Juan Santamaría.
- **Clima**: Lee et al. (2021) para el forzamiento radiativo y el reparto entre
  efectos CO₂ y no CO₂, Our World in Data para la cuota de la aviación y para
  la emisión per cápita de Costa Rica, y los factores de conversión oficiales
  británicos (DESNZ, 2025) para las emisiones por pasajero-kilómetro.
- **Supersónico**: Boom Supersonic para el vuelo del XB-1 del 28 de enero de
  2025 y la NASA para el primer vuelo del X-59 (28 de octubre de 2025) y su
  primer vuelo supersónico (5 de junio de 2026).
- **Eficiencia**: IATA y Peeters et al. (2005) para la tasa de mejora anual.

Las distancias, los tiempos de bloque, las emisiones por tramo y las dos curvas
construidas (el índice de energía del Panel B de la Figura 1 y las tres series
del Panel B de la Figura 3) son cálculo propio, con el método declarado en cada
pie de figura.

La sección 9 del documento recoge ocho limitaciones explícitas, entre ellas que
no llevo registro de itinerarios (de ahí que la huella se dé como rango y no
como cifra), que las distancias son de círculo máximo, que los tiempos en
tierra son mis hábitos y no un promedio, que los rankings de aeropuertos no son
comparables entre sí y que no conozco Changi, que incluyo por el ranking y
declaro como tal.
