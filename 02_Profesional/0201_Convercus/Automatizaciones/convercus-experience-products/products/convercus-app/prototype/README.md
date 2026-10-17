# Prototipo de Convercus App

Base mobile-first de Convercus App. Tras A1 ofrece una GUI comercial navegable con datos mock y no requiere credenciales ni conexión con staging.

## Requisitos

- Node.js 24 o posterior.
- Dependencias instaladas con `npm ci`.

## Comandos

### Abrir Sports Season / Carrera en este Mac

Haz doble clic en `Abrir demo.command` desde Finder. Arranca el servidor en `127.0.0.1:4173` y abre la demo en el navegador. Mantén la terminal abierta; `Control + C` detiene el servidor. Después de reiniciar el Mac o detener el servidor, vuelve a ejecutar el lanzador.

También puedes ejecutarlo desde esta carpeta:

```bash
./"Abrir demo.command"
```

El lanzador usa Node oficial 24.14.0 para macOS arm64 guardado en `.local-runtime/`, fuera de `/tmp` y excluido de Git; si no existe, busca Node >=24 en el PATH. En otra máquina se necesita instalar Node y ejecutar `npm ci`. No instala servicios al iniciar el Mac. `ERR_CONNECTION_REFUSED` en el enlace local indica que hay que comprobar que el servidor sigue activo. Si el puerto 4173 está ocupado, el lanzador muestra el error y no cambia de puerto.

### Desarrollo y comprobaciones

```bash
npm run dev
npm run check
npm run typecheck
npm run lint
npm test
npm run build
npm run preview
```

El servidor de desarrollo muestra la URL local en la terminal. `npm run check` ejecuta la puerta de calidad completa. `npm run build` genera la PWA estática en `dist/`; `npm run preview` permite verificar ese artefacto localmente.

Para detener el servidor, pulsa `Control + C` en la terminal que lo ejecuta.

## Vistas disponibles

- `/`: App responsive y punto de entrada de la interfaz comercial.
- `/benefits`: beneficios mock.
- `/activity`: actividad mock.
- `/profile`: perfil y acceso a herramientas de presentación.
- `/showcase`: la misma App dentro de un marco visual de iPhone a 393 × 852 px.
- `/?demo=sports-season-running`: Sports Season BUILD 02, con selección de persona y recorrido de participación o intereses.
- `/showcase?demo=sports-season-running`: Sports Season dentro del marco de iPhone, con recorrido interactivo y desplazamiento dentro del teléfono. «Ver como App» y «Ver como Web» conservan el recorrido y los formularios en la misma pestaña. Recargar o abrir otra pestaña inicia una ejecución nueva en memoria.
- `/system`: estado técnico de la demo.

## Selección experimental de demo

Session 5 utiliza un query parameter porque permite probar dos composiciones sobre el mismo bundle sin introducir routing de deployment ni multitenancy:

- `/?demo=retail-baseline`: control Retail actual.
- `/?demo=hospitality-stay`: configuración Hospitality de Aurora Stay.
- sin parámetro: selecciona explícitamente el control `retail-baseline`.

Un identificador desconocido o una referencia inválida detienen el bootstrap; nunca se sustituyen silenciosamente por datos de otro prospecto. Este mecanismo es experimental y no decide si una solución futura utilizará selección runtime, builds separados o configuración de deployment.

Hospitality representa individuo, grupo, booking, stay y property mediante referencias tipadas mínimas. Es una prueba de extensibilidad, no una ontología completa de sujetos o participaciones.

En `/system`, Hospitality expone la única acción de presentación de Session 7: `Confirmar llegada`. El control toma la acción del Demo Script, la entrega al límite público del runtime y muestra el checkpoint resultante. `pre-arrival-confirmed` y `checked-in` son checkpoints controlados de la demo; no representan TES Progression, Result ni Completion.

El modo `/showcase` sirve para presentación y capturas. No emula Safari/iOS ni acredita funcionamiento en un dispositivo real. Esa instalación y validación forman parte de A5.

## Fuentes gobernadas

- La configuración de producto se carga desde `../config/app.yaml`.
- La marca y sus activos se cargan desde `../../../03-shared-assets/brands/convercus/`.
- `src/demo/canonical-demo-package.ts` declara las capacidades disponibles y sus limitaciones en la fase actual.
- `src/demo-factory/` contiene los dos manifiestos experimentales, sus artefactos y el bootstrap reversible de Session 5.

No deben incorporarse secretos al frontend ni presentarse capacidades propuestas como integraciones reales.
