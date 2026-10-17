# Recuperación del arranque local — 2026-09-24

Error comunicado: `ERR_CONNECTION_REFUSED (-102)` al abrir `http://127.0.0.1:4173/?demo=sports-season-running`.

Diagnóstico: no había ningún proceso escuchando en el puerto 4173. El Node oficial usado en BUILD 01, alojado en `/private/tmp`, y su archivo descargado ya no existían; tampoco había Node en el PATH. El enlace dependía del servidor de aquella sesión.

Corrección: Node oficial 24.14.0 arm64 recuperado en `prototype/.local-runtime/`, excluido de Git. SHA-256 del archivo descargado comprobado contra el valor oficial verificado en BUILD 01: `a1a54f46a750d2523d628d924aab61758a51c9dad3e0238beb14141be9615dd3`. No se instala Node en el sistema ni un servicio al inicio del Mac.

Se incorpora [Abrir demo.command](../prototype/Abrir%20demo.command): doble clic para arrancar Vite en el puerto fijo 4173 y abrir Sports Season. Mantener la terminal abierta; Control + C detiene el servidor. Incluye diagnóstico de Node/dependencias ausentes y opción `--no-open`. [Instrucciones de arranque](../prototype/README.md).

Verificación: lanzador ejecutado con `--no-open`, Vite activo en 127.0.0.1:4173, respuesta HTTP 200. En Edge headless con perfil temporal se comprobó carga, inscripción Social, check-in, esfuerzo Suave, insignia y reset, sin errores de página ni consola. El primer intento del lanzador detectó una incompatibilidad de arrays vacíos con Bash de macOS; se corrigió antes de la pasada satisfactoria.

Los 202 archivos recogidos en `sourceHashes` de BUILD 01 permanecen byte-idénticos. No se modifica el producto, dependencias, configuración de herramientas ni evidencia histórica; no se repite la suite completa. Sus resultados históricos conservan las cualificaciones documentadas en BUILD 01.

El servidor queda activo al terminar esta intervención. Después de detenerlo o reiniciar el Mac hay que volver a ejecutar el lanzador. Esta recuperación acredita ejecución local, no aceptación humana de UX.
