---
title: "ADR-003 — Composición deseada y efectiva de una demo"
aliases:
- "Desired and Effective Demo Composition"
language: es
version: "v1.0"
status: "aceptado"
date: "2026-09-03"
project: "Convercus Experience Products"
document_type: "registro de decisión de arquitectura"
scope: "separación entre la intención declarada de una demo y la composición que el entorno puede resolver"
repository_role: "decisión de arquitectura de Demo Factory"
semantic_authority: "construcción técnica de producto subordinada; no modifica TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
decision_id: "ADR-003"
decision_status: "accepted"
---

# ADR-003 — Composición deseada y efectiva de una demo

## Estado

**Aceptado.**

## Contexto

El experimento de Session 5 demostró que un mismo núcleo React puede ejecutar dos demos materialmente distintas cuando recibe una composición resuelta antes del render. Retail y Hospitality declaran referencias diferentes a marca y fixtures; Hospitality añade Scenario, Experience reference y Demo Script. `bootstrap.ts` valida esas referencias, instancia el mock con el fixture correspondiente y entrega a `App.tsx` un runtime efectivo. Un identificador desconocido, una marca o fixture ausente y una capability no resoluble producen errores explícitos.

Antes del experimento, `DemoPackage`, `canonical-demo-package.ts` y `app.yaml` describían partes solapadas de una demo sin componer el runtime. También existía el riesgo de tratar un paquete declarativo como autoridad simultánea sobre intención, implementaciones, secretos y estado mutable.

La evidencia apoya separar la declaración de lo deseado de aquello que el entorno puede materializar. No apoya todavía una topología final de catálogos, selección de deployment o providers.

## Decisión

Demo Factory distinguirá siempre:

```text
composición deseada != composición efectiva
```

Un manifiesto versionado declara la **composición deseada** de una demo. Un límite de bootstrap/resolución, condicionado por el deployment o entorno, valida referencias y determina la **composición efectiva** que puede instanciarse.

La aplicación consume composición efectiva. No interpreta por sí sola referencias declarativas ni selecciona implementaciones concretas.

## Composición deseada

El manifiesto expresa intención lógica. Según las necesidades de cada demo puede declarar o referenciar:

- identidad de demo y prospecto;
- marca y locale;
- Scenario y referencias a Experience;
- módulos visibles;
- fixtures o estado inicial controlado;
- requisitos de capabilities y expectativas de procedencia;
- Demo Script opcional;
- alcance de reset.

La lista no obliga a que todos esos campos existan en el contrato actual ni a que sean obligatorios en todas las demos. El manifiesto debe mantenerse pequeño: cuando un artefacto tenga identidad o ciclo de vida propios, se referencia en lugar de copiarse dentro del manifiesto.

Las referencias necesarias para reproducibilidad deben estar versionadas, fijadas mediante digest o sujetas a otro mecanismo equivalente. La versión del esquema no sustituye a la versión de la instancia del manifiesto.

## Composición efectiva

Bootstrap/resolución determina qué puede materializarse en el entorno actual a partir de:

- existencia y compatibilidad de los artefactos referenciados;
- providers e implementaciones disponibles;
- restricciones del deployment o entorno;
- disponibilidad y procedencia real de capabilities;
- resultados de validación;
- políticas operativas aplicables.

La composición efectiva puede aceptar, rechazar o cualificar la intención declarada. Una referencia requerida no resuelta detiene el arranque con un error explícito. No se permite sustituir silenciosamente una demo, marca, fixture o capability por los de otro prospecto.

Una capability solicitada y una capability resuelta son conceptos distintos. La primera expresa necesidad o expectativa; la segunda identifica disponibilidad, implementación y procedencia efectivas.

## Límites de autoridad

| Ámbito | Autoridad | Responsabilidad |
|---|---|---|
| TES | Significado semántico gobernado | Define significado, relaciones e invariantes de Experience y conceptos TES. |
| Contratos de producto versionados | Traducción funcional | Expresan formas de producto subordinadas a la baseline TES aplicable. |
| Demo manifest | Composición deseada | Declara intención y referencias; no garantiza disponibilidad. |
| Bootstrap/resolución | Composición efectiva | Valida, resuelve, cualifica o rechaza la intención. |
| Deployment/entorno | Restricciones e implementaciones disponibles | Aporta secretos, endpoints, providers permitidos y políticas operativas. |
| Runtime session | Estado mutable cuando sea necesario | Controla o referencia el estado efectivo de la ejecución. |
| Read models/UI | Presentación | Proyectan estructuras consumibles sin adquirir autoridad factual o semántica. |

## Restricciones obligatorias

1. Un prospecto puede poseer cero, una o varias demos.
2. Un manifiesto no representa por defecto al prospecto completo.
3. El manifiesto no contiene secretos, credenciales ni detalles sensibles del entorno.
4. El manifiesto no almacena estado mutable de runtime.
5. Toda referencia requerida no resuelta falla explícitamente.
6. Capability solicitada y capability resuelta permanecen diferenciadas.
7. Las referencias necesarias para reproducibilidad se versionan o fijan de forma equivalente.
8. El manifiesto no se convierte en una configuración soberana que copie todos los artefactos.
9. Deployment/bootstrap puede rechazar o cualificar la composición deseada.
10. La selección mediante query parameter utilizada en Session 5 no forma parte de esta decisión.
11. Los catálogos estáticos locales del experimento no se declaran arquitectura final de registry.
12. El único mock provider actual no se declara arquitectura final de providers.

## Consecuencias

### Positivas

- El mismo core puede recibir composiciones diferentes sin branches por prospecto.
- Los fallos de referencia aparecen antes de presentar datos de otra demo.
- Secretos, restricciones de deployment y clases concretas quedan fuera del manifiesto.
- El estado mutable y los read models no contaminan la declaración de intención.
- Las capabilities pueden revelar una realidad distinta de la expectativa declarada.
- Cambiar el mecanismo de selección o registry no exige redefinir qué significa composición deseada.

### Costes y obligaciones

- Deben existir contratos y errores legibles en la frontera de resolución.
- Las referencias y sus versiones requieren gobierno de compatibilidad.
- El runtime necesita conservar trazabilidad a la intención que lo originó.
- Los documentos y artefactos anteriores que solapan composición deben migrarse o marcarse como legacy.
- La validación debe distinguir ausencia requerida, incompatibilidad y cualificación permitida.

## Interpretaciones prohibidas

Este ADR no establece:

- que el manifiesto sea un `DemoPackage` monolítico;
- que el manifiesto contenga todos los datos, reglas o artefactos;
- que una demo equivalga a un prospecto;
- que `schemaVersion` baste para versionar una instancia;
- que el query parameter sea el mecanismo productivo de selección;
- que los catálogos TypeScript sean el registry definitivo;
- que todas las capabilities utilicen un solo provider o un mismo contrato;
- que bootstrap pueda redefinir conceptos TES;
- que resolver una referencia conceda autoridad sobre estado live;
- que la composición efectiva deba persistirse como una copia completa.

## Evidencia de aceptación

- El mismo `App.tsx` renderiza Retail y Hospitality mediante `ResolvedDemoRuntime`.
- `App.tsx` no importa `MockDataAdapter`, fixtures ni identidades de prospecto.
- Los manifiestos no contienen `providerId`, secretos ni estado mutable.
- Bootstrap resuelve marca, fixture, Scenario, Experience reference, Script, provider y capabilities.
- Las pruebas verifican demo desconocida, referencias requeridas ausentes, capability no resuelta, aislamiento y ausencia de fuga cruzada.
- La prueba de cardinalidad admite dos `demoId` para un mismo `prospectId`.

La implementación actual no posee una versión explícita de instancia de manifiesto y resuelve todas las capabilities al mismo mock. Son cualificaciones de implementación, no objeciones a la decisión de separar autoridades.

## Implicaciones de versionado

- Deben versionarse independientemente el esquema del manifiesto, la instancia del manifiesto y los artefactos referenciados cuando afecten a reproducibilidad.
- Cambiar una referencia puede producir una nueva versión de demo aunque el esquema no cambie.
- La composición efectiva debe permitir identificar la versión o digest de la intención resuelta.
- Una actualización de provider no reinterpreta silenciosamente el manifiesto ni la baseline TES.
- La política concreta de compatibilidad y migración se decidirá cuando exista evidencia adicional; no forma parte de este ADR.

## Condiciones de reconsideración

La decisión se revisará si:

- una tercera demo compatible no puede incorporarse sin branches de prospecto en el core;
- un entorno real demuestra que intención y resolución no pueden separarse sin perder garantías esenciales;
- la reproducibilidad exige capturar información que no puede expresarse por referencias fijadas;
- la validación previa no puede impedir fugas silenciosas entre prospectos;
- una política regulatoria obliga a trasladar responsabilidades entre manifiesto, deployment y runtime;
- el coste de mantener ambas representaciones supera de forma demostrable su valor de aislamiento y trazabilidad.
