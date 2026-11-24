import React, {useEffect, useState} from 'react';
import {
  AbsoluteFill,
  continueRender,
  delayRender,
  Easing,
  interpolate,
  staticFile,
  useCurrentFrame,
} from 'remotion';
import {color, ENTRADA, FPS, letra, tenue} from './estilo';

export type Frase = {texto: string; inicio: number; fin: number};
export type PropsEscena = {frases: Frase[]; numero: number};

// Cuadro (frame) en que empieza la frase i de la narración de la escena.
export const inicioFrase = (frases: Frase[], i: number) =>
  Math.round((ENTRADA + frases[Math.min(i, frases.length - 1)].inicio) * FPS);

// Entrada suave: aparece y sube unos pixeles.
export const useEntrada = (desde: number, duracion = 16, distancia = 24) => {
  const frame = useCurrentFrame();
  const p = interpolate(frame, [desde, desde + duracion], [0, 1], {
    extrapolateLeft: 'clamp',
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  return {opacity: p, transform: `translateY(${(1 - p) * distancia}px)`};
};

export const Aparece: React.FC<{
  desde: number;
  children: React.ReactNode;
  style?: React.CSSProperties;
  distancia?: number;
}> = ({desde, children, style, distancia}) => {
  const e = useEntrada(desde, 16, distancia);
  return <div style={{...style, ...e}}>{children}</div>;
};

// Carga las fuentes antes de renderizar el primer cuadro.
const fuentes: [string, string, string][] = [
  ['Nimbus Sans', 'fonts/NimbusSans-Regular.otf', '400'],
  ['Nimbus Sans', 'fonts/NimbusSans-Bold.otf', '700'],
  ['Liberation Sans', 'fonts/LiberationSans-Regular.ttf', '400'],
  ['Liberation Sans', 'fonts/LiberationSans-Bold.ttf', '700'],
];

export const useFuentes = () => {
  const [handle] = useState(() => delayRender('Cargando fuentes'));
  useEffect(() => {
    Promise.all(
      fuentes.map(([familia, archivo, peso]) =>
        new FontFace(familia, `url(${staticFile(archivo)})`, {weight: peso})
          .load()
          .then((f) => document.fonts.add(f)),
      ),
    ).then(() => continueRender(handle));
  }, [handle]);
};

// Marco de cada diapositiva: barra roja arriba y pie gris.
export const Marco: React.FC<{numero: number; children: React.ReactNode; pie?: boolean}> = ({
  numero,
  children,
  pie = true,
}) => {
  const frame = useCurrentFrame();
  const fundido = interpolate(frame, [0, 10], [0, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{background: color.blanco, fontFamily: letra, color: color.texto}}>
      <div style={{position: 'absolute', top: 0, left: 0, right: 0, height: 10, background: color.rojo}} />
      <AbsoluteFill style={{opacity: fundido}}>{children}</AbsoluteFill>
      {pie && (
        <div
          style={{
            position: 'absolute',
            left: 108,
            right: 108,
            bottom: 34,
            borderTop: `1.5px solid ${color.gris}`,
            paddingTop: 10,
            display: 'flex',
            justifyContent: 'space-between',
            fontSize: 20,
            color: color.gris,
          }}
        >
          <span>Teach-back. Ingeniería de prompts</span>
          <span>Módulo 4. Actividad 4.1 &nbsp;|&nbsp; {numero}</span>
        </div>
      )}
    </AbsoluteFill>
  );
};

// Área de contenido, con los mismos márgenes del pie.
export const Contenido: React.FC<{children: React.ReactNode}> = ({children}) => (
  <div style={{position: 'absolute', left: 108, right: 108, top: 70}}>{children}</div>
);

export const Titulo: React.FC<{desde: number; children: React.ReactNode}> = ({desde, children}) => (
  <Aparece desde={desde}>
    <div style={{fontSize: 68, fontWeight: 700, color: color.rojo, lineHeight: 1.1}}>{children}</div>
  </Aparece>
);

export const Rotulo: React.FC<{children: React.ReactNode; c?: string}> = ({children, c = color.rojo}) => (
  <div style={{fontSize: 22, fontWeight: 700, color: c, letterSpacing: 0.5, textTransform: 'uppercase'}}>
    {children}
  </div>
);

export const Caja: React.FC<{
  children: React.ReactNode;
  borde?: string;
  style?: React.CSSProperties;
}> = ({children, borde = color.gris, style}) => (
  <div
    style={{
      border: `2px solid ${borde}`,
      borderRadius: 4,
      padding: '22px 28px',
      background: color.blanco,
      ...style,
    }}
  >
    {children}
  </div>
);

export const Destacado: React.FC<{children: React.ReactNode; style?: React.CSSProperties}> = ({
  children,
  style,
}) => (
  <div
    style={{
      borderLeft: `8px solid ${color.rojo}`,
      background: tenue(color.rojo, 0.05),
      padding: '22px 30px',
      fontSize: 36,
      lineHeight: 1.35,
      ...style,
    }}
  >
    {children}
  </div>
);

// Subtítulo de la frase que se está narrando.
export const Subtitulos: React.FC<{frases: Frase[]}> = ({frases}) => {
  const frame = useCurrentFrame();
  const t = frame / FPS - ENTRADA;
  const actual = frases.find((f, i) => {
    const siguiente = i + 1 < frases.length ? frases[i + 1].inicio : f.fin + 0.4;
    return t >= f.inicio - 0.05 && t < siguiente;
  });
  if (!actual) return null;
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        bottom: 92,
        display: 'flex',
        justifyContent: 'center',
        pointerEvents: 'none',
      }}
    >
      <div
        style={{
          maxWidth: 1500,
          background: 'rgba(26, 26, 26, 0.82)',
          color: color.blanco,
          fontFamily: letra,
          fontSize: 32,
          lineHeight: 1.3,
          padding: '10px 24px',
          borderRadius: 6,
          textAlign: 'center',
        }}
      >
        {actual.texto}
      </div>
    </div>
  );
};
