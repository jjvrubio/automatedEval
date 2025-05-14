import json
import re

def fix_broken_references(extracted_text):
    """Fix broken references by splitting lines based on URLs, while preserving URLs within their references."""
    
    # Regex to detect URLs ending with a dot and followed by a space and uppercase letter (indicating a new reference)
    url_pattern = r"(https?://[^\s]+\.?)\s(?=[A-Z])"

    # This will store the final references
    references = []
    
    # Process each line
    lines = extracted_text.splitlines()

    for line in lines:
        print(f"Processing line: '{line}'")  # Debug statement

        # Find all URL matches
        matches = re.finditer(url_pattern, line)
        last_end = 0

        for match in matches:
            # Add the text before the URL + URL itself as one reference
            reference = line[last_end:match.end()].strip()
            references.append(reference)
            last_end = match.end()

        # Add any remaining text after the last URL
        if last_end < len(line):
            references.append(line[last_end:].strip())

    # Save debug information to markdown (for debugging)
    debug_to_markdown(references)

    # Return the final references
    return references

def debug_to_markdown(debug_info, filename="debug_log.md"):
    """Save the debug information to a markdown file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("# Debugging Information: References Split by URL\n\n")
            for entry in debug_info:
                file.write(f"**Reference**: {entry}\n\n")
        print(f"Debug info saved successfully to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the debug file: {e}")

def save_to_json(data, filename):
    """Save the extracted and merged references to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)
        print(f"JSON file saved successfully to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the JSON file: {e}")

# Test case with a single line containing multiple references (this will be split based on the URL)
test_text = """
Bizagi (s.f.). Caso de Éxito Geometry. Geometry disminuye errores en un 60% en 60días con la solución colaborativa de Bizagi. Recuperado de http://bit.ly/2V2uZA0. Factorial. (s.f). Software Para RRHH. Recuperado de: https://factorialhr.es/. Gamelearn. (s.f). 10 tendencias que Marcarán las Futuro de los Recursos Humanos. Tomado de Deloitte, The social Enterpreside in a World Disrupted. Recuperado de: https://www.game-learn.com/10-tendencias-futuro-recursos-humanos/.
"""

# Run the fix_broken_references function to test the URL regex and splitting logic
merged_references = fix_broken_references(test_text)

# Save the merged references to a JSON file
save_to_json(merged_references, 'merged_references.json')
