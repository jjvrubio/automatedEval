He revisado la v0.5A y creo que estamos en un buen punto para cambiar de hilo, pero he encontrado **un último defecto técnico que conviene cerrar antes del triage de señales**.

La parte de Revenue ha funcionado muy bien: pasamos a **40 elegibles, 7 no elegibles y sólo 3 desconocidas**, con `UniverseResolutionRate = 94%`, `EligibleFreshCoverage = 95%` y `EndToEndTerminalResolution = 90%`. Los tres casos que permanecen abiertos son dos `context_mismatch` y una ambigüedad real; no merece la pena forzarlos sólo para ganar cobertura. D2_diagnostics_v05A D2_diagnostics_v05A

El problema está en los flags derivados. Al auditar directamente `D2_results_v05A.csv`, **AAON** tiene:

```
candidate_d2 = true
d2_signal = true
freshness_status = fresh
universe_eligible = true

raw_d2_signal = false
eligible_d2_signal = false
```

y sus datos calculados son aproximadamente:

\[ Revenue\ Growth=+20.11\% \]\[ OM: 17.42\%\rightarrow10.14\% \]\[ \Delta OM=-7.28pp \]

Por tanto, con nuestras propias reglas, **AAON debería contar como señal elegible**. El diagnóstico v0.5A dice que existen dos señales, pero el propio CSV contiene tres `candidate_d2=true`: **AAON, CXT y FUN**. Antes de estudiar económicamente esas señales hay que arreglar esa incoherencia.

Por eso dividiría la transición así:

1. **Nuevo hilo → v0.5B:** reparar únicamente la consistencia `d2_signal → raw_d2_signal → eligible_d2_signal`, sin tocar Revenue, D2, umbrales ni universo.
2. Si v0.5B confirma cero inconsistencias, el siguiente paso será ya el **triage D2** de las señales que emerjan —previsiblemente AAON, CXT y FUN, pero sin hardcodearlas.
3. En ese triage investigaremos M&A/perímetro, deterioros contables, reestructuración, amortización de intangibles, mix, pricing, costes transitorios frente a deterioro operativo recurrente. Seguimos en **Investigando mercados**, no en decisión de inversión.

He preparado los dos documentos para hacer limpio el cambio de hilo:

TRANSFERENCIA_HILO_P1_D2_v05A.md

CODEX_TASK_05B.md

### Cómo abriría el nuevo hilo

Sube al nuevo hilo la transferencia y, por prudencia, estos seis outputs actuales:

```
D2_diagnostics_v05A.md
D2_results_v05A.csv
D2_provenance_v05A.csv
P1_universe_v05A.csv
Revenue_tag_decisions_v05A.csv
Revenue_unknown_diagnostics_v05A.csv
```

Y empieza simplemente con:

```
Continúa el desarrollo de P1.D2 siguiendo íntegramente
TRANSFERENCIA_HILO_P1_D2_v05A.md.

Los archivos v0.5A adjuntos son el estado vigente.

Primero audita el estado transferido y la inconsistencia de AAON.
La siguiente ejecución técnica está especificada en CODEX_TASK_05B.md.

No avances al triage económico de señales hasta que v0.5B cierre
la consistencia de flags.
```

Después, en VS Code, GitHub Copilot puede ejecutar `CODEX_TASK_05B.md` exactamente igual que venimos haciendo. Si devuelve `READY_FOR_SIGNAL_TRIAGE`, ése será el punto en que diseñaremos en el **nuevo hilo** la siguiente capa metodológica: convertir una señal D2 bruta en una divergencia fundamental explicada y una pregunta de investigación.