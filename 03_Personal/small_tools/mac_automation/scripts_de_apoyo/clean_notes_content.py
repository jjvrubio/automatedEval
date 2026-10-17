#!/usr/bin/env python3
"""
Script para limpiar el contenido de 'notes' eliminando todo hasta encontrar 'Notes'.
"""

import json
from pathlib import Path
from datetime import datetime


def clean_notes_prefix(input_file: str, output_file: str = None) -> dict:
    """
    Elimina todo el contenido antes de 'Notes' en el campo 'notes'.
    
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
    print(f"Total de entradas: {total_entries}")
    
    # Procesar cada entrada
    cleaned_data = []
    entries_modified = 0
    
    for entry in data:
        notes_content = entry.get('notes', '')
        
        # Buscar la cadena 'Notes'
        if 'Notes' in notes_content:
            # Encontrar la posición de 'Notes'
            notes_index = notes_content.find('Notes')
            
            # Verificar si hay ':' después de 'Notes'
            if notes_index + 5 < len(notes_content) and notes_content[notes_index + 5] == ':':
                # Eliminar hasta después de 'Notes:'
                cleaned_content = notes_content[notes_index + 6:].strip()
            else:
                # Eliminar hasta después de 'Notes'
                cleaned_content = notes_content[notes_index + 5:].strip()
            
            # Si el contenido cambió, contar como modificado
            if cleaned_content != notes_content:
                entries_modified += 1
            
            cleaned_entry = {
                'subject': entry.get('subject', ''),
                'notes': cleaned_content
            }
        else:
            # No tiene 'Notes', mantener como está
            cleaned_entry = {
                'subject': entry.get('subject', ''),
                'notes': notes_content.strip()
            }
        
        cleaned_data.append(cleaned_entry)
    
    # Generar nombre de archivo de salida si no se especificó
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = input_path.parent / f"Streak-notes-clean-{timestamp}.json"
    else:
        output_file = Path(output_file)
    
    # Guardar el JSON limpio
    print(f"\nGuardando datos limpios en: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    
    # Estadísticas
    stats = {
        'total_entries': total_entries,
        'entries_modified': entries_modified,
        'output_file': str(output_file)
    }
    
    print("\n" + "="*60)
    print("RESUMEN DE LIMPIEZA")
    print("="*60)
    print(f"Total de entradas: {stats['total_entries']}")
    print(f"Entradas modificadas: {stats['entries_modified']}")
    print(f"Entradas sin cambios: {total_entries - entries_modified}")
    print(f"Archivo de salida: {stats['output_file']}")
    print("="*60)
    
    return stats


if __name__ == "__main__":
    import sys
    
    # Archivo de entrada
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Buscar el archivo más reciente de Streak-notes-filtered
        script_dir = Path(__file__).parent
        filtered_files = list(script_dir.glob("Streak-notes-filtered-*.json"))
        
        if not filtered_files:
            print("Error: No se encontraron archivos Streak-notes-filtered-*.json")
            print("Uso: python3 clean_notes_content.py [archivo_entrada.json] [archivo_salida.json]")
            sys.exit(1)
        
        # Ordenar por fecha de modificación y tomar el más reciente
        input_file = max(filtered_files, key=lambda p: p.stat().st_mtime)
        print(f"Usando el archivo más reciente: {input_file}")
    
    # Archivo de salida (opcional)
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        stats = clean_notes_prefix(input_file, output_file)
        print("\n✅ Limpieza completada exitosamente")
    except Exception as e:
        print(f"\n❌ Error durante la limpieza: {e}")
        sys.exit(1)
