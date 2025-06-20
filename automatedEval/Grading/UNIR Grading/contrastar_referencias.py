import json

# Carga los archivos
with open('tfm_entrega_final_ordinaria_referencias_apa.json', encoding='utf-8') as f:
    referencias = json.load(f)
with open('tfm_entrega_final_ordinaria_referencias_no_citadas.json', encoding='utf-8') as f:
    no_citadas = json.load(f)

# Normaliza y extrae primer apellido y año de cada referencia
import re
def normaliza(s):
    return s.lower().replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')

def ref_key(ref):
    m = re.match(r'^([A-ZÁÉÍÓÚÑ][a-záéíóúñA-ZÁÉÍÓÚÑ .,&-]+)\s*\((\d{4}[a-z]?)', ref)
    if m:
        autores = m.group(1)
        year = m.group(2)
        norm_autores = normaliza(autores)
        norm_autores = re.sub(r"et al\.|&", "", norm_autores)
        norm_autores = re.sub(r"[^a-zñ .,]", "", norm_autores)
        norm_autores = norm_autores.strip()
        primer_apellido = norm_autores.split(',')[0].split()[0]
        return f"{primer_apellido}, {year}"
    return None

claves_referencias = set(ref_key(r) for r in referencias if ref_key(r))
claves_no_citadas = set(ref_key(r) for r in no_citadas if ref_key(r))

print("Claves de referencias:", claves_referencias)
print("Claves de referencias no citadas:", claves_no_citadas)
print("Diferencia (referencias no citadas reales):", claves_no_citadas - claves_referencias)
print("Diferencia (referencias que sí están citadas):", claves_referencias - claves_no_citadas)
