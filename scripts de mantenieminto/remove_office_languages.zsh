#!/bin/zsh
#
# remove_office_languages_fixed.zsh
#
# Propósito:
#   Eliminar paquetes de idiomas innecesarios de las aplicaciones de Microsoft Office para macOS
#   (Word, Excel, PowerPoint, Outlook, OneNote) dentro de /Applications.
#
# Cambios clave respecto a versiones anteriores:
#   - Elevación automática a privilegios de administrador cuando es necesario.
#   - Comprobación precisa de procesos de Office en ejecución (sin falsos positivos por "Microsoft" genérico).
#   - Manejo de errores granular (sin `set -e` global).
#   - Globbing controlado: NULL_GLOB (silencioso cuando no hay coincidencias) y sin NOMATCH.
#   - Opción de dry-run, respaldo opcional de lo que se elimina y registro claro.
#   - Avisos sobre invalidez de firma de código y posibles efectos colaterales.
#
# ADVERTENCIA IMPORTANTE:
#   Modificar el contenido de un app bundle firmado puede invalidar su firma de código. Esto puede afectar
#   verificaciones, integraciones y futuras actualizaciones. MAU (Microsoft AutoUpdate) puede restaurar
#   archivos eliminados tras actualizar.
#
# Uso:
#   zsh remove_office_languages_fixed.zsh [--dry-run] [--backup] [--backup-dir <ruta>] [--ignore-running]
#                                         [--keep "en es pt"] [--apps "Word Excel PowerPoint Outlook OneNote"]
#
# Ejemplos:
#   # Ejecutar en modo simulación, mostrando qué se eliminaría
#   ./remove_office_languages_fixed.zsh --dry-run
#
#   # Eliminar realmente, con copia de seguridad en el Escritorio
#   ./remove_office_languages_fixed.zsh --backup
#
#   # Conservar sólo inglés y español, procesando Word y Excel
#   ./remove_office_languages_fixed.zsh --keep "en es" --apps "Word Excel"
#

emulate -L zsh
setopt EXTENDED_GLOB
setopt NULL_GLOB        # Los patrones sin coincidencias se reducen a vacío (no error)
unsetopt NOMATCH        # Evita lanzar error si un patrón no coincide

SCRIPT_NAME=${0:t}
VERSION="1.0.0"

# Resolver ruta absoluta del propio script (robusto en zsh)
# ${(%):-%x} devuelve el nombre del script incluso dentro de funciones
SCRIPT_PATH=${${(%):-%x}:A}

# ===================== Configuración por defecto =====================
DRY_RUN=false
DO_BACKUP=false
BACKUP_DIR="$HOME/Desktop/OfficeLanguageBackups"
IGNORE_RUNNING=false

# Idiomas a conservar (prefijos). Puedes usar códigos de 2-3 letras o variantes (en, en_US, es, es_ES, pt, pt_PT).
# Nota: si quieres excluir es_MX o pt-BR explícitamente, no los pongas en esta lista.
KEEP_LANGS=( en es pt en_US es_ES pt_PT )

# Aplicaciones a procesar (nombres "cortos")
DEFAULT_APPS=( Word Excel PowerPoint Outlook OneNote )
APPS=( ${DEFAULT_APPS[@]} )

# Rutas candidatas de bundles de Office (por si hay instalaciones en otras carpetas compartidas)
APP_DIRS=( /Applications )

# ===================== Utilidades de salida =====================
ansi_green="\033[32m"; ansi_red="\033[31m"; ansi_yellow="\033[33m"; ansi_blue="\033[34m"; ansi_reset="\033[0m"

log_info()    { print -r -- "${ansi_blue}[INFO]${ansi_reset} $*"; }
log_warn()    { print -r -- "${ansi_yellow}[AVISO]${ansi_reset} $*"; }
log_error()   { print -r -- "${ansi_red}[ERROR]${ansi_reset} $*"; }
log_success() { print -r -- "${ansi_green}[OK]${ansi_reset} $*"; }

# ===================== Ayuda =====================
show_help() {
  cat <<EOF
$SCRIPT_NAME v$VERSION
Elimina paquetes de idiomas innecesarios en Microsoft Office para macOS.

Opciones:
  --dry-run                 No hace cambios; muestra lo que haría
  --backup                  Copia a respaldo cada carpeta eliminada
  --backup-dir <ruta>       Directorio base para los respaldos (por defecto: $BACKUP_DIR)
  --ignore-running          Ignora comprobación de apps de Office en ejecución
  --keep "<langs>"          Espacio-separado de idiomas a conservar (prefijos o códigos completos)
  --apps "<lista>"          Apps a procesar: Word Excel PowerPoint Outlook OneNote
  -h, --help                Muestra esta ayuda

Advertencia: Modificar un bundle firmado puede invalidar su firma y afectar actualizaciones de Office.
EOF
}

# ===================== Análisis de argumentos =====================
ORIGINAL_ARGS=( "$@" )
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --backup) DO_BACKUP=true; shift ;;
    --backup-dir) BACKUP_DIR="$2"; shift 2 ;;
    --ignore-running) IGNORE_RUNNING=true; shift ;;
    --keep) KEEP_LANGS=( ${(z)2} ); shift 2 ;;
    --apps) APPS=( ${(z)2} ); shift 2 ;;
    -h|--help) show_help; exit 0 ;;
    *) log_error "Opción no reconocida: $1"; show_help; exit 2 ;;
  esac
done

# Normaliza a minúsculas para comparaciones tolerantes
KEEP_LANGS=( ${KEEP_LANGS[@]:l} )

# ===================== Elevación (sudo) =====================
require_admin() {
  if [[ $EUID -ne 0 ]]; then
    log_info "Se requieren privilegios administrativos. Reintentando con sudo…"
    exec sudo -p "[sudo] Contraseña para %u: " -- /bin/zsh "$SCRIPT_PATH" "${ORIGINAL_ARGS[@]}"
  fi
}

require_admin

# ===================== Comprobación de procesos en ejecución =====================
# Coincide solamente con procesos de Office principales
OFFICE_PROCS=(
  "Microsoft Word"
  "Microsoft Excel"
  "Microsoft PowerPoint"
  "Microsoft Outlook"
  "Microsoft OneNote"
)

check_running_office() {
  local found=false
  for p in $OFFICE_PROCS[@]; do
    if pgrep -x "$p" >/dev/null 2>&1; then
      print -r -- "$p en ejecución"
      found=true
    fi
  done
  $found && return 0 || return 1
}

if ! $IGNORE_RUNNING; then
  if check_running_office; then
    log_error "Cierra Word/Excel/PowerPoint/Outlook/OneNote antes de continuar o usa --ignore-running bajo tu responsabilidad."
    exit 1
  fi
else
  log_warn "Se ignora la comprobación de aplicaciones en ejecución (--ignore-running)."
fi

# ===================== Utilidades de respaldo =====================
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_ROOT="$BACKUP_DIR/$TIMESTAMP"

backup_path_for() { # $1 = ruta absoluta a carpeta .lproj
  local src="$1"
  # Mantén estructura relativa a la raíz del volumen
  print -r -- "$BACKUP_ROOT${src}"
}

ensure_backup_dir() {
  if $DO_BACKUP; then
    if $DRY_RUN; then
      log_info "[dry-run] Crear directorio de respaldo: $BACKUP_ROOT"
    else
      mkdir -p "$BACKUP_ROOT" || { log_error "No se pudo crear $BACKUP_ROOT"; exit 1; }
    fi
  fi
}

perform_backup() { # $1 = ruta fuente (carpeta .lproj existente)
  $DO_BACKUP || return 0
  local src="$1"
  local dst; dst=$(backup_path_for "$src")
  if $DRY_RUN; then
    log_info "[dry-run] Respaldar $src -> $dst"
  else
    mkdir -p "${dst:h}" || { log_error "No se pudo crear ${dst:h}"; return 1; }
    # Usa 'ditto' para preservar atributos de macOS
    if ditto "$src" "$dst"; then
      log_success "Respaldo creado: $dst"
    else
      log_error "Fallo al respaldar $src"
      return 1
    fi
  fi
}

# ===================== Lógica de idiomas =====================
# Devuelve 0 (verdadero) si debemos conservar el idioma indicado por el nombre de la carpeta .lproj
should_keep_language() { # $1 = nombre como "es.lproj" o "es_ES.lproj"
  local base="$1:t"           # último componente
  base="${base%.lproj}"       # quita sufijo
  local lower=${base:l}

  # Protección adicional: hay ciertos .lproj que son necesarios para Office y no
  # son estrictamente idiomas (por ejemplo "Base.lproj"). Protegemos esos nombres
  # explícitamente para evitar romper la aplicación.
  local PROTECTED=( base )
  local p
  for p in $PROTECTED[@]; do
    if [[ "$lower" == "$p" ]]; then
      return 0
    fi
  done

  # Si KEEP_LANGS contiene un prefijo que coincida, conservar
  local k
  for k in $KEEP_LANGS[@]; do
    local kl=${k:l}
    # Coincidencia por prefijo o igualdad completa
    if [[ "$lower" == "$kl" || "$lower" == ${kl}_* || "$lower" == ${kl}-* ]]; then
      return 0
    fi
  done

  return 1
}

# ===================== Descubrimiento de bundles de Office =====================
# Construye APP_PATHS sin usar sustitución de comandos para evitar divisiones por espacios
APP_PATHS=()
for short in $APPS[@]; do
  local_name="Microsoft ${short}.app"
  for d in $APP_DIRS[@]; do
    p="$d/$local_name"
    if [[ -d "$p" ]]; then
      APP_PATHS+="$p"
    fi
  done
done

if [[ ${#APP_PATHS[@]} -eq 0 ]]; then
  log_warn "No se encontraron aplicaciones de Office en: ${APP_DIRS[*]}"
  exit 0
fi

log_info "Aplicaciones detectadas:"
for a in $APP_PATHS[@]; do
  print -r -- "  - ${a}"
done

log_warn "Este procedimiento puede invalidar firmas de código y afectar actualizaciones. Procede bajo tu responsabilidad."

ensure_backup_dir

# ===================== Proceso principal =====================
# Rutas dentro del bundle donde suelen residir las localizaciones
REL_LANG_DIRS=(
  "Contents/Resources"
  "Contents/SharedSupport"
  "Contents/Frameworks"
)

# Recolecta candidatos *.lproj y elimina los que no estén en KEEP_LANGS
process_app() { # $1 = ruta del .app
  local app="$1"
  log_info "Procesando: $app"
  local rel
  local removed_count=0 kept_count=0 notfound_count=0

  for rel in $REL_LANG_DIRS[@]; do
    local base="$app/$rel"
    if [[ ! -d "$base" ]]; then
      (( notfound_count++ ))
      continue
    fi

    # Busca directorios *.lproj (no desciendas demasiado para evitar costes altos)
    local lproj
    local candidates=( "$base"/**/*.lproj(N/) )
    for lproj in $candidates[@]; do
      if should_keep_language "$lproj"; then
        (( kept_count++ ))
        continue
      fi
      # Respaldar si procede y eliminar
      perform_backup "$lproj" || true
      if $DRY_RUN; then
        log_info "[dry-run] rm -rf \"$lproj\""
        (( removed_count++ ))
      else
        if rm -rf "$lproj" 2>/dev/null; then
          log_success "Eliminado: $lproj"
          (( removed_count++ ))
        else
          # Puede ser un problema de permisos o protección (TCC/SIP)
          log_error "No se pudo eliminar: $lproj"
        fi
      fi
    done
  done

  log_info "Resumen $app: eliminados=$removed_count, conservados=$kept_count, rutas no presentes=$notfound_count"
}

for app in $APP_PATHS[@]; do
  process_app "$app"
done

log_success "Finalizado."
if $DO_BACKUP; then
  log_info "Respaldos en: $BACKUP_ROOT"
fi
if $DRY_RUN; then
  log_info "No se realizaron cambios (dry-run). Ejecuta sin --dry-run para aplicar."
fi
