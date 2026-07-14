#!/usr/bin/env python3
"""
Script para limpiar el JSON de Streak emails.
- Mantiene solo las entradas que contienen 'Notes:' en el content
- Extrae únicamente el contenido después de 'Notes:'
"""

import json
from pathlib import Path
from datetime import datetime


def clean_streak_notes(input_file: str, output_file: str = None) -> dict:
    """
    Limpia el JSON de Streak manteniendo solo el contenido después de 'Notes:'.
    
    Args:
        input_file: Ruta al archivo JSON de entrada
        output_file: Ruta al archivo JSON de salida (opcional)
    
    Returns:
        dict con estadísticas del proceso
    """
    input_path = Path(input_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"No se encuentra el archivo: {input_file}")
    
    # Leer el JSON original
    print(f"Leyendo {input_file}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    total_entries = len(data)
    print(f"Total de entradas en el archivo: {total_entries}")
    
    # Procesar cada entrada
    cleaned_data = []
    entries_with_notes = 0
    entries_without_notes = 0
    
    for entry in data:
        content = entry.get('content', '')
        
        # Verificar si contiene 'Notes:'
        if 'Notes:' in content:
            entries_with_notes += 1
            # Extraer solo el contenido después de 'Notes:'
            notes_index = content.find('Notes:')
            notes_content = content[notes_index + len('Notes:'):].strip()
            
            # Crear nueva entrada con solo el contenido de Notes
            cleaned_entry = {
                'subject': entry.get('subject', ''),
                'notes': notes_content
            }
            cleaned_data.append(cleaned_entry)
        else:
            entries_without_notes += 1
            # Línea sin 'Notes:' - se elimina (no se añade a cleaned_data)
    
    # Generar nombre de archivo de salida si no se especificó
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = input_path.parent / f"Streak-notes-cleaned-{timestamp}.json"
    else:
        output_file = Path(output_file)
    
    # Guardar el JSON limpio
    print(f"\nGuardando datos limpios en: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    
    # Estadísticas
    stats = {
        'total_original': total_entries,
        'with_notes': entries_with_notes,
        'without_notes': entries_without_notes,
        'final_entries': len(cleaned_data),
        'output_file': str(output_file)
    }
    
    print("\n" + "="*60)
    print("RESUMEN DE LIMPIEZA")
    print("="*60)
    print(f"Entradas originales: {stats['total_original']}")
    print(f"Entradas CON 'Notes:': {stats['with_notes']}")
    print(f"Entradas SIN 'Notes:' (eliminadas): {stats['without_notes']}")
    print(f"Entradas finales guardadas: {stats['final_entries']}")
    print(f"Archivo de salida: {stats['output_file']}")
    print("="*60)
    
    return stats


if __name__ == "__main__":
    import sys
    
    # Archivo de entrada (buscar el más reciente si no se especifica)
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Buscar el archivo más reciente de Streak-mails
        script_dir = Path(__file__).parent
        streak_files = list(script_dir.glob("Streak-mails-*.json"))
        
        if not streak_files:
            print("Error: No se encontraron archivos Streak-mails-*.json")
            print("Uso: python3 clean_streak_notes.py [archivo_entrada.json] [archivo_salida.json]")
            sys.exit(1)
        
        # Ordenar por fecha de modificación y tomar el más reciente
        input_file = max(streak_files, key=lambda p: p.stat().st_mtime)
        print(f"Usando el archivo más reciente: {input_file}")
    
    # Archivo de salida (opcional)
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        stats = clean_streak_notes(input_file, output_file)
        print("\n✅ Limpieza completada exitosamente")
    except Exception as e:
        print(f"\n❌ Error durante la limpieza: {e}")
        sys.exit(1)
