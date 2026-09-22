# Actividad 3.1: Cálculo del RSSI de un ordenador portátil

Medición de la potencia recibida de un portátil a cuatro distancias del rúter
doméstico, con `iw` sobre `nl80211`, y ajuste de un modelo de pérdida
logarítmica con la distancia.

## Resultado

De **&minus;41 dBm** pegado al rúter a **&minus;67 dBm** a diez metros: 26 dB,
es decir un factor de **398** en potencia recibida (de 79,4 a 0,20 nanovatios).

| Distancia | Señal | Potencia | Δ frente a 0 m |
|---|---|---|---|
| 0 m | −41 dBm | 79,4 nW | 0 dB |
| 3 m | −59 dBm | 1,26 nW | −18 dB |
| 6 m | −65 dBm | 0,32 nW | −24 dB |
| 10 m | −67 dBm | 0,20 nW | −26 dB |

Ajustando `P(d) = A − 10 n log10(d)` sobre los tres puntos con `d > 0`:

```
P(d) = −51,96 − 15,57 log10(d)    ->    n = 1,56    R² = 0,963    RMSE = 0,65 dB
```

Tres lecturas del ajuste, que son el contenido del documento:

- **El exponente sale por debajo de 2**, el valor del espacio libre: entre 3 y
  10 metros se observaron 8 dB de caída frente a los 10,5 dB que predice la
  propagación libre. Es el efecto de la propagación guiada en interiores, con
  las réplicas reflejadas sumándose en fase con la señal directa.
- **El punto de 0 metros queda fuera del modelo**, y con razón: los 18 dB entre
  esa posición y los 3 metros corresponden, en propagación libre, a una
  separación real de antenas de unos 0,4 metros. «0 metros» era *al lado* del
  rúter, no en su antena.
- **El rendimiento decreciente es inmediato**: los primeros tres metros se
  llevan el 69 por ciento de toda la pérdida de la serie.

## Por qué `iw` y no otra herramienta

El criterio fue la longitud de la cadena de medida y la unidad que devuelve.
`iw` lee el campo `signal` en dBm directamente del controlador a través de
`nl80211`; `nmcli` da un porcentaje de 0 a 100 definido por NetworkManager,
`iwconfig` se apoya en las Wireless Extensions obsoletas y `wavemon` es una
capa de presentación sobre las mismas llamadas de `iw`. Anotar porcentajes
habría hecho imposible el apartado 6 del documento: sin dBm no hay conversión
a nanovatios, ni ajuste del exponente, ni comparación con el espacio libre.

## Ficheros

| Fichero | Qué es |
|---|---|
| `actividad-3.1.html` | el documento maestro, editable a mano; referencia las imágenes por ruta |
| `actividad-3.1-tinymce.html` | **el entregable**: el mismo documento con las dos imágenes en base64. Se abre en el navegador, se selecciona todo, se copia y se pega en el editor de la plataforma |
| `muestras.csv` | las cuatro medidas, fuente de verdad del gráfico y del ajuste |
| `output.png` | captura de la salida de `iw dev wlp194s0 link` (Figura 1) |
| `grafico.py` | genera `figuras/grafico.svg` y `.png` desde el CSV, e imprime el ajuste |
| `incrustar-figuras.py` | produce el entregable autocontenido desde el maestro |
| `contexto.txt` | el planteamiento de la actividad, tal como lo publica la plataforma |

## Cómo se construye

```
make figura   # regenera el gráfico desde muestras.csv y muestra el ajuste
make html     # entregable con las imágenes incrustadas
make pdf      # vista.pdf para revisar la paginación
make check    # comprueba que el entregable no depende de ficheros externos
make clean    # borra lo generado
```

El gráfico se deriva de `muestras.csv` y no de números copiados en el guion, de
modo que corregir una muestra y ejecutar `make` rehace la figura y vuelve a
imprimir el ajuste. Las cifras del apartado 6 del documento son exactamente lo
que escribe `make figura` por pantalla.

## Límites declarados en el documento

Una sola lectura por posición (sin repeticiones no hay estimación de la
dispersión, y el desvanecimiento multitrayecto mueve varios decibelios en el
mismo sitio); tres puntos para ajustar dos parámetros, con cuantificación de
1 dB, lo que deja el intervalo de confianza de `n` demasiado ancho para
afirmar que el valor real está por debajo de 2; el parámetro `A` no es un
balance de enlace y no debe compararse con la potencia nominal del punto de
acceso; las distancias de 14 y 30 metros para los umbrales de &minus;70 y
&minus;75 dBm son extrapolaciones fuera del intervalo medido; y no se midió el
nivel de ruido, de modo que no hay relación señal a ruido.
