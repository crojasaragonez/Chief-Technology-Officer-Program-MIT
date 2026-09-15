# Foro 2.1: Ejemplo de integración de una nueva tecnología en un sistema actual

Análisis de la integración de una **capa de agentes de inteligencia
artificial** en el proceso de planificación semanal de una empresa de
transporte de carga por carretera que opera en todo Estados Unidos con unos
400 choferes y sus equipos.

Responde al planteamiento del foro, que pide **definir un marco de trabajo y
un método para evaluar cuantitativamente el impacto de la adopción sobre la
arquitectura, actual o futura, del producto**, y responde también a las seis
preguntas de la plataforma (Cuadro 1 del documento).

## Tesis

**La tecnología no compró velocidad de cálculo: compró número de escenarios.**

- El proceso anterior producía **un solo escenario por ciclo** porque construir
  uno costaba 48 horas de persona. La capa de agentes produce **120 en 40
  minutos**. Eso convierte un proceso de satisfacción, en el sentido de Simon
  (1956), en uno de optimización muestreada.
- Con un modelo de estadísticos de orden calibrado sobre el único punto
  observado, **el escenario número veinte ya recoge el 73 por ciento del
  ahorro** y el número ciento veinte aporta 1,56 dólares al día. El óptimo
  económico está alrededor de 300 escenarios, no de 120.
- **El impacto arquitectónico fue deliberadamente nulo**: 6 interfaces nuevas
  (5 de lectura, 1 de escritura), 0 sistemas de registro modificados y 2 horas
  de tiempo de reversión. Esa reversibilidad, y no la calidad del modelo, es lo
  que hizo defendible la inversión.
- El resultado: **$1.282 de ahorro por día trabajado**. La empresa opera
  **260 días al año**, no 365, de modo que eso son **$333.216 anuales** brutos
  y **$298.416 netos**: repago en **6,1 meses** y **$147.000** de saldo
  acumulado al cierre del primer año. Pero el precio al cliente no bajó: el
  ahorro se quedó en el margen.

## El método en cinco pasos

1. Declarar la función y la figura de mérito **del proceso**, no de la
   tecnología.
2. Medir la línea base con el sistema actual.
3. Localizar la restricción activa.
4. Situar la tecnología en la arquitectura y medir su huella con tres métricas:
   superficie de integración *S*, profundidad de la intrusión *P* y tiempo de
   reversión *R*.
5. Calcular el impacto y su sensibilidad.

La figura de mérito del proceso es el coste del plan semanal,
*C*(*P*) = *c*<sub>m</sub>·*M*(*P*) + *T*(*P*) + *D*(*P*) + *L*, y el
rendimiento del escenario marginal se modela con
*a*(*N*) = σ·*E*[max{*Z*<sub>1</sub>…*Z*<sub>N</sub>}].

## Contenido gráfico

Las cuatro figuras están compuestas en TikZ dentro de `main.tex`, sin imágenes
externas:

- **Figura 1**: la arquitectura antes y después. Panel A, cinco exportaciones
  manuales, una hoja de cálculo y dos personas. Panel B, capa de integración de
  solo lectura, cuatro agentes, motor de escenarios y un único conector de
  escritura tras la revisión humana. Ninguna caja del Panel A cambia de forma.
- **Figura 2**: el dinero. Panel A, las cuatro partidas del ahorro por semana
  de operación de cinco días. Panel B, el reparto de los $100.000 de
  implantación.
- **Figura 3**: la pieza analítica. Panel A, el valor del escenario número *N*
  con su curva de coste y su óptimo económico. Panel B, el flujo de caja
  acumulado con la rampa de adopción y el punto de repago.
- **Figura 4**: la sensibilidad. Panel A, diagrama de tornado del repago con
  cinco supuestos. Panel B, las cuatro opciones de diseño situadas frente al
  retorno y al tiempo de reversión.

## Cuadros

1. El caso respondido en corto: las seis preguntas de la plataforma.
2. El método en cinco pasos, con lo que produce cada uno.
3. Las cuatro opciones de diseño consideradas, con su huella arquitectónica al
   lado del retorno.
4. Las restricciones activas después de la adopción.

## Cómo se construye

```
make pdf     # main.pdf con LuaLaTeX y Biber
make html    # regenera figuras/*.png desde main.tex y produce el HTML final
make check   # verifica que no hay avisos y que el HTML tiene todas las figuras
make all     # pdf + html
make clean   # borra los intermedios
```

El entregable para el foro es **`foro-2.1-tinymce.html`**: se abre en el
navegador, se selecciona todo, se copia y se pega en el editor WYSIWYG. Lleva
las cuatro imágenes incrustadas en base64, de modo que no depende de ningún
fichero externo.

`foro-2.1.html` es el maestro editable a mano; `exportar-figuras.py` extrae los
entornos `tikzpicture` de `main.tex`, **junto con los colores y las macros de
figura del propio preámbulo**, los compila con la clase `standalone`, los
convierte a PNG y sustituye las referencias `figuras/figura-N.png` por los datos
en base64. Como el preámbulo de las figuras no se duplica en el script sino que
se lee de `main.tex`, las imágenes del HTML no pueden desincronizarse del
informe ni por el contenido ni por el estilo.

## Sobre las cifras

El documento distingue explícitamente dos clases de número, y el apartado 10
recoge siete limitaciones. Toda cifra anual se obtiene multiplicando por **260
días de operación**, no por 365.

**Anclas** (experiencia directa en el proyecto): unos 400 choferes con equipo;
dos planificadores a tiempo completo; ciclo de planificación semanal; **260
días de operación al año**, cinco por semana; ahorro reportado de al menos
$1.000 por día trabajado; implantación en torno a $100.000; repago antes del
primer año; recurso habitual a terceros para cubrir cargas.

**Parámetros modelados** (elaboración propia): millas por chofer y semana,
porcentaje de millas en vacío, cargas por semana, sobrecoste de ceder una
carga, reparto del ahorro entre partidas, rampa de adopción, número de
escenarios por ciclo y la dispersión σ del coste de los planes.

**Costes unitarios del sector** (fuentes públicas, verificadas el 15 de
septiembre de 2026): el coste marginal de $2,336 por milla en 2025 del American
Transportation Research Institute; el 16,5 por ciento de millas en vacío
recogido por FreightWaves; el margen bruto del corretaje del 12 al 20 por
ciento según Anderson Trucking Service; las horas de servicio de la FMCSA; y el
estudio de detención de conductores del ATRI de 2024.

**Marco conceptual**: de Weck (2022) para la disciplina de la figura de mérito,
Simon (1956) para la satisfacción frente a la optimización, David y Nagaraja
(2003) para los estadísticos de orden y el informe del MIT Project NANDA (2025)
para el 95 por ciento de pilotos de inteligencia artificial sin retorno medible
y su atribución a la integración y no al modelo.
