#!/usr/bin/env bash

set -euo pipefail

PRIMARY_DIR="/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/The Octavius/Convercus"
WORKING_DIR="/Users/juanjo/Library/CloudStorage/OneDrive-ConvercusGmbH/Convercus"
LOG_FILE="${LOG_FILE:-$HOME/Library/Logs/convercus-sync.log}"
RSYNC_TIMEOUT="${RSYNC_TIMEOUT:-120}"
EXTRA_EXCLUDES=()
DRY_RUN=0
MODE="daily"
RUN_ID="$(date "+%Y%m%d-%H%M%S")"

usage() {
  cat <<'EOF'
Usage: sync_convercus_daily.sh [--initial-copy] [--dry-run] [--exclude PATH]

Options:
  --initial-copy   First copy: primary OneDrive -> working OneDrive.
  --dry-run, -n    Show what would be copied without changing files.
  --exclude PATH  Temporarily skip a path relative to the source (repeatable).
  Default mode:   Daily sync: working OneDrive -> primary OneDrive.

RSYNC_TIMEOUT sets the I/O inactivity timeout in seconds (default: 120).
This is not a limit on total runtime or a filesystem-level watchdog.
For OneDrive read errors, download the affected file using Finder's
"Always Keep on This Device" action before retrying.

Safety:
  If a file in the destination is going to be replaced, the previous version is
  saved under .sync-backups/<timestamp>/ inside the destination folder.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --initial-copy)
      MODE="initial"
      shift
      ;;
    --dry-run|-n)
      DRY_RUN=1
      shift
      ;;
    --exclude)
      if [[ $# -lt 2 || -z "$2" || "$2" == -* ]]; then
        echo "--exclude requires a path relative to the source." >&2
        exit 2
      fi
      EXTRA_EXCLUDES+=("$2")
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

if [[ ! "$RSYNC_TIMEOUT" =~ ^[1-9][0-9]*$ ]]; then
  echo "RSYNC_TIMEOUT must be a positive number of seconds." >&2
  exit 2
fi

timestamp() {
  date "+%Y-%m-%d %H:%M:%S"
}

log() {
  if [[ -n "${LOG_FILE:-}" ]]; then
    printf "[%s] %s\n" "$(timestamp)" "$1" | tee -a "$LOG_FILE"
  else
    printf "[%s] %s\n" "$(timestamp)" "$1"
  fi
}

if [[ "$MODE" == "initial" ]]; then
  SOURCE_DIR="$PRIMARY_DIR"
  TARGET_DIR="$WORKING_DIR"
  MODE_LABEL="initial copy"
else
  SOURCE_DIR="$WORKING_DIR"
  TARGET_DIR="$PRIMARY_DIR"
  MODE_LABEL="daily sync"
fi

BACKUP_DIR="$TARGET_DIR/.sync-backups/$RUN_ID"

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync is required but was not found." >&2
  exit 1
fi

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Source folder not found: $SOURCE_DIR" >&2
  exit 1
fi

if [[ ! -d "$TARGET_DIR" ]]; then
  echo "Target folder not found: $TARGET_DIR" >&2
  exit 1
fi

if [[ -n "${LOG_FILE:-}" ]]; then
  if ! { mkdir -p "$(dirname "$LOG_FILE")" && touch "$LOG_FILE"; } 2>/dev/null; then
    echo "Warning: cannot write log file at $LOG_FILE. Continuing without file logging." >&2
    LOG_FILE=""
  fi
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  log "Starting $MODE_LABEL dry run from '$SOURCE_DIR' to '$TARGET_DIR'"
else
  log "Starting $MODE_LABEL from '$SOURCE_DIR' to '$TARGET_DIR'"
  log "Backup directory for replaced files: '$BACKUP_DIR'"
fi

rsync_args=(
  -avh \
  --progress \
  --timeout="$RSYNC_TIMEOUT" \
  --update \
  --backup \
  --backup-dir="$BACKUP_DIR" \
  --exclude ".DS_Store" \
  --exclude ".sync-backups/" \
  
)

if [[ ${#EXTRA_EXCLUDES[@]} -gt 0 ]]; then
  for excluded_path in "${EXTRA_EXCLUDES[@]}"; do
    rsync_args+=(--exclude "$excluded_path")
    log "Explicitly excluded from this run: $excluded_path"
  done
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  rsync_args+=(-n)
fi

run_sync() {
  if [[ -n "${LOG_FILE:-}" ]]; then
    rsync "${rsync_args[@]}" "$SOURCE_DIR/" "$TARGET_DIR/" 2>&1 | tee -a "$LOG_FILE"
  else
    rsync "${rsync_args[@]}" "$SOURCE_DIR/" "$TARGET_DIR/"
  fi
}

if run_sync; then
  :
else
  sync_status=$?
  log "Sync failed (exit $sync_status); the copy is incomplete."
  log "For OneDrive read errors, select 'Always Keep on This Device' in Finder for the affected file, wait for download, then retry."
  exit "$sync_status"
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  log "$MODE_LABEL dry run finished"
else
  log "$MODE_LABEL finished"
fi
