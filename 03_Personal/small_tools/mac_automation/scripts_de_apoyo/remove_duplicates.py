#!/usr/bin/env python3
"""
Script para eliminar entradas duplicadas del JSON de Streak notes.
Considera duplicados cuando el contenido de 'notes' es idéntico.
"""

import json
from pathlib import Path
from datetime import datetime


def remove_duplicates(input_file: str, output_file: str = None) -> dict:
    """
    Elimina entradas duplicadas del JSON.
    
    Args:
        input_file: Ruta al archivo JSON de entrada
        output_file: Ruta al archivo JSON de salida (opcional)
    
    Returns:
        dict con estadísticas del proceso
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {input_file}")
    
    # Leer el JSON
    print(f"Leyendo {input_file}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_entries = len(data)
    print(f"Total de entradas originales: {total_entries}")
    
    # Usar un set para detectar duplicados y un dict para mantener el orden
    seen_notes = set()
    unique_data = []
    duplicates = 0
    
    for entry in data:
        notes_content = entry.get('notes', '').strip()
        
        if notes_content not in seen_notes:
            # Primera vez que vemos este contenido
            seen_notes.add(notes_content)
            unique_data.append(entry)
        else:
            # Es un duplicado
            duplicates += 1
    
    # Generar nombre de archivo de salida si no se especificó
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = input_path.parent / f"Streak-notes-unique-{timestamp}.json"
    else:
        output_file = Path(output_file)
    
    # Guardar el JSON sin duplicados
    print(f"\nGuardando datos únicos en: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(unique_data, f, ensure_ascii=False, indent=2)
    
    # Estadísticas
    stats = {
        'total_original': total_entries,
        'duplicates_removed': duplicates,
        'unique_entries': len(unique_data),
        'output_file': str(output_file)
    }
    
    print("\n" + "="*60)
    print("RESUMEN DE DEDUPLICACIÓN")
    print("="*60)
    print(f"Entradas originales: {stats['total_original']}")
    print(f"Duplicados eliminados: {stats['duplicates_removed']}")
    print(f"Entradas únicas guardadas: {stats['unique_entries']}")
    print(f"Porcentaje eliminado: {(duplicates/total_entries*100):.1f}%")
    print(f"Archivo de salida: {stats['output_file']}")
    print("="*60)
    
    return stats


if __name__ == "__main__":
    import sys
    
    # Archivo de entrada
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Buscar el archivo más reciente de Streak-notes-cleaned
        script_dir = Path(__file__).parent
        cleaned_files = list(script_dir.glob("Streak-notes-cleaned-*.json"))
        
        if not cleaned_files:
            print("Error: No se encontraron archivos Streak-notes-cleaned-*.json")
            print("Uso: python3 remove_duplicates.py [archivo_entrada.json] [archivo_salida.json]")
            sys.exit(1)
        
        # Ordenar por fecha de modificación y tomar el más reciente
        input_file = max(cleaned_files, key=lambda p: p.stat().st_mtime)
        print(f"Usando el archivo más reciente: {input_file}")
    
    # Archivo de salida (opcional)
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        stats = remove_duplicates(input_file, output_file)
        print("\n✅ Deduplicación completada exitosamente")
    except Exception as e:
        print(f"\n❌ Error durante la deduplicación: {e}")
        sys.exit(1)
