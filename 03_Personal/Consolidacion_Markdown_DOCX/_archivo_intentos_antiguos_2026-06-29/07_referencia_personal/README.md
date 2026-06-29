
# Scripts de mantenimiento

Esta carpeta contiene utilidades y scripts para mantenimiento y limpieza en macOS.

# Exportar contactos a CSV

- `export_contacts_to_csv.applescript` — Recorre todos los contactos de la app Contactos y crea un CSV con nombre, empresa, cargo, notas, teléfonos/correos/direcciones/URLs etiquetados y fechas de creación/modificación.

Pasos rápidos:

1. Abre el archivo en Script Editor y ejecútalo (otorga acceso a Contactos si macOS lo pide).
2. Elige la ruta del `.csv` (se sugiere `Contactos-YYYYMMDD-HHMMSS.csv`).
3. Espera el aviso de finalización con el número de contactos exportados.

El CSV se guarda en UTF-8 y usa ` | ` como separador interno para valores múltiples.

# Exportar correos "via Streak"

- `export_streak_mail.applescript` — Busca en la cuenta de Mail llamada `plesepoint`, dentro del buzón `Archivado`, todos los mensajes cuyo remitente contiene la cadena ` (via Streak)` y los vuelca a un JSON con cuenta, buzón, remitente, asunto, fecha y `messageId`.

Instrucciones:

1. Ejecuta el script desde Script Editor y permite el acceso a Mail cuando lo solicite.
2. Elige el nombre del archivo JSON (se propone `Streak-mails-YYYYMMDD-HHMMSS.json`).
3. Espera el mensaje final con el número de coincidencias exportadas.

El JSON se genera en UTF-8 y escapa los caracteres especiales para que puedas tratarlo directamente con Python, jq, etc.


# Ajustar SVG exportados desde PowerPoint

- `adjust_svg_dpi.py` — Reescala los atributos `width` y `height` de SVG exportados desde PowerPoint para pasar, por ejemplo, de 300 dpi a 96 dpi sin cambiar el contenido vectorial ni el `viewBox`.

Uso típico:

```bash
python3 "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/adjust_svg_dpi.py" ~/ruta/a/los/svg --recursive
```

Eso genera copias con sufijo `-96dpi.svg`. Si quieres sobrescribir los originales:

```bash
python3 "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/adjust_svg_dpi.py" ~/ruta/a/los/svg --recursive --in-place
```

Notas:

- Está pensado para SVG cuyo tamaño lógico se exportó en píxeles a 300 dpi.
- Si el SVG ya usa unidades físicas como `in`, `cm` o `mm`, el script no toca esas medidas.
- Mantiene intacto el `viewBox`, así que la diapositiva conserva proporción y contenido.


# Insertar SVG en PowerPoint

- `insert_svgs_into_pptx.py` — Añade una diapositiva nueva por cada SVG y coloca la imagen ocupando todo el lienzo de la presentación.

Uso típico:

```bash
python3 "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/insert_svgs_into_pptx.py" \
	"/ruta/a/slides" \
	"/ruta/a/presentacion.pptx"
```

Eso genera una copia del `.pptx` original con sufijo `-with-svg-slides.pptx`. Para procesar carpetas anidadas:

```bash
python3 "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/insert_svgs_into_pptx.py" \
	"/ruta/a/slides" \
	"/ruta/a/presentacion.pptx" \
	--recursive
```


# Comparar dos Word

- `comparar_docx.py` — Compara dos archivos `.docx` y genera un informe Markdown con diferencias de texto por capitulo y cambios de imagenes.

Uso tipico:

```bash
python3 "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/comparar_docx.py" \
	"/ruta/original.docx" \
	"/ruta/revisado.docx" \
	--salida "/ruta/comparativa.md"
```

Notas:

- Detecta capitulos por estilos `Heading 1`/`Titulo 1` o por encabezados tipo `Capitulo 1`.
- Si tus capitulos usan otro estilo, indicalo con `--chapter-style "Nombre del estilo"`.
- Las imagenes se comparan por contenido interno, no por nombre visual.


# Reestructurar repositorio por mapa

- `reestructurar_repo.sh` — Aplica una reorganizacion de carpetas a partir de un mapa TSV (`repo_restructure_map.tsv`) en la raiz del repo.

Uso recomendado:

```bash
bash "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/reestructurar_repo.sh"
```

Ese comando hace simulacion (`dry-run`) y no mueve nada. Para aplicar cambios reales:

```bash
bash "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/reestructurar_repo.sh" --apply
```

Notas:

- Formato del mapa: `origen<TAB>destino` (rutas relativas al root del repo).
- Ignora lineas vacias y comentarios (`#`).
- Si el origen no existe o el destino ya existe, la entrada se omite sin abortar el proceso completo.


# Archivo principal

- `remove_office_languages.zsh` — Script para eliminar paquetes de idiomas (`*.lproj`) de bundles de Microsoft Office instalados en `/Applications`.


# Objetivo

Reducir el tamaño de instalaciones de Office eliminando localizaciones no necesarias. El script incluye salvaguardas (lista de tokens protegidos, `--dry-run`, respaldos con `--backup`) y por defecto no modifica nada sin confirmación explícita.


# Advertencias importantes

- Modificar bundles puede invalidar la firma de código y afectar actualizaciones.
- No ejecutes el script sin `--dry-run` hasta que revises la salida.
- Usa la opción `--backup` para crear copias de seguridad antes de borrar.
- El script protege por defecto carpetas críticas como `Base.lproj`, `DFonts`, `Office Themes`, `Metadata.appintents`, `sdx`, entre otros.


# Uso recomendado (pasos)

1. Ejecuta en modo simulación (sin sudo) para verificar la lista de eliminaciones propuestas:

```bash
zsh "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/remove_office_languages.zsh" --dry-run --no-sudo --apps "Word Excel"
```

1. Revisa la salida. Si identificas rutas que quieras proteger, puedes pasarlas con `--protect` (espacio-separadas):

```bash
zsh "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/remove_office_languages.zsh" --dry-run --no-sudo --apps "Word Excel" --protect "sdx 'Office Themes'"
```

1. Si estás satisfecho y quieres aplicar cambios, haz un respaldo y ejecuta sin `--dry-run` (se te pedirá sudo si es necesario):

```bash
zsh "03_Personal/Automaciones/mac_automation/scripts_de_apoyo/remove_office_languages.zsh" --backup --backup-dir "$HOME/Desktop/OfficeBackups" --apps "Word Excel"
```


# Notas para desarrolladores

- El script intenta re-ejecutarse con `sudo` si detecta que no tiene privilegios.
- El globing está limitado a dos niveles dentro del bundle para evitar recorridos infinitos o seguir enlaces simbólicos no deseados.
- Si necesitas ampliar la lista de aplicaciones a procesar o directorios de búsqueda, ajusta `DEFAULT_APPS` y `APP_DIRS` al inicio del script.


# Contribuciones

Si añades protección para tokens adicionales o mejoras, por favor abre un PR en la rama `feature/maintenance-scripts` y añade pruebas/revisiones en dry‑run.


# Licencia

MIT (por defecto — adapta si procede)
