# Actividad 2.2: Ejemplo de adopción tecnológica

Análisis del **paso del Mac de los procesadores x86-64 de Intel al silicio
propio de arquitectura Arm**, del M1 (noviembre de 2020) al M5 (octubre de
2025), y de su impacto neto sobre el producto, sus consumidores, sus
competidores y el mercado.

Responde al planteamiento de la actividad, que pide exponer un ejemplo de
adopción tecnológica actual, seleccionar un producto que haya pasado por ese
proceso y describir su impacto neto con figuras de mérito cuantitativas.

## Tesis

**Lo que se adoptó no fue un procesador más rápido: fue la desaparición de la
interfaz de memoria del sistema.** El rendimiento por vatio es la
consecuencia, no la causa.

- Frente al Mac Intel al que sustituyó, el M1 multiplicó por **2,0** la
  puntuación multinúcleo y por **2,7** el rendimiento por vatio. El acumulado
  hasta el M5 es de **4,6**, y la trayectoria posterior crece al **16,5 % anual**,
  con duplicación cada 4,5 años.
- Aplicando la lógica de matriz delta del caso del módulo, esta adopción tocó
  en torno al **90 % de los elementos del sistema** (9 añadidos, 6 eliminados,
  14 modificados), frente al **8,5 %** del caso del sistema de impresión
  digital. Es innovación arquitectónica en el sentido de Henderson y Clark
  (1990).
- Para el comprador: mismo precio nominal de **999 dólares** durante cinco
  años, **84 % menos de coste por punto de rendimiento** y **50 % más de
  autonomía**, a cambio de perder memoria ampliable, GPU externa y arranque
  nativo de Windows.
- Para el sector: Intel integró la memoria en el paquete cuatro años después,
  Qualcomm entró en el PC con los arquitectos que habían diseñado esos núcleos
  y Microsoft redefinió su gama en torno a una figura de mérito (los TOPS de
  la unidad neuronal) que en 2020 no existía en la conversación del PC.

## Contenido gráfico

La figura está compuesta en TikZ dentro de `main.tex`, sin imágenes externas:

- **Panel A**: rendimiento multinúcleo frente a potencia de paquete estimada,
  con rectas de isoeficiencia, para los siete silicios comparados.
- **Panel B**: la misma figura de mérito generación a generación, de 2020 a
  2025, con la referencia x86 en paralelo.

## Cómo compilar

```
make pdf      # compone main.pdf con LuaLaTeX y Biber
make check    # verifica que la composición no dejó avisos
make clean    # borra los intermedios (main.pdf no se borra)
```

Requiere LuaLaTeX, Biber y la fuente Source Serif Pro.

## Clases de cifra

El documento separa de forma explícita tres tipos de dato:

1. **Publicadas por el fabricante**: fechas, proceso, ancho de banda,
   autonomía declarada, precios de lista y ventas netas del segmento Mac de
   los informes 10-K.
2. **Medidas por terceros**: medianas de Geekbench 6, con dispersión del orden
   del 5 %.
3. **Estimaciones propias**: potencias de paquete sostenidas, recuento de
   elementos de la matriz delta, coste por punto de rendimiento y tasas de
   crecimiento derivadas.

Las seis limitaciones del apartado 7 acotan hasta dónde llega cada una.
