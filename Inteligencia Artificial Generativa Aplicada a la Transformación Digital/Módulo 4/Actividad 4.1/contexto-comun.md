# Contexto común para los cuatro agentes de la actividad 4.1

Carpeta de trabajo: `Módulo 4/Actividad 4.1/` (este archivo está ahí).
Enunciado completo: `Enunciado.txt` en la misma carpeta.

## Quién escribe y para quién

- Autor: Carlos Luis Rojas Aragonés, CTO de Subaxa. Curso: "Inteligencia
  Artificial Generativa Aplicada a la Transformación Digital", programa CTO
  del MIT Professional Education. Módulo 4, actividad 4.1 (teach-back).
- Público imaginado: el equipo de customer success managers (CSM) de Subaxa.
  Público NO técnico.

## Decisiones ya tomadas por el usuario

- Concepto: **ingeniería de prompts: qué es y por qué importa**.
- Ejemplo: el agente de user engagement de Subaxa, que genera contenido
  hiperpersonalizado para cada usuario.
- Formato del Agente 3: diapositivas (5 a 7, con notas detalladas) en PDF
  **y** video de 3 a 5 minutos hecho con Remotion (https://www.remotion.dev/)
  con el mismo contenido.
- Narración del video: voz sintética con `edge-tts` (ya instalado; el usuario
  autorizó enviar el guion a Microsoft). Voz en español latino, preferir
  `es-CR-*` si existe, si no `es-MX-*`.
- Look & feel del MIT: rojo MIT #A31F34, gris (#8A8B8C) y negro/blanco,
  tipografía sans serif limpia (Helvetica, Arial o similar disponible).
  Portada con "MIT Professional Education, Chief Technology Officer Program"
  como contexto del curso. **Sin logotipo oficial del MIT.**
- Idioma: todo en español de Costa Rica.
- Agente 2 entrega PDF. Se compone con LaTeX (LuaLaTeX), siguiendo el
  estilo de las actividades anteriores (ver `../../Módulo 3/Actividad 3.1/`,
  `main.tex` y `Makefile`, con `make pdf` y `make check`).

## Hechos sobre Subaxa y el agente (lo único que se puede afirmar)

Subaxa es una PropTech costarricense. Su plataforma ayuda a inversionistas a
comprar propiedades en remates judiciales en Costa Rica: mapa interactivo de
oportunidades, análisis con IA y un equipo legal y de inversión que acompaña
al inversionista durante el remate. Depende de los edictos de remate del
Boletín Judicial y de datos de propiedades del Registro Nacional.

Agente de user engagement (en producción):
- Canales: correo y WhatsApp.
- Datos que usa para personalizar: preferencias del usuario (zonas, tipo de
  propiedad, presupuesto), comportamiento en la plataforma (remates que vio,
  guardó o en los que participó), remates nuevos del Boletín Judicial que
  calzan con su perfil, y etapa del cliente (nuevo, activo, inactivo, etc.).
- Momento: alertas por evento (aparece un remate que calza, o el usuario hace
  o deja de hacer algo) y además un resumen periódico personalizado.
- Los CSM **aprueban los mensajes antes de que salgan**.

Cualquier otra cosa (nombres de usuarios, cifras de resultados, el prompt
real) NO se conoce. Si se necesita un prompt o mensaje de ejemplo, se
construye uno **ilustrativo y simplificado**, y se dice así. No inventar
métricas de impacto; si se menciona un efecto, que sea cualitativo.

## Reglas de estilo (obligatorias)

1. Nunca usar el carácter raya `—` ni `---` en LaTeX. Reformular con comas,
   dos puntos, paréntesis o punto y seguido. Verificar con grep al terminar.
2. Voz del usuario: primera persona ("elegí", "creo", "aprendí"), español de
   Costa Rica ("costo", "calza", "portafolio"), frases cortas y simples,
   títulos en lenguaje llano sin juegos de palabras, sin retórica de más.
3. Lenguaje no técnico: si aparece un término (prompt, modelo, contexto), se
   explica en una línea con palabras cotidianas.

## Salidas por agente

- Agente 1 → `1-concepto/concepto.md`
- Agente 2 → `2-contenido/` (main.tex, Makefile, main.pdf)
- Agente 3 → `3-presentacion/diapositivas/` (PDF con notas) y
  `3-presentacion/video/` (proyecto Remotion, audio, `teach-back.mp4`)
- Agente 4 → `4-entrega/nota-de-entrega.md` (y .txt para pegar)
