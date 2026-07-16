# Contrato de dominio de Experiences

## Estado

Este contrato se encuentra en preparación. Su objetivo será expresar el dominio compartido sin acoplarlo a la interfaz de la App ni del Builder.

## Entidades iniciales

```text
ExperienceDefinition
ExperienceParticipation
SignificantEvent
PatternHypothesis
Sequence
ProgressionState
Intervention
Incentive
Reward
ObservedOutcome
Measurement
ReusableLearning
WorkflowReference
```

## Principio de separación

El Builder crea y modifica definiciones. La App representa participaciones. Los contratos comunes deben permitir relacionarlas sin compartir estado de interfaz.

Los esquemas TypeScript y fixtures se incorporarán al comenzar el prototipo de la App.
