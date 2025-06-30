# test_imports_diagnostico.py
import time

def test_import(module_name):
    print(f"Intentando importar: {module_name} ...", end=" ")
    t0 = time.time()
    try:
        __import__(module_name)
        print(f"OK ({time.time()-t0:.2f}s)")
    except Exception as e:
        print(f"FALLO: {e}")

modules = [
    "os",
    "pandas",
    "openai",
    "pdfplumber",
    "docx",
    "logging",
    "dotenv",
    # "AppKit",  # Descomenta si quieres probar AppKit
    # "tkinter",  # Descomenta si quieres probar tkinter
]

for mod in modules:
    test_import(mod)

print("\nPrueba de imports finalizada.")
