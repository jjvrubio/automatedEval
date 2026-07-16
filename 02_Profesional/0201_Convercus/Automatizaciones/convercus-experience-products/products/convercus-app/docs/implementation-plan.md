# Plan inicial de implementación de Convercus App

## Objetivo de la primera versión

Construir una PWA mobile-first, repetible y demostrable, sin depender de staging.

## Stack previsto

- Node.js 24 LTS.
- React.
- TypeScript.
- Vite.
- React Router.
- Tailwind CSS.
- Vitest.
- Playwright.

## Fases

### A0 — Preparación

- Crear rama de implementación.
- Crear proyecto aislado dentro de `prototype/`.
- Configurar calidad, pruebas y scripts.
- Formalizar los contratos mínimos de dominio.

### A1 — Sistema visual y navegación

- Navegación mobile-first.
- Componentes base.
- Estados de carga, vacío y error.
- Datos mock tipados.

### A2 — Fidelización

- Perfil.
- Puntos y nivel.
- Cupones.
- Noticias y actividad.

### A3 — Simulación de Experiences

- Motor local de eventos y estado.
- Panel interno de simulación.
- Primer escenario canónico completo.
- Resultado, medición y aprendizaje observables.

### A4 — Escenarios adicionales

- Circuito de decisión: ocasión.
- Maratón de Temporada.
- Desafío Activo o Aventura Familiar.

### A5 — Demo

- Recorrido automatizado.
- Reinicio determinista.
- Validación responsive.
- Guion comercial.

### A6 — Staging

Orden de integración:

1. Autenticación.
2. Perfil.
3. Saldo.
4. Cupones.
5. Newsfeed.
6. Transacciones.
7. Niveles.
8. Workflows.

Las credenciales y tokens no se expondrán en el frontend.

## Definición de terminado para la demo inicial

- Arranca con comandos documentados.
- Funciona en móvil y escritorio.
- Opera completamente en modo mock.
- Permite repetir y reiniciar el escenario.
- Diferencia eventos, intervenciones, incentivos y recompensas.
- Representa progresión como cambio de estado, no como mera acumulación.
- Muestra resultado, medición y aprendizaje.
- No contiene secretos.
- Supera las pruebas principales.
