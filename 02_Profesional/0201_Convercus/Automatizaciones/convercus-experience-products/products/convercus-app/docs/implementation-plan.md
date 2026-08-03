---
title: "Plan inicial de implementación de Convercus App"
aliases:
- "Plan de implementación de la demo canónica"
language: es
version: "v0.1"
status: "planificado"
date: "2026-07-17"
project: "Convercus App"
document_type: "plan de implementación"
scope: "fases, stack y criterios de construcción de la primera versión de Convercus App"
repository_role: "hoja de ruta técnica inicial del producto"
semantic_authority: "implementación subordinada al contrato semántico"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Plan inicial de implementación de Convercus App

## Objetivo de la primera versión

Construir una PWA mobile-first, repetible y demostrable, sin depender de staging. Será la primera instancia de una arquitectura configurable: el contenido, el escenario, el guion y las capacidades declaradas no quedarán incrustados en el núcleo de la App.

El marco que gobierna esta separación está en [canonical-demo-framework.md](canonical-demo-framework.md).

## Decisión de presentación móvil

Desde A1 existen dos vistas del mismo prototipo:

- la App responsive, que constituye la interfaz comercial;
- `/showcase`, una envolvente de presentación a 393 × 852 px con marco de iPhone.

El modo `/showcase` no es una implementación nativa ni demuestra compatibilidad con iOS. La instalación PWA, Safari, áreas seguras, HTTPS y funcionamiento offline en un iPhone real se validarán en A5.

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

### A0 — Preparación — completada

- [x] Crear rama de implementación.
- [x] Crear proyecto aislado dentro de `prototype/`.
- [x] Configurar calidad, pruebas y scripts.
- [x] Formalizar los contratos mínimos de dominio.
- [x] Definir el contrato de `DemoPackage` y su manifiesto de capacidades.

### A1 — Sistema visual y navegación — completada

- [x] Navegación mobile-first.
- [x] Componentes base.
- [x] Estados de carga, vacío y error.
- [x] Datos mock tipados.

### A2 — Fidelización

- Perfil.
- Puntos y nivel.
- Cupones.
- Noticias y actividad.

### A3 — Simulación de Experiences

- Motor local de eventos y estado.
- Panel interno de simulación.
- Primer escenario canónico completo.
- Cargar el escenario desde configuración, no desde componentes de interfaz.
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
- Validar una segunda configuración mínima sin bifurcar el núcleo.
- Preparar acceso seguro mediante HTTPS para un dispositivo real.
- Completar iconos, metadatos y comportamiento PWA específico de iOS.
- Instalar y validar la App en un iPhone real, incluida la experiencia offline prevista.

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
- Declara qué capacidades son reales, simuladas, mock, propuestas o no soportadas.
- Permite sustituir el paquete canónico sin modificar navegación ni lógica común.
