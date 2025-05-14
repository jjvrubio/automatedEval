import os
import json
import re
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer
from AppKit import NSOpenPanel


class PDFAnalyzer:
    """Encapsulates logic for PDF text extraction and analysis."""

    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.text_elements = []
        self.merged_lines = []

    def extract_text_with_positions(self):
        """Extract text with positional data using PDFMiner."""
        text_elements = []
        for page_layout in extract_pages(self.pdf_path):
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    for line in element:
                        if hasattr(line, "x0") and hasattr(line, "y0"):
                            text_elements.append({
                                "text": line.get_text().strip(),
                                "x0": line.x0,
                                "y0": line.y0,
                                "x1": line.x1,
                                "y1": line.y1
                            })
        self.text_elements = text_elements

    def merge_lines_with_positions(self, y_tolerance=2):
        """Merge fragmented lines into paragraphs based on positional data."""
        if not self.text_elements:
            raise ValueError("No text elements found. Run `extract_text_with_positions` first.")

        # Sort elements by Y descending and X ascending
        self.text_elements.sort(key=lambda e: (-e["y0"], e["x0"]))
        merged_lines = []
        current_line = ""
        last_y = None

        for element in self.text_elements:
            line_text = element["text"]
            current_y = element["y0"]

            # Check proximity to decide if it belongs to the same paragraph
            if last_y is not None and abs(current_y - last_y) > y_tolerance:
                # Start a new paragraph if Y difference exceeds tolerance
                if current_line:
                    merged_lines.append(current_line.strip())
                current_line = line_text
            else:
                # Continue the current paragraph
                current_line += " " + line_text

            last_y = current_y

        # Add the last line
        if current_line:
            merged_lines.append(current_line.strip())

        self.merged_lines = merged_lines

    def filter_repeated_lines(self, min_repetition=3):
        """Filter out lines repeated more than a certain number of times."""
        if not self.merged_lines:
            raise ValueError("No merged lines found. Run `merge_lines_with_positions` first.")

        line_counts = {}
        for line in self.merged_lines:
            line_counts[line] = line_counts.get(line, 0) + 1

        self.merged_lines = [line for line in self.merged_lines if line_counts[line] <= min_repetition]

    def analyze_text(self):
        """Analyze the merged text for metrics and prepare the last 10 paragraphs."""
        if not self.merged_lines:
            raise ValueError("No merged lines found. Run `merge_lines_with_positions` first.")

        eol_count = sum(line.count("\n") for line in self.merged_lines)
        paragraph_count = len(self.merged_lines)
        last_10_paragraphs = self.merged_lines[-10:] if paragraph_count >= 10 else self.merged_lines

        # Prepare paragraph details
        paragraph_details = [
            {"paragraph_number": idx + 1, "text": paragraph}
            for idx, paragraph in enumerate(last_10_paragraphs)
        ]

        return {
            "metrics": {
                "paragraph_count": paragraph_count,
                "eol_count": eol_count,
            },
            "contents": paragraph_details
        }

    def save_to_json(self, output_path, analysis):
        """Save the analysis results to a JSON file."""
        data = {"library": "PDFMiner"}
        data.update(analysis)

        try:
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(data, json_file, indent=4, ensure_ascii=False)
            print(f"Analysis saved to {output_path}")
        except Exception as e:
            print(f"Error saving to JSON file: {e}")


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
    """Main function to run the PDF analysis."""
    print("Select a PDF file...")
    pdf_path = select_pdf_file()

    if pdf_path:
        # Create analyzer instance
        analyzer = PDFAnalyzer(pdf_path)

        # Step-by-step execution
        print("Extracting text with positions...")
        analyzer.extract_text_with_positions()

        print("Merging lines with positions...")
        analyzer.merge_lines_with_positions()

        print("Filtering repeated lines...")
        analyzer.filter_repeated_lines(min_repetition=3)

        print("Analyzing text...")
        analysis = analyzer.analyze_text()

        # Save results
        output_path = os.path.splitext(pdf_path)[0] + "_analysis.json"
        print("Saving analysis to JSON...")
        analyzer.save_to_json(output_path, analysis)
    else:
        print("File selection cancelled.")


if __name__ == "__main__":
    main()
