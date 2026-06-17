#!/usr/bin/env bash

set -euo pipefail

PRIMARY_DIR="/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/The Octavius/Convercus"
WORKING_DIR="/Users/juanjo/Library/CloudStorage/OneDrive-ConvercusGmbH/Convercus"
LOG_FILE="${LOG_FILE:-$HOME/Library/Logs/convercus-sync.log}"
DRY_RUN=0
MODE="daily"
RUN_ID="$(date "+%Y%m%d-%H%M%S")"

usage() {
  cat <<'EOF'
Usage: sync_convercus_daily.sh [--initial-copy] [--dry-run]

Options:
  --initial-copy   First copy: Convercus -> Documentos.
  --dry-run, -n    Show what would be copied without changing files.
  Default mode:    Daily sync: Documentos -> Convercus.

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
  if ! mkdir -p "$(dirname "$LOG_FILE")" 2>/dev/null; then
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
  --update \
  --backup \
  --backup-dir="$BACKUP_DIR" \
  --exclude ".DS_Store"
)

if [[ "$DRY_RUN" -eq 1 ]]; then
  rsync_args+=(-n)
fi

if [[ -n "${LOG_FILE:-}" ]]; then
  rsync "${rsync_args[@]}" "$SOURCE_DIR/" "$TARGET_DIR/" 2>&1 | tee -a "$LOG_FILE"
else
  rsync "${rsync_args[@]}" "$SOURCE_DIR/" "$TARGET_DIR/"
fi

if [[ "$DRY_RUN" -eq 1 ]]; then
  log "$MODE_LABEL dry run finished"
else
  log "$MODE_LABEL finished"
fi
