import zipfile
import json
from lxml import etree
from AppKit import NSApp
from Cocoa import NSOpenPanel


def select_docx_file():
    """Open a native macOS file picker to select a DOCX file."""
    panel = NSOpenPanel.openPanel()
    panel.setAllowedFileTypes_(["docx"])
    panel.setCanChooseFiles_(True)
    panel.setCanChooseDirectories_(False)

    if panel.runModal() == 1:  # 1 means OK button clicked
        return panel.URLs()[0].path()
    return None


def extract_body_text(docx_path):
    """Extract all body text from the main document."""
    body_text = []
    try:
        with zipfile.ZipFile(docx_path, "r") as docx_zip:
            # Read the main document.xml
            document_xml = docx_zip.read("word/document.xml")
            tree = etree.XML(document_xml)

            # Extract all paragraphs from the document body
            for element in tree.xpath(
                "//w:p",
                namespaces={
                    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
                },
            ):
                paragraph_text = "".join(
                    t.text
                    for t in element.xpath(
                        ".//w:t",
                        namespaces={
                            "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
                        },
                    )
                    if t.text
                ).strip()
                if paragraph_text:
                    body_text.append(paragraph_text)
    except Exception as e:
        print(f"Error extracting body text: {e}")
    return body_text


def detect_language(body_text):
    """Detect whether the document is in English or Spanish."""
    spanish_keywords = ["referencias bibliográficas"]
    english_keywords = ["references"]

    for paragraph in body_text:
        paragraph_lower = paragraph.lower()
        if any(keyword in paragraph_lower for keyword in spanish_keywords):
            return "spanish"
        elif any(keyword in paragraph_lower for keyword in english_keywords):
            return "english"

    return "unknown"


def extract_last_bibliography_section(body_text, language):
    """Extract text starting from the last occurrence of the bibliography section, excluding the keyword line."""
    last_index = -1
    keyword = "referencias bibliográficas" if language == "spanish" else "references"

    # Find the last occurrence of the keyword
    for i, paragraph in enumerate(body_text):
        if keyword in paragraph.lower():
            last_index = i

    if last_index != -1:
        # Skip the line containing the keyword and return the rest
        return body_text[last_index + 1 :]
    else:
        return []


def save_bibliography_to_markdown(docx_path, output_path, language):
    """Save the extracted Bibliography section to a Markdown file."""
    body_text = extract_body_text(docx_path)
    bibliography_content = extract_last_bibliography_section(body_text, language)

    if bibliography_content:
        try:
            with open(output_path, "w", encoding="utf-8") as md_file:
                md_file.write(f"# Bibliography Section ({language.capitalize()})\n\n")
                md_file.write("\n".join(bibliography_content) + "\n")
            print(f"Bibliography section saved to {output_path}")
        except Exception as e:
            print(f"Error saving Bibliography section: {e}")
    else:
        print(
            f"No bibliography section found in the document for language: {language}."
        )


def save_bibliography_to_json(docx_path, output_path, language):
    """Save the extracted Bibliography section to a JSON file."""
    body_text = extract_body_text(docx_path)
    bibliography_content = extract_last_bibliography_section(body_text, language)

    if bibliography_content:
        try:
            bibliography_data = {
                "language": language,
                "references": bibliography_content,
            }
            with open(output_path, "w", encoding="utf-8") as json_file:
                json.dump(bibliography_data, json_file, indent=4, ensure_ascii=False)
            print(f"Bibliography section saved to {output_path}")
        except Exception as e:
            print(f"Error saving Bibliography section: {e}")
    else:
        print(
            f"No bibliography section found in the document for language: {language}."
        )


def main():
    """Main function to select DOCX file and extract Bibliography section."""
    NSApp()
    print("Select a DOCX file...")
    docx_path = select_docx_file()

    if docx_path:
        # Extract body text to detect language
        body_text = extract_body_text(docx_path)
        language = detect_language(body_text)

        if language == "unknown":
            print(
                "Could not determine the language. Please ensure the document contains either 'Referencias bibliográficas' or 'References'."
            )
        else:
            print(f"Detected language: {language.capitalize()}")

            # Output paths for Bibliography Markdown and JSON files
            bibliography_md_path = docx_path.replace(
                ".docx", f"_{language}_bibliography.md"
            )
            bibliography_json_path = docx_path.replace(
                ".docx", f"_{language}_bibliography.json"
            )

            # Save bibliography to both formats
            save_bibliography_to_markdown(docx_path, bibliography_md_path, language)
            save_bibliography_to_json(docx_path, bibliography_json_path, language)
    else:
        print("File selection cancelled.")


if __name__ == "__main__":
    main()
