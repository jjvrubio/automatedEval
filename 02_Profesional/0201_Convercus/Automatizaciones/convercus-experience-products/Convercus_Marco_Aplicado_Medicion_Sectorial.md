---
titulo: Convercus_Marco_Aplicado_Medicion_Sectorial
aliases:
  - Marco aplicado de KPI sectoriales para Convercus
  - Aplicación Convercus de la medición sectorial TES
idioma: es
fecha: '2026-07-26'
version: v1.0
estado: activo_en_proyecto_convercus
estado_edicion: externalizado_desde_tes
tipo: aplicacion_derivada_de_medicion
capa: proyecto_convercus
alcance: seleccion_uso_e_instrumentacion_de_kpi_de_comportamiento_resultado_y_operacion_sectorial_mediante_convercus
funcion: aplicar_la_gramatica_y_las_definiciones_kpi_del_tes_a_diagnosticos_pilotos_propuestas_y_operacion_convercus_sin_redefinir_los_indicadores_ni_confundirlos_con_kpi_de_plataforma
canonico: false
fuentes_metodologicas:
  - TES/medicion/TES_KPI_Dictionary
  - TES/medicion/TES_KPI_Sectores
procedencia:
  - KPI Dictionary VERTICALS v1_6
tags:
  - Convercus
  - KPI
  - medicion
  - fidelizacion
  - comportamiento-consumidor
  - sectores
  - plataforma
---

# Convercus_Marco_Aplicado_Medicion_Sectorial

## 0. Estatuto

Este documento es una aplicación derivada para el proyecto Convercus.

No redefine:

- las fichas KPI;
- sus fórmulas;
- la arquitectura de IDs;
- los niveles de atribución;
- ni los módulos sectoriales.

Esos elementos permanecen gobernados por:

- `TES_KPI_Dictionary`;
- `TES_KPI_Sectores`.

Su función es seleccionar, relacionar e instrumentar KPI mediante capacidades de Convercus.

## 1. Principio de independencia del KPI

La mayor parte de los KPI utilizados por Convercus miden:

- comportamiento del consumidor;
- respuesta a mecanismos de fidelización;
- recurrencia;
- identificación;
- conversión;
- margen;
- coste de servicio;
- operación sectorial;
- y resultados de negocio.

Estos KPI no pertenecen a una plataforma concreta.

La cadena correcta es:

> **comportamiento o resultado → mecanismo de intervención → sistema habilitador → implementación tecnológica**

Convercus puede ser el sistema habilitador o la implementación observada. No es la definición del KPI.

## 2. Tres planos de medición

### 2.1. Comportamiento y resultado

Responde a:

- qué hace el consumidor;
- qué transición ocurre;
- qué resultado económico u operativo se observa;
- y qué diferencia puede contrastarse.

Utiliza los IDs y fichas de TES.

### 2.2. Mecanismo e intervención

Responde a qué capacidad se utiliza para intentar producir el cambio:

- journeys;
- personalización;
- omnicanalidad;
- venta social;
- gamificación;
- programa de socios;
- incentivos;
- mensajería;
- identificación;
- orquestación;
- y automatización.

El mecanismo no garantiza el resultado.

### 2.3. Desempeño operativo de plataforma

Responde a si la tecnología permite ejecutar el mecanismo de forma productiva, estable y eficiente.

Puede incluir:

- disponibilidad;
- latencia;
- integridad de eventos;
- calidad de integración;
- automatización;
- productividad del usuario;
- tasa de error;
- recuperación;
- adopción funcional;
- coste operativo;
- y eficiencia de ejecución.

Esta familia no usa todavía IDs TES. Requiere un diccionario tecnológico propio o una extensión contrastada.

## 3. Mapa KPI → capacidad Convercus

- **Journeys:** KPI-055, KPI-059, KPI-060, KPI-061, KPI-062, KPI-067  
- **Omnicanalidad:** KPI-056, KPI-058, KPI-064, KPI-065  
- **Venta social:** KPI-054, KPI-056, KPI-058  
- **Gamificación:** KPI-068, KPI-070, KPI-059, KPI-076  
- **Programa de socios:** KPI-059, KPI-073, KPI-075, KPI-076

### Regla de uso

El mapa identifica relaciones plausibles de instrumentación.

No autoriza afirmar que:

- una capacidad cause por sí sola el KPI;
- el KPI solo pueda moverse mediante Convercus;
- ni el resultado observado sea atribuible sin método de contraste.

Cada piloto deberá declarar:

```yaml
KPI:
Resultado esperado:
Mecanismo de intervención:
Capacidad Convercus:
Eventos instrumentados:
Cohorte o población:
Baseline o control:
Método de atribución:
Guardarraíl:
Compuerta de decisión:
KPI operativo de plataforma, si aplica:
```

## 4. Selección de KPI para pilotos

No existe un paquete universal válido para cualquier sector.

Todo piloto debería combinar:

1. **habilitación de trazabilidad**, cuando sea necesaria;
2. **comportamiento o progresión**;
3. **resultado económico**;
4. **eficiencia operativa**;
5. **guardarraíl sectorial**;
6. **método de contraste**;
7. **desempeño de plataforma**, cuando la ejecución tecnológica sea parte del objeto.

### Paquete transversal orientativo

- `KPI-010` — identificación, cuando el piloto necesite trazabilidad individual;
- `KPI-012` — repetición, cuando la ventana permita observarla;
- `KPI-003` — margen de contribución por transacción;
- un KPI sectorial de resultado;
- un KPI sectorial de fricción o riesgo;
- uno o más indicadores operativos de plataforma, separados del cuadro de comportamiento.

### Paquete de referencia para viajes

- `KPI-053` — margen de contribución;
- `KPI-062` — tiempo de ciclo de reembolso;
- `KPI-065` — tasa de contacto por reserva;
- `KPI-060` — tasa de cancelación;
- `KPI-059` — incorporación de servicios complementarios;
- `KPI-051` — ingresos netos.

La selección final depende del objeto, el subsector, la instrumentación, la calidad del dato y el método de atribución.

## 5. Material histórico no reactivado

El precursor contenía un paquete genérico con:

- `KPI-020`;
- `KPI-021`;
- `KPI-024`;
- `KPI-025`;
- además de referencias a `KPI-022`, `KPI-023`, `KPI-026`, `KPI-041` y `KPI-042`.

Esos IDs carecen de ficha vigente y permanecen en cuarentena TES.

Por tanto:

- no se incorporan al paquete activo de Convercus;
- no se sustituyen por inferencia;
- y solo permanecen en el precursor archivado como trazabilidad.

## 6. Claims y formulaciones aplicadas — Viajes

Estas propuestas están pensadas para comunicar valor sin “promesas vagas”; cada una sugiere un ángulo medible.

- **“Más repetición, sin destruir margen.”**  
- **“Del postventa reactivo al journey orquestado.”**  
- **“Omnicanal real: tienda, web, call center y mensajería con una sola lógica de fidelización.”**  
- **“Habilite a su red de agentes con venta social y trazabilidad.”**  
- **“Incentivos medibles para socios estratégicos: más calidad, menos cancelaciones.”**  
- **“Gamificación útil: acelere reservas anticipadas y reduzca descuentos de última hora.”**

### Regla de validación comercial

Cada claim deberá asociarse a:

- KPI;
- baseline;
- ventana;
- fuente;
- método;
- guardarraíl;
- y límite de afirmación.

Sin esos campos, el claim es una hipótesis de comunicación, no una promesa validada.

## 7. Terminología narrativa y comercial — Viajes

- **Booking (como sustantivo)** → Evitar “un booking”; usar **reserva**.  
- **Ancillaries (sin traducir)** → Usar **servicios complementarios (ancillaries)**.  
- **Partner (como único término)** → Usar **socio estratégico** (y especificar tipo: proveedor, afiliado, franquiciado, receptivo).  
- **Engagement** → Evitar, usar **vinculación**.  
- **Insights** → Evitar, usar **información accionable** (reservar “inteligencia” para IA/ML).  
- **Leakage** (sin contexto) → Usar **fugas de margen** y describir el mecanismo (descuentos, comisiones, errores).

Estas recomendaciones gobiernan comunicación aplicada de Convercus. No sustituyen al léxico TES ni a la definición sectorial del KPI.

## 8. Backlog de KPI operativos de plataforma

Antes de crear una familia tecnológica deberán responderse estas preguntas:

1. ¿Qué funciones de Convercus son críticas para ejecutar cada mecanismo?
2. ¿Qué telemetría existe y con qué calidad?
3. ¿Qué indicador mide productividad o eficiencia de uso?
4. ¿Qué indicador mide disponibilidad o rendimiento?
5. ¿Qué indicador mide integridad de eventos y conciliación?
6. ¿Qué indicador permite separar fallo de plataforma, fallo de configuración y fallo de adopción?
7. ¿Qué relación se espera con los KPI de comportamiento?
8. ¿Qué mejoras técnicas solo habilitan el resultado y cuáles pueden contrastarse como intervención?

No se asignarán IDs hasta resolver:

- nomenclatura;
- fuente;
- fórmula;
- owner;
- umbral;
- relación con KPI de comportamiento;
- y política de colisiones.

## 9. Criterio de cierre de un piloto

Un piloto Convercus queda preparado para decisión cuando puede reconstruirse:

> **problema situado → comportamiento objetivo → mecanismo → instrumentación → resultado → medición → atribución → decisión → aprendizaje**

y cuando el cuadro de mando distingue:

- efecto en consumidor o negocio;
- calidad de ejecución del mecanismo;
- y desempeño operativo de la plataforma.

## 10. Límites

Este marco no:

- demuestra causalidad por usar Convercus;
- convierte una funcionalidad en resultado;
- confunde adopción de plataforma con fidelización;
- ni trata rendimiento técnico como valor económico automático.
