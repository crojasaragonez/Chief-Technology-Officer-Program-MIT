# Concepto del teach-back: ingeniería de prompts

Documento de trabajo del Agente 1. Es el insumo para el contenido (Agente 2),
la presentación y el video (Agente 3) y la nota de entrega (Agente 4).

Público: el equipo de customer success managers (CSM) de Subaxa. No es un
público técnico.

## 1. El concepto y hasta dónde llega

**Concepto elegido:** ingeniería de prompts, qué es y por qué importa.

**Qué es un prompt, en una línea:** son las instrucciones por escrito que le
damos a la IA para que haga un trabajo.

**Qué es la ingeniería de prompts, en una línea:** es el oficio de escribir
esas instrucciones de forma que la IA entregue lo que necesitamos, y no lo
que ella supone.

**Qué voy a enseñar.** Las seis piezas de un buen prompt, aplicadas a un
caso que el equipo conoce: el mensaje de WhatsApp o correo que genera el
agente de user engagement para un usuario.

| Pieza | Qué es, en palabras simples | En el agente de user engagement |
| :-- | :-- | :-- |
| Rol | Quién "es" la IA en esta tarea | Alguien del equipo de Subaxa que acompaña a inversionistas |
| Contexto del usuario | Lo que sabemos de la persona | Zonas, tipo de propiedad, presupuesto, qué remates vio o guardó, etapa del cliente |
| Tarea | Qué tiene que hacer, una sola cosa | Avisar de un remate nuevo que calza con su perfil |
| Reglas | Lo que puede y no puede hacer | No prometer ganancias, no inventar datos del remate, invitar a hablar con el equipo |
| Ejemplos | Un mensaje modelo de cómo suena "bien" | Un mensaje corto, cercano y profesional ya aprobado |
| Formato | Cómo se entrega | Canal (WhatsApp o correo), largo máximo, un solo llamado a la acción |

**Qué dejo fuera, a propósito.**

- Cómo funciona un modelo de lenguaje por dentro (tokens, entrenamiento).
- Técnicas avanzadas con nombre propio (cadena de pensamiento, cadenas de
  prompts, ajuste fino). Las menciono, como mucho, de pasada.
- Cómo está programado el agente, de dónde salen los datos técnicamente o
  qué modelo usa.
- El prompt real del agente. No lo voy a mostrar: todo ejemplo es
  ilustrativo y simplificado.
- Métricas de resultados del agente. No las tenemos para esta actividad; si
  hablo de efecto, es cualitativo.

**Términos que hay que explicar cuando aparezcan:**

- *Modelo* o *IA generativa:* el programa que escribe el texto a partir de
  las instrucciones.
- *Contexto:* la información que le pasamos junto con la tarea, en este caso
  lo que sabemos del usuario y del remate.
- *Alucinación:* cuando la IA inventa un dato que suena creíble. Solo si
  hace falta para explicar la regla "no inventar datos".

## 2. Por qué le importa a un CSM

- **Ustedes aprueban cada mensaje antes de que salga.** Son la última
  revisión entre la IA y el inversionista.
- **Un mensaje bueno o malo casi siempre se explica por el prompt.** Si
  falta el contexto, sale genérico. Si falta una regla, puede prometer algo
  que no debe. Si falta el formato, sale largo o en el tono equivocado.
- **Entender las piezas cambia el trabajo.** En lugar de corregir a mano el
  mismo error en cada mensaje, el CSM puede decir qué pieza falló y proponer
  un ajuste al prompt. Ese ajuste mejora todos los mensajes que vienen, no
  solo uno.
- **Es el mismo criterio que ya tienen.** Un CSM sabe cómo se le habla a un
  cliente nuevo y cómo a uno inactivo. El prompt es el lugar donde ese
  criterio queda por escrito para la IA.

## 3. La idea clave que me llevo

> Al preparar esto me di cuenta de que un mensaje genérico casi nunca es
> culpa de la IA: es un prompt que dejó decisiones sin tomar. Y que las
> personas que mejor pueden tomar esas decisiones son los CSM, no yo.

## 4. Ejemplo ilustrativo y simplificado

> **Importante:** este ejemplo es ilustrativo y simplificado. No es el
> prompt real del agente. La usuaria, el remate y los montos son ficticios.

### 4a. Prompt pobre

```
Escriba un mensaje de WhatsApp para un usuario de Subaxa sobre un remate nuevo.
```

**Mensaje que produciría (genérico):**

> ¡Hola! En Subaxa tenemos nuevas oportunidades de inversión en remates
> judiciales. ¡No se las pierda! Entre a la plataforma y descubra las mejores
> propiedades al mejor precio. ¡Invierta hoy!

Qué está mal: no dice cuál remate, no sabe a quién le habla, suena a
publicidad masiva y "al mejor precio" es una promesa que no podemos hacer.

### 4b. Prompt bien construido

```
ROL
Usted es parte del equipo de Subaxa que acompaña a inversionistas en remates
judiciales en Costa Rica. Escribe de forma cercana y profesional, tratando de "usted".

CONTEXTO DEL USUARIO (ficticio)
- Nombre: Ana (usuaria ficticia)
- Etapa: activa, se registró hace unos meses, todavía no ha participado
  en un remate.
- Busca: casas en Heredia.
- Presupuesto: hasta ₡80 000 000.
- Comportamiento: la semana pasada guardó dos casas en Heredia en remate.

REMATE NUEVO QUE CALZA (ficticio)
- Casa de 3 habitaciones en Heredia.
- Base del remate: ₡65 000 000.
- Fecha del primer remate: 15 de enero (ficticia).

TAREA
Avísele a Ana de este remate nuevo y por qué podría interesarle.

REGLAS
- Use solo los datos de arriba. No invente nada del remate.
- No prometa ganancias ni diga que es "una ganga".
- No ponga direcciones exactas.
- Invítela a ver el detalle o a hablar con el equipo legal y de inversión.

EJEMPLO DE TONO
"Hola, Luis. Vimos que le interesan los lotes en Cartago y apareció uno
nuevo en el Boletín Judicial. Si gusta, lo revisamos juntos." (ficticio)

FORMATO
WhatsApp. Máximo 4 líneas. Un solo llamado a la acción. Sin emojis.
```

**Mensaje que produciría (personalizado):**

> Hola, Ana. Salió en el Boletín Judicial una casa de 3 habitaciones en
> Heredia, parecida a las que guardó la semana pasada. La base es de
> ₡65 000 000 y el primer remate es el 15 de enero. Si gusta, el equipo
> legal y de inversión le acompaña a revisarla antes de decidir.

Qué cambió: el mensaje usa su zona, su tipo de propiedad y lo que hizo en
la plataforma; está dentro de su presupuesto; no promete nada; y es corto.

**Uso en diapositivas y video:** mostrar 4a y 4b lado a lado, y resaltar
en el prompt 4b cada una de las seis piezas con un color o etiqueta.

## 5. Mensajes clave y conclusión práctica

**Mensajes clave (repetir igual en documento, diapositivas y video):**

1. Un prompt es el brief que le damos a la IA: si el brief es vago, el
   resultado es vago.
2. Un buen prompt tiene seis piezas: rol, contexto del usuario, tarea,
   reglas, ejemplo y formato.
3. Cuando un mensaje sale mal, casi siempre falta o falla una pieza.
4. El CSM no solo aprueba: puede mejorar el prompt, y eso mejora todos los
   mensajes que vienen.

**Conclusión práctica: qué puede hacer un CSM mañana.**

Al aprobar un mensaje, cinco preguntas rápidas:

1. ¿Se nota que es para esta persona? (zona, tipo de propiedad, lo que hizo)
2. ¿Los datos del remate son correctos y no hay nada inventado?
3. ¿Promete algo que no debe? (ganancias, "ganga", certeza del resultado)
4. ¿El tono calza con la etapa del cliente? (nuevo, activo, inactivo)
5. ¿Tiene el largo del canal y un solo llamado a la acción?

Si una respuesta es "no", además de corregir el mensaje, escribir una
sugerencia de ajuste con esta forma simple:

> **Pieza:** reglas
> **Qué pasó:** el mensaje dijo "excelente oportunidad de ganancia".
> **Ajuste propuesto:** agregar la regla "no hablar de ganancias ni de
> rentabilidad esperada".

## 6. Analogía para explicar qué es un prompt

**El brief a un compañero nuevo.** Imaginen que llega alguien nuevo al
equipo y le piden: "escribile a un cliente sobre un remate". Va a escribir
algo correcto, pero genérico, porque no conoce al cliente ni nuestras
reglas. Si en cambio le dicen quién es el cliente, qué busca, qué remate
salió, qué no puede prometer, le muestran un mensaje que ya funcionó y le
piden que sea corto por WhatsApp, el mensaje sale bien desde la primera
vez.

La IA es ese compañero nuevo: escribe rápido y bien, pero solo sabe lo que
le decimos. El prompt es el brief.
