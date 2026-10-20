# New Session Invocation Test

Use the parent directory that contains the skill as a capability directory in a new self-hosted Codex session:

`/Users/juanjo/Documents/Personal/JJVR/automatizaciones/02_Profesional/0201_Convercus/Automatizaciones`

Representative prompt:

```text
Usa $convercus-offer-builder para preparar una revisión de ensayo de Compactor.
No modifiques los documentos originales. Identifica las fuentes disponibles,
comprueba la configuración del conversor y separa generación Word, revisión
documental y aprobación comercial.
```

Expected behavior:

- The session discovers `convercus-offer-builder` from `convercus-offer-builder/SKILL.md`.
- The agent reads `assets/convercus_offer_builder.yaml`.
- The agent treats `Compactor_Ensayo_v0_1.docx` and `Compactor_Informe_Ensayo_v0_1.md` as trial-only references.
- The agent does not claim client-ready status or commercial approval.
- The agent does not reuse Compactor prices for another account.
