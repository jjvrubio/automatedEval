# test_input_file_path.py
print("[INPUT] Introduce la ruta completa del archivo (puedes arrastrar el archivo aquí y pulsar Enter):")
file_path = input().strip()
if file_path:
    print(f"[INPUT] Archivo introducido: {file_path}")
else:
    print("[INPUT] No se introdujo ninguna ruta.")
