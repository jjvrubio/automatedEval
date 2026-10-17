---
title: "ADR-001 — Autoridad semántica acotada del TES"
aliases:
- "Bounded TES Semantic Authority"
language: es
version: "v1.0"
status: "aceptado"
date: "2026-09-03"
project: "Convercus Experience Products"
document_type: "registro de decisión de arquitectura"
scope: "autoridad semántica del TES y límites de las extensiones funcionales y técnicas de producto"
repository_role: "decisión de arquitectura transversal"
semantic_authority: "producto subordinado a TES"
tes_baseline: "TES_CONVERCUS_BUILDER_2026_07_R1"
decision_id: "ADR-001"
decision_status: "accepted"
---

# ADR-001 — Autoridad semántica acotada del TES

## Estado

**Aceptado.**

## Contexto

Convercus App y TES Experience Builder necesitan operacionalizar Experiences mediante contratos de producto, interfaces, datos e integraciones. El TES, externo a este repositorio, define el significado de Experience y de los conceptos gobernados que la estructuran. Sin embargo, no prescribe la arquitectura ejecutable necesaria para convertir ese significado en software.

Interpretar la autoridad TES sin límites bloquearía decisiones legítimas sobre persistencia, APIs, privacidad, despliegue o proveedores. Interpretarla de forma débil permitiría que una conveniencia técnica, un dato mock o una representación visual redefinieran silenciosamente Experience. También haría posible que una nueva versión del TES reinterpretara datos históricos sin revisión.

Esta decisión formaliza el límite que sobrevivió a la falsificación de la Arquitectura v0.1 y concreta las políticas existentes de precedencia de fuentes, límites de producto y cambio semántico.

## Decisión

El TES es la autoridad sobre el **significado, las relaciones y los invariantes semánticos** de Experience y de sus conceptos gobernados.

El TES no es autoridad sobre arquitectura de software, persistencia, APIs, despliegue, privacidad, cachés, credenciales ni implementación de proveedores. Esas decisiones pertenecen a los niveles funcional y técnico del producto, sujetos a no contradecir el contrato semántico aplicable.

Las extensiones funcionales y técnicas están permitidas cuando cumplen simultáneamente estas condiciones:

1. se clasifican explícitamente como derivación TES, traducción funcional, construcción de producto, capacidad técnica o elemento de interfaz;
2. no sustituyen ni redefinen silenciosamente un concepto TES;
3. declaran cualquier pérdida, mediación o limitación de representación;
4. conservan trazabilidad semántica cuando operacionalizan una Experience;
5. mantienen separadas su propia versión técnica y la baseline TES que interpretan.

Toda `ExperienceDefinition` debe identificar la baseline TES contra la que fue validada. Un cambio de baseline no reinterpreta automáticamente definiciones o participaciones ya versionadas.

## Alcance de autoridad

| Ámbito | Autoridad | Regla aplicable |
|---|---|---|
| Definición de Experience y conceptos TES gobernados | TES | La baseline declarada fija significado, relaciones e invariantes. |
| Derivación semántica utilizada por el producto | Contrato semántico de producto | Debe ser trazable a TES y no adquiere autoridad ontológica propia. |
| Traducción a capacidades y comportamiento de producto | Producto | Puede mediar o limitar, pero no redefinir TES. |
| Arquitectura, almacenamiento, APIs, despliegue, privacidad y proveedores | Arquitectura técnica y políticas operativas | Se deciden fuera del TES y se clasifican como no-TES. |
| Representación visual y read models | Producto/interfaz | Simplifican la superficie sin alterar el significado subyacente. |
| Evolución del corpus TES | Gobernanza TES | Solo afecta al producto tras una evaluación explícita de impacto. |

La precedencia permanece:

```text
Definición ontológica TES
        >
Contrato semántico de producto
        >
Modelo funcional
        >
Modelo de interacción
        >
Representación visual
        >
Conveniencia técnica
```

## Consecuencias

### Positivas

- Las decisiones técnicas pueden evolucionar sin fingir que proceden del TES.
- Experience conserva un significado estable y reconstruible a través de productos e implementaciones.
- Los conceptos técnicos necesarios —por ejemplo `AppSnapshot`, referencias de procedencia, cachés o adaptadores— pueden existir sin solicitar estatuto ontológico.
- Las versiones históricas permanecen reproducibles porque su baseline no cambia implícitamente.
- Una limitación técnica puede declararse como tal en vez de resolverse mediante una equivalencia semántica falsa.

### Costes y obligaciones

- Los contratos y especificaciones deben clasificar las extensiones no-TES relevantes.
- La operacionalización de Experience debe conservar referencias de baseline y trazabilidad suficiente.
- Los cambios TES requieren evaluación de impacto y, cuando corresponda, nueva validación o migración explícita.
- Pueden coexistir durante un tiempo definiciones validadas contra baselines diferentes.
- El producto debe admitir `unsupported`, mediación explícita o reducción de alcance cuando no pueda representar fielmente una definición.

## Interpretaciones prohibidas

Esta decisión no permite:

- afirmar que TES prescribe una base de datos, una API, event sourcing, un proveedor o una topología de despliegue;
- presentar `Observed Occurrence`, `Demo Manifest`, `AppSnapshot`, `Activity`, `DataAdapter` o `Demo Script` como conceptos TES por el mero hecho de ser útiles;
- tratar una pantalla, un endpoint, un Workflow, un fixture o una convención de código como definición de Experience;
- omitir la clasificación no-TES de una extensión que pueda confundirse con semántica gobernada;
- redefinir un concepto TES dentro de una extensión técnica o de producto;
- asumir que «la última versión del TES» sustituye la baseline declarada por una definición existente;
- migrar o reinterpretar automáticamente definiciones versionadas por la aparición de una baseline posterior;
- considerar la trazabilidad como obligación de copiar el corpus TES completo dentro de cada artefacto.

## Implicaciones de versionado

1. La baseline TES y la versión del contrato técnico son identificadores independientes.
2. Cada `ExperienceDefinition` versionada conserva `tesBaseline` y la evidencia de validación correspondiente.
3. Las referencias a definiciones deben identificar una versión o digest cuando su mutación pueda afectar a reproducibilidad.
4. Adoptar una nueva baseline abre el proceso de cambio semántico y produce uno de los resultados gobernados: sin impacto, aclaración, cambio funcional, cambio de interacción, migración, no soportado o diferido.
5. Una definición existente mantiene su interpretación original hasta que una decisión explícita cree una versión nueva o autorice una migración trazable.
6. Una aclaración técnica que no altere significado puede versionarse sin cambiar de baseline, siempre que quede registrada como tal.

## Condiciones de reconsideración

La decisión debe revisarse si ocurre cualquiera de estas condiciones:

- la gobernanza TES cambia explícitamente su ámbito y asume autoridad sobre contratos ejecutables hoy externos;
- no puede trazarse una Experience implementada a una baseline identificable;
- casos reales demuestran que una extensión necesaria altera inevitablemente un invariante TES;
- el proceso de cambio semántico no puede representar migraciones o coexistencia entre baselines sin reinterpretación silenciosa;
- aparece una contradicción normativa entre el TES y el contrato semántico congelado que no pueda resolverse mediante la precedencia vigente;
- requisitos legales o regulatorios obligan a retirar o transformar datos de forma incompatible con las garantías aquí definidas.

## Revisión de aceptación

Permanece abierta la forma operativa exacta de migrar definiciones entre baselines, pero esa cuestión no impide aceptar el límite de autoridad: la política vigente ya exige evaluación y prohíbe la reinterpretación automática. La mecánica de migración podrá decidirse por separado cuando exista un caso concreto.
