// Las siete escenas siguen las siete diapositivas. Cada elemento aparece
// cuando la narración llega a la frase que lo menciona (inicioFrase).
import React from 'react';
import {Easing, interpolate, useCurrentFrame} from 'remotion';
import {
  Aparece,
  Caja,
  Contenido,
  Destacado,
  inicioFrase,
  Marco,
  PropsEscena,
  Rotulo,
  Titulo,
} from './comun';
import {color, pieza, tenue} from './estilo';

const gris = (t: React.ReactNode) => <span style={{color: color.gris}}>{t}</span>;

// === 1. Portada ==============================================================
export const Portada: React.FC<PropsEscena> = ({frases, numero}) => {
  const frame = useCurrentFrame();
  const t = (i: number) => inicioFrase(frases, i);
  const ancho = interpolate(frame, [0, 24], [0, 1704], {
    extrapolateRight: 'clamp',
    easing: Easing.out(Easing.cubic),
  });
  return (
    <Marco numero={numero} pie={false}>
      <div style={{position: 'absolute', left: 108, top: 70}}>
        <div style={{height: 6, width: ancho, background: color.rojo}} />
        <Aparece desde={6}>
          <div style={{marginTop: 24, fontSize: 28, fontWeight: 700, color: color.gris}}>
            MIT Professional Education, Chief Technology Officer Program
          </div>
        </Aparece>
        <Aparece desde={14}>
          <div style={{marginTop: 100, fontSize: 34}}>
            Inteligencia Artificial Generativa Aplicada a la Transformación Digital
          </div>
          <div style={{marginTop: 8, fontSize: 26, color: color.gris}}>
            Módulo 4. Actividad 4.1. Teach-back
          </div>
        </Aparece>
        <Aparece desde={Math.min(t(2), 40)}>
          <div style={{marginTop: 60, fontSize: 110, fontWeight: 700, color: color.rojo, lineHeight: 1.08}}>
            Ingeniería de prompts:
            <br />
            qué es y por qué importa
          </div>
        </Aparece>
        <Aparece desde={Math.min(t(3), 60)}>
          <div style={{marginTop: 30, fontSize: 36}}>
            Una explicación para el equipo de customer success managers de Subaxa
          </div>
        </Aparece>
      </div>
      <Aparece desde={20} style={{position: 'absolute', left: 108, right: 108, bottom: 200}}>
        <div style={{borderTop: `1.5px solid ${color.gris}`, paddingTop: 16}}>
          <div style={{fontSize: 34, fontWeight: 700}}>Carlos Luis Rojas Aragonés</div>
          <div style={{fontSize: 26, color: color.gris, marginTop: 6}}>
            CTO de Subaxa &nbsp;|&nbsp; 23 de noviembre de 2026
          </div>
        </div>
      </Aparece>
    </Marco>
  );
};

// === 2. El brief =============================================================
export const Brief: React.FC<PropsEscena> = ({frases, numero}) => {
  const t = (i: number) => inicioFrase(frases, i);
  return (
    <Marco numero={numero}>
      <Contenido>
        <Titulo desde={4}>Un prompt es el brief que le damos a la IA</Titulo>
        <Aparece desde={t(1)}>
          <div style={{marginTop: 26, fontSize: 38}}>
            <b>Prompt:</b> las instrucciones por escrito que le damos a la IA para que haga un trabajo.
          </div>
        </Aparece>
        <div style={{display: 'flex', gap: 60, marginTop: 50}}>
          <Aparece desde={t(2)} style={{flex: 1}}>
            <Caja style={{minHeight: 300}}>
              <Rotulo c={color.gris}>A un compañero nuevo, brief vago</Rotulo>
              <div style={{fontSize: 36, marginTop: 18}}>«Escribile a un cliente sobre un remate.»</div>
              <Aparece desde={t(3)}>
                <div style={{fontSize: 30, marginTop: 24, color: color.gris, lineHeight: 1.3}}>
                  Resultado: algo correcto, pero genérico. No conoce al cliente ni nuestras reglas.
                </div>
              </Aparece>
            </Caja>
          </Aparece>
          <Aparece desde={t(5)} style={{flex: 1}}>
            <Caja borde={color.rojo} style={{minHeight: 300}}>
              <Rotulo>Al mismo compañero, brief completo</Rotulo>
              <div style={{fontSize: 32, marginTop: 18, lineHeight: 1.3}}>
                Quién es el cliente y qué busca. Qué remate salió. Qué no puede prometer. Un mensaje que
                ya funcionó. Corto, para WhatsApp.
              </div>
              <Aparece desde={t(7)}>
                <div style={{fontSize: 30, marginTop: 20, color: color.gris}}>
                  Resultado: sale bien desde la primera vez.
                </div>
              </Aparece>
            </Caja>
          </Aparece>
        </div>
        <Aparece desde={t(8)}>
          <Destacado style={{marginTop: 44}}>
            <b>La IA es ese compañero nuevo:</b> escribe rápido y bien, pero solo sabe lo que le decimos.
            Si el brief es vago, el resultado es vago.
          </Destacado>
        </Aparece>
      </Contenido>
    </Marco>
  );
};

// === 3. Las seis piezas ======================================================
const Tarjeta: React.FC<{
  p: {nombre: string; color: string};
  que: string;
  subaxa: string;
  desde: number;
  resalte?: number;
}> = ({p, que, subaxa, desde, resalte}) => {
  const frame = useCurrentFrame();
  const brillo =
    resalte === undefined
      ? 0
      : interpolate(frame, [resalte, resalte + 10, resalte + 70, resalte + 90], [0, 1, 1, 0], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
  return (
    <Aparece desde={desde} style={{width: 548}}>
      <div
        style={{
          borderTop: `8px solid ${p.color}`,
          background: tenue(p.color, 0.07),
          padding: '20px 26px',
          height: 270,
          boxShadow: brillo ? `0 0 0 ${4 * brillo}px ${p.color}` : undefined,
        }}
      >
        <div style={{fontSize: 30, fontWeight: 700, color: p.color, textTransform: 'uppercase'}}>{p.nombre}</div>
        <div style={{fontSize: 34, marginTop: 12, lineHeight: 1.25}}>{que}</div>
        <div style={{fontSize: 25, marginTop: 14, lineHeight: 1.3}}>
          {gris('En Subaxa: ')}
          {subaxa}
        </div>
      </div>
    </Aparece>
  );
};

export const Piezas: React.FC<PropsEscena> = ({frases, numero}) => {
  const t = (i: number) => inicioFrase(frases, i);
  return (
    <Marco numero={numero}>
      <Contenido>
        <Titulo desde={4}>Un buen prompt tiene seis piezas</Titulo>
        <Aparece desde={10}>
          <div style={{marginTop: 18, fontSize: 32}}>
            Cada pieza responde una pregunta que el compañero nuevo nos haría.
          </div>
        </Aparece>
        <div style={{display: 'flex', flexWrap: 'wrap', gap: 30, marginTop: 36}}>
          <Tarjeta p={pieza.rol} que="Quién «es» la IA en esta tarea." subaxa="alguien del equipo que acompaña a inversionistas." desde={t(1)} />
          <Tarjeta p={pieza.contexto} que="Lo que sabemos de la persona." subaxa="zonas, tipo de propiedad, presupuesto, qué vio o guardó, etapa." desde={t(2)} />
          <Tarjeta p={pieza.tarea} que="Qué tiene que hacer, una sola cosa." subaxa="avisar de un remate nuevo que calza con su perfil." desde={t(3)} />
          <Tarjeta p={pieza.reglas} que="Lo que puede y no puede hacer." subaxa="no prometer ganancias ni inventar datos." desde={t(4)} resalte={t(5)} />
          <Tarjeta p={pieza.ejemplo} que="Un mensaje modelo de cómo suena «bien»." subaxa="un mensaje corto y cercano ya aprobado." desde={t(6)} />
          <Tarjeta p={pieza.formato} que="Cómo se entrega." subaxa="canal, largo máximo, un solo llamado a la acción." desde={t(7)} />
        </div>
      </Contenido>
    </Marco>
  );
};

// === 4. El agente de user engagement =========================================
export const Agente: React.FC<PropsEscena> = ({frases, numero}) => {
  const t = (i: number) => inicioFrase(frases, i);
  const datos = [
    'Preferencias: zonas, tipo de propiedad y presupuesto.',
    'Lo que hace en la plataforma: remates que vio, guardó o en los que participó.',
    'Remates nuevos del Boletín Judicial que calzan.',
    'Etapa del cliente: nuevo, activo, inactivo.',
  ];
  return (
    <Marco numero={numero}>
      <Contenido>
        <Titulo desde={4}>Nuestro caso: el agente de user engagement</Titulo>
        <Aparece desde={t(1)}>
          <div style={{marginTop: 18, fontSize: 32}}>
            Está en producción. Escribe mensajes personalizados para cada usuario de la plataforma.
          </div>
        </Aparece>
        <div style={{display: 'flex', gap: 36, marginTop: 40, alignItems: 'flex-start'}}>
          <Aparece desde={t(2)} style={{width: 300}}>
            <Caja>
              <Rotulo>Canales</Rotulo>
              <div style={{fontSize: 34, marginTop: 14, lineHeight: 1.35}}>
                Correo
                <br />
                WhatsApp
              </div>
            </Caja>
          </Aparece>
          <Aparece desde={t(3)} style={{flex: 1}}>
            <Caja>
              <Rotulo>Datos que usa</Rotulo>
              <div style={{marginTop: 10}}>
                {datos.map((d, i) => (
                  <Aparece key={d} desde={t(3) + 10 + i * 22} distancia={12}>
                    <div style={{fontSize: 28, lineHeight: 1.3, marginTop: 10, display: 'flex', gap: 14}}>
                      <span style={{color: color.rojo}}>■</span>
                      <span>{d}</span>
                    </div>
                  </Aparece>
                ))}
              </div>
            </Caja>
          </Aparece>
          <Aparece desde={t(4)} style={{width: 430}}>
            <Caja>
              <Rotulo>Cuándo escribe</Rotulo>
              <div style={{fontSize: 28, marginTop: 14, lineHeight: 1.3}}>
                Cuando pasa algo: sale un remate que calza, o el usuario hace o deja de hacer algo.
                <div style={{marginTop: 10}}>Y en un resumen periódico.</div>
              </div>
            </Caja>
          </Aparece>
        </div>
        <Aparece desde={t(5)}>
          <Destacado style={{marginTop: 40}}>
            <b>Antes de que un mensaje salga, un CSM lo aprueba.</b> Ustedes son la última revisión entre la
            IA y el inversionista.
          </Destacado>
        </Aparece>
      </Contenido>
    </Marco>
  );
};

// === 5. Ana: prompt pobre y prompt completo ==================================
const Pieza: React.FC<{p: {nombre: string; color: string}; desde: number; children: React.ReactNode}> = ({
  p,
  desde,
  children,
}) => (
  <Aparece desde={desde} distancia={14}>
    <div
      style={{
        borderLeft: `6px solid ${p.color}`,
        background: tenue(p.color, 0.07),
        padding: '7px 16px',
        marginTop: 7,
        fontSize: 24,
        lineHeight: 1.3,
      }}
    >
      <span style={{fontSize: 18, fontWeight: 700, color: p.color, textTransform: 'uppercase', marginRight: 12}}>
        {p.nombre}
      </span>
      {children}
    </div>
  </Aparece>
);

const Mensaje: React.FC<{titulo: string; children: React.ReactNode; style?: React.CSSProperties}> = ({
  titulo,
  children,
  style,
}) => (
  <div style={{background: color.fondo, borderRadius: 10, padding: '12px 18px', ...style}}>
    <div style={{fontSize: 18, fontWeight: 700, color: color.gris}}>{titulo}</div>
    <div style={{fontSize: 24, lineHeight: 1.35, marginTop: 4}}>{children}</div>
  </div>
);

export const Ana: React.FC<PropsEscena> = ({frases, numero}) => {
  const t = (i: number) => inicioFrase(frases, i);
  return (
    <Marco numero={numero}>
      <Contenido>
        <Aparece desde={4}>
          <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 30}}>
            <div style={{fontSize: 58, fontWeight: 700, color: color.rojo}}>
              El mismo pedido, con dos prompts distintos
            </div>
          </div>
        </Aparece>
        <div style={{display: 'flex', gap: 44, marginTop: 22}}>
          <div style={{width: 560}}>
            <Aparece desde={t(0)}>
              <div
                style={{
                  borderLeft: `6px solid ${color.rojo}`,
                  background: tenue(color.rojo, 0.06),
                  padding: '10px 16px',
                  fontSize: 22,
                  lineHeight: 1.3,
                  marginBottom: 20,
                }}
              >
                <b style={{color: color.rojo}}>Ejemplo ilustrativo y simplificado.</b> No es el prompt real del
                agente. Ana, el remate y los montos son ficticios.
              </div>
            </Aparece>
            <Aparece desde={t(2)}>
              <Rotulo c={color.gris}>Prompt pobre</Rotulo>
              <div
                style={{
                  border: `2px solid ${color.gris}`,
                  borderRadius: 4,
                  padding: '10px 16px',
                  fontSize: 24,
                  lineHeight: 1.3,
                  marginTop: 8,
                }}
              >
                Escriba un mensaje de WhatsApp para un usuario de Subaxa sobre un remate nuevo.
              </div>
            </Aparece>
            <Aparece desde={t(3)}>
              <Mensaje titulo="Mensaje que produciría (genérico)" style={{marginTop: 14}}>
                ¡Hola! En Subaxa tenemos nuevas oportunidades de inversión en remates judiciales. ¡No se las
                pierda! Entre a la plataforma y descubra las mejores propiedades{' '}
                <span style={{background: '#F6D7DC'}}>al mejor precio</span>. ¡Invierta hoy!
              </Mensaje>
            </Aparece>
          </div>
          <div style={{flex: 1}}>
            <Aparece desde={t(4)}>
              <Rotulo>Prompt con las seis piezas</Rotulo>
            </Aparece>
            <Pieza p={pieza.rol} desde={t(5)}>
              Equipo de Subaxa que acompaña a inversionistas. Cercano, de «usted».
            </Pieza>
            <Pieza p={pieza.contexto} desde={t(6)}>
              Ana (ficticia), activa. Busca casas en Heredia, hasta ₡80 000 000. Guardó dos la semana pasada.
              Remate: casa de 3 habitaciones en Heredia, base ₡65 000 000, 15 de enero.
            </Pieza>
            <Pieza p={pieza.tarea} desde={t(7)}>
              Avísele de este remate y por qué podría interesarle.
            </Pieza>
            <Pieza p={pieza.reglas} desde={t(8)}>
              Solo estos datos. No prometa ganancias ni diga «ganga». Sin direcciones exactas. Invítela a
              hablar con el equipo.
            </Pieza>
            <Pieza p={pieza.ejemplo} desde={t(9)}>
              «Hola, Luis. Vimos que le interesan los lotes en Cartago… Si gusta, lo revisamos juntos.»
            </Pieza>
            <Pieza p={pieza.formato} desde={t(10)}>
              WhatsApp. Máximo 4 líneas. Un llamado a la acción. Sin emojis.
            </Pieza>
            <Aparece desde={t(11)}>
              <Mensaje titulo="Mensaje que produciría (personalizado)" style={{marginTop: 14}}>
                Hola, Ana. Salió en el Boletín Judicial una casa de 3 habitaciones en Heredia, parecida a las
                que guardó la semana pasada. La base es de ₡65 000 000 y el primer remate es el 15 de enero. Si
                gusta, el equipo legal y de inversión le acompaña a revisarla antes de decidir.
              </Mensaje>
            </Aparece>
          </div>
        </div>
      </Contenido>
    </Marco>
  );
};

// === 6. Qué cambia para los CSM ==============================================
export const Cambia: React.FC<PropsEscena> = ({frases, numero}) => {
  const t = (i: number) => inicioFrase(frases, i);
  return (
    <Marco numero={numero}>
      <Contenido>
        <Titulo desde={4}>Qué cambia para ustedes</Titulo>
        <Aparece desde={t(1)}>
          <div style={{marginTop: 22, fontSize: 36}}>
            Cuando un mensaje sale mal, casi siempre falta o falla una pieza.
          </div>
        </Aparece>
        <div style={{display: 'flex', gap: 60, marginTop: 44}}>
          <Aparece desde={t(2)} style={{flex: 1}}>
            <Caja style={{minHeight: 200}}>
              <Rotulo c={color.gris}>Corregir el mensaje a mano</Rotulo>
              <div style={{fontSize: 40, marginTop: 16}}>
                Arregla <b>un</b> mensaje.
              </div>
              <div style={{fontSize: 30, marginTop: 12, color: color.gris}}>
                El mismo error vuelve a aparecer en el siguiente.
              </div>
            </Caja>
          </Aparece>
          <Aparece desde={t(3)} style={{flex: 1}}>
            <Caja borde={color.rojo} style={{minHeight: 200}}>
              <Rotulo>Ajustar el prompt una vez</Rotulo>
              <div style={{fontSize: 40, marginTop: 16}}>Arregla la causa.</div>
              <div style={{fontSize: 30, marginTop: 12, color: color.gris}}>
                Mejora <b>todos</b> los mensajes que vienen.
              </div>
            </Caja>
          </Aparece>
        </div>
        <Aparece desde={t(4)}>
          <Destacado style={{marginTop: 44}}>
            <b>Ustedes ya tienen el criterio.</b> Saben cómo se le habla a un cliente nuevo y cómo a uno
            inactivo. El prompt es el lugar donde ese criterio queda por escrito para la IA.
          </Destacado>
        </Aparece>
      </Contenido>
    </Marco>
  );
};

// === 7. Las cinco preguntas y la plantilla ===================================
export const Preguntas: React.FC<PropsEscena> = ({frases, numero}) => {
  const t = (i: number) => inicioFrase(frases, i);
  const preguntas = [
    '¿Se nota que es para esta persona?',
    '¿Los datos del remate son correctos y no hay nada inventado?',
    '¿Promete algo que no debe?',
    '¿El tono calza con la etapa del cliente?',
    '¿Tiene el largo del canal y un solo llamado a la acción?',
  ];
  return (
    <Marco numero={numero}>
      <Contenido>
        <Titulo desde={4}>Qué pueden hacer desde mañana</Titulo>
        <div style={{display: 'flex', gap: 50, marginTop: 34}}>
          <div style={{flex: 1.15}}>
            <Aparece desde={t(0)}>
              <Rotulo>Al aprobar un mensaje, cinco preguntas</Rotulo>
            </Aparece>
            <Aparece desde={t(0) + 6}>
              <Caja borde={color.rojo} style={{marginTop: 10, minHeight: 330}}>
                {preguntas.map((p, i) => (
                  <Aparece key={p} desde={t(i + 1)} distancia={10}>
                    <div style={{display: 'flex', gap: 16, fontSize: 29, lineHeight: 1.3, marginTop: i ? 12 : 0}}>
                      <b style={{color: color.rojo, width: 30}}>{i + 1}.</b>
                      <span>{p}</span>
                    </div>
                  </Aparece>
                ))}
              </Caja>
            </Aparece>
          </div>
          <Aparece desde={t(6)} style={{flex: 0.85}}>
            <Rotulo c={color.gris}>Si una respuesta es «no»</Rotulo>
            <div style={{background: color.fondo, borderRadius: 4, padding: '20px 26px', marginTop: 10}}>
              <div style={{fontSize: 24, fontWeight: 700}}>Plantilla para sugerir un ajuste al prompt</div>
              {[
                ['Pieza:', <b style={{color: pieza.reglas.color}}>Reglas</b>],
                ['Qué pasó:', 'El mensaje dijo «excelente oportunidad de ganancia».'],
                ['Ajuste:', 'Agregar la regla «no hablar de ganancias ni de rentabilidad esperada».'],
              ].map(([k, v], i) => (
                <div key={i} style={{display: 'flex', gap: 14, fontSize: 24, lineHeight: 1.3, marginTop: 14}}>
                  <b style={{width: 130, flexShrink: 0}}>{k}</b>
                  <span>{v}</span>
                </div>
              ))}
            </div>
            <div style={{fontSize: 22, color: color.gris, marginTop: 10}}>Además de corregir el mensaje.</div>
          </Aparece>
        </div>
        <Aparece desde={t(8)}>
          <Destacado style={{marginTop: 34, fontSize: 32}}>
            Un mensaje genérico casi nunca es culpa de la IA: es un prompt que dejó decisiones sin tomar.
          </Destacado>
        </Aparece>
      </Contenido>
    </Marco>
  );
};
