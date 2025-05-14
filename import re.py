import re
import json
from AppKit import NSOpenPanel

# Utility function for debug output
def debug_output(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Step 0: Load references from a user-chosen file
def load_references():
    """
    Loads references from a user-selected file (JSON or TXT) using macOS native file dialog.
    Returns a list of references.
    """
    # Create the file open dialog
    panel = NSOpenPanel.openPanel()
    panel.setAllowsMultipleSelection_(False)  # Single file selection
    panel.setCanChooseDirectories_(False)    # Only files, not directories
    panel.setAllowedFileTypes_(["json", "txt"])  # Allow JSON or text files

    if panel.runModal() == 1:  # If the user selected a file
        file_path = panel.URLs()[0].path()
        try:
            # Determine file type by extension
            if file_path.endswith(".json"):
                with open(file_path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        return [ref.strip() for ref in data if isinstance(ref, str) and ref.strip()]
                    else:
                        print("The selected JSON file does not contain a list of references.")
                        return []
            elif file_path.endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as file:
                    return [line.strip() for line in file.readlines() if line.strip()]
            else:
                print("Unsupported file type selected.")
                return []
        except Exception as e:
            print(f"Error reading file: {e}")
            return []
    else:
        print("No file selected.")
        return []

# Step 1A: Detect embedded references
def detect_embedded_references(references):
    split_references = []
    embedded_indices = []

    author_year_pattern = r"[A-Za-z0-9.,&\s]+\.?\s*\((\d{4}|s\.f\.|s\.f)\)\s*"
    url_pattern = r"https?://[\w./-]+"

    for i, line in enumerate(references):
        matches = list(re.finditer(author_year_pattern, line))
        if len(matches) > 1:
            embedded_indices.append(i)

            second_ref_start = matches[1].start()
            url_match = re.search(url_pattern, line)
            if url_match and url_match.end() > second_ref_start:
                first_part = line[:url_match.end()].strip()
                second_part = line[url_match.end():].strip()
            else:
                first_part = line[:second_ref_start].strip()
                second_part = line[second_ref_start:].strip()

            split_references.append(first_part)
            split_references.append(second_part)
        else:
            split_references.append(line.strip())

    debug_output("refined_detect_embedded_references.json", {
        "embedded_indices": embedded_indices,
        "split_references": split_references
    })

    return split_references, embedded_indices

# Step 1B: Identify offending lines
def identify_offending_lines(references):
    author_year_pattern = r"^[A-Za-z0-9.,&\s]+\.?\s*\((\d{4}|s\.f\.|s\.f)\)\s*"
    offending_indices = [i for i, line in enumerate(references) if not re.match(author_year_pattern, line)]
    debug_output("identify_offending_lines.json", [references[i] for i in offending_indices])
    return offending_indices

# Step 1C: Merge offending lines
def merge_offending_lines(references, offending_indices):
    merged_references = []
    current_ref = ""

    for i, line in enumerate(references):
        if i in offending_indices:
            current_ref += " " + line.strip()
        else:
            if current_ref:
                merged_references.append(current_ref.strip())
            current_ref = line.strip()

    if current_ref:
        merged_references.append(current_ref.strip())

    debug_output("merge_offending_lines.json", merged_references)
    return merged_references

# Step 2: Check APA format compliance
def check_apa_format(references):
    results = []
    for reference in references:
        author_regex = r"^[A-Za-z.,&\s]+"
        year_regex = r"\((\d{4}|s\.f\.)\)"
        title_regex = r"\).+?\."
        url_regex = r"https?://[\w./-]+"

        compliance = {
            "author": bool(re.search(author_regex, reference)),
            "year": bool(re.search(year_regex, reference)),
            "title": bool(re.search(title_regex, reference)),
            "url": bool(re.search(url_regex, reference)),
            "is_compliant": all([bool(re.search(r, reference)) for r in [author_regex, year_regex, title_regex, url_regex]])
        }
        results.append({"reference": reference, **compliance})

    debug_output("check_apa_format.json", results)
    return results

# Main function
def main():
    # Step 0: Load references from user-selected file
    references = load_references()
    if not references:
        print("No references loaded. Exiting.")
        return

    # Step 1A: Detect embedded references
    split_references, embedded_indices = detect_embedded_references(references)
    offending_indices = identify_offending_lines(split_references)
    merged_references = merge_offending_lines(split_references, offending_indices)
    checked_references = check_apa_format(merged_references)

    print("Processing completed. Debug outputs saved for each step.")

if __name__ == "__main__":
    main()
