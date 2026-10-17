# VISUAL DELTA 01 — Brisa Sport / paleta Convercus

2026-09-24. Brisa Sport conserva su identidad ficticia y su recorrido. Cambio exclusivamente cromático, separado de BUILD 01. [Instrucción recibida](evidence/visual-delta-01/instruction.md).

Disponible en [vista iPhone](http://127.0.0.1:4173/showcase?demo=sports-season-running) y [escritorio](http://127.0.0.1:4173/?demo=sports-season-running), mientras esté activo el servidor local.

## A. Archivos modificados

Tres archivos de producto:

- [sports-season/artifacts.ts](../prototype/src/demo-factory/sports-season/artifacts.ts): únicamente colores de `sportsBrand.cssVariables`.
- [sports-season.css](../prototype/src/styles/sports-season.css): consumidores cromáticos conectados a esos tokens.
- [brisa-logo.svg](../prototype/src/demo-factory/sports-season/brisa-logo.svg): tres sustituciones de color; misma geometría, dimensiones y texto.

Se añaden este informe y [evidencia separada](evidence/visual-delta-01/preservation.json). De 749 archivos recibidos, 746 permanecen idénticos y sólo cambian los tres anteriores. Los 572 documentos, tests y fixtures históricos comprobados permanecen intactos, incluidos BUILD 01, SAFE-TO-BUILD y S01–S39. Demo Definition, runtime, contratos, React, navegación, datos funcionales y configuración de herramientas permanecen intactos.

## B. Tokens y colores anteriores → nuevos

| Token existente en BrandArtifact | Antes en Brisa Sport | Ahora |
| --- | --- | --- |
| `--color-primary` | `#193e37` | `#090685` |
| `--color-primary-action` | `#225d4b` | `#092BFD` |
| `--color-background` | `#fbfaf5` | `#FFFFFF` |
| `--color-surface` | `#f0efe6` | `#F1F1F1` |
| `--color-text` | `#263b33` | `#333333` |
| `--color-text-strong` | `#18382e` | `#000000` |
| `--color-text-muted` | `#5a6960` | `#5F5F5F` |
| `--color-focus` | `#225d4b` | `#092BFD` |
| `--color-on-primary` | `#ffffff` | `#FFFFFF`, equivalente |

Brisa declara también cinco roles que ya existían en los consumidores de marca del proyecto: `--color-accent=#0AEFFF`, `--color-highlight=#F72585`, `--color-border=#5F5F5F`, `--color-on-action=#FFFFFF` y `--color-on-accent=#000000`. Sin cambio de contrato ni tipografía. Negro y grises de texto proceden de los neutros ya presentes en la marca Convercus; no se introduce otra paleta.

Logo: verde `#225d4b` → Mid Blue; terracota `#d2673f` → Tech Blue; texto verde `#193e37` → Ultramarine. Sus colores anteriores mantenían materialmente la identidad cromática verde/terracota; sólo se sustituyen los rellenos.

## C. Usos finales de la paleta

| Color | Uso |
| --- | --- |
| Ultramarine `#090685` | Texto del logo, títulos, perspectiva activa, acciones principales, selección y base gráfica del bloque introductorio |
| Mid Blue `#092BFD` | Acciones secundarias, enlaces, radios, foco, hover de acciones y una forma del logo |
| Tech Blue `#0AEFFF` | Líneas decorativas, «Conecta.» sobre Ultramarine, detalles de evidencia y forma secundaria del logo; ningún párrafo ni texto pequeño sobre blanco |
| Berry Red `#F72585` | Medallón y borde del reconocimiento; símbolo negro sobre Berry Red |
| Warm Grey `#F1F1F1` | Paneles, navegación, superficies secundarias, selección y fondo exterior |
| White `#FFFFFF` | Superficie principal, formulario, paneles y texto sobre acciones oscuras |

La insignia mantiene su significado individual. La oportunidad y los errores no reciben el color distintivo del reconocimiento.

## D. Edición directa de CSS y asset

Cambiar sólo BrandArtifact no bastaba: Sports Season tenía colores literales repartidos por el CSS y tres rellenos en el SVG. Se sustituyen por referencias a los roles existentes, asignando por separado usos que antes compartían verde. Se añaden únicamente dos declaraciones de fondo, limitadas a Sports Season y su marco móvil, para sustituir el fondo cromático heredado.

La [auditoría cromática](evidence/visual-delta-01/colour-only-audit.json) verifica que todas las declaraciones CSS no cromáticas son idénticas; el [patch](evidence/visual-delta-01/product-delta.patch) conserva el detalle. No cambian dimensiones, orden, espaciado, tipografía, formulario ni longitud del recorrido. El SVG externo conserva colores literales; no se construye un mecanismo para tematizar assets.

## E. Comprobaciones funcionales

- 17 tests deportivos PASS antes y después, con expectativas intactas. La traza posterior es byte-idéntica a la previa y a la conservada en BUILD 01: seis combinaciones de modalidad y esfuerzo con los mismos hechos, evidencia, regla, insignia y oportunidad.
- Suite completa: **112 PASS / 18 FAIL / 0 skipped**. Son los mismos 18 fallos históricos por guards de hashes ya documentados; ningún fallo nuevo. No se presenta la suite como verde.
- Typecheck, lint y build: PASS.
- Navegador: 20 fases PASS en escritorio y móvil. Incluyen apertura, errores por elecciones vacías, modalidad, inscripción, check-in simulado, esfuerzo, insignia, invitación, CRM, regreso y reset. Sin errores de página/consola ni overflow horizontal.

[Resultados y equivalencia](evidence/visual-delta-01/equivalence.json), [comandos y exit codes](evidence/visual-delta-01/checks.json), [reporter completo](evidence/visual-delta-01/tests-after.json).

## F. Comprobaciones visuales

Inspeccionadas las capturas de [inicio escritorio](evidence/visual-delta-01/browser-after/desktop-initial.png), [insignia](evidence/visual-delta-01/browser-after/desktop-badge.png), [CRM](evidence/visual-delta-01/browser-after/desktop-crm.png), [error móvil](evidence/visual-delta-01/browser-after/mobile-registration-error.png) y [marco iPhone](evidence/visual-delta-01/phone-after.png). Paleta coherente, controles legibles y reconocimiento rosa diferenciado de acciones azules.

322 muestras de texto en seis estados pasan el contraste comprobado; mínimo observado 5,65:1. Foco de teclado de 3 px: 6,70:1 frente a su superficie; borde seleccionado: 13,51:1; símbolo de insignia: 5,56:1. Errores con texto oscuro sobre Warm Grey y borde negro. [Informe de contraste y límites](evidence/visual-delta-01/contrast-report.json).

La comparación de 20 fases conserva texto y geometría. Única variación geométrica medida: ancho de cuatro horas del CRM, menor de 0,54 px, por los distintos dígitos del reloj entre ejecuciones; posición y altura iguales. No se corrigen las fricciones UX de BUILD 01.

## G. Observación Demo-Author UX

La paleta puede declararse en BrandArtifact, pero adoptar esos colores exigió conectar manualmente consumidores CSS y recolorear el SVG. La configuración de marca por sí sola no cubría esta superficie. Se registra esta fricción sin construir herramientas de autoría ni una infraestructura de temas.

## H. Límites

Intervención limitada a Brisa Sport; no se recolorean otras demos ni se añade una política automática de selección de marca. Se mantiene la preferencia de usar la paleta Convercus para futuras demos sin cliente identificado, sin ampliar esta implementación. Sin nueva identidad comercial, rediseño, cambios semánticos, BUILD 02 ni H40.

Inspección con Edge headless y perfil temporal; el navegador integrado no dispone de herramienta de control en esta sesión. Contraste sobre fondos sólidos calculados y revisión visual; no constituye auditoría general de accesibilidad ni validación en dispositivo real. Uso humano, aceptación de UX y comercial siguen pendientes. No se observa el acoplamiento visual/funcional definido en STOP.

VISUAL DELTA 01
→ COMPLETED
→ READY FOR HUMAN UX CHALLENGE
