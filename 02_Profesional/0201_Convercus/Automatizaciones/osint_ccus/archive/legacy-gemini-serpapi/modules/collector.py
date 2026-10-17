#!/usr/bin/env python3
"""
Módulo 2: EL RECOLECTOR (Scraper + PDF Extractor)
Descarga y extrae contenido de URLs (HTML y PDF).
"""

import requests
import time
from bs4 import BeautifulSoup
from typing import Dict, Optional
from pathlib import Path
import tempfile

try:
    import pdfplumber
    PDF_SUPPORT = True
except ImportError:
    PDF_SUPPORT = False
    print("⚠️  pdfplumber no disponible. Instala: pip install pdfplumber")


class Collector:
    """Recolector de contenido web y documentos."""
    
    def __init__(self, max_text_length: int = 50000):
        self.max_text_length = max_text_length
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
    
    def scrape_url(self, url: str) -> Dict[str, str]:
        """
        Descarga y extrae texto limpio de una URL.
        
        Args:
            url: URL a procesar
        
        Returns:
            Dict con 'url', 'content', 'status'
        """
        print(f"📥 Procesando: {url}...")
        
        result = {
            "url": url,
            "content": "",
            "status": "error",
            "type": "unknown"
        }
        
        try:
            # Detectar tipo de contenido
            if url.lower().endswith('.pdf'):
                return self._extract_pdf(url)
            else:
                return self._extract_html(url)
                
        except Exception as e:
            result["status"] = f"error: {str(e)}"
            return result
    
    def _extract_html(self, url: str) -> Dict[str, str]:
        """Extrae texto de páginas HTML."""
        result = {"url": url, "content": "", "status": "error", "type": "html"}
        
        try:
            resp = requests.get(url, headers=self.headers, timeout=15)
            
            if resp.status_code != 200:
                result["status"] = f"http_error_{resp.status_code}"
                return result
            
            soup = BeautifulSoup(resp.content, 'html.parser')
            
            # Eliminar elementos no deseados
            for element in soup(["script", "style", "nav", "footer", "header", "form", "iframe"]):
                element.extract()
            
            # Extraer texto limpio
            text = soup.get_text(separator=' ')
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            clean_text = '\n'.join(chunk for chunk in chunks if chunk)
            
            result["content"] = clean_text[:self.max_text_length]
            result["status"] = "success"
            
        except requests.Timeout:
            result["status"] = "timeout"
        except Exception as e:
            result["status"] = f"error: {str(e)}"
        
        return result
    
    def _extract_pdf(self, url: str) -> Dict[str, str]:
        """Descarga y extrae texto de PDFs."""
        result = {"url": url, "content": "", "status": "error", "type": "pdf"}
        
        if not PDF_SUPPORT:
            result["status"] = "pdf_support_missing"
            return result
        
        try:
            # Descargar PDF a archivo temporal
            resp = requests.get(url, headers=self.headers, timeout=20)
            
            if resp.status_code != 200:
                result["status"] = f"http_error_{resp.status_code}"
                return result
            
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
                tmp_file.write(resp.content)
                tmp_path = tmp_file.name
            
            # Extraer texto con pdfplumber
            text_content = []
            with pdfplumber.open(tmp_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text_content.append(page_text)
            
            # Limpiar archivo temporal
            Path(tmp_path).unlink()
            
            full_text = '\n'.join(text_content)
            result["content"] = full_text[:self.max_text_length]
            result["status"] = "success"
            
        except Exception as e:
            result["status"] = f"error: {str(e)}"
        
        return result
    
    def collect_batch(
        self, 
        urls: list[str], 
        delay: float = 0.5
    ) -> list[Dict[str, str]]:
        """
        Recolecta contenido de múltiples URLs con rate limiting.
        
        Args:
            urls: Lista de URLs a procesar
            delay: Segundos de espera entre requests
        
        Returns:
            Lista de resultados por URL
        """
        results = []
        
        for i, url in enumerate(urls, 1):
            print(f"[{i}/{len(urls)}]", end=" ")
            result = self.scrape_url(url)
            results.append(result)
            
            if i < len(urls):
                time.sleep(delay)
        
        # Estadísticas
        successful = sum(1 for r in results if r["status"] == "success")
        print(f"\n✅ Extracción completa: {successful}/{len(urls)} exitosas")
        
        return results


if __name__ == "__main__":
    # Test básico
    collector = Collector()
    
    test_urls = [
        "https://www.example.com",
        "https://www.python.org"
    ]
    
    results = collector.collect_batch(test_urls)
    
    for r in results:
        print(f"\n{r['url']}")
        print(f"  Status: {r['status']}")
        print(f"  Caracteres: {len(r['content'])}")
