# Guion del video: ingeniería de prompts

Narración por escena. Cada escena corresponde a una diapositiva de
`../diapositivas/diapositivas.pdf` y resume sus notas. El texto que va entre
las líneas `<!-- escena-N -->` y `<!-- fin -->` es el que se convierte en
audio con `edge-tts` (ver `scripts/voz.sh`); cada frase es también un
subtítulo.

Voz: `es-CR-JuanNeural`. Duración objetivo: 3:30 a 4:30.

## Escena 1. Portada

<!-- escena-1 -->
Hola. Soy Carlos Luis Rojas Aragonés, CTO de Subaxa.
Este es mi teach-back para el programa de CTO del MIT Professional Education.
El tema es la ingeniería de prompts: qué es y por qué importa.
Lo preparé para ustedes, el equipo de customer success managers de Subaxa.
No hace falta saber nada técnico.
<!-- fin -->

## Escena 2. Un prompt es el brief que le damos a la IA

<!-- escena-2 -->
Empiezo por la palabra.
Un prompt son las instrucciones por escrito que le damos a la IA para que haga un trabajo.
Imaginen que llega alguien nuevo al equipo y le piden: escribile a un cliente sobre un remate.
Va a escribir algo correcto, pero genérico.
No conoce al cliente ni nuestras reglas.
Ahora imaginen que le dicen quién es el cliente, qué busca y qué no puede prometer.
Y le muestran un mensaje que ya funcionó.
El mensaje sale bien desde la primera vez.
La IA es ese compañero nuevo: escribe rápido y bien, pero solo sabe lo que le decimos.
El prompt es el brief. Si el brief es vago, el resultado es vago.
<!-- fin -->

## Escena 3. Un buen prompt tiene seis piezas

<!-- escena-3 -->
Un buen prompt tiene seis piezas.
El rol: quién es la IA en esta tarea.
El contexto: lo que sabemos de la persona.
La tarea: qué tiene que hacer, una sola cosa.
Las reglas: lo que puede y no puede hacer.
Por ejemplo, no inventar datos, porque la IA a veces inventa un dato que suena creíble.
El ejemplo: un mensaje modelo de cómo suena bien.
Y el formato: cómo se entrega, por qué canal y de qué largo.
<!-- fin -->

## Escena 4. Nuestro caso: el agente de user engagement

<!-- escena-4 -->
Llevemos esto a algo que ustedes conocen.
Nuestro agente de user engagement está en producción.
Escribe mensajes por correo y WhatsApp para cada usuario.
Usa sus preferencias, lo que hace en la plataforma, los remates nuevos del Boletín Judicial que calzan con su perfil, y su etapa como cliente.
Escribe cuando pasa algo, y también en un resumen periódico.
Y antes de que un mensaje salga, uno de ustedes lo aprueba.
<!-- fin -->

## Escena 5. El mismo pedido, con dos prompts distintos

<!-- escena-5 -->
Veamos un ejemplo ilustrativo y simplificado.
No es el prompt real, y Ana es una usuaria ficticia.
A la izquierda, un prompt pobre: escriba un mensaje de WhatsApp para un usuario sobre un remate nuevo.
El resultado suena a publicidad masiva, y hasta promete el mejor precio.
A la derecha, el mismo pedido con las seis piezas.
El rol.
El contexto: Ana busca casas en Heredia, y la semana pasada guardó dos.
La tarea.
Las reglas.
Un ejemplo de tono.
Y el formato.
Ahora el mensaje habla de lo que Ana busca, con datos correctos y sin promesas.
La IA es la misma. Lo único que cambió fue el prompt.
<!-- fin -->

## Escena 6. Qué cambia para ustedes

<!-- escena-6 -->
¿Qué cambia para ustedes?
Cuando un mensaje sale mal, casi siempre falta o falla una pieza.
Corregir a mano arregla un mensaje, pero el mismo error vuelve en el siguiente.
Ajustar el prompt arregla la causa, y mejora todos los mensajes que vienen.
Ustedes ya tienen el criterio: saben cómo se le habla a un cliente nuevo y cómo a uno inactivo.
El prompt es donde ese criterio queda por escrito.
Por eso no solo aprueban. También pueden mejorar el prompt.
<!-- fin -->

## Escena 7. Qué pueden hacer desde mañana

<!-- escena-7 -->
Desde mañana, al aprobar un mensaje, háganse cinco preguntas.
¿Se nota que es para esta persona?
¿Los datos del remate son correctos?
¿Promete algo que no debe?
¿El tono calza con la etapa del cliente?
¿Tiene el largo del canal y un solo llamado a la acción?
Si una respuesta es no, corrijan el mensaje y escriban una sugerencia corta: qué pieza falló, qué pasó y qué ajuste proponen.
Al preparar esto aprendí algo.
Un mensaje genérico casi nunca es culpa de la IA: es un prompt que dejó decisiones sin tomar.
Y quienes mejor pueden tomar esas decisiones son ustedes.
Muchas gracias.
<!-- fin -->
