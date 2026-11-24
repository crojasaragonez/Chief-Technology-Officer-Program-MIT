import React from 'react';
import {AbsoluteFill, Html5Audio, Sequence, Series, staticFile} from 'remotion';
import {Frase, PropsEscena, Subtitulos, useFuentes} from './comun';
import {Agente, Ana, Brief, Cambia, Piezas, Portada, Preguntas} from './escenas';
import escenas from './escenas.json';
import {ENTRADA, FPS, SALIDA} from './estilo';

// Una escena por diapositiva, en el mismo orden.
const componentes: React.FC<PropsEscena>[] = [Portada, Brief, Piezas, Agente, Ana, Cambia, Preguntas];

const duracionEscena = (duracionAudio: number) => Math.ceil((ENTRADA + duracionAudio + SALIDA) * FPS);

export const duracionTotal = () => escenas.reduce((s, e) => s + duracionEscena(e.duracionAudio), 0);

export const TeachBack: React.FC = () => {
  useFuentes();
  return (
    <AbsoluteFill style={{background: '#FFFFFF'}}>
      <Series>
        {escenas.map((e, i) => {
          const Escena = componentes[i];
          const frases = e.frases as Frase[];
          return (
            <Series.Sequence key={e.escena} durationInFrames={duracionEscena(e.duracionAudio)}>
              <Escena frases={frases} numero={e.escena} />
              <Sequence from={Math.round(ENTRADA * FPS)}>
                <Html5Audio src={staticFile(e.audio)} />
              </Sequence>
              <Subtitulos frases={frases} />
            </Series.Sequence>
          );
        })}
      </Series>
    </AbsoluteFill>
  );
};
