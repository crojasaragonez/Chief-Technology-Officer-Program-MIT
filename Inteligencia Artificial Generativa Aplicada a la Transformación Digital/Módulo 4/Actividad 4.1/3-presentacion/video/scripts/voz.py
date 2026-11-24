"""Genera la narración del video a partir de guion.md.

Por cada escena:
  1. sintetiza cada frase con edge-tts (una frase por línea del guion);
  2. las une con una pausa corta en public/audio/escena-N.mp3;
  3. mide todo con ffprobe y escribe src/escenas.json con la duración de
     la escena y el inicio y fin de cada frase (para los subtítulos y para
     sincronizar las animaciones).

Uso: python3 scripts/voz.py   (variables opcionales: EDGE_TTS, VOZ, RITMO)
"""
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
GUION = RAIZ / "guion.md"
TMP = RAIZ / "tmp"
AUDIO = RAIZ / "public" / "audio"
SALIDA = RAIZ / "src" / "escenas.json"

EDGE_TTS = os.environ.get("EDGE_TTS", "edge-tts")
VOZ = os.environ.get("VOZ", "es-CR-JuanNeural")
RITMO = os.environ.get("RITMO", "+0%")
PAUSA = 0.45  # segundos entre frases
FPS = 30


def duracion(ruta: Path) -> float:
    salida = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "csv=p=0", str(ruta)], text=True)
    return float(salida.strip())


def escenas_del_guion():
    texto = GUION.read_text(encoding="utf-8")
    bloques = re.findall(r"<!-- escena-(\d+) -->\n(.*?)<!-- fin -->", texto, re.S)
    return [(int(n), [l.strip() for l in b.strip().splitlines() if l.strip()])
            for n, b in bloques]


def main():
    TMP.mkdir(exist_ok=True)
    AUDIO.mkdir(parents=True, exist_ok=True)
    silencio = TMP / "silencio.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i",
                    "anullsrc=r=24000:cl=mono", "-t", str(PAUSA), str(silencio)],
                   check=True)
    resultado = []
    for n, frases in escenas_del_guion():
        partes, cues, t = [], [], 0.0
        for i, frase in enumerate(frases):
            mp3 = TMP / f"e{n}-f{i:02d}.mp3"
            if not mp3.exists():
                subprocess.run([EDGE_TTS, "-v", VOZ, f"--rate={RITMO}", "-t", frase,
                                "--write-media", str(mp3)], check=True)
            wav = TMP / f"e{n}-f{i:02d}.wav"
            # Recorta el silencio que edge-tts deja al inicio y al final.
            recorte = ("silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
                       "silenceremove=start_periods=1:start_threshold=-50dB,areverse")
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-af",
                            recorte, "-ar", "24000", "-ac", "1", str(wav)], check=True)
            d = duracion(wav)
            cues.append({"texto": frase, "inicio": round(t, 3), "fin": round(t + d, 3)})
            partes.append(wav)
            t += d
            if i < len(frases) - 1:
                partes.append(silencio)
                t += PAUSA
        lista = TMP / f"e{n}.txt"
        lista.write_text("".join(f"file '{p.name}'\n" for p in partes))
        destino = AUDIO / f"escena-{n}.mp3"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
                        "-i", str(lista), "-c:a", "libmp3lame", "-b:a", "128k",
                        str(destino)], check=True)
        d = duracion(destino)
        resultado.append({"escena": n, "audio": f"audio/escena-{n}.mp3",
                          "duracionAudio": round(d, 3), "frases": cues})
        print(f"escena {n}: {d:6.2f} s, {sum(len(c['texto'].split()) for c in cues)} palabras")
    SALIDA.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n",
                      encoding="utf-8")
    total = sum(e["duracionAudio"] for e in resultado)
    print(f"total de audio: {total:.1f} s")


if __name__ == "__main__":
    main()
