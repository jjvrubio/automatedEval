# Obsidian Bridge — VP-03: aislamiento entre bóvedas anidadas

Fecha de análisis: 2026-10-26. Alcance: código fuente público del tag
[`5.5.2`](https://github.com/coddingtonbear/obsidian-local-rest-api/tree/5.5.2)
de Local REST API with MCP y fixtures locales temporales. No se abrió Obsidian,
no se iniciaron servidores, no se accedió a Keychain, iCloud, credenciales ni
documentos de producción, y no se realizaron escrituras por REST/MCP.

## Decisión

**D — evidencia todavía insuficiente para decidir.**

Hay evidencia estática de que una instancia protege su propio `.obsidian`, pero
no hay evidencia dinámica de que el padre no pueda exponer los documentos o el
`.obsidian` de una hija cuando ambos directorios están dentro de la raíz que
Obsidian indexa. La política operativa debe seguir bloqueando las conexiones de
bóvedas anidadas.

## A. Análisis estático

### Hechos demostrados por 5.5.2

| Dimensión | Evidencia | Clasificación |
|---|---|---|
| Raíz de bóveda | `RequestHandler` recibe `app` de la instancia y resuelve rutas mediante la API `Vault`; `vaultPath.ts` usa `/vault` como raíz sintética para validar rutas relativas. | `ISOLATED` para escape de raíz; no demuestra separación padre/hija |
| Descubrimiento/indexación | `getAbstractFileByPath`/`getFile` consultan el índice de la bóveda de la instancia. El plugin no crea un segundo índice por cada `.obsidian` descendiente. | `UNVERIFIED` para padre/hija |
| Descendientes | `/vault/{path}` sirve archivos de la bóveda y el README afirma “any file in your vault”. Una hija física es descendiente del padre. | `EXPOSED` potencial; falta prueba dinámica |
| `.obsidian` de la instancia | `vaultPathIsInConfigDir` compara contra `app.vault.configDir` (normalmente `.obsidian`) y rechaza el directorio y sus descendientes. | `ISOLATED` para el `.obsidian` raíz de esa instancia |
| `.obsidian` anidado | La comparación se hace contra un único `configDir` de la instancia. No existe una lista automática de configuraciones anidadas. | `UNVERIFIED`; no asumir cobertura |
| Traversal | `vaultPathIsContained` rechaza absolutos, `..`, NUL, `:`, separadores problemáticos y limita segmentos. | `ISOLATED` frente a traversal textual |
| Symlinks | El propio comentario de `vaultPath.ts` indica que containment no resuelve symlinks; la comprobación de configuración sí tiene resolución en disco en ciertos caminos. | `UNVERIFIED` para separación física |
| REST y MCP | README dice que REST y MCP comparten las mismas capacidades nucleares; ambos llegan al mismo `RequestHandler`/operaciones. | `UNVERIFIED` para padre/hija; sin instancia dinámica |
| Escrituras | `/vault/{path}` admite GET, PUT, PATCH, POST y DELETE; la protección de configuración evita `.obsidian` de la instancia, no una segunda raíz lógica. | `EXPOSED` potencial; no ejecutar sin autorización |
| Eventos/índices | El handler mantiene observadores de `metadataCache`, listeners de Vault y streams de eventos de una instancia. No se observa un ámbito descendiente independiente. | `UNVERIFIED` |
| Credenciales, certificados y puerto | `main.ts` carga `data.json`, genera API key/certificado y escucha el `settings.port` de cada instancia. Esto no prueba identidad del vault detrás de un puerto. | `UNVERIFIED` como aislamiento operativo |

### Interpretación

El control `.obsidian` es de ámbito de instancia, no una frontera de filesystem
entre bóvedas. La hija podría ser indexada como contenido descendiente por el
padre; si se demuestra, el padre puede leerla y posiblemente modificarla como
un archivo ordinario. La hija, a su vez, tiene su propio `configDir` si se abre
como bóveda independiente. Eso protege su `.obsidian` frente a la instancia
hija, pero no convierte el anidamiento en separación física ni impide que otra
instancia con una raíz superior alcance sus documentos.

Fuentes revisadas:

- [`vaultPath.ts`](https://github.com/coddingtonbear/obsidian-local-rest-api/blob/5.5.2/src/vaultPath.ts)
- [`requestHandler.ts`](https://github.com/coddingtonbear/obsidian-local-rest-api/blob/5.5.2/src/requestHandler.ts)
- [`main.ts`](https://github.com/coddingtonbear/obsidian-local-rest-api/blob/5.5.2/src/main.ts)
- [`vaultSubresources.ts`](https://github.com/coddingtonbear/obsidian-local-rest-api/blob/5.5.2/src/vaultSubresources.ts)
- [`README.md`](https://github.com/coddingtonbear/obsidian-local-rest-api/blob/5.5.2/README.md)

## B. Diseño del laboratorio

El script [`nested_vault_isolation_lab.py`](./nested_vault_isolation_lab.py)
crea exclusivamente un `TemporaryDirectory` del sistema:

```text
parent-vault/
├── .obsidian/parent-config.json
├── parent-document.md
└── child-vault/
    ├── .obsidian/child-config.json
    └── child-document.md
```

Los contenidos son marcadores no sensibles. No contiene API keys, certificados
reales ni datos de producción. El script comprueba la topología, la existencia
de los documentos y que el fixture desaparece al terminar.

Resultados esperados:

1. La ruta física del documento hijo es descendiente de la raíz padre.
2. El archivo de configuración hijo no aparece mágicamente en el `.obsidian`
   propio del padre.
3. La mera separación de dos directorios `.obsidian` no prueba aislamiento de
   la instancia padre.

Violación de aislamiento: una instancia padre devuelve `child-document.md`,
observa eventos del hijo, incluye el hijo en su búsqueda/índice, o permite
escritura/borrado cruzado; también lo es que la instancia padre lea o escriba
`child-vault/.obsidian/*`.

Controles positivos: padre no accede a rutas fuera de su raíz; las rutas
`.obsidian/*` de cada instancia son rechazadas; credenciales/certificados y
puertos de las instancias son distintos y verificables. Controles negativos:
documento hijo dentro de la raíz padre y traversal `child-vault/../...`.

## C. Pruebas ejecutadas

Ejecutar desde el directorio del módulo:

```bash
python3 nested_vault_isolation_lab.py
```

Resultado: **PASS para la topología y los controles de filesystem**. Esto no
clasifica REST/MCP como `ISOLATED`.

La suite existente de provisioning mantiene la conexión de una bóveda anidada
en `BLOCKED_NESTED_ISOLATION`; el planner es de solo lectura y no inspecciona
`data.json`, documentos, Keychain ni endpoints.

## D. Protocolo dinámico pendiente de aprobación

No ejecutar automáticamente. Requiere dos instalaciones aisladas de Obsidian,
la misma versión del plugin 5.5.2, certificados y tokens de prueba, y puertos
loopback distintos. La aprobación debe autorizar explícitamente cualquier
escritura únicamente dentro del fixture.

1. Abrir solo el padre; probar listado, lectura, búsqueda y eventos del
   documento hijo.
2. Probar desde el padre `parent-vault/.obsidian/*`,
   `parent-vault/child-vault/.obsidian/*` y variantes de encoding/case; esperar
   rechazo en todos los casos.
3. Abrir solo la hija; repetir las pruebas contra su propio documento y
   configuración.
4. Con ambos abiertos, repetir lecturas cruzadas REST y MCP con cada
   credencial; comprobar que cada credencial solo autentica su servidor.
5. Verificar certificados por fingerprint y puerto; un puerto que responda no
   acredita qué bóveda atiende.
6. Suscribirse a eventos de cada instancia, modificar solo fixtures autorizados
   y comprobar que no aparecen eventos cruzados.
7. Solo tras aprobación separada, ejecutar una escritura inocua en cada
   documento fixture y confirmar que no cambia el otro ni ninguna configuración.

Si cualquier lectura, búsqueda, evento o escritura cruzada tiene éxito, la
dimensión correspondiente es `EXPOSED`, aunque exista una exclusión declarada
en Vault Manager.

## E. Matriz de riesgos

| Riesgo | Evidencia actual | Impacto | Control recomendado | Estado |
|---|---|---:|---|---|
| Padre indexa documentos hijos | Topología física y API de archivos amplia | Alto | No anidar; separación física | `UNVERIFIED` |
| Padre accede al `.obsidian` hijo | Un único `configDir` por instancia | Crítico | Policy Gateway con deny-by-default y prefijo exacto | `UNVERIFIED` |
| Escritura/borrado cruzado | Operaciones PUT/PATCH/POST/DELETE | Crítico | Bloquear MCP/REST directo; gateway de solo lectura | `UNVERIFIED` |
| Eventos o búsquedas cruzadas | Observadores a nivel de Vault | Alto | Instancias físicamente separadas y pruebas de eventos | `UNVERIFIED` |
| Confusión de servidor por puerto | `status` solo prueba TCP | Alto | Identidad autenticada, certificado y documento de desafío | `UNVERIFIED` |
| Credencial/certificado compartido | Configuración por instancia, no verificada en vivo | Alto | referencias únicas y fingerprints registrados | `UNVERIFIED` |

## F. Implicaciones arquitectónicas

- **Vault Provisioner:** conservar `BLOCKED_NESTED_ISOLATION`; no cambiarlo a
  `CONNECTION_ELIGIBLE` por una exclusión de catálogo. Añadir, cuando exista
  evidencia dinámica, un resultado explícito de identidad/ámbito, no solo
  `plugin_version`.
- **Policy Gateway:** debe ser obligatorio para cualquier conexión operativa,
  autenticar servidor y vault, aplicar allowlist de raíz exacta, rechazar
  `.obsidian` en cada ámbito, impedir traversal/symlinks y bloquear escrituras
  por defecto. Una exclusión del Vault Manager no controla un servidor que ya
  indexa la raíz padre.
- **Recomendación:** para el requisito de separación documental y de
  configuración, preferir bóvedas físicamente hermanas fuera de otra raíz de
  bóveda. Si el anidamiento es imprescindible, tratarlo como no confiable hasta
  completar el protocolo dinámico y mantener mediación externa obligatoria.
