#!/usr/bin/env python3
"""
Script para limpiar el footer de Streak del contenido de 'notes'.
Elimina todo el contenido después (e incluyendo) el footer.
"""

import json
from pathlib import Path
from datetime import datetime


def clean_notes_footer(input_file: str, footer_marker: str, output_file: str = None) -> dict:
    """
    Elimina el footer y todo lo que viene después en el campo 'notes'.
    
    Args:
        input_file: Ruta al archivo JSON de entrada
        footer_marker: Marcador de inicio del footer a eliminar
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
    print(f"Buscando y eliminando footer: '{footer_marker[:50]}...'")
    
    # Limpiar cada entrada
    cleaned_data = []
    entries_cleaned = 0
    
    for entry in data:
        notes_content = entry.get('notes', '')
        
        # Buscar el marcador del footer
        if footer_marker in notes_content:
            # Cortar todo desde el footer (incluyéndolo)
            footer_index = notes_content.find(footer_marker)
            cleaned_content = notes_content[:footer_index].strip()
            entries_cleaned += 1
        else:
            # No tiene footer, mantener como está
            cleaned_content = notes_content.strip()
        
        cleaned_entry = {
            'subject': entry.get('subject', ''),
            'notes': cleaned_content
        }
        cleaned_data.append(cleaned_entry)
    
    # Generar nombre de archivo de salida si no se especificó
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = input_path.parent / f"Streak-notes-final-{timestamp}.json"
    else:
        output_file = Path(output_file)
    
    # Guardar el JSON limpio
    print(f"\nGuardando datos limpios en: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
    
    # Estadísticas
    stats = {
        'total_entries': total_entries,
        'entries_cleaned': entries_cleaned,
        'entries_unchanged': total_entries - entries_cleaned,
        'output_file': str(output_file)
    }
    
    print("\n" + "="*60)
    print("RESUMEN DE LIMPIEZA DE FOOTER")
    print("="*60)
    print(f"Total de entradas: {stats['total_entries']}")
    print(f"Entradas con footer eliminado: {stats['entries_cleaned']}")
    print(f"Entradas sin cambios: {stats['entries_unchanged']}")
    print(f"Archivo de salida: {stats['output_file']}")
    print("="*60)
    
    return stats


if __name__ == "__main__":
    import sys
    
    # Marcador del footer a eliminar
    FOOTER_MARKER = " =20 =20 =20 =20 =20 =C2=A9 2011-2025 "
    
    # Archivo de entrada
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Buscar el archivo más reciente de Streak-notes-filtered
        script_dir = Path(__file__).parent
        filtered_files = list(script_dir.glob("Streak-notes-filtered-*.json"))
        
        if not filtered_files:
            print("Error: No se encontraron archivos Streak-notes-filtered-*.json")
            print("Uso: python3 clean_footer.py [archivo_entrada.json] [archivo_salida.json]")
            sys.exit(1)
        
        # Ordenar por fecha de modificación y tomar el más reciente
        input_file = max(filtered_files, key=lambda p: p.stat().st_mtime)
        print(f"Usando el archivo más reciente: {input_file}")
    
    # Archivo de salida (opcional)
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    try:
        stats = clean_notes_footer(input_file, FOOTER_MARKER, output_file)
        print("\n✅ Limpieza completada exitosamente")
    except Exception as e:
        print(f"\n❌ Error durante la limpieza: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
