# Video del teach-back (Remotion)

Video de 4 minutos sobre ingeniería de prompts, con las mismas siete escenas
que `../diapositivas/diapositivas.pdf`. Salida: `teach-back.mp4`
(1920x1080, 30 fps, narración en español con subtítulos).

## Archivos

- `guion.md`: narración por escena. Cada línea es una frase y un subtítulo.
- `scripts/voz.py`: genera `public/audio/escena-N.mp3` con `edge-tts`
  (voz `es-CR-JuanNeural`) y escribe `src/escenas.json` con la duración de
  cada escena y el inicio de cada frase.
- `src/escenas.tsx`: las siete escenas. Cada elemento aparece cuando la
  narración llega a la frase que lo menciona.
- `src/estilo.ts`: colores del MIT, colores de las piezas y letra
  (Nimbus Sans; el símbolo ₡ sale de Liberation Sans).

## Cómo re-renderizar

```sh
npm install
# Solo si cambió el guion (envía el texto a Microsoft):
npm run voz
npm run render          # produce teach-back.mp4
npm run studio          # vista previa en el navegador
```

`npm run voz` necesita `edge-tts` 7.3 o más nuevo y `ffmpeg`. Con la
versión 7.2.8 el servicio responde 403. Si `edge-tts` no está en el PATH,
indique la ruta con `EDGE_TTS=/ruta/a/edge-tts npm run voz`. Las frases ya
sintetizadas quedan en `tmp/` y no se vuelven a pedir; borre `tmp/` para
regenerar todo.

Verificar la duración:

```sh
ffprobe -v error -show_entries format=duration -of csv=p=0 teach-back.mp4
```
