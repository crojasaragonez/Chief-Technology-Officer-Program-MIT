// Diseño compartido: los mismos colores y la misma letra del PDF de contenido.
export const FPS = 30;

export const color = {
  rojo: '#A31F34',
  gris: '#8A8B8C',
  fondo: '#F3F3F3',
  texto: '#1A1A1A',
  blanco: '#FFFFFF',
};

// Un color por pieza del prompt (igual que en el PDF y las diapositivas).
export const pieza = {
  rol: {nombre: 'Rol', color: '#A31F34'},
  contexto: {nombre: 'Contexto', color: '#1F5C99'},
  tarea: {nombre: 'Tarea', color: '#2E7D32'},
  reglas: {nombre: 'Reglas', color: '#B35C00'},
  ejemplo: {nombre: 'Ejemplo', color: '#6A4C93'},
  formato: {nombre: 'Formato', color: '#5A5B5C'},
};

// Nimbus Sans no trae el símbolo del colón: el navegador lo toma de Liberation Sans.
export const letra = '"Nimbus Sans", "Liberation Sans", Arial, sans-serif';

// Mezcla un color con blanco (como el "!6" de LaTeX).
export const tenue = (hex: string, alfa = 0.07) => {
  const n = parseInt(hex.slice(1), 16);
  const r = (n >> 16) & 255;
  const g = (n >> 8) & 255;
  const b = n & 255;
  const m = (c: number) => Math.round(255 - (255 - c) * alfa);
  return `rgb(${m(r)}, ${m(g)}, ${m(b)})`;
};

// Margen de la escena antes y después de la narración, en segundos.
export const ENTRADA = 0.7;
export const SALIDA = 1.2;
