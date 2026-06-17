from Quartz import PDFDocument
from Cocoa import NSOpenPanel, NSURL
import os
import re
import json


def select_pdf_file():
    """Open a native macOS file picker to select a PDF file."""
    panel = NSOpenPanel.openPanel()
    panel.setAllowedFileTypes_(["pdf"])
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)

    if panel.runModal() == 1:  # 1 means OK button clicked
        return panel.URLs()[0].path()
    return None


def extract_text_with_eol_quartz(pdf_path):
    """Extract text with explicit EOL detection using Quartz."""
    full_text = []
    url = NSURL.fileURLWithPath_(pdf_path)
    pdf = PDFDocument.alloc().initWithURL_(url)

    if pdf:
        for page_number in range(pdf.pageCount()):
            page = pdf.pageAtIndex_(page_number)
            if page is not None:
                page_text = page.string()
                if page_text:
                    full_text.append(page_text)

    # Combine all pages with explicit EOLs preserved
    full_text_str = "\n".join(full_text)
    return full_text_str


def remove_repeated_strings(full_text, repeated_strings):
    """Remove all instances of the repeated strings from the text."""
    for string in repeated_strings:
        full_text = re.sub(re.escape(string), "", full_text)
    return full_text


def remove_page_numbers(full_text):
    """Remove common page number patterns from the text."""
    page_number_patterns = [
        r"^\s*\d+\s*$",  # Standalone numbers (e.g., "1")
        r"^\s*Page\s*\d+\s*$",  # Page numbers with "Page" prefix (e.g., "Page 2")
        r"^\s*\(\d+\)\s*$",  # Numbers enclosed in parentheses (e.g., "(3)")
        r"^\s*Página\s*\d+\s*$",  # Spanish page numbers (e.g., "Página 4")
    ]

    for pattern in page_number_patterns:
        full_text = re.sub(pattern, "", full_text, flags=re.MULTILINE)
    return full_text


def prune_to_last_references(full_text):
    """Prune all text before the last occurrence of 'REFERENCIAS'."""
    matches = list(re.finditer(r"\bREFERENCIAS\b", full_text, re.IGNORECASE))
    if matches:
        last_match = matches[-1]
        return full_text[last_match.start() :]
    return ""


def merge_lines_into_references(pruned_text):
    """Merge fragmented lines into coherent references using author+year patterns."""
    lines = pruned_text.splitlines()
    references = []
    current_reference = ""

    # Regex to detect the start of a reference
    reference_start_pattern = re.compile(
        r"^[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+,?\s+[A-Z](?:\.|,)\s.*?\(\d{4}\)", re.UNICODE
    )

    for line in lines:
        line = line.strip()
        if reference_start_pattern.match(line):
            # Start a new reference if we detect an author+year pattern
            if current_reference:
                references.append(current_reference.strip())
            current_reference = line
        else:
            # Append to the current reference
            current_reference += " " + line

    # Add the last reference
    if current_reference:
        references.append(current_reference.strip())

    return references


def save_to_md_file(output_path, references):
    """Save the extracted references to a Markdown file."""
    try:
        with open(output_path, "w", encoding="utf-8") as md_file:
            md_file.write("# References\n\n")
            for ref in references:
                md_file.write(f"- {ref}\n")
        print(f"References saved to {output_path}")
    except Exception as e:
        print(f"Error saving to Markdown file: {e}")


def save_to_json_file(output_path, references):
    """Save the extracted references to a JSON file."""
    try:
        json_data = {"references": references}

        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, indent=4, ensure_ascii=False)
        print(f"References saved to {output_path}")
    except Exception as e:
        print(f"Error saving to JSON file: {e}")


def main():
    """Main function to extract and prune references."""
    print("Select a PDF file...")
    pdf_path = select_pdf_file()

    if pdf_path:
        # Extract text with explicit EOLs using Quartz
        full_text = extract_text_with_eol_quartz(pdf_path)

        # Remove headers/footers and page numbers
        cleaned_text = remove_page_numbers(full_text)

        # Prune everything before the last 'REFERENCIAS'
        pruned_text = prune_to_last_references(cleaned_text)

        if pruned_text:
            # Merge fragmented lines into coherent references
            references = merge_lines_into_references(pruned_text)

            # Save outputs to Markdown and JSON files
            base_path = os.path.splitext(pdf_path)[0]
            md_output_path = f"{base_path}_references.md"
            json_output_path = f"{base_path}_references.json"

            save_to_md_file(md_output_path, references)
            save_to_json_file(json_output_path, references)
        else:
            print("No 'REFERENCIAS' section found in the document.")
    else:
        print("File selection cancelled.")


if __name__ == "__main__":
    main()
