#!/bin/bash
set -euo pipefail

cd -- "$(dirname -- "$0")"

finish() {
  result=$?
  if [ "$result" -ne 0 ] && [ -t 0 ]; then
    printf '\nNo se pudo arrancar la demo. Revisa el error anterior.\n'
    read -r -p 'Pulsa Intro para cerrar.' _answer
  fi
  exit "$result"
}
trap finish EXIT

node_bin="$PWD/.local-runtime/node-v24.14.0-darwin-arm64/bin/node"
if [ ! -x "$node_bin" ]; then
  node_bin="$(command -v node || true)"
fi
if [ -z "$node_bin" ] || [ ! -x "$node_bin" ]; then
  printf 'Falta Node.js 24 o posterior. Instálalo o restaura .local-runtime.\n' >&2
  exit 1
fi
"$node_bin" -e 'if (Number(process.versions.node.split(".")[0]) < 24) { console.error("Se requiere Node.js 24 o posterior."); process.exit(1); }'
export PATH="$(dirname -- "$node_bin"):$PATH"
if [ ! -f node_modules/vite/bin/vite.js ]; then
  printf 'Faltan dependencias. Ejecuta npm ci desde esta carpeta.\n' >&2
  exit 1
fi

if [ "${1:-}" = '--no-open' ]; then
  set --
elif [ "$#" -gt 0 ]; then
  printf 'Uso: Abrir demo.command [--no-open]\n' >&2
  exit 1
else
  set -- --open '/?demo=sports-season-running'
fi
printf 'Demo: http://127.0.0.1:4173/?demo=sports-season-running\n'
printf 'Mantén esta ventana abierta. Para detener la demo: Control + C.\n'
"$node_bin" node_modules/vite/bin/vite.js --host 127.0.0.1 --port 4173 --strictPort "$@"
