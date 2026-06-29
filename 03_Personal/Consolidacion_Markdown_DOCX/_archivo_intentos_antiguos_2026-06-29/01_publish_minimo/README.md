# publish

This folder contains a minimal Pandoc pipeline to generate a Word document
(with a real Word TOC field) from structured Markdown.

## Files

- `publish/convert.sh` - conversion script
- `publish/profiles/docx.yaml` - Pandoc defaults for docx
- `publish/filters/docprep.lua` - inserts the Word TOC field
- `publish/templates/frontmatter.yaml` - optional metadata template

## Usage

1) Put front matter in your markdown or keep it in a separate YAML file.

Example front matter in the markdown:

```
---
title: "My Document"
author: "Author"
date: "2025-12-29"
lang: en
toc: true
toc-depth: 3
---

:::toc:::
```

2) Run the converter:

```
publish/convert.sh /path/to/input.md
```

Optional metadata and reference docx:

```
publish/convert.sh /path/to/input.md publish/templates/frontmatter.yaml /path/to/reference.docx
```

## Notes

- The TOC is inserted as a Word field. After opening the docx in Word, update the
  TOC field (right click -> Update Field) to refresh page numbers.
- Use `:::toc:::` where you want the TOC to appear. If you set `toc: true` and
  omit the marker, the TOC is inserted at the top of the document.
