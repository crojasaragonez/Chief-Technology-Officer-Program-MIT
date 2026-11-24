import {Composition} from 'remotion';
import {TeachBack, duracionTotal} from './TeachBack';
import {FPS} from './estilo';

export const Root: React.FC = () => (
  <Composition
    id="TeachBack"
    component={TeachBack}
    durationInFrames={duracionTotal()}
    fps={FPS}
    width={1920}
    height={1080}
  />
);
