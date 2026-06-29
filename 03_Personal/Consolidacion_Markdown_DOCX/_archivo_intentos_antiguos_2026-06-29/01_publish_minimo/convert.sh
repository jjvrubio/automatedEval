#!/usr/bin/env bash
set -euo pipefail

if [ $# -lt 1 ]; then
  echo "Usage: publish/convert.sh <input.md> [metadata.yaml] [reference.docx]"
  exit 1
fi

MD="$1"
META_FILE="${2:-}"
REF_DOC="${3:-}"

if [ ! -f "$MD" ]; then
  echo "Error: input markdown not found: $MD"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROFILE="$SCRIPT_DIR/profiles/docx.yaml"

META_OPTION=()
if [ -n "$META_FILE" ]; then
  if [ ! -f "$META_FILE" ]; then
    echo "Error: metadata file not found: $META_FILE"
    exit 1
  fi
  META_OPTION=(--metadata-file "$META_FILE")
fi

REF_OPTION=()
if [ -n "$REF_DOC" ]; then
  if [ ! -f "$REF_DOC" ]; then
    echo "Error: reference docx not found: $REF_DOC"
    exit 1
  fi
  REF_OPTION=(--reference-doc "$REF_DOC")
fi

OUT="${MD%.md}.docx"

pandoc "$MD" \
  --defaults "$PROFILE" \
  "${META_OPTION[@]}" \
  "${REF_OPTION[@]}" \
  -o "$OUT"

echo "Done: $OUT"
