# Foro 3.2: curvas S, progreso exponencial y la Red del Espacio Profundo

Respuesta al planteamiento del foro, que presenta **cuatro afirmaciones sobre
cómo progresan las tecnologías** y pide decidir cuáles son verdaderas y por
qué, además de exponer un caso tecnológico distinto que haya evolucionado con
el tiempo.

Las cuatro afirmaciones se evalúan **midiendo**, no opinando: sobre la
capacidad normalizada de la Red del Espacio Profundo que la JPL publica, y
sobre la velocidad de acceso doméstico a internet entre 1984 y 2026, que es el
caso distinto que aporto.

## Tesis

**Las cuatro afirmaciones son la misma curva mirada a tres alturas distintas**,
y cada una es verdadera a una altura y falsa a las otras.

- **Afirmación 1** (todo satura; el progreso exponencial no existe): cierta la
  premisa, falsa la conclusión. Las asíntotas de la DSN no se conjeturan, se
  **demuestran**: en 1995 la codificación ya había consumido el **80 por ciento**
  de toda la ganancia que el teorema de Shannon permitirá jamás. Pero la
  función ganó **20,8 órdenes de magnitud en 64 años**.
- **Afirmación 2** (tasa decreciente por ingreso marginal decreciente): cierta
  para esta envolvente y falsa como ley. La tasa de la DSN cae de **0,889 a
  0,076 a 0,007 a 0,121 décadas al año**, con una **meseta plana de doce años
  entre 1993 y 2005**. Pero el mecanismo que actúa no es un rendimiento
  marginal genérico: son asíntotas con nombre más una decisión de capital
  aplazada.
- **Afirmación 3** (tasa constante por alternancia de curvas S): **la más útil
  de las cuatro**. El gráfico de la JPL literalmente la dibuja (banda S, banda
  X, banda Ka, óptico). Pero la alternancia *sostiene* el progreso, no
  garantiza la tasa: **el hueco entre curvas es tan parte del fenómeno como el
  salto**.
- **Afirmación 4** (tasa creciente por las capacidades humanas): no la sostiene
  ningún tramo realizado. El único tramo acelerado del gráfico es el que aún no
  ha ocurrido, y Bloom et al. (2020) miden lo contrario: sostener la ley de
  Moore exige hoy **18 veces más investigadores** que en 1971.

El caso de contraste da la respuesta opuesta con la misma unidad de medida: el
acceso doméstico a internet sostuvo **0,179 décadas al año durante 42 años**
(un 51 por ciento anual, la ley de Nielsen) atravesando tres medios físicos.
Por eso las afirmaciones 2 y 4 no son leyes sino mediciones que hay que
repetir para cada tecnología.

## Los números que sostienen el documento

| Serie | Recorrido | Tasa | Comportamiento |
| --- | --- | --- | --- |
| Red del Espacio Profundo, 1958-2022 | 20,78 décadas | 0,889 → 0,076 → 0,007 → 0,121 déc./año | decelera |
| Acceso a internet, 1984-2026 | 7,52 décadas | 0,162 → 0,177 → 0,127 déc./año | constante |
| Cómputo de entrenamiento en IA | Sevilla et al. (2022) | 0,170 → 0,634 déc./año | acelera |

Las cuatro asíntotas de la DSN, con la fracción ya gastada:

| Palanca | Límite físico | Gastado |
| --- | --- | --- |
| Codificación | teorema de Shannon, *E*<sub>b</sub>/*N*<sub>0</sub> = −1,59 dB | 80,0 % |
| Temperatura de ruido | fondo cósmico de microondas, 2,725 K | 67,9 % |
| Apertura de un solo plato | deformación gravitatoria del reflector | ≈100 % |
| Banda de radio | absorción del vapor de agua sobre 32 GHz | ≈100 % |

El salto a óptico (32 GHz a 193 THz) abre **7,56 décadas teóricas**, más que
todo lo ganado en radiofrecuencia desde 1958. Esa es la razón física por la que
la afirmación 3 puede seguir cumpliéndose pese a la 1.

## Contenido gráfico

Las cuatro figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: la capacidad de la DSN de 1958 a 2033, redibujada del gráfico
  de escalones de la JPL, con un color por paradigma y la recta de tendencia de
  cada era. Panel B, la tasa era por era.
- **Figura 2**: Panel A, la ganancia ya extraída y la que queda hasta el límite
  físico en las cuatro palancas de tierra. Panel B, la escalera de frecuencia y
  por qué el siguiente peldaño no está en radiofrecuencia.
- **Figura 3**: el acceso doméstico a internet con la misma figura de mérito,
  la recta de la ley de Nielsen sin ajustar y el límite de Shannon del canal
  telefónico dibujado como asíntota. Panel B, la tasa por era.
- **Figura 4**: Panel A, las tres series en la misma unidad, deceleración,
  constancia y aceleración. Panel B, los tres niveles de agregación y qué
  afirmación es verdadera en cada uno.

## Cuadros

1. Las cuatro afirmaciones con su veredicto y su razón.
2. La envolvente de la DSN era por era, con décadas, pendiente y duplicación.
3. Las cuatro palancas de tierra, su asíntota y el margen restante.
4. La velocidad de acceso doméstico hito a hito, con lo que cerró cada
   paradigma.

## Cómo se construye

```
make pdf     # main.pdf con LuaLaTeX y Biber
make html    # regenera figuras/*.png desde main.tex y produce el HTML final
make check   # verifica que no hay avisos y que el HTML tiene todas las figuras
make all     # pdf + html
make clean   # borra los intermedios
```

El entregable para el foro es **`foro-3.2-tinymce.html`**: se abre en el
navegador, se selecciona todo, se copia y se pega en el editor WYSIWYG. Lleva
las cuatro imágenes incrustadas en base64, de modo que no depende de ningún
fichero externo.

`foro-3.2.html` es el maestro editable a mano; `exportar-figuras.py` extrae los
entornos `tikzpicture` de `main.tex`, **junto con los colores y las macros de
figura del propio preámbulo**, los compila con la clase `standalone`, los
convierte a PNG y sustituye las referencias `figuras/figura-N.png` por los datos
en base64. Como el preámbulo de las figuras no se duplica en el script sino que
se lee de `main.tex`, las imágenes del HTML no pueden desincronizarse del
informe ni por el contenido ni por el estilo.

## Sobre las cifras

El documento distingue tres clases de número y el apartado 11 recoge siete
limitaciones.

**Lecturas del gráfico** de la JPL (agosto de 2015), que es el dato primario de
todo el apartado 3. Son lecturas visuales de un eje logarítmico de 24 décadas,
con una tolerancia declarada de **±0,2 décadas** por punto: basta para las
pendientes y no basta para ningún escalón individual pequeño.

**Valores citados**: la temperatura de ruido operativa de 20,9 K y la relación
*E*<sub>b</sub>/*N*<sub>0</sub> de 0,65 dB de Galileo, de Layland y Rauch
(1997); los 2,725 K del fondo cósmico, de Fixsen (2009); las velocidades de
acceso, de las recomendaciones ITU-T V.34, V.90, G.992.1, G.992.5 y G.9807.1.

**Cálculos propios**: las fronteras entre eras, las pendientes en décadas al
año, las ganancias teóricas por cambio de banda, la capacidad de Shannon del
canal telefónico de voz y el reparto entre ganancia extraída y margen restante
del Cuadro 3.

**Marco conceptual**: de Weck (2022) para la disciplina de la figura de mérito
y los tres niveles de agregación; Foster (1986) y Sood y Tellis (2005) para la
alternancia de curvas S; Koh y Magee (2006), Farmer y Lafond (2016) y Nagy et
al. (2013) para los contraejemplos a la afirmación 2; Bloom et al. (2020) y
Sevilla et al. (2022) para la afirmación 4; Shannon (1948) para las dos
asíntotas demostrables del documento.

La entrevista al doctor Deutsch se cita de memoria, sin transcripción, y así
queda declarado en las limitaciones.
