<!--
Plantilla de Pull Request (español).
Rellena los apartados para facilitar revisiones y control de cambios.
-->


# Título del PR

Breve título claro y conciso (ej: chore(maintenance): harden remove_office_languages)


## Resumen

Explica en 1–3 frases qué hace este PR y por qué es necesario.


## Tipo de cambio

- [ ] bugfix
- [ ] feature
- [ ] chore/maintenance
- [ ] docs
- [ ] ci/cd


## Descripción de cambios

Lista concreta de cambios (archivos principales, comportamientos modificados):

- `scripts de mantenieminto/remove_office_languages.zsh`: límite de glob, protección tokens, --no-sudo, dry-run por defecto en ejemplos
- `scripts de mantenieminto/README.md`: uso, advertencias y ejemplos


## Cómo probar (steps to reproduce / testing)

Indica pasos claros para validar los cambios localmente, por ejemplo:

1. Ejecutar en modo simulación sin sudo:

```bash
zsh "scripts de mantenieminto/remove_office_languages.zsh" --dry-run --no-sudo --apps "Word Excel"
```

1. Revisar que las rutas protegidas (Base.lproj, DFonts, Office Themes, Metadata.appintents, sdx, etc.) no aparecen para borrado.
1. Opcional: ejecutar con `--backup` y revisar que los respaldos se crean correctamente.


## Rollback / Seguridad

Si algo va mal, restaurar desde los respaldos creados en `--backup-dir` o restaurar desde el control de versiones (tag/commit previo).


## Checklist del autor

- [ ] He probado localmente en modo `--dry-run` y verificado rutas protegidas
- [ ] Añadí o actualicé documentación si procede
- [ ] Los cambios están en una rama con un nombre descriptivo


## Checklist del revisor

- [ ] Cambios lógicos coherentes y seguros (no borra recursos protegidos)
- [ ] Uso correcto de flags y comportamiento por defecto
- [ ] Documentación y mensajes de commit claros


## Notas de release (breve)

Incluye aquí el texto que debería aparecer en el release asociado (si aplica).
