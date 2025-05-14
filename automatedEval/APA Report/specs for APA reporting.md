I have this code: 

''' import Quartz as qtz

from AppKit import NSOpenPanel

from Foundation import NSURL

import re

\# PDF file selection function using macOS native file dialog

def get_file_path():

​    panel = NSOpenPanel.alloc().init()

​    panel.setTitle_("Choose a PDF file")

​    panel.setAllowedFileTypes_(["pdf"])

​    panel.setCanChooseFiles_(True)

​    panel.setCanChooseDirectories_(False)

​    panel.setAllowsMultipleSelection_(False)

​    if panel.runModal() == 1:

​        return panel.URLs()[0].path()

​    return None

\# Function to remove headers, footers, and page numbers from the text

def remove_headers_footers(text):

​    """Removes headers, footers, and page numbers from the extracted text."""

​    lines = text.splitlines()

​    clean_lines = []

​    for line in lines:

​        if not re.match(r'^(--- Page \d+ ---|\d+)$', line):

​            clean_lines.append(line)

​    return "\n".join(clean_lines)

\# Function to gather text between "Referencias bibliográficas" and the first valid "Anexo"

def gather_text_between_marks(text):

​    """Gathers text between the first valid 'Referencias bibliográficas' not followed by dots, blanks, or numbers and the first valid 'Anexo'."""

​    start_pattern = re.compile(r'(?i)^Referencias bibliográficas', re.MULTILINE)

​    end_pattern = re.compile(r'(?i)^Anexo\b', re.MULTILINE)

​    start_match = None

​    for match in start_pattern.finditer(text):

​        line_end = text[match.end():text.find("\n", match.end())].strip()

​        if not re.match(r'[.\s\d]', line_end):

​            start_match = match

​            break

​    if not start_match:

​        print("DEBUG: No valid start marker found.")

​        return "No valid start marker found."

​    start_index = text.find("\n", start_match.end()) + 1

​    end_match = end_pattern.search(text, start_index)

​    if not end_match:

​        print("DEBUG: No valid end marker found after the start marker.")

​        return "No valid end marker found."

​    gathered_text = text[start_index:end_match.start()].strip()

​    return gathered_text

\# PDF extraction function using Quartz/Core Graphics

def extract_text_from_pdf(file_path):

​    """Extract text from a PDF file using macOS native Core Graphics."""

​    pdf_url = NSURL.fileURLWithPath_(file_path)

​    pdf_doc = qtz.PDFDocument.alloc().initWithURL_(pdf_url)

​    if not pdf_doc:

​        print("Failed to open PDF file.")

​        return

​    extracted_text = ""

​    for page_number in range(pdf_doc.pageCount()):

​        page = pdf_doc.pageAtIndex_(page_number)

​        if page:

​            page_text = page.string()

​            extracted_text += f"\n--- Page {page_number + 1} ---\n{page_text}\n"

​    \# Remove headers, footers, and page numbers

​    cleaned_text = remove_headers_footers(extracted_text)

​    \# Gather the extracted text

​    gathered_text = gather_text_between_marks(cleaned_text)

​    \# Save the gathered text to a file

​    with open("gathered_text.md", "w", encoding="utf-8") as f:

​        f.write(gathered_text)

​    print("Gathered text saved to gathered_text.md")

​    return gathered_text

\# Main function to run the extraction

def main():

​    file_path = get_file_path()

​    if not file_path:

​        print("No file selected. Exiting.")

​        return

​    extract_text_from_pdf(file_path)

if __name__ == "__main__":

​    main()'''



Whic is working properly generating the expect contets in text extraction file.



For this file to be useful to analyse its APA 7 compliance it is needed to remove headers, footers, and page numbers that comes form the origional PDF document. These are Function 1, 2 and 3.

# Function 1

'''

def identify_head_footer_pattern(pdf):

​    """Identify potential header and footer patterns by analyzing text repetition across pages."""

​    text_patterns = Counter()

​    for page in pdf.pages:

​        page_text = page.extract_text()

​        if page_text:

​            lines = page_text.splitlines()

​            for line in lines:

​                text_patterns[line] += 1

​    total_pages = len(pdf.pages)

​    head_footer_patterns = [pattern for pattern, count in text_patterns.items() if count > 0.8 * total_pages]

​    return head_footer_patterns

'''

# Function 2

'''

def is_page_number(text):

​    """Detect if the given text is a page number."""

​    patterns = [

​        r"^\d+$",

​        r"^(Page|Página) \d+$",

​        r"^\d+/\d+$"

​    ]

​    return any(re.match(pattern, text.strip()) for pattern in patterns)

'''

# Function 3

'''

def filter_head_footer_patterns(text, patterns):

​    """Remove identified header/footer patterns from the text."""

​    lines = text.splitlines()

​    filtered_text = "\n".join(line for line in lines if line.strip() not in patterns and not is_page_number(line))

​    return filtered_text

'''

---



Because I like isolation I prefer having a funtion which orchestrate the 3 funtions above. Whose output is a file that will used in Funtion 4. nad at this stage please add a markdown debug file.

# Function 4

'''

def review_apa7_format(references):

​    """Check if the given references comply with APA 7 format."""

​    report = []

​    apa_pattern = r"^[A-Za-zÁÉÍÓÚÑáéíóúñ]+(?:, [A-Z]\.)+ \(\d{4}\)"

​    for i, ref in enumerate(references, 1):

​        if re.match(apa_pattern, ref):

​            report.append(f"Reference {i}: ✅ APA 7 Compliant\n{ref}")

​        else:

​            report.append(f"Reference {i}: ❌ Not APA 7 Compliant\n{ref}")

​    return report

'''

Its out are two files with the same content one in .md format and the other in json format.