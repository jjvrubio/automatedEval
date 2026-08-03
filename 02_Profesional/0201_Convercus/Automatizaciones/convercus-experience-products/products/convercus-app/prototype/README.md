# Prototipo de Convercus App

Base mobile-first de Convercus App. Tras A1 ofrece una GUI comercial navegable con datos mock y no requiere credenciales ni conexión con staging.

## Requisitos

- Node.js 24 o posterior.
- Dependencias instaladas con `npm ci`.

## Comandos

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
- `/system`: estado técnico de la demo.

El modo `/showcase` sirve para presentación y capturas. No emula Safari/iOS ni acredita funcionamiento en un dispositivo real. Esa instalación y validación forman parte de A5.

## Fuentes gobernadas

- La configuración de producto se carga desde `../config/app.yaml`.
- La marca y sus activos se cargan desde `../../../03-shared-assets/brands/convercus/`.
- `src/demo/canonical-demo-package.ts` declara las capacidades disponibles y sus limitaciones en la fase actual.

No deben incorporarse secretos al frontend ni presentarse capacidades propuestas como integraciones reales.
