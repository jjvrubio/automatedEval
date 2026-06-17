from Quartz import PDFDocument
from pdfminer.high_level import extract_text
from Cocoa import NSOpenPanel, NSURL
import os
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


def extract_text_with_quartz(pdf_path):
    """Extract all text from a PDF file using Quartz."""
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
    return "\n".join(full_text)  # Join all pages with explicit EOLs


def extract_text_with_pdfminer(pdf_path):
    """Extract all text from a PDF file using PDFMiner."""
    try:
        return extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting text with PDFMiner: {e}")
        return ""


def analyze_text_and_extract_paragraphs(text):
    """Analyze the text and extract metrics and the last 10 paragraphs."""
    lines = text.splitlines()
    eol_count = text.count("\n")
    paragraphs = [
        p.strip() for p in text.split("\n\n") if p.strip()
    ]  # Split by double line breaks

    # Extract the last 10 paragraphs
    last_10_paragraphs = paragraphs[-10:] if len(paragraphs) >= 10 else paragraphs

    # Prepare paragraph details
    paragraph_details = [
        {"paragraph_number": idx + 1, "text": paragraph}
        for idx, paragraph in enumerate(last_10_paragraphs)
    ]

    return {
        "metrics": {
            "paragraph_count": len(paragraphs),
            "line_count": len(lines),
            "eol_count": eol_count,
        },
        "contents": paragraph_details,
    }


def save_analysis_to_json(output_path, library_name, analysis):
    """Save the analysis results and last 10 paragraphs to a JSON file."""
    data = {"library": library_name}
    data.update(analysis)  # Merge metrics and contents into the data dictionary

    try:
        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Analysis and paragraphs saved to {output_path}")
    except Exception as e:
        print(f"Error saving to JSON file: {e}")


def main():
    """Main function to select PDF, analyze text, and save results."""
    print("Select a PDF file...")
    pdf_path = select_pdf_file()

    if pdf_path:
        # Prompt user to select the library
        library_choice = (
            input("Choose library for text extraction (Quartz/PDFMiner): ")
            .strip()
            .lower()
        )

        if library_choice == "quartz":
            print("Using Quartz for text extraction...")
            text = extract_text_with_quartz(pdf_path)
            library_name = "Quartz"
        elif library_choice == "pdfminer":
            print("Using PDFMiner for text extraction...")
            text = extract_text_with_pdfminer(pdf_path)
            library_name = "PDFMiner"
        else:
            print("Invalid choice. Please choose 'Quartz' or 'PDFMiner'.")
            return

        if text.strip():
            # Analyze the text and extract metrics and paragraphs
            analysis = analyze_text_and_extract_paragraphs(text)

            # Save analysis and paragraphs to a JSON file
            base_path = os.path.splitext(pdf_path)[0]
            json_output_path = f"{base_path}_analysis.json"
            save_analysis_to_json(json_output_path, library_name, analysis)
        else:
            print("The selected PDF does not contain extractable text.")
    else:
        print("File selection cancelled.")


if __name__ == "__main__":
    main()
