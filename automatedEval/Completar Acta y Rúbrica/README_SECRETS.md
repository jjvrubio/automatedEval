# Secrets y ejecución segura para `importarActa.py`

Este documento explica cómo gestionar y usar las credenciales necesarias para `importarActa.py` de forma segura.

## Variables esperadas
- `ACTA_PASSWORD`: contraseña utilizada por el script. (Obligatoria)
- `ACTA_EMAIL_SECRETARIO`: email del secretario (opcional, el script usa un valor por defecto si no está).

## Ejecutar localmente (zsh)
Exporta las variables en tu shell antes de ejecutar el script:

```bash
export ACTA_PASSWORD='mi_contraseña_segura'
export ACTA_EMAIL_SECRETARIO='juanjose.vazquez@unir.net'  # opcional
python automatedEval/Completar\ Acta\ y\ Rúbrica/importarActa.py
```

Si no exportas `ACTA_PASSWORD`, el script solicitará la contraseña mediante un diálogo oculto (AppleScript) y la mantendrá sólo en memoria.

## Uso en GitHub Actions (snippet)

Añade los secrets en Settings → Secrets del repositorio: `ACTA_PASSWORD` y `ACTA_EMAIL_SECRETARIO`.

Ejemplo mínimo de job en `.github/workflows/run-import.yml`:

```yaml
name: Run importarActa

on: [workflow_dispatch]

jobs:
  run-import:
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run importarActa
        env:
          ACTA_PASSWORD: ${{ secrets.ACTA_PASSWORD }}
          ACTA_EMAIL_SECRETARIO: ${{ secrets.ACTA_EMAIL_SECRETARIO }}
        run: |
          python automatedEval/Completar\ Acta\ y\ R\u00fabrica/importarActa.py
```

> Nota: muchas operaciones del script usan AppleScript/GUI (selección de fichero, diálogos) y no funcionarán en un runner macOS sin sesión gráfica interactiva. Para CI, es preferible usar un runner self-hosted con entorno gráfico o adaptar el script para no requerir GUI (ej.: pasar argumentos en línea).

## .env y .gitignore
Si usas un fichero `.env` local para desarrollo, añade `.env` a `.gitignore` y usa `importarActa.env.example` como plantilla. Nunca commitees un fichero con credenciales reales.

## Rotación y limpieza del historial
Has ya creado el secret en GitHub y rotado la credencial: muy bien. Si quieres eliminar toda traza en el historial de Git (opcional), puedo preparar los comandos para `git filter-repo` o BFG, pero ten en cuenta que reescribe el historial y requerirá forzar push y que cualquier colaborador actualice su clone.

---

Si quieres, añado este archivo al PR y muestro un mensaje adicional en el PR con el resumen de pasos que ya has completado.
