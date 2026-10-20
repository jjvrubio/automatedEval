# Word Publication

Use this reference when converting Markdown to DOCX.

## Converter

The canonical converter is configured in `assets/convercus_offer_builder.yaml`:

`/Users/juanjo/Documents/Personal/JJVR/automatizaciones/03_Personal/Consolidacion_Markdown_DOCX`

Use it in place. The skill must not maintain a second converter implementation.

The recommended profile for reusable Convercus offers is `commercial_proposal`. The existing `docx_convercus_offer` profile is account-specific because it contains a Compactor resource path; do not use it for other accounts unless the profile has first been made account-neutral.

## Safe Conversion Pattern

1. Copy or create the working Markdown inside the workspace or another approved output folder.
2. Keep the original source document unchanged.
3. Confirm the profile, template, filters, and image/resource paths exist.
4. Generate DOCX from the converter root, for example:

```bash
cd /Users/juanjo/Documents/Personal/JJVR/automatizaciones/03_Personal/Consolidacion_Markdown_DOCX
python3 md2docx.py build --input /path/to/working.md --profile commercial_proposal --output /path/to/output.docx
```

5. Review Pandoc warnings. Missing images or unresolved resources block publication.
6. Reconcile the generated Word against the Markdown for headings, tables, visible numbers, assumptions, exclusions, and document control fields.
7. Report generation, documentary review, and commercial approval separately.

## Required Frontmatter

Prefer explicit frontmatter on working Markdown:

```yaml
---
title: "Offer title"
date: "YYYY-MM-DD"
version: "v0.1"
status: "internal_draft"
client: "Client name"
lang: "es"
document_control: true
---
```

Use `status: internal_draft` until the documentary and commercial gates are passed.
