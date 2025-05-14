import re
import json

# Input JSON with split references
references = [
    "ABPMP. (2009). Association of Business Process Management Professionals. BPM CBOK –",
    "Business Process Management: common body of knowledge. ABPMP, Chicago.",
    "AENOR. (2005). Norma ISO 9000:2005 Sistemas de gestión de la calidad - Fundamentos y",
    "vocabulario. ISO (Organización Internacional de Normalización). Traducción Certificada. Madrid. Recuperado de https://www.iso.org/obp/ui/#iso:std:iso:9000:ed-3:v1:es",
    "Albatian (2019). Banco Fie Transformación Digital. Albatian, Madrid. Recuperado de http://bit.ly/2UkpVmd.",
    "AuraPortal (s.f.). Caso de Éxito CAF Power & Automation. Recuperado de http://bit.ly/2IJcOsM.",
    "Bizneo. (s.f). Gestión de RRHH, Eficiente, Sencilla y Automatizada. Recuperado de: https://cutt.ly/GkxN7xQ",
    "Bizagi (s.f.). Caso de Éxito Geometry. Geometry disminuye errores en un 60% en 60días con la solución colaborativa de Bizagi. Recuperado de http://bit.ly/2V2uZA0. Factorial. (s.f). Software Para RRHH. Recuperado de: https://factorialhr.es/",
    "Gamelearn. (s.f). 10 tendencias que Marcarán las Futuro de los Recursos Humanos. Tomado de Deloitte, The social Enterpreside in a World Disrupted. Recuperado de: https://www.game-learn.com/10-tendencias-futuro-recursos-humanos/",
    "Garimella, K., Lees, M., & Williams, B. (2008). BPM (Gerencia de procesos de",
    "negocio). Introducción a BPM.",
    "Novasoft. (s.f). Software de Gestión Humana. Recuperado de: https://www.novasoft.com.co/gestion-talento-humano/",
    "Oracle. (s.f). Oracle Human Capital Management. Recuperado de: https://www.oracle.com/human-capital-management/",
    "Pectra (s.f.). Caso Quala. Recuperado de https://n9.cl/bplus.",
    "Piraquive, F. N. D. (2008). Gestión de procesos de negocio BPM (Business Process",
    "Management), TICs y crecimiento empresarial. ¿Qué es BPM y cómo se articula con el",
    "crecimiento empresarial? Universidad & Empresa, 7(15), 151-176.",
    "Robledo, P. (2014). BPMteca.com: El Ciclo de Vida de BPM. Recuperado de: https://bit.ly/324QfGz.",
    "Robledo, P. (2018). ¿Cómo seleccionar software BPM? Recuperado de http://bit.ly/2FoansT.",
    "Robledo, P. (2019). Fundamentos de Transformación Digita y Business Process Management.",
    "UNIR, España. Material de clase del MUBPM.",
    "Ultimus (s.f.). El bufete de abogados Cuatrecasas ahorra semanas de tiempo al automatizar nuevos procesos de empleados de recursos humanos. Recuperado de https://n9.cl/y5nov.",
    "Ultimus (s.f.). Las escuelas de Eyuboglu implementan soluciones empresariales. Recuperado de https://n9.cl/7hbog."
]

# Utility function for debug output
def debug_output(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# Step 0: Enhanced Detector for Embedded References
def detect_and_split_embedded_references(references):
    embedded_indices = []
    split_references = []

    # Pattern for valid Author/Corporate + [(Year) | (s.f.)]
    author_year_pattern = r"[A-Za-z0-9.,&\s]+\.?\s*\((\d{4}|s\.f\.)\)"

    for i, line in enumerate(references):
        matches = list(re.finditer(author_year_pattern, line))
        if len(matches) > 1:  # Multiple references found in the same line
            embedded_indices.append(i)
            
            # Perform split
            start = 0
            for match in matches:
                end = match.start()
                if start != end:  # Add the text before the next match
                    split_references.append(line[start:end].strip())
                start = match.start()
            split_references.append(line[start:].strip())  # Add the remaining part of the line
        else:
            split_references.append(line.strip())  # Keep the line unchanged if no split is needed

    # Debug output for split references
    debug_output("split_embedded_references.json", {
        "embedded_indices": embedded_indices,
        "split_references": split_references
    })

    return split_references, embedded_indices


# Test the function and debug outputs
split_references, embedded_indices = detect_and_split_embedded_references(references)
debug_output("split_references.json", split_references)
debug_output("embedded_indices.json", embedded_indices)

