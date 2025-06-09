
# ESBS/AMOS Ultra-Strict Grading Script – Documentation

## 🎯 Purpose

This Python script enables strict, rubric-based evaluation of academic final projects (TFMs, case studies, etc.) using the ESBS/AMOS protocol. It supports `.docx` and `.pdf`, provides structured feedback, and integrates optionally with OpenAI's GPT models.

---

## ⚙️ Features

- Native file selection via macOS (`AppKit`)
- Compatible with `.docx` and `.pdf`
- Initial structural coherence analysis
- Ultra-strict evaluation per YAML rubric
- OpenAI GPT-4 Turbo API integration (optional)
- Outputs:
  - `evaluation_output.md` — full annotated feedback
  - `evaluation_output.json` — rubric scores
  - `rubric.json` — converted rubric for validation
- Validation-ready schema (`rubric.schema.json`)

---

## 📂 File Structure

```
esbs_grader/
├── ultra_strict_grader_esbs.py
├── config.yaml                # Editable rubric
├── rubric.schema.json         # Validation schema
├── examples/
│   ├── evaluation_output.md   # Example feedback
│   ├── evaluation_output.json # Rubric results
│   └── sample_input.docx      # Sample student project
```

---

## 🧠 Workflow

1. Run the script:
   ```bash
   python3 ultra_strict_grader_esbs.py
   ```
2. Select a `.docx` or `.pdf` file via macOS file dialog.
3. The script:
   - Reads and analyzes the document
   - Loads `config.yaml` (rubric)
   - Converts rubric to `rubric.json`
   - Calls OpenAI (if API key is present)
   - Generates `.md` and `.json` outputs

---

## 🔑 OpenAI API (Optional)

Set your API key as an environment variable:

```bash
export OPENAI_API_KEY=your-key-here
```

If no key is set, fallback scoring and comments are used from `config.yaml`.

---

## 🔍 Validation

To validate your rubric:

```bash
pip install jsonschema
python -m jsonschema -i config.json rubric.schema.json
```

---

## 🧪 Testing

Use the `examples/` folder for sandboxing and trials.

---

## ✏️ Future Extensions

- Multi-language rubric switching
- HTML report generation
- Integration with LMS platforms
