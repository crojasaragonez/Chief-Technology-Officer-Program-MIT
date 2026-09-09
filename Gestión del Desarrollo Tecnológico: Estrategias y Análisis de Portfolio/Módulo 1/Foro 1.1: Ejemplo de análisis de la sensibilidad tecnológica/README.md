# Foro 1.1: Ejemplo de análisis de la sensibilidad tecnológica

Análisis de **GraphQL** como posible alternativa a REST, leído sobre la
genealogía completa de la función «pedir datos a otra máquina»: RPC (1984),
CORBA y DCOM (1991 y 1996), SOAP y WS-\* (1998 y 2003), REST y JSON (2000 y
2006) y GraphQL (2012 y 2015).

Responde a las tres preguntas del planteamiento: de qué tecnología se trata,
cuánto tiempo transcurrió hasta que empezó a ser viable y qué restricciones
activas de su diseño limitan hoy el rendimiento del sistema.

## Tesis

**GraphQL llevó su figura de mérito original hasta el límite teórico en menos
de tres años, y desde entonces el problema que la justificaba se ha ido
disolviendo por otro lado: la red se hizo rápida.**

- La ventaja de GraphQL sobre REST, medida en **tiempo hasta la vista
  completa**, pasa de un **factor 13,5** en la red móvil de 2012 a un **factor
  1,03** entre dos servicios del mismo centro de datos. HTTP/2, que llegó en
  mayo de 2015, se llevó tres cuartas partes de esa ventaja el mismo año en que
  GraphQL se publicó.
- La figura de mérito principal **no distingue a GraphQL de un endpoint
  compuesto escrito a mano**: los dos dan 366 ms en el escenario de cálculo.
  Lo que los separa es la segunda figura de mérito, el esfuerzo por consulta
  nueva, donde el experimento controlado de Brito y Valente (2020) mide un 33
  por ciento menos de tiempo con GraphQL.
- **La restricción activa se mudó de la red al servidor.** En 2012 el 69 por
  ciento del tiempo eran viajes de ida y vuelta; entre servicios del mismo
  centro de datos el 99 por ciento es trabajo de servidor, es decir el modelo
  de ejecución campo a campo de GraphQL y su problema *N*+1 de resolvedores.
- **REST, gRPC y GraphQL están los tres sobre el frente de Pareto.** SOAP y el
  *backend for frontend* a medida están dominados. Por eso la pregunta «¿GraphQL
  sustituirá a REST?» está mal planteada: no se sustituye a un punto del frente,
  se elige otro punto.

## Figuras de mérito declaradas

La principal es el tiempo hasta la vista completa,
*T* = *n* · RTT + *B*/*v* + *T*<sub>s</sub>, y sus tres componentes que un
diseño puede mover: *n* (viajes por vista, mínimo teórico 1), η (eficiencia de
carga útil, máximo teórico 1) y *E* (esfuerzo de desarrollo por consulta
nueva, la única que no depende de la red).

## Contenido gráfico

Las cuatro figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: cinco curvas S para la misma función, 1980 a 2032, una por
  carril y cada una normalizada al techo de *su propia* figura de mérito, con el
  año de saturación, la restricción que la detuvo y las flechas de relevo.
- **Figura 2**: cuánto tardó en ser viable. Panel A, cronología con los hitos
  documentados y los cinco umbrales de viabilidad (meses, 3, 4, 7 y 12 años).
  Panel B, la curva S de difusión ajustada a las dos referencias de Gartner,
  con su punto de inflexión en 2026 y la línea de REST saturada en el 93 por
  ciento.
- **Figura 3**: el análisis de sensibilidad, que es la pieza central. Panel A,
  descomposición del tiempo en la red de 2012 para cuatro arquitecturas. Panel
  B, la ventaja de GraphQL frente a REST en cinco entornos de red, de 200 ms de
  RTT a 0,5 ms, en escala logarítmica.
- **Figura 4**: restricciones activas. Panel A, el problema *N*+1 de
  resolvedores frente al tamaño de la lista, con y sin DataLoader. Panel B, el
  frente de Pareto entre eficiencia de carga útil y coste de servidor y de
  gobernanza, con las cinco arquitecturas situadas.

## Cuadros

1. Las cinco generaciones: origen, figura de mérito dominante, restricción que
   la detuvo y qué la relevó.
2. El escenario de cálculo (pantalla de muro con 20 publicaciones, autores y
   comentarios): bytes, eficiencia de carga útil, peticiones y viajes.
3. Las cinco restricciones activas de GraphQL, ordenadas por cuánto limitan hoy
   la figura de mérito, con su mitigación y el coste de esa mitigación.

## Cómo se construye

```
make pdf     # main.pdf con LuaLaTeX y Biber
make html    # regenera figuras/*.png desde main.tex y produce el HTML final
make check   # verifica que no hay avisos y que el HTML tiene todas las figuras
make all     # pdf + html
make clean   # borra los intermedios
```

El entregable para el foro es **`foro-1.1-tinymce.html`**: se abre en el
navegador, se selecciona todo, se copia y se pega en el editor WYSIWYG. Lleva
las cuatro imágenes incrustadas en base64, de modo que no depende de ningún
fichero externo.

`foro-1.1.html` es el maestro editable a mano; `exportar-figuras.py` extrae los
entornos `tikzpicture` de `main.tex`, **junto con los colores y las macros de
figura del propio preámbulo**, los compila con la clase `standalone`, los
convierte a PNG y sustituye las referencias `figuras/figura-N.png` por los datos
en base64. Como el preámbulo de las figuras no se duplica en el script sino que
se lee de `main.tex`, las imágenes del HTML no pueden desincronizarse del
informe ni por el contenido ni por el estilo.

## Sobre las fuentes

Todo verificado el 9 de septiembre de 2026:

- **Genealogía**: Birrell y Nelson (1984) para RPC, Wikipedia para CORBA, DCOM
  y XML-RPC, la recomendación del W3C de junio de 2003 para SOAP 1.2, la tesis
  de Fielding (2000) para REST, la RFC 7540 para HTTP/2 y el blog de Google
  para gRPC.
- **Origen de GraphQL**: Postman para la reconstrucción de los años de
  Facebook, el anuncio de Meta Engineering del 14 de septiembre de 2015, el
  blog de GitHub para la API de septiembre de 2016, TechCrunch para la GraphQL
  Foundation de noviembre de 2018 y Apollo para la federación de mayo de 2019.
- **Evidencia empírica**: Brito, Mombach y Valente (2019) para la reducción del
  94 por ciento en campos y del 99 por ciento en bytes; Brito y Valente (2020)
  para el experimento controlado de esfuerzo (9 frente a 6 minutos de mediana,
  22 participantes); Seabra et al. (2019) para el comportamiento bajo carga.
- **Adopción**: las dos referencias de Gartner recogidas por IBM y por
  WunderGraph, y el informe de Postman de 2025 (REST 93 por ciento, GraphQL 33
  por ciento de desarrolladores).
- **Restricciones activas**: la documentación de DataLoader, el informe de
  Escape de 2024 (69 por ciento de 160 endpoints públicos con problemas de
  consumo de recursos no restringido), el coste calculado de consulta de
  Shopify y sus fechas de obsolescencia de la REST Admin API.

El escenario de cálculo del Cuadro 2, los tiempos de la Figura 3, las cinco
logísticas de la Figura 1 y el eje vertical del frente de Pareto son
elaboración propia, con el método declarado en cada pie de figura. El apartado
9 del documento recoge ocho limitaciones explícitas, entre ellas que el
escenario es sintético, que fijar el tiempo de servidor en 50 ms es una
simplificación fuerte, que la asíntota de la curva de difusión está supuesta
en 100 por falta de un dato que la acote, que los datos de Gartner y de Postman
no son comparables entre sí y que no he medido nada yo.
