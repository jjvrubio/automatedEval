# Scripts de mantenimiento

Esta carpeta contiene utilidades y scripts para mantenimiento y limpieza en macOS.

Archivo principal
------------------

- `remove_office_languages.zsh` — Script para eliminar paquetes de idiomas (`*.lproj`) de bundles de Microsoft Office instalados en `/Applications`.

Objetivo
--------

Reducir el tamaño de instalaciones de Office eliminando localizaciones no necesarias. El script incluye salvaguardas (lista de tokens protegidos, `--dry-run`, respaldos con `--backup`) y por defecto no modifica nada sin confirmación explícita.

Advertencias importantes
-----------------------

- Modificar bundles puede invalidar la firma de código y afectar actualizaciones.
- No ejecutes el script sin `--dry-run` hasta que revises la salida.
- Usa la opción `--backup` para crear copias de seguridad antes de borrar.
- El script protege por defecto carpetas críticas como `Base.lproj`, `DFonts`, `Office Themes`, `Metadata.appintents`, `sdx`, entre otros.

Uso recomendado (pasos)
----------------------

1. Ejecuta en modo simulación (sin sudo) para verificar la lista de eliminaciones propuestas:

```bash
zsh "scripts de mantenieminto/remove_office_languages.zsh" --dry-run --no-sudo --apps "Word Excel"
```

2. Revisa la salida. Si identificas rutas que quieras proteger, puedes pasarlas con `--protect` (espacio-separadas):

```bash
zsh "scripts de mantenieminto/remove_office_languages.zsh" --dry-run --no-sudo --apps "Word Excel" --protect "sdx 'Office Themes'"
```

3. Si estás satisfecho y quieres aplicar cambios, haz un respaldo y ejecuta sin `--dry-run` (se te pedirá sudo si es necesario):

```bash
zsh "scripts de mantenieminto/remove_office_languages.zsh" --backup --backup-dir "$HOME/Desktop/OfficeBackups" --apps "Word Excel"
```

Notas para desarrolladores
-------------------------

- El script intenta re-ejecutarse con `sudo` si detecta que no tiene privilegios.
- El globing está limitado a dos niveles dentro del bundle para evitar recorridos infinitos o seguir enlaces simbólicos no deseados.
- Si necesitas ampliar la lista de aplicaciones a procesar o directorios de búsqueda, ajusta `DEFAULT_APPS` y `APP_DIRS` al inicio del script.

Contribuciones
-------------

Si añades protección para tokens adicionales o mejoras, por favor abre un PR en la rama `feature/maintenance-scripts` y añade pruebas/revisiones en dry‑run.

Licencia
--------
MIT (por defecto — adapta si procede)
