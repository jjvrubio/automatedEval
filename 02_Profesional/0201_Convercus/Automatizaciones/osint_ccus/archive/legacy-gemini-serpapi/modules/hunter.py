#!/usr/bin/env python3
"""
Módulo 1: EL CAZADOR (Search API)
Encuentra fuentes automáticamente usando SerpAPI.
"""

from serpapi import GoogleSearch
from typing import List, Dict, Optional


class Hunter:
    """Cazador de fuentes OSINT."""
    
    def __init__(self, serp_key: str, region: str = "es", language: str = "es"):
        self.serp_key = serp_key
        self.region = region
        self.language = language
    
    def search_google(
        self, 
        query: str, 
        num_results: int = 5,
        file_type: Optional[str] = None
    ) -> List[str]:
        """
        Busca en Google y retorna lista de URLs limpias.
        
        Args:
            query: Consulta de búsqueda
            num_results: Número de resultados a recuperar
            file_type: Tipo de archivo opcional (pdf, xlsx, docx, etc.)
        
        Returns:
            Lista de URLs encontradas
        """
        print(f"🕵️  Buscando: '{query}'...")
        
        # Modificar query si se especifica tipo de archivo
        search_query = f"{query} filetype:{file_type}" if file_type else query
        
        try:
            params = {
                "q": search_query,
                "api_key": self.serp_key,
                "num": num_results,
                "gl": self.region,
                "hl": self.language
            }
            
            search = GoogleSearch(params)
            results = search.get_dict()
            
            urls = [r["link"] for r in results.get("organic_results", [])]
            print(f"✅ Encontradas {len(urls)} fuentes")
            return urls
            
        except Exception as e:
            print(f"❌ Error en búsqueda: {e}")
            return []
    
    def search_multi_query(self, queries: List[str], max_per_query: int = 3) -> List[str]:
        """
        Ejecuta múltiples búsquedas y consolida resultados.
        
        Args:
            queries: Lista de consultas a ejecutar
            max_per_query: Máximo de resultados por consulta
        
        Returns:
            Lista consolidada de URLs únicas
        """
        all_urls = []
        for query in queries:
            urls = self.search_google(query, num_results=max_per_query)
            all_urls.extend(urls)
        
        # Eliminar duplicados preservando orden
        unique_urls = list(dict.fromkeys(all_urls))
        print(f"📋 Total URLs únicas: {len(unique_urls)}")
        return unique_urls
    
    def build_search_queries(
        self, 
        empresa: str, 
        keywords: List[str],
        year: Optional[str] = None
    ) -> List[str]:
        """
        Construye múltiples queries estratégicas.
        
        Args:
            empresa: Nombre de la empresa target
            keywords: Palabras clave relevantes
            year: Año opcional para filtrar resultados
        
        Returns:
            Lista de queries optimizadas
        """
        queries = []
        
        for keyword in keywords:
            base_query = f"{empresa} {keyword}"
            if year:
                base_query += f" {year}"
            queries.append(base_query)
        
        return queries


if __name__ == "__main__":
    # Test básico
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    serp_key = os.getenv("MI_CLAVE_API_SERPAPI")
    
    if serp_key:
        hunter = Hunter(serp_key)
        urls = hunter.search_google("Inditex facturación 2024", num_results=3)
        for url in urls:
            print(f"  → {url}")
    else:
        print("❌ Configura MI_CLAVE_API_SERPAPI en .env")
