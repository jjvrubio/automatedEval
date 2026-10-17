---
title: "Protocolo de especificación de una demo"
aliases:
- "Protocolo de demos de Convercus App"
- "Demo Specification Protocol"
language: es
version: "v0.4"
status: "borrador de producto"
date: "2026-07-17"
project: "Convercus App"
document_type: "protocolo de especificación"
scope: "conversión de solicitudes comerciales en demos reproducibles con una o varias Experiences"
repository_role: "plantilla normativa de entrada y salidas para generar demos"
semantic_authority: "construcción de producto subordinada; no sustituye el contrato semántico"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
---

# Protocolo de especificación de una demo

## Estado

Borrador v0.4. Es una construcción de producto destinada a convertir una petición comercial en un paquete de demo reproducible. No sustituye al contrato semántico ni presupone capacidades técnicas no verificadas.

## Principio

La misma estructura debe servir para una descripción breve inicial y para una especificación más precisa. Los campos desconocidos pueden quedar pendientes; Codex deberá hacer explícitas sus inferencias y no presentar una hipótesis como información confirmada.

Una demo puede contener una o varias Experiences activas de forma simultánea. La especificación debe distinguir:

- la arquitectura de cada Experience;
- la participación concreta del miembro en cada una;
- las señales y eventos que pueden ser relevantes para una o varias Experiences;
- el recorrido seleccionado para hacer comprensible la demostración.

Que dos Experiences reciban o reconozcan la misma evidencia no implica que esta tenga en ambas el mismo significado o efecto. Cada Experience la evalúa conforme a su contexto, estado y reglas; puede producir progresión, una intervención, un cambio de estado o ningún efecto.

Una solicitud puede corresponder únicamente a capacidades de fidelización. En ese caso no se fabricará una Experience para completar la plantilla: se declarará que la capa experiencial TES no aplica a esa versión. Si la solicitud denomina Experience a una capacidad, deberá poder reconstruirla y validarla conforme a la baseline.

## Plantilla mínima

```markdown
# Solicitud de demo

## Cliente y contexto
- Cliente o marca:
- Sector:
- País e idioma:
- Audiencia de la demo:

## Objetivo
- Qué quiere conseguir el cliente:
- Qué queremos demostrar:
- Mensaje que debe recordar el interlocutor:

## Aplicabilidad TES y madurez de fidelización
- Nivel: fidelización operativa | contextual | orquestada | basada en Experiences
- ¿La demo presenta alguna capacidad como Experience?:
- Justificación de aplicabilidad TES:
- Capacidades de fidelización que quedan fuera del dominio experiencial TES:

## Miembro o protagonista
- Quién es:
- Situación inicial:
- Necesidad, intención u ocasión:
- Perfil de lealtad aplicable:
- Actor circunstancial primario:

## Experiences que se demostrarán, si procede

### Experience 1
- Nombre o identificador:
- Propósito:
- Hipótesis de transformación:
- Campo de mediación:
- Arquetipo de sujeto participante:
- Fuente y versión del arquetipo:
- Propensión ordinal en el sector:
- Escala, fuente y justificación de la propensión:
- Estado inicial:
- Resultado que se pretende observar:
- Baseline TES aplicable:

#### Arquitectura experiencial
- Señales relevantes y fuentes de evidencia:
- Eventos significativos:
- Propiedades de los eventos necesarias:
- Patrón o regularidad:
- Secuencia y rutas posibles:
- Estados, hitos o umbrales:
- Reglas de avance:
- Intervenciones:
- Incentivos:
- Recompensas:
- Resultado observado:
- Medición:
- Aprendizaje:

### Experience 2, si procede
- Repetir la estructura anterior.

## Participaciones simultáneas
- Experiences activas para el miembro:
- Estado actual en cada Experience:
- Prioridad o regla de coordinación entre intervenciones:
- Conflictos, exclusiones o dependencias:
- Continuidad, reentrada o cierre de cada participación:

## Señales, eventos y alcance experiencial
- Señales o datos recibidos:
- Fuente, fiabilidad y latencia:
- Evento significativo que puede derivarse:
- Experience o Experiences potencialmente afectadas:
- Regla aplicada dentro de cada Experience:
- Efecto independiente en cada participación:
- Tratamiento cuando no produce efecto:

## Contenido y fidelización
- Noticias o contenidos:
- Cupones o beneficios:
- Puntos, nivel o membresía:
- Vinculación de cada elemento con una o varias Experiences:

## Superficie, activos y recepción
- Audiencia y régimen de recepción:
- Simplificaciones de superficie admitidas:
- Arquitectura profunda que debe permanecer reconstruible:
- Activos de ecosistema:
- Activos de secuencia:
- Activos de resultado:
- Activos explicativos, de contraste o articulación:
- Instrucción suficiente para producir cada activo:

## Recorrido de demostración
- Estado inicial de cada participación visible:
- Señales que se producirán o simularán:
- Eventos que reconocerá el sistema:
- Experiences que evaluarán cada evento:
- Intervenciones visibles y Experience que las justifica:
- Cambios de estado o progresión por Experience:
- Coincidencias o interferencias entre Experiences:
- Resultado que se mostrará por Experience:
- Elementos de las Experiences que no se demostrarán:

## Identidad y tono
- Nombre visible de la App:
- Colores, logotipo o referencias:
- Tono y vocabulario:

## Alcance técnico
- Capacidades reales conocidas:
- Elementos que pueden simularse:
- Integraciones requeridas:
- Datos o acciones que no deben aparecer:

## Ejecución de la demo
- Duración disponible:
- Dispositivo o formato:
- Superficie: App responsive | modo iPhone `/showcase` | iPhone real:
- Requisitos de instalación, red, HTTPS u offline:
- Quién controla la demo:
- Condición de finalización:

## Validación TES
- Objeto, función y estrato validados:
- Nodo TES que rige cada dominio:
- Reconstruibilidad:
- Coherencia de capas:
- Integridad y clasificación de activos:
- Evidencia de resultado, eficacia o aprendizaje:
- Hallazgos y correcciones requeridas:
- Dictamen: conforme | conforme con ajuste menor | conforme condicionado | no conforme
```

## Salidas que debe producir Codex

A partir de la solicitud, Codex preparará:

1. resumen interpretado del caso;
2. preguntas o ambigüedades que cambien materialmente el resultado;
3. mapa de congruencia semántica;
4. declaración de aplicabilidad TES y nivel de madurez de fidelización;
5. inventario de Experiences, participaciones y relaciones entre ellas, cuando proceda;
6. matriz de señales y eventos por Experience, con sus reglas y efectos independientes;
7. mapa de arquetipos, propensiones sectoriales, fuentes y justificaciones;
8. inventario de pantallas, contenidos y activos clasificados;
9. escenario y estados de simulación;
10. manifiesto de capacidades reales, simuladas, mock y propuestas;
11. guion de demostración;
12. paquete de configuración implementable;
13. dictamen de validación TES cuando existan Experiences;
14. comprobaciones y limitaciones conocidas.

Cuando se solicite apariencia de iPhone, la salida deberá precisar si se pide el marco de presentación o una validación real en dispositivo. El marco `/showcase` no se registrará como prueba de compatibilidad con Safari/iOS ni como instalación PWA satisfactoria.

## Regla de aceptación

La generación no comienza silenciosamente si la petición confunde una Experience con un incentivo, un Workflow, una campaña o una secuencia sin progresión y resultado. Una demo de fidelización sin Experiences es admisible; presentar como Experience una capacidad no reconstruible no lo es.

Cuando existan Experiences, Codex no asumirá que una señal o un evento pertenece de forma exclusiva a una Experience, que produce el mismo efecto en todas las Experiences afectadas o que la simultaneidad permite fusionar sus estados, progresiones o resultados. Tampoco aceptará una Experience sin arquetipo participante, propensión ordinal sectorial justificada, cadena reconstruible, evidencia compatible y validación de capas y activos. Codex señalará la tensión y propondrá una traducción funcional compatible o una limitación explícita.
