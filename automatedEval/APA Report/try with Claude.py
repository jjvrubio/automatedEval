def clean_and_prepare_references(raw_text, debug=True):
    """Orchestrating function to clean and prepare references."""
    debug_info = {
        "identified_patterns": [],
        "raw_text_length": len(raw_text),
        "cleaned_text_length": 0,
        "references_count": 0,
        "references": [],
        "marker_debug": {
            "start_marker_found": False,
            "end_marker_found": False,
            "start_marker_line": "",
            "end_marker_line": "",
            "start_marker_position": -1,
            "end_marker_position": -1
        }
    }

    # Step 1: Identify patterns
    patterns = identify_head_footer_pattern(raw_text)
    debug_info["identified_patterns"] = patterns
    
    # Step 2: Filter out headers and footers
    cleaned_text = filter_head_footer_patterns(raw_text, patterns)
    debug_info["cleaned_text_length"] = len(cleaned_text)
    
    # Step 3: Extract references section
    start_pattern = re.compile(r'(?i)^Referencias bibliográficas(?![.\s\d])', re.MULTILINE)
    end_pattern = re.compile(r'(?i)^Anexo\b', re.MULTILINE)
    
    # Look for start marker
    start_match = None
    for match in start_pattern.finditer(cleaned_text):
        line_end = cleaned_text[match.end():cleaned_text.find("\n", match.end())].strip()
        if not re.match(r'[.\s\d]', line_end):
            start_match = match
            debug_info["marker_debug"]["start_marker_found"] = True
            debug_info["marker_debug"]["start_marker_position"] = match.start()
            debug_info["marker_debug"]["start_marker_line"] = cleaned_text[match.start():cleaned_text.find("\n", match.start())].strip()
            break
    
    if not start_match:
        if debug:
            with open("references_debug.md", "w", encoding="utf-8") as f:
                f.write("# References Processing Debug Info\n\n")
                f.write("## Marker Pattern Analysis\n")
                f.write("❌ Start marker 'Referencias bibliográficas' not found\n")
                f.write("\n## Identified Headers/Footers Patterns\n")
                for pattern in patterns:
                    f.write(f"- `{pattern}`\n")
                f.write(f"\n## Text Statistics\n")
                f.write(f"- Raw text length: {debug_info['raw_text_length']}\n")
                f.write(f"- Cleaned text length: {debug_info['cleaned_text_length']}\n")
                f.write("\n## First 500 characters of cleaned text:\n")
                f.write("```\n")
                f.write(cleaned_text[:500] + "...\n")
                f.write("```\n")
                f.write("\n## Last 500 characters of cleaned text:\n")
                f.write("```\n")
                f.write(cleaned_text[-500:] + "\n")
                f.write("```\n")
        return None, "No valid references section found."
    
    start_idx = cleaned_text.find("\n", start_match.end()) + 1
    end_match = end_pattern.search(cleaned_text, start_idx)
    
    if end_match:
        end_idx = end_match.start()
        debug_info["marker_debug"]["end_marker_found"] = True
        debug_info["marker_debug"]["end_marker_position"] = end_match.start()
        debug_info["marker_debug"]["end_marker_line"] = cleaned_text[end_match.start():cleaned_text.find("\n", end_match.start())].strip()
    else:
        end_idx = len(cleaned_text)
    
    references_text = cleaned_text[start_idx:end_idx].strip()
    references = [ref.strip() for ref in references_text.split('\n') if ref.strip()]
    debug_info["references"] = references
    debug_info["references_count"] = len(references)
    
    # Create debug file
    if debug:
        with open("references_debug.md", "w", encoding="utf-8") as f:
            f.write("# References Processing Debug Info\n\n")
            f.write("## Marker Pattern Analysis\n")
            f.write(f"✅ Start marker found at position {debug_info['marker_debug']['start_marker_position']}\n")
            f.write(f"- Line: `{debug_info['marker_debug']['start_marker_line']}`\n\n")
            
            if debug_info["marker_debug"]["end_marker_found"]:
                f.write(f"✅ End marker found at position {debug_info['marker_debug']['end_marker_position']}\n")
                f.write(f"- Line: `{debug_info['marker_debug']['end_marker_line']}`\n")
            else:
                f.write("❌ End marker 'Anexo' not found\n")
                f.write("- Using end of document as boundary\n")
            
            f.write("\n## Identified Headers/Footers Patterns\n")
            for pattern in patterns:
                f.write(f"- `{pattern}`\n")
            
            f.write(f"\n## Statistics\n")
            f.write(f"- Raw text length: {debug_info['raw_text_length']}\n")
            f.write(f"- Cleaned text length: {debug_info['cleaned_text_length']}\n")
            f.write(f"- References found: {debug_info['references_count']}\n")
            
            f.write("\n## Extracted References\n")
            for i, ref in enumerate(references, 1):
                f.write(f"{i}. {ref}\n")
            
            if not debug_info["marker_debug"]["end_marker_found"]:
                f.write("\n## Context Around End of References\n")
                f.write("Last 500 characters of extracted text:\n```\n")
                f.write(references_text[-500:] + "\n```\n")
    
    return references, None