import os
from typing import Literal


def extract_text(file_path: str, source_type: Literal["pdf", "docx"]) -> str:
    if source_type == "pdf":
        return extract_pdf(file_path)
    elif source_type == "docx":
        return extract_docx(file_path)
    else:
        raise ValueError("source_type must be 'pdf' or 'docx'")


def get_file_title(file_path: str) -> str:
    return os.path.splitext(os.path.basename(file_path))[0]


def extract_pdf(file_path: str) -> str:
    from Quartz import PDFDocument
    from Foundation import NSURL

    url = NSURL.fileURLWithPath_(file_path)
    pdf_doc = PDFDocument.alloc().initWithURL_(url)
    if not pdf_doc:
        raise ValueError("No se pudo abrir el PDF")
    text = ""
    for i in range(pdf_doc.pageCount()):
        page = pdf_doc.pageAtIndex_(i)
        if page:
            text += page.string()
    return text


def extract_docx(file_path: str) -> str:
    from docx import Document

    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs])
