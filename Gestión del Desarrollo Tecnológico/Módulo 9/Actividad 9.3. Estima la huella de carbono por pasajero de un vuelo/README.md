# Actividad 9.3: ¿Cuánto queroseno hace falta para volar de Boston a Los Ángeles?

Estimación del combustible de un vuelo de 5.000 km con la **ecuación de
alcance y resistencia de Bréguet**, comprobación de la estimación por cuatro
caminos independientes y respuesta razonada a la segunda pregunta del
enunciado: por qué el cálculo es complicado.

## La respuesta

Con los datos del enunciado (10 t de peso total, L/D = 15, eficiencia total
0,3, h = 42,8 MJ/kg):

| Magnitud | Valor |
|---|---|
| Parámetro adimensional `x = Rg/(η·h·L/D)` | 0,2547 |
| Razón de pesos `e^x` | 1,2900 |
| **Queroseno (10 t = peso al despegue)** | **2.248 kg** (2,25 t, 2.800 L) |
| Queroseno (10 t = peso sin combustible) | 2.900 kg |
| Queroseno con la forma lineal de la ecuación | 2.547 kg |
| Fracción del peso al despegue | 22,5 % |
| Energía química embarcada | 96,2 GJ |
| CO₂ emitido (factor 3,16 kg/kg) | 7,1 t |
| Duración del crucero (resistencia) | 4,63 h |
| Combustible que habría que embarcar de verdad | 2.847 kg |

## Los dos hallazgos que no estaban en el enunciado

1. **La velocidad y la densidad del aire no entran en la ecuación del alcance**
   (la velocidad se cancela al pasar de la resistencia al alcance y la densidad
   no aparece). Sirven para otra cosa: para comprobar si el enunciado describe
   un avión posible. Y **no lo describe**. A 300 m/s y 6.000 m el número de
   Mach es 0,948, la presión dinámica es 2,9 veces la de crucero de un reactor
   de línea, el coeficiente de sustentación cae a 0,123 y el `L/D` realmente
   alcanzable es **5,6 y no 15**. Con ese `L/D` el combustible sería de
   4.958 kg, el 50 por ciento del peso al despegue.
2. **Con las reservas normativas puestas el avión no llega.** El combustible de
   trayecto (2.248 kg) más ascenso, contingencia, alternativo, reserva final y
   rodaje suma 2.847 kg, y la capacidad de depósito del reactor de negocios
   real de masa equivalente (9.752 kg de MTOW) es de 2.750 kg. El vuelo
   Boston–Los Ángeles sin escalas queda fuera de alcance para un avión de
   10 toneladas incluso concediéndole el `L/D` imposible del enunciado.

## Por qué el cálculo es complicado

Diez razones, cada una con su magnitud medida en este problema, en la
sección 10 del documento. Las tres primeras por peso:

- **Los datos de entrada están acoplados por la física** y en este enunciado no
  cierran: +120 % sobre la respuesta si se corrige el `L/D`.
- **El combustible pesa y hay que transportarlo**, lo que hace el problema
  implícito y logarítmico en lugar de proporcional: cada kilogramo de carga
  extra obliga a embarcar 0,29 kg más de queroseno.
- **Las reservas normativas** añaden un 23 por ciento que no está en ninguna
  ecuación de la mecánica del vuelo.

La conclusión de fondo: la ecuación de Bréguet no es una herramienta de
cálculo, es una **herramienta de descomposición**. Separa el problema en cuatro
figuras de mérito independientes (η, h, L/D y la fracción estructural) y dice
cuánto vale mejorar cada una, que es exactamente para lo que se usa en una hoja
de ruta tecnológica.

## Contenido gráfico

Las cinco figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: la ecuación en dos vistas. Panel A, el equilibrio de fuerzas
  del que se deduce, con los valores de este problema. Panel B, los cuatro
  factores del segundo miembro y la disciplina de la que sale cada uno.
- **Figura 2**: la fracción de combustible frente al alcance, con la forma
  exacta y la lineal, el alcance característico `R* = 19.633 km`, el punto de
  operación y la banda de capacidad de depósito de un avión real.
- **Figura 3**: el examen de coherencia. Panel A, presión dinámica y `C_L` del
  enunciado frente a los de un reactor de línea. Panel B, el `L/D` supuesto,
  el alcanzable y el combustible que resulta de cada uno.
- **Figura 4**: la cascada del combustible, del crucero ideal de Bréguet al
  total que habría que embarcar, con la línea de capacidad del depósito.
- **Figura 5**: diagrama de tornado de la sensibilidad a cada dato de entrada.

## Cuadros

1. La respuesta en las cuatro formas en que puede pedirse.
2. Datos de partida, con la columna que declara qué dato entra en la ecuación.
3. Las cuatro comprobaciones independientes y su veredicto.
4. Examen de coherencia entre el enunciado y la aerodinámica.
5. Sensibilidad a cada dato de entrada.
6. La misma tonelada de queroseno repartida entre distintos pasajeros.
7. Las diez razones por las que el cálculo es complicado, ordenadas por efecto.
8. Respuesta a las dos preguntas del enunciado.

## Cómo se construye

```
make pdf     # main.pdf con LuaLaTeX y Biber
make check   # verifica que la composición no dejó avisos
make clean   # borra los intermedios
```

## Sobre las fuentes

- **La ecuación**: la derivación sigue las notas de Unified Engineering del MIT
  (Waitz, 2008) y Torenbeek & Wittenberg (2009). La forma lineal y el dato de
  la densidad energética son de Tennekes (2009), que es la fuente de la
  sección 3 del módulo. La atribución histórica va a Coffin (1920), NACA
  Report 69, anterior a Bréguet.
- **Combustible**: poder calorífico inferior y densidad del Jet A-1 de Chevron
  (2007); factor de emisión de 3,16 kg de CO₂ por kilogramo de queroseno de la
  metodología de la calculadora de la OACI.
- **Aerodinámica**: coeficiente de arrastre parásito de Anderson (1999) y
  Raymer (2018); atmósfera estándar de ISO 2533:1975.
- **Reservas**: política de combustible del Reglamento (UE) 965/2012.
- **Avión de referencia**: Learjet 70/75, 9.752 kg de MTOW, 2.750 kg de
  combustible y 3.797 km de alcance, según Wikipedia y la guía de aeronaves de
  la AOPA.
- **Efecto climático no CO₂**: Lee et al. (2021).

Todos los cálculos (parámetro adimensional, razón de pesos, combustible,
comprobaciones energéticas, número de Mach, presión dinámica, `L/D` alcanzable,
cascada de reservas, sensibilidad, distancia de círculo máximo Boston–Los
Ángeles y huella por pasajero) son propios y están detallados paso a paso en el
documento.

La sección 12 recoge diez limitaciones explícitas, entre ellas que el `L/D`
alcanzable de 5,6 depende de dos supuestos declarados, que no se ha modelado
la divergencia de arrastre transónica (de modo que 5,6 es todavía optimista),
que el incremento por ascenso es un mínimo termodinámico y no una estimación
operativa, y que el multiplicador de tres para el efecto climático no CO₂ es
indicativo y no cuantitativo para un vuelo concreto.
