from FileReader import FileReader

docx_path = "/path/to/problematic.docx"
try:
    text = FileReader.read_docx(docx_path)
    print(f"Extracted text from DOCX (first 500 chars):\n{text[:500]}")
except Exception as e:
    print(f"Error reading DOCX file: {e}")
