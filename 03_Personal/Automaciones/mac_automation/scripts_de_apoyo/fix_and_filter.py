#!/usr/bin/env python3
"""
Script para corregir y filtrar un JSON malformado.
"""

import json
from pathlib import Path
from datetime import datetime


def fix_and_filter_json(input_file: str, prefix_to_remove: str, output_file: str = None):
    """
    Corrige un JSON sin corchetes iniciales y filtra por prefijo.
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {input_file}")
    
    print(f"Leyendo y corrigiendo {input_file}...")
    
    # Leer el contenido
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    # Intentar arreglar el JSON
    # Si no empieza con '[', intentar agregarlo
    if not content.startswith('['):
        print("Agregando '[' al inicio...")
        content = '[' + content
    
    # Si no termina con ']', intentar agregarlo
    if not content.endswith(']'):
        print("Agregando ']' al final...")
        content = content + ']'
    
    # Intentar parsear
    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        print(f"Error parseando JSON: {e}")
        raise
    
    total_entries = len(data)
    print(f"Total de entradas: {total_entries}")
    print(f"Filtrando entradas que empiecen con: '{prefix_to_remove[:50]}...'")
    
    # Filtrar
    filtered_data = []
    removed = 0
    
    for entry in data:
        notes_content = entry.get('notes', '').strip()
        
        if notes_content.startswith(prefix_to_remove):
            removed += 1
        else:
            filtered_data.append(entry)
    
    # Generar nombre de salida
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = input_path.parent / f"{input_path.stem}-filtered-{timestamp}.json"
    else:
        output_file = Path(output_file)
    
    # Guardar
    print(f"\nGuardando datos filtrados en: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*60)
    print("RESUMEN")
    print("="*60)
    print(f"Entradas originales: {total_entries}")
    print(f"Entradas eliminadas: {removed}")
    print(f"Entradas restantes: {len(filtered_data)}")
    print(f"Porcentaje eliminado: {(removed/total_entries*100):.1f}%")
    print(f"Archivo de salida: {output_file}")
    print("="*60)
    
    return {
        'total': total_entries,
        'removed': removed,
        'remaining': len(filtered_data),
        'output': str(output_file)
    }


if __name__ == "__main__":
    import sys
    
    PREFIX = "=20 =20 =20 =20 =20 =C2=A9 2011-"
    
    if len(sys.argv) < 2:
        print("Uso: python3 fix_and_filter.py <archivo_entrada.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        fix_and_filter_json(input_file, PREFIX, output_file)
        print("\n✅ Proceso completado exitosamente")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
