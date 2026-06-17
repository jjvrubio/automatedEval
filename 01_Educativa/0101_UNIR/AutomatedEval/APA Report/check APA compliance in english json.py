import re
import os
import json
from typing import List
from AppKit import NSOpenPanel, NSApplication


def read_json_file(file_path: str) -> List[str]:
    """Read references from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data.get("references", [])


def write_markdown_file(file_path: str, content: str):
    """Write content to a Markdown file."""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def check_apa_compliance(reference: str) -> str:
    """Check if a reference complies with APA 7 format."""
    # Simple regex patterns for APA 7 compliance (this can be expanded for more detailed checks)
    patterns = {
        "author": r"^[A-Z][a-z]+, [A-Z]\.",
        "year": r"\(\d{4}\)",
        "title": r"\. [A-Z][a-z]+",
        "source": r"\. [A-Z][a-z]+",
    }

    issues = []
    for key, pattern in patterns.items():
        if not re.search(pattern, reference):
            issues.append(f"Missing or incorrect {key} format.")

    if issues:
        return "Issues found: " + "; ".join(issues)
    else:
        return "Complies with APA 7 format."


def generate_report(references: List[str], report_path: str):
    """Generate a compliance report in Markdown format."""
    report_lines = ["# APA 7 Compliance Report\n"]

    for i, reference in enumerate(references, start=1):
        compliance_result = check_apa_compliance(reference)
        report_lines.append(f"## Reference {i}\n")
        report_lines.append(f"**Reference:** {reference}\n")
        report_lines.append(f"**Compliance Check:** {compliance_result}\n")
        report_lines.append("\n")

    write_markdown_file(report_path, "\n".join(report_lines))


def select_file() -> str:
    """Open a file dialog to select a JSON file and return the file path."""
    NSApplication.sharedApplication()
    panel = NSOpenPanel.alloc().init()
    panel.setTitle_("Select the bibliography JSON file")
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)
    panel.setAllowsMultipleSelection_(False)
    panel.setAllowedFileTypes_(["json"])

    if panel.runModal() == 1:
        return panel.URLs()[0].path()
    return None


def main():
    # Select the bibliography file
    input_path = select_file()
    if not input_path:
        print("No file selected.")
        return

    # Generate the report path in the same folder as the source file
    report_path = os.path.splitext(input_path)[0] + "_compliance_report.md"

    # Read references from the JSON file
    references = read_json_file(input_path)

    if not references:
        print("No references found in the JSON file.")
        return

    # Generate the compliance report
    generate_report(references, report_path)

    print(f"Compliance report generated at {report_path}")


if __name__ == "__main__":
    main()
