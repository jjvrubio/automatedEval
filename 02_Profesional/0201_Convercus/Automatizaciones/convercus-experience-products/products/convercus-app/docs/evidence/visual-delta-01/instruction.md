# Convercus Demo Factory — DELTA VISUAL 01

## Sports Season / Brisa Sport — adopción de la paleta Convercus

## 0. Propósito

BUILD 01 está cerrado con:

```text
BUILD COMPLETED
→ READY FOR HUMAN UX CHALLENGE
```

La demo Sports Season es funcional y no debe ampliarse en esta intervención.

Esta instrucción autoriza exclusivamente un **delta visual cromático** antes del desafío humano:

```text
Brisa Sport
→ utilizar paleta Convercus
```

No constituye BUILD 02.

No abre H40.

No modifica la Demo Definition.

No cambia comportamiento, estructura, navegación, copy, reglas, estado, Evidencia ni recorrido.

---

# 1. Principio

Aplicar:

```text
VISUAL BRAND CONFIGURATION
!=
PRODUCT SEMANTICS
```

y:

```text
PALETTE CHANGE
!=
UX REDESIGN
```

El objetivo consiste únicamente en adoptar la paleta cromática Convercus dentro de la identidad ficticia de Brisa Sport.

La marca continúa siendo:

```text
Brisa Sport
```

No convertirla en una demo llamada Convercus.

No introducir branding comercial adicional de Convercus salvo los colores.

---

# 2. Paleta autorizada

Utilizar exclusivamente como paleta principal:

```text
Ultramarine
#090685

Mid Blue
#092BFD

Tech Blue
#0AEFFF

Berry Red
#F72585

Warm Grey
#F1F1F1

White
#FFFFFF
```

No introducir una segunda paleta sustitutiva.

Los colores neutros estrictamente necesarios para texto, bordes, sombras o estados de accesibilidad pueden conservarse si ya existen y son necesarios para legibilidad.

No reinterpretar esos neutros como nuevos colores de marca.

---

# 3. Roles cromáticos preferidos

Aplicar aproximadamente esta responsabilidad visual:

```text
#090685
→ color primario
→ cabecera
→ navegación
→ acciones principales
→ elementos seleccionados cuando proceda

#092BFD
→ color interactivo secundario
→ controles
→ enlaces
→ foco / estados interactivos cuando proceda

#0AEFFF
→ acento
→ indicadores
→ detalles gráficos
→ elementos de énfasis no dominantes

#F72585
→ reconocimiento
→ insignia
→ hitos visuales relacionados con reconocimiento

#F1F1F1
→ fondos secundarios
→ paneles
→ separación de superficies

#FFFFFF
→ superficie principal
→ espacios de respiración
```

Estos roles son una orientación visual.

No deben obligar a modificar estructura o comportamiento para hacerlos encajar.

---

# 4. Insignia

Utilizar preferentemente:

```text
Berry Red
#F72585
```

como color distintivo del reconocimiento.

La finalidad es separar visualmente:

```text
acción / navegación
```

de:

```text
reconocimiento conseguido
```

No convertir por ello la insignia en:

```text
beneficio
cupón
trofeo
nivel
```

Su significado funcional permanece exactamente igual.

---

# 5. Tech Blue

`#0AEFFF` debe utilizarse como acento.

Evitar su empleo para:

```text
texto pequeño sobre blanco
párrafos
información crítica de bajo contraste
```

Si un uso propuesto no proporciona contraste razonable:

```text
DO NOT USE IT THERE
```

No alterar el significado de estados o controles para poder utilizar todos los colores de la paleta.

No es obligatorio que los seis colores aparezcan con la misma intensidad o frecuencia.

---

# 6. Frontera de implementación

Inspeccionar primero:

```text
sports-season/artifacts.ts
sports-season.css
BrandArtifact / tokens existentes
brisa-logo.svg
```

y los consumidores cromáticos directamente relacionados.

Preferir:

```text
brand tokens
→ visual consumer
```

frente a:

```text
hard-coded Convercus colours
inside behavioural components
```

Cuando sea razonable con la estructura existente, hacer que la identidad cromática proceda de la configuración/tokens de marca ya disponibles.

No crear en esta intervención:

```text
theme engine
design system
generic theming framework
CSS abstraction layer
brand editor
palette editor
```

Si algún color debe permanecer local en `sports-season.css`, mantenerlo acotado a la superficie Sports Season.

---

# 7. Logo

No rediseñar el logo Brisa Sport en esta intervención.

Sólo modificarlo si contiene colores incompatibles que impidan materialmente la coherencia cromática.

En tal caso:

```text
same logo
same geometry
same text
same meaning
→ colour substitution only
```

No crear una nueva identidad visual.

---

# 8. Prohibiciones expresas

No modificar:

```text
recorrido
orden de elementos
posición del formulario
posición del selector Participante / Marketing-CRM
longitud del recorrido móvil
copy
densidad informativa
mensajes de procedencia
formularios
acciones
validaciones
modalidades
regla de insignia
Evidencia
runtime
estado
reset
navegación
perspectivas
Demo Definition
```

En particular, no corregir todavía las fricciones UX ya observadas en BUILD 01.

Esas fricciones deben permanecer disponibles para el desafío humano.

---

# 9. No convertir presentación en semántica

El color no debe controlar:

```text
elegibilidad
estado
Evidencia
membresía
modalidad
reconocimiento
oportunidad
```

Cambiar un token cromático debe poder alterar únicamente la presentación.

Mantener:

```text
visual token
!=
business rule
```

---

# 10. Accesibilidad mínima

Comprobar que el cambio no deteriora materialmente:

```text
legibilidad
contraste de texto
visibilidad de controles
focus visible
estado seleccionado
mensajes de error
```

No realizar un proyecto general de accesibilidad.

Corregir únicamente un problema cromático introducido por este delta.

---

# 11. Verificación funcional

Después del delta, ejecutar las comprobaciones actuales pertinentes.

Como mínimo verificar que sigue funcionando:

```text
abrir Sports Season
→ elegir modalidad
→ inscripción
→ check-in simulado
→ declarar esfuerzo
→ insignia
→ invitación al club
→ Marketing / CRM
→ regreso a participante
→ reset
```

El resultado factual debe permanecer idéntico al BUILD 01.

No actualizar expectativas funcionales para acomodar el cambio visual.

---

# 12. Verificación visual

Inspeccionar al menos:

```text
inicio — escritorio
insignia — escritorio o móvil
Marketing / CRM
error de formulario
```

Comprobar:

```text
coherencia de paleta
contraste
ausencia de regresión visual grave
ausencia de overflow nuevo
distinción acción / reconocimiento
```

No evaluar todavía si la UX es buena.

No rediseñar aquello que parezca incómodo.

---

# 13. Preservación

Mantener intactos:

```text
informes S01–S39
BUILD 01
SAFE-TO-BUILD review
Demo Definition v0.2
evidencia histórica
tests históricos
reglas deportivas
datos funcionales
```

Registrar el cambio como:

```text
VISUAL DELTA 01
```

separado de BUILD 01.

---

# 14. Demo-Author UX

Registrar una única observación adicional:

```text
¿hasta qué punto cambiar la paleta de una demo
ha podido realizarse mediante BrandArtifact/tokens
frente a edición directa de CSS/assets?
```

No resolver la fricción observada.

No construir una herramienta de tematización.

Este dato servirá posteriormente para estudiar la futura autoría de demos a partir de narrativa/protocolo.

---

# 15. STOP

Detenerse si incorporar la paleta exige modificar:

```text
runtime
contratos funcionales
reglas
estado
arquitectura de composición
estructura del recorrido
```

Eso indicaría un acoplamiento visual inesperado que debe documentarse antes de continuar.

No arquitectar alrededor del problema dentro de este delta.

---

# 16. Informe final

Entregar un informe breve con:

```text
A. archivos modificados
B. tokens/colores anteriores → nuevos
C. usos finales de cada color Convercus
D. cambios directos de CSS que hayan sido inevitables
E. comprobaciones funcionales
F. comprobaciones visuales
G. observación Demo-Author UX
H. límites
```

Finalizar con:

```text
VISUAL DELTA 01
→ COMPLETED
→ READY FOR HUMAN UX CHALLENGE
```

o, si aparece el acoplamiento definido en STOP:

```text
VISUAL DELTA 01
→ STOPPED
→ UNEXPECTED VISUAL/FUNCTIONAL COUPLING OBSERVED
```

---

# 17. Finalidad

Después de esta intervención no continuar desarrollando.

No corregir UX.

No construir el siguiente corte.

No abrir H40.

El siguiente paso será:

```text
HUMAN USE
→ OBSERVATION
→ CRITIQUE
```

La demo debe quedar funcionalmente equivalente a BUILD 01, con una única diferencia deliberada:

```text
Brisa Sport
→ paleta visual Convercus
```
