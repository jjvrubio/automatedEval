# WIP: Auto-fixes ruff/black/isort/autoflake

Fecha: 2025-11-03

Estado actual
- Rama local: `chore/auto-fix-problems` (checkout local). No se ha hecho `commit` ni `push`.
- Herramientas ejecutadas en el venv: `ruff`, `black`, `isort`, `autoflake`.
- Archivos reformateados automáticamente: ~58 (cambios en el working tree).
- Errores detectados por `ruff` tras auto-fix: 32 restantes (categorías principales: `F821` undefined-name, `F841` unused-variable, `F401` unused-import, `E741` ambiguous-variable-name, `E402` import not at top, `E722` bare-except).

Por qué se dejó en WIP
- Las herramientas automáticas arreglan formato y muchos problemas triviales, pero pueden eliminar imports o tocar lógica sutil. Para evitar romper comportamiento, los cambios quedaron en el working tree para revisión manual antes de commitear.

Qué hacer para retomar
1. Cambiar a la rama donde queda el trabajo:

```bash
git checkout chore/auto-fix-problems
```

2. Ver los archivos modificados:

```bash
git status --porcelain
git diff --name-only | sed -n '1,200p'
```

3. Inspeccionar diffs por archivo (ejemplo):

```bash
git diff -- path/to/file.py | sed -n '1,300p'
```

4. Ejecutar linters/tests localmente antes de commitear:

```bash
/path/to/venv/bin/python -m ruff check . --statistics
# y si tienes test suite:
pytest -q || true
```

5. Opciones para guardar el trabajo:

- Guardar como commit provisional (recomendado si quieres conservar y compartir):

```bash
git add -A
git commit -m "chore: provisional auto-fixes (ruff/black/isort/autoflake) - WIP"
git push -u origin chore/auto-fix-problems
```

- Guardar temporalmente en stash (si no quieres commit):

```bash
git stash push -m "auto-fixes ruff/black/isort/autoflake - provisional"
git checkout principal
```

- Revertir TODO (si decides cancelar):

```bash
git checkout principal
git branch -D chore/auto-fix-problems
# si hay cambios no stashed y quieres descartarlos:
git restore --staged . || true
git restore . || true
```

Próximos pasos recomendados
- Revisar los 30 archivos con más incidencias (ejecutar `ruff check .` y ordenar por archivo). Corregir los `undefined-name` y las variables sin usar manualmente — son los que probablemente necesiten contexto humano.
- Hacer commit y abrir PR para revisión en remoto; ejecutar CI/tests.

Notas y enlaces rápidos
- Para listar errores por archivo:

```bash
/path/to/venv/bin/python -m ruff check . --format default | sort | uniq -c | sort -nr | sed -n '1,200p'
```

- Si quieres, puedo (cuando vuelvas) preparar el commit, abrir el PR y/o iterar por lotes sobre los ficheros con `F821`.

Contacto
- Guardé esto en `automatedEval/WIP_AUTOFIX.md` para que esté en el contexto más cercano a los ficheros afectados.

---
Pequeña nota: si prefieres que borre la rama y el working tree ahora, dime y lo ejecuto; si prefieres que haga el commit y push al remoto para que lo tengas disponible desde otra máquina, también lo puedo hacer.
