# Límites de producto

## Propósito

Este documento evita que Convercus App y Experience Builder se conviertan accidentalmente en un único producto o se condicionen mutuamente de forma prematura.

## Convercus App

La App está dirigida al cliente o miembro del programa. Su primera finalidad es proporcionar una demostración comercial mobile-first, estable y repetible.

Pertenece a la App:

- Inicio y perfil de miembro.
- Puntos, niveles y membresías.
- Cupones y beneficios.
- Noticias y actividad.
- Intervenciones y próximas acciones.
- Participaciones en Experiences.
- Panel interno de simulación para demos.
- Adaptadores mock, simulation y staging.

No pertenece a la App:

- Crear o publicar definiciones de Experiences.
- Editar visualmente Workflows.
- Configurar reglas técnicas de ejecución.
- Administrar versiones de Experiences.
- Mostrar conceptos TES internos sin traducción.

## Experience Builder

El Builder está dirigido a diseñadores, consultores, marketers y operadores que configuran Experiences.

Pertenece al Builder:

- Experiencia candidata.
- Reconocimiento o formulación del patrón.
- Diseño de secuencia y progresión.
- Eventos, evidencias y reglas.
- Intervenciones, incentivos y recompensas.
- Resultados, medición y aprendizaje.
- Simulación y validación técnica.
- Mapeo a Workflows.
- Publicación y versionado.

No pertenece al Builder:

- Ser la aplicación cotidiana del miembro.
- Convertirse en un dashboard genérico de campañas.
- Equiparar una Experience con un Workflow.
- Gobernar la navegación o presentación de la App.

## Base compartida

Pueden compartirse:

- Definiciones de dominio.
- Léxico y política terminológica.
- Identificadores estables.
- Escenarios canónicos.
- Fixtures separados por definición y participación.
- Contratos de API.
- Identidad de marca y primitivas visuales realmente comunes.

No se comparten por defecto:

- Navegación.
- Estado de interfaz.
- Componentes complejos.
- Ciclos de vida de pantalla.
- Permisos y operaciones.

## Regla de independencia

La App puede simular participaciones sin que el Builder esté implementado. El Builder puede diseñar definiciones sin depender de los componentes de la App. La convergencia debe producirse mediante contratos compartidos versionados.
