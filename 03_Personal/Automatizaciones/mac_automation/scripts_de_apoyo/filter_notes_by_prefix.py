#!/usr/bin/env python3
"""
Script para eliminar entradas donde 'notes' empiece con una URL específica.
"""

import json
from pathlib import Path
from datetime import datetime


def filter_by_notes_prefix(input_file: str, prefix_to_remove: str, output_file: str = None) -> dict:
    """
    Elimina entradas donde 'notes' empiece con el prefijo especificado.
    
    Args:
        input_file: Ruta al archivo JSON de entrada
        prefix_to_remove: Prefijo a buscar al inicio de 'notes'
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
    print(f"Buscando entradas que empiecen con: '{prefix_to_remove}'...")
    
    # Filtrar entradas
    filtered_data = []
    removed = 0
    
    for entry in data:
        notes_content = entry.get('notes', '').strip()
        
        if notes_content.startswith(prefix_to_remove):
            # Eliminar esta entrada
            removed += 1
        else:
            # Mantener esta entrada
            filtered_data.append(entry)
    
    # Generar nombre de archivo de salida si no se especificó
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_file = input_path.parent / f"Streak-notes-filtered-{timestamp}.json"
    else:
        output_file = Path(output_file)
    
    # Guardar el JSON filtrado
    print(f"\nGuardando datos filtrados en: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=2)
    
    # Estadísticas
    stats = {
        'total_original': total_entries,
        'removed': removed,
        'remaining': len(filtered_data),
        'output_file': str(output_file)
    }
    
    print("\n" + "="*60)
    print("RESUMEN DE FILTRADO")
    print("="*60)
    print(f"Entradas originales: {stats['total_original']}")
    print(f"Entradas eliminadas (empiezan con '{prefix_to_remove[:50]}...'): {stats['removed']}")
    print(f"Entradas restantes: {stats['remaining']}")
    print(f"Porcentaje eliminado: {(removed/total_entries*100):.1f}%")
    print(f"Archivo de salida: {stats['output_file']}")
    print("="*60)
    
    return stats


if __name__ == "__main__":
    import sys
    
    # Prefijo a filtrar (puede pasarse como argumento o usar el default)
    if len(sys.argv) > 2 and sys.argv[2] != "":
        PREFIX_TO_REMOVE = sys.argv[2]
    else:
        # Default: footer de Streak
        PREFIX_TO_REMOVE = "=20 =20 =20 =20 =20 =C2=A9 2011-2025 Streak 2261"
    
    # Archivo de entrada
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        # Buscar el archivo más reciente de Streak-notes-clean
        script_dir = Path(__file__).parent
        clean_files = list(script_dir.glob("Streak-notes-clean-*.json"))
        
        if not clean_files:
            # Intentar con otros patrones
            clean_files = list(script_dir.glob("Streak-notes-unique-*.json"))
            if not clean_files:
                clean_files = list(script_dir.glob("Streak-notes-filtered-*.json"))
        
        if not clean_files:
            print("Error: No se encontraron archivos Streak-notes-*.json")
            print("Uso: python3 filter_notes_by_prefix.py [archivo_entrada.json] [prefijo_a_eliminar] [archivo_salida.json]")
            sys.exit(1)
        
        # Ordenar por fecha de modificación y tomar el más reciente
        input_file = max(clean_files, key=lambda p: p.stat().st_mtime)
        print(f"Usando el archivo más reciente: {input_file}")
    
    # Archivo de salida (opcional)
    output_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    try:
        stats = filter_by_notes_prefix(input_file, PREFIX_TO_REMOVE, output_file)
        print("\n✅ Filtrado completado exitosamente")
    except Exception as e:
        print(f"\n❌ Error durante el filtrado: {e}")
        sys.exit(1)
