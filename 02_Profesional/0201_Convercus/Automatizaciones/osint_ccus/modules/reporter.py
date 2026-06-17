#!/usr/bin/env python3
"""
Módulo 4: EL REPORTERO (Output Generator)
Genera reportes en múltiples formatos.
"""

from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
import json


class Reporter:
    """Generador de reportes estructurados."""
    
    def __init__(self, output_dir: Path):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def generate_markdown(
        self,
        content: str,
        metadata: Dict[str, str],
        filename: Optional[str] = None
    ) -> Path:
        """
        Genera reporte en formato Markdown.
        
        Args:
            content: Contenido principal del reporte
            metadata: Dict con metadatos (empresa, fecha, etc.)
            filename: Nombre personalizado (opcional)
        
        Returns:
            Path al archivo generado
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            empresa = metadata.get("empresa", "unknown").replace(" ", "_")
            filename = f"reporte_{empresa}_{timestamp}.md"
        
        # Construir documento Markdown
        doc = self._build_markdown_header(metadata)
        doc += "\n\n---\n\n"
        doc += content
        
        # Guardar
        output_path = self.output_dir / filename
        output_path.write_text(doc, encoding='utf-8')
        
        print(f"📝 Reporte guardado: {output_path}")
        return output_path
    
    def _build_markdown_header(self, metadata: Dict[str, str]) -> str:
        """Construye encabezado YAML front matter."""
        header = "---\n"
        for key, value in metadata.items():
            header += f"{key}: {value}\n"
        header += f"generado: {datetime.now().isoformat()}\n"
        header += "---\n"
        return header
    
    def generate_json(
        self,
        data: Dict,
        filename: Optional[str] = None
    ) -> Path:
        """
        Genera reporte en formato JSON.
        
        Args:
            data: Diccionario con datos estructurados
            filename: Nombre personalizado (opcional)
        
        Returns:
            Path al archivo generado
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"reporte_{timestamp}.json"
        
        output_path = self.output_dir / filename
        
        with output_path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Datos guardados: {output_path}")
        return output_path
    
    def generate_multi_phase_report(
        self,
        phases: List[Dict[str, str]],
        metadata: Dict[str, str],
        filename: Optional[str] = None
    ) -> Path:
        """
        Genera reporte consolidado de análisis multi-fase.
        
        Args:
            phases: Lista de dicts con {title, content} por fase
            metadata: Metadatos del análisis
            filename: Nombre personalizado (opcional)
        
        Returns:
            Path al reporte consolidado
        """
        # Construir documento
        doc = self._build_markdown_header(metadata)
        doc += f"\n# Reporte de Análisis: {metadata.get('empresa', 'N/A')}\n\n"
        
        # Agregar índice
        doc += "## Índice\n\n"
        for i, phase in enumerate(phases, 1):
            doc += f"{i}. [{phase['title']}](#{self._slugify(phase['title'])})\n"
        doc += "\n---\n\n"
        
        # Agregar cada fase
        for i, phase in enumerate(phases, 1):
            doc += f"## {i}. {phase['title']}\n\n"
            doc += phase['content']
            doc += "\n\n---\n\n"
        
        # Guardar
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            empresa = metadata.get("empresa", "unknown").replace(" ", "_")
            filename = f"analisis_multifase_{empresa}_{timestamp}.md"
        
        output_path = self.output_dir / filename
        output_path.write_text(doc, encoding='utf-8')
        
        print(f"📑 Reporte multi-fase guardado: {output_path}")
        return output_path
    
    def _slugify(self, text: str) -> str:
        """Convierte título a slug para enlaces internos."""
        return text.lower().replace(" ", "-").replace(",", "").replace(":", "")
    
    def print_summary(self, content: str, max_lines: int = 10):
        """Imprime resumen del contenido en consola."""
        lines = content.split('\n')
        preview = '\n'.join(lines[:max_lines])
        
        print("\n" + "="*70)
        print(preview)
        if len(lines) > max_lines:
            print(f"\n... ({len(lines) - max_lines} líneas adicionales)")
        print("="*70)


if __name__ == "__main__":
    # Test básico
    reporter = Reporter(output_dir=Path("./test_reports"))
    
    test_metadata = {
        "empresa": "Test Corp",
        "escenario": "Due Diligence",
        "analista": "Sistema Automático"
    }
    
    test_content = """
# Análisis Financiero

## KPIs Principales
- Facturación: €50M
- EBITDA: 15%

## Recomendaciones
1. Optimizar cadena de suministro
2. Expandir mercado digital
"""
    
    reporter.generate_markdown(test_content, test_metadata)
    reporter.print_summary(test_content)
