import os
import re
import json
import Cocoa
import datetime
from Quartz import PDFDocument
from Foundation import NSURL
import docx


def debug_log(message, output_dir="", title="# debug_log"):
    """Appends debug messages to a Markdown log file in the specified directory."""
    if not output_dir:
        output_dir = os.getcwd()  # Default to the current working directory

    debug_file = os.path.join(output_dir, f"{title}.md")
    try:
        with open(debug_file, "a") as log_file:
            timestamp = datetime.datetime.now().isoformat()
            log_file.write(f"- **[{timestamp}]** {message}\n")
    except Exception as e:
        print(f"Failed to write debug log: {e}")


def choose_file(file_type):
    """Use a native macOS file dialog to select a file and return its path and directory."""
    panel = Cocoa.NSOpenPanel.openPanel()
    panel.setAllowsMultipleSelection_(False)
    panel.setCanChooseDirectories_(False)

    if file_type == "thesis":
        panel.setAllowedFileTypes_(["pdf", "docx"])
    elif file_type == "references":
        panel.setAllowedFileTypes_(["json"])

    if panel.runModal() == Cocoa.NSModalResponseOK:
        file_path = panel.URLs()[0].path()
        file_dir = os.path.dirname(file_path)
        # debug_log(f"Selected {file_type} file: {file_path}")
        return file_path, file_dir
    else:
        # debug_log(f"No {file_type} file selected.")
        return None, None


def get_file_title(file_path):
    """Extract the file title (name without extension) from the file path."""
    return os.path.splitext(os.path.basename(file_path))[0]


def prepare_metadata(full_text, source_type, output_dir, title):
    """Prepare metadata for citation search based on the document structure."""
    return {
        "total_units": len(full_text.split("\n")),
        "unit_type": "paragraphs" if source_type == "docx" else "pages",
        "output_dir": output_dir,
        "title": title,
    }


def extract_text(file_path, source_type):
    """Generalized text extraction for PDF and DOCX formats."""
    if source_type == "pdf":
        extracted_text = extract_pdf(file_path)
    elif source_type == "docx":
        extracted_text = extract_docx(file_path)
    else:
        raise ValueError("Unsupported file format")

    # debug_log(f"Extracted text length: {len(extracted_text)}")
    # debug_log(f"Extracted text sample:\n{extracted_text[:500]}")
    return extracted_text


def extract_pdf(file_path):
    """Extract and preprocess text from a PDF using Quartz."""
    url = NSURL.fileURLWithPath_(file_path)
    pdf_doc = PDFDocument.alloc().initWithURL_(url)
    text = ""

    # debug_log(f"Starting PDF extraction for file: {file_path}")

    for page_num in range(pdf_doc.pageCount()):
        page = pdf_doc.pageAtIndex_(page_num)
        page_text = page.string()

        if page_text:
            # debug_log(f"Extracted raw text from page {page_num + 1}:\n{page_text[:200]}...")

            # Remove page numbers and clean artifacts
            page_lines = page_text.splitlines()
            cleaned_lines = []

            for line in page_lines:
                # Remove leading page numbers
                line = re.sub(r"^\d+\s*", "", line)
                # Join fragmented lines into paragraphs
                if line.strip():
                    cleaned_lines.append(line.strip())

            # Add cleaned lines for this page to the overall text
            text += " ".join(cleaned_lines) + "\n"

    # debug_log(f"PDF extraction completed. Total length: {len(text)} characters.")
    return text


def extract_docx(file_path):
    """Extract and preprocess text from a DOCX file."""
    doc = docx.Document(file_path)
    text = ""

    for paragraph in doc.paragraphs:
        line = paragraph.text.strip()
        # Skip empty lines
        if not line:
            continue
        # Remove leading numbers (e.g., page numbers or section numbers)
        line = re.sub(r"^\d+\s*", "", line)
        # Append cleaned lines
        text += line + "\n"

    # Optionally remove repeated blank lines and normalize spacing
    text = re.sub(r"\n\s*\n", "\n", text)  # Collapse multiple blank lines into one
    return text


def save_debug_text_to_file(output_dir, filename, content):
    """Save content to a JSON file for debugging."""
    filepath = os.path.join(output_dir, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump({"text": content}, file, ensure_ascii=False, indent=2)
        # debug_log(f"Saved debug text to {filepath}")
        return filepath  # Return the path for verification
    except Exception:
        # debug_log(f"Failed to save debug text to {filepath}: {e}")
        return None  # Return None in case of failure


def process_extracted_text(raw_text, output_dir):
    """Process raw extracted text, stopping at the 'Anexo' marker."""
    if not raw_text.strip():
        # debug_log("Raw text is empty. Processing aborted.")
        return ""

    # Define the 'Anexo' marker pattern
    anexo_pattern = r"^\s*Anexo\b"

    # Split into lines and process
    lines = raw_text.splitlines()
    processed_text = []

    for index, line in enumerate(lines):
        # debug_log(f"Processing line {index + 1}: {line.strip()}")

        # Stop processing when the 'Anexo' marker is encountered
        if re.search(anexo_pattern, line, re.IGNORECASE):
            # debug_log(f"Found 'Anexo' marker at line {index + 1}. Stopping processing.")
            break

        # Append all lines before the 'Anexo' marker
        processed_text.append(line)

    # debug_log(f"Processed text contains {len(processed_text)} lines.")
    # debug_log(f"Processed text sample:\n{'\n'.join(processed_text[:5])}")

    # Save the processed text for debugging
    # save_debug_text_to_file(output_dir, "processed_text.json", "\n".join(processed_text))
    return "\n".join(processed_text)


# Removed normalize_text
# Optional log_artifacts remains
def log_artifacts(raw_text, output_dir):
    """Log the raw text with artifact visualization for debugging."""
    artifact_log_path = os.path.join(output_dir, "artifact_debug.log")
    try:
        with open(artifact_log_path, "w", encoding="utf-8") as file:
            for char in raw_text:
                if char.isprintable():
                    file.write(char)
                else:
                    file.write(f"[{repr(char)}]")  # Represent non-printable characters
        # debug_log(f"Artifact debug saved to {artifact_log_path}")
    except Exception as e:
        debug_log(f"Failed to log artifacts: {e}")


# Example optional call in main()


def load_references(json_path):
    """Load references from JSON and parse relevant details."""
    try:
        with open(json_path, "r") as file:
            references = json.load(file)
    except json.JSONDecodeError:
        # debug_log("Failed to load references: Invalid JSON format.")
        return []

    parsed_references = []
    for ref in references:
        match = re.search(r"(.*?)\.\s\((\d{4})\)\.\s(.*?)\.", ref["reference"])
        if match:
            parsed_references.append(
                {
                    "author": match.group(1),
                    "year": match.group(2),
                    "title": match.group(3),
                    "reference": ref["reference"],
                    "is_compliant": ref["is_compliant"],
                    "url": ref.get("url", False),
                }
            )
    # debug_log(f"Loaded {len(parsed_references)} references.")
    return parsed_references


def search_citations_in_text(full_text, metadata):
    """Locate and log citations in the text, capturing their locations."""
    # debug_log("Starting citation search in extracted text.")

    total_units = metadata.get("total_units", 0)  # Total lines in the text
    unit_type = metadata.get("unit_type", "lines")  # Either "pages" or "lines"
    # debug_log(f"Exploring {total_units} {unit_type} in the text.")

    # Regex to match APA-style citations
    citation_pattern = r"\(([^()]+?),\s*(\d{4})(?:, p\.?\s*\d+)?\)"
    citations_with_locations = []
    lines = full_text.split("\n")  # Split text into lines

    for index, line in enumerate(lines, start=1):
        # debug_log(f"Checking line {index}: {line.strip()}")
        matches = re.findall(citation_pattern, line)
        if matches:
            # debug_log(f"Matches found in line {index}: {matches}")
            for match in matches:
                citations_with_locations.append({"citation": match, "location": index})
        else:
            debug_log(f"No matches in line {index}.")  # Log if no match is found

    # debug_log(f"Total citations found: {len(citations_with_locations)}")
    return citations_with_locations


def generate_report_with_locations(
    matched, unmatched, references, output_dir, title, report_name="citation_report.md"
):
    """Generate a markdown report with citation locations and save it in the specified directory."""
    report_name = f"{title}_{report_name}"
    output_path = os.path.join(output_dir, report_name)

    cited_references = {f"{c['citation'][0]}, {c['citation'][1]}" for c in matched}
    uncited_references = [
        ref
        for ref in references
        if f"{ref['author']}, {ref['year']}" not in cited_references
    ]

    # debug_log(f"Generating Markdown report at: {output_path}")

    with open(output_path, "w") as report:
        report.write("# Citation Analysis Report\n\n")
        report.write("## Summary\n")
        report.write(f"- Total Citations: {len(matched) + len(unmatched)}\n")
        report.write(f"- Properly Cited: {len(matched)}\n")
        report.write(f"- Improperly Cited: {len(unmatched)}\n")
        report.write(f"- References Not Cited: {len(uncited_references)}\n\n")

        if matched:
            report.write("### Properly Cited:\n")
            for item in matched:
                location = item.get("location", "Unknown")
                report.write(
                    f"- {item['citation'][0]}, {item['citation'][1]} (Location: {location})\n"
                )

        if unmatched:
            report.write("\n### Improperly Cited:\n")
            for item in unmatched:
                location = item.get("location", "Unknown")
                report.write(
                    f"- {item['citation'][0]}, {item['citation'][1]} (Location: {location})\n"
                )

        report.write("\n## References Not Cited:\n")
        for ref in uncited_references:
            report.write(f"- {ref['author']} ({ref['year']}). {ref['title']}\n")

    # debug_log(f"Markdown report successfully saved at: {output_path}")


def main():
    thesis_file, thesis_dir = choose_file("thesis")
    # debug_log(f"Selected thesis file: {thesis_file}")

    references_file, _ = choose_file("references")
    # debug_log(f"Selected references file: {references_file}")

    if not thesis_file or not references_file:
        # debug_log("File selection aborted.")
        return

    thesis_title = get_file_title(thesis_file)
    # debug_log(f"Thesis title: {thesis_title}")

    source_type = "pdf" if thesis_file.endswith(".pdf") else "docx"
    raw_text = extract_text(thesis_file, source_type)

    # Save raw text to a JSON file
    # save_debug_text_to_file(thesis_dir, "raw_text.json", raw_text)

    filtered_text = process_extracted_text(raw_text, thesis_dir)

    references = load_references(references_file)

    metadata = {"total_units": len(filtered_text.split("\n")), "unit_type": "lines"}

    # debug_log(f"Metadata for citation search: {metadata}")

    citations_with_locations = search_citations_in_text(filtered_text, metadata)

    matched = []
    unmatched = []
    for citation in citations_with_locations:
        author, year = citation["citation"]
        # debug_log(f"Checking citation: Author={author}, Year={year}")
        if any(
            ref for ref in references if ref["author"] == author and ref["year"] == year
        ):
            matched.append(citation)
            # debug_log(f"Match found for: Author={author}, Year={year}")
        else:
            unmatched.append(citation)
            # debug_log(f"No match for: Author={author}, Year={year}")

    # debug_log(f"Matched citations: {matched}")
    # debug_log(f"Unmatched citations: {unmatched}")

    generate_report_with_locations(
        matched, unmatched, references, thesis_dir, thesis_title
    )
    # debug_log("Report generation completed.")


if __name__ == "__main__":
    main()
