import re
import os
import json
import logging
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from AppKit import NSOpenPanel

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")


class ReferencesDetector:
    """Class to identify and extract the References section."""

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text_elements = []
        self.references = []
        self.references_matches_count = 0

    def extract_text_with_positions(self):
        """Extract text with positional data using PDFMiner."""
        try:
            for page_layout in extract_pages(self.pdf_path):
                for element in page_layout:
                    if isinstance(element, LTTextContainer):
                        for line in element:
                            if hasattr(line, "x0") and hasattr(line, "y0"):
                                self.text_elements.append({
                                    "text": line.get_text().strip(),
                                    "x0": line.x0,
                                    "y0": line.y0,
                                    "x1": line.x1,
                                    "y1": line.y1,
                                    "page": page_layout.pageid  # Track page number
                                })
        except Exception as e:
            raise RuntimeError(f"Error extracting text from PDF: {e}")

    def trim_to_references_section(self):
        """Trim all text before the last occurrence of 'REFERENCIAS' or equivalent."""
        if not self.text_elements:
            raise ValueError("No text elements found. Run `extract_text_with_positions` first.")

        # Regex to detect 'REFERENCIAS'-like headings
        references_heading_pattern = re.compile(r"(?i)\b(REFERENCIAS|BIBLIOGRAPHY|REFERENCES)\b")

        # Find all matches for the heading
        matches = [
            idx for idx, element in enumerate(self.text_elements)
            if references_heading_pattern.search(element["text"])
        ]

        # Record the number of matches
        self.references_matches_count = len(matches)

        if not matches:
            logging.warning("No 'REFERENCES' section detected.")
            return

        # Use the last match as the start of the References section
        references_start = matches[-1]

        # Keep only the elements from the start of the References section onward
        self.text_elements = self.text_elements[references_start:]


    def detect_references(self):
        """Detect the References section based on Author-Year patterns."""
        if not self.text_elements:
            raise ValueError("No text elements found. Run `extract_text_with_positions` first.")

        # Regex pattern for references
        reference_pattern = re.compile(
            r"([A-Z][A-Za-z\s&.,]+)\.\s*\(?\d{1,2}\s+de\s+[A-Za-z]+\s+de\s+\d{4}\)?\..*?https?://\S+",
            re.DOTALL
        )

        # Concatenate all text elements with their page numbers
        full_text = " ".join(element["text"] for element in self.text_elements)

        # Find all references
        references = reference_pattern.findall(full_text)

        # Store references with their corresponding page numbers
        self.references = []
        for ref in references:
            # Find the page number for this reference
            # Iterate through text_elements to find the element containing this reference
            for element in self.text_elements:
                if ref in element["text"]:
                    page_number = element["page"]
                    break
            else:
                # If no page number is found, default to the last page
                page_number = self.text_elements[-1]["page"]

            self.references.append({"text": ref.strip(), "page": page_number})

        return self.references


    def save_to_json(self, output_path):
        """Save the detected References section to a JSON file."""
        data = {
            "library": "PDFMiner",
            "pdf_path": self.pdf_path,
            "references_matches_count": self.references_matches_count,
            "references": self.references
        }

        try:
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            logging.info(f"References saved to {output_path}")
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")
        """Save the detected References section to a JSON file."""
        data = {
            "library": "PDFMiner",
            "pdf_path": self.pdf_path,
            "references_matches_count": self.references_matches_count,
            "references": self.references
        }

        try:
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            logging.info(f"References saved to {output_path}")
        except Exception as e:
            logging.error(f"Error saving to JSON file: {e}")


def select_pdf_file():
    """Open a native macOS file picker to select a PDF file."""
    panel = NSOpenPanel.openPanel()
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["pdf"])

    if panel.runModal() == 1:  # 1 means OK button clicked
        return panel.URLs()[0].path()
    return None


def main():
    """Main function to detect References in a PDF."""
    logging.info("Select a PDF file...")
    pdf_path = select_pdf_file()

    if not pdf_path:
        logging.warning("No file selected. Exiting.")
        return

    detector = ReferencesDetector(pdf_path)

    logging.info("Extracting text with positions...")
    detector.extract_text_with_positions()  # <-- Ensure this is called

    logging.info("Trimming to References section...")
    detector.trim_to_references_section()

    logging.info("Detecting References section...")
    references = detector.detect_references()

    if references:
        logging.info("\nReferences Detected:")
        for ref in references:
            logging.info(f"  Page {ref['page']}: {ref['text']}")

        # Save results to JSON
        output_path = os.path.splitext(pdf_path)[0] + "_references.json"
        detector.save_to_json(output_path)
    else:
        logging.warning("No References found in the document.")


if __name__ == "__main__":
    main()