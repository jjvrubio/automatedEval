import Quartz as qtz
from AppKit import NSOpenPanel
from Foundation import NSURL
import re
import json
from collections import Counter
import pdfplumber

# PDF file selection function using macOS native file dialog
def get_file_path():
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_("Choose a PDF file")
    panel.setAllowedFileTypes_(["pdf"])
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None

# Function 1: Identify header and footer patterns
def identify_head_footer_pattern(pdf):
    """Identify potential header and footer patterns by analyzing text repetition across pages."""
    text_patterns = Counter()
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            lines = page_text.splitlines()
            for line in lines:
                text_patterns[line] += 1
    total_pages = len(pdf.pages)
    head_footer_patterns = [pattern for pattern, count in text_patterns.items() if count > 0.8 * total_pages]

    # Save identified patterns to a debug file
    with open("identified_patterns.md", "w", encoding="utf-8") as f:
        f.write("Identified Header/Footer Patterns:\n")
        for pattern in head_footer_patterns:
            f.write(f"{pattern}\n")
    print("Identified header/footer patterns saved to identified_patterns.md")

    return head_footer_patterns

# Function 2: Detect if text is a page number
def is_page_number(text):
    """Detect if the given text is a page number or a page marker."""
    patterns = [
        r"^\d+$",
        r"^(Page|Página) \d+$",
        r"^\d+/\d+$",
        r"^--- Page \d+ ---$"  # New pattern for page markers
    ]
    return any(re.match(pattern, text.strip()) for pattern in patterns)

# Function 3: Filter out identified header/footer patterns and page numbers
def filter_head_footer_patterns(text, patterns):
    """Remove identified header/footer patterns from the text."""
    lines = text.splitlines()
    filtered_text = "\n".join(line for line in lines if line.strip() not in patterns and not is_page_number(line))
    return filtered_text

# Function to gather text between "Referencias bibliográficas" and the first valid "Anexo"
def gather_text_between_marks(text):
    """Gathers text between the first valid 'Referencias bibliográficas' not followed by dots, blanks, or numbers and the first valid 'Anexo'."""
    start_pattern = re.compile(r'(?i)^Referencias bibliográficas', re.MULTILINE)
    end_pattern = re.compile(r'(?i)^Anexo\b', re.MULTILINE)

    start_match = None
    for match in start_pattern.finditer(text):
        line_end = text[match.end():text.find("\n", match.end())].strip()
        if not re.match(r'[.\s\d]', line_end):
            start_match = match
            break

    if not start_match:
        print("DEBUG: No valid start marker found.")
        return "No valid start marker found."

    start_index = text.find("\n", start_match.end()) + 1

    end_match = end_pattern.search(text, start_index)
    if not end_match:
        print("DEBUG: No valid end marker found after the start marker.")
        return "No valid end marker found."

    gathered_text = text[start_index:end_match.start()].strip()
    return gathered_text

# PDF extraction function using Quartz/Core Graphics
def extract_text_from_pdf(file_path):
    """Extract text from a PDF file using macOS native Core Graphics."""
    pdf_url = NSURL.fileURLWithPath_(file_path)
    pdf_doc = qtz.PDFDocument.alloc().initWithURL_(pdf_url)

    if not pdf_doc:
        print("Failed to open PDF file.")
        return

    extracted_text = ""
    for page_number in range(pdf_doc.pageCount()):
        page = pdf_doc.pageAtIndex_(page_number)
        if page:
            page_text = page.string()
            extracted_text += f"\n--- Page {page_number + 1} ---\n{page_text}\n"

    # Save the raw extracted text to a file for debugging
    with open("raw_extracted_text.md", "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print("Raw extracted text saved to raw_extracted_text.md")
    return extracted_text

# Function to clean the raw extracted text before gathering text between marks
def clean_extracted_text(raw_text, pdf_path):
    """Clean the raw extracted text by removing headers, footers, and page numbers."""
    with pdfplumber.open(pdf_path) as pdf:
        patterns = identify_head_footer_pattern(pdf)
    cleaned_text = filter_head_footer_patterns(raw_text, patterns)

    # Save the cleaned text to a markdown file for debugging
    with open("cleaned_text.md", "w", encoding="utf-8") as f:
        f.write(cleaned_text)
    print("Cleaned text saved to cleaned_text.md")

    return cleaned_text

# Function 1: Assemble references from text
def assemble_references(gathered_text):
    """Parse gathered text and assemble structured references."""
    references = [ref.strip() for ref in gathered_text.split("\n") if ref.strip()]

    with open("assembled_references.json", "w", encoding="utf-8") as f:
        json.dump(references, f, ensure_ascii=False, indent=4)
    print("Assembled references saved to assembled_references.json")

    return references

# Function 2: Check APA 7 compliance
def check_apa7_compliance(references):
    """Check if the given references comply with APA 7 format and save results in JSON format."""
    apa_pattern = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ]+(?:, [A-Z]\.)+ \(\d{4}\)"
    report = []
    for i, ref in enumerate(references, 1):
        if re.match(apa_pattern, ref):
            report.append({
                "Reference": i,
                "Status": "✅ APA 7 Compliant",
                "Text": ref
            })
        else:
            report.append({
                "Reference": i,
                "Status": "❌ Not APA 7 Compliant",
                "Text": ref
            })

    with open("compliance_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
    print("APA 7 compliance report saved to compliance_report.json")

    return report

# Function 3: Orchestrator for APA 7 compliance check
def run_apa7_compliance_check(gathered_text):
    """Orchestrates the APA 7 compliance check process."""
    references = assemble_references(gathered_text)
    compliance_report = check_apa7_compliance(references)
    return compliance_report

# Main function to run the extraction and analysis
def main():
    file_path = get_file_path()
    if not file_path:
        print("No file selected. Exiting.")
        return

    # Step 1: Extract text from PDF
    extracted_text = extract_text_from_pdf(file_path)

    # Step 2: Clean the raw extracted text
    cleaned_raw_text = clean_extracted_text(extracted_text, file_path)

    # Step 3: Gather text between marks
    gathered_text = gather_text_between_marks(cleaned_raw_text)
    with open("gathered_between_marks.md", "w", encoding="utf-8") as f:
        f.write(gathered_text)
    print("Gathered text saved to gathered_between_marks.md")

    # Step 4: Run APA 7 compliance check
    run_apa7_compliance_check(gathered_text)

if __name__ == "__main__":
    main()
