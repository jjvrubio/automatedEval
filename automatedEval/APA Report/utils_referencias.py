#!/usr/bin/env python3
"""
Utilidades auxiliares para el Sistema de Validación de Referencias
================================================================

Funciones de apoyo para detección de patrones, limpieza de texto,
y operaciones especializadas del validador de referencias.
"""

import re
from typing import List, Dict, Tuple, Optional
from collections import Counter
import unicodedata


class DetectorPatrones:
    """Utilidades para detectar patrones en texto académico"""
    
    @staticmethod
    def detectar_idioma_documento(texto: str) -> str:
        """
        Detecta el idioma principal del documento basado en palabras clave.
        
        Args:
            texto: Texto completo del documento
            
        Returns:
            'español', 'english', o 'unknown'
        """
        texto_lower = texto.lower()
        
        # Indicadores en español
        indicadores_es = [
            "referencias bibliográficas", "bibliografía", "universidad",
            "revista", "editorial", "páginas", "volumen", "número",
            "accedido", "recuperado", "disponible en"
        ]
        
        # Indicadores en inglés  
        indicadores_en = [
            "references", "bibliography", "university", "journal",
            "press", "publisher", "pages", "volume", "issue",
            "accessed", "retrieved", "available at"
        ]
        
        contador_es = sum(1 for indicador in indicadores_es if indicador in texto_lower)
        contador_en = sum(1 for indicador in indicadores_en if indicador in texto_lower)
        
        if contador_es > contador_en:
            return "español"
        elif contador_en > contador_es:
            return "english"
        else:
            return "unknown"
    
    @staticmethod
    def extraer_seccion_referencias(texto: str, idioma: str = "auto") -> Tuple[str, int]:
        """
        Extrae la sección de referencias del texto completo.
        
        Args:
            texto: Texto completo del documento
            idioma: 'español', 'english', o 'auto'
            
        Returns:
            Tupla con (texto_referencias, posicion_inicio)
        """
        if idioma == "auto":
            idioma = DetectorPatrones.detectar_idioma_documento(texto)
        
        # Palabras clave según idioma
        if idioma == "español":
            palabras_clave = [
                r"referencias\s+bibliográficas",
                r"bibliografía",
                r"referencias",
                r"fuentes\s+consultadas",
                r"obras\s+citadas"
            ]
        else:  # english o unknown
            palabras_clave = [
                r"references",
                r"bibliography", 
                r"works\s+cited",
                r"literature\s+cited",
                r"sources"
            ]
        
        # Buscar inicio de sección
        texto_lower = texto.lower()
        posicion_inicio = -1
        
        for patron in palabras_clave:
            match = re.search(patron, texto_lower)
            if match:
                posicion_inicio = match.start()
                break
        
        if posicion_inicio == -1:
            return "", -1
        
        # Extraer desde la posición encontrada hasta el final
        seccion_referencias = texto[posicion_inicio:]
        
        # Intentar delimitar el final (opcional)
        patrones_fin = [
            r"\n\s*anexos?\s*\n",
            r"\n\s*apéndices?\s*\n", 
            r"\n\s*appendix\s*\n",
            r"\n\s*notas?\s*\n"
        ]
        
        for patron_fin in patrones_fin:
            match_fin = re.search(patron_fin, seccion_referencias.lower())
            if match_fin:
                seccion_referencias = seccion_referencias[:match_fin.start()]
                break
        
        return seccion_referencias, posicion_inicio
    
    @staticmethod
    def identificar_tipo_referencia(referencia: str) -> str:
        """
        Identifica el tipo de referencia basado en patrones del texto.
        
        Args:
            referencia: Texto de la referencia individual
            
        Returns:
            Tipo identificado: 'articulo', 'libro', 'capitulo', 'tesis', 'web', 'unknown'
        """
        ref_lower = referencia.lower()
        
        # Patrones para artículos de revista
        if any(patron in ref_lower for patron in ["vol.", "volume", "núm.", "number", "pp.", "pages"]):
            if any(patron in ref_lower for patron in ["journal", "revista", "review"]):
                return "articulo"
        
        # Patrones para libros
        if any(patron in ref_lower for patron in ["editorial", "press", "publisher", "ediciones"]):
            if not any(patron in ref_lower for patron in ["journal", "revista", "vol."]):
                return "libro"
        
        # Patrones para capítulos de libro
        if any(patron in ref_lower for patron in ["en:", "in:", "editor", "eds.", "compilador"]):
            return "capitulo"
        
        # Patrones para tesis
        if any(patron in ref_lower for patron in ["tesis", "thesis", "dissertat", "maestría", "doctorado"]):
            return "tesis"
        
        # Patrones para recursos web
        if any(patron in ref_lower for patron in ["http", "www.", "recuperado", "accessed", "available"]):
            return "web"
        
        return "unknown"


class LimpiadorTexto:
    """Utilidades para limpieza y normalización de texto"""
    
    @staticmethod
    def limpiar_referencia(referencia: str) -> str:
        """
        Limpia una referencia individual eliminando elementos no deseados.
        
        Args:
            referencia: Texto de la referencia sin procesar
            
        Returns:
            Referencia limpia
        """
        # Remover caracteres de control y espacios extra
        texto_limpio = re.sub(r'\s+', ' ', referencia.strip())
        
        # Remover marcadores de párrafo y numeración
        texto_limpio = re.sub(r'^\d+[\.\)]\s*', '', texto_limpio)
        
        # Remover marcas de agua o metadatos
        texto_limpio = re.sub(r'\(PDF\)', '', texto_limpio, flags=re.IGNORECASE)
        texto_limpio = re.sub(r'\[En línea\]', '', texto_limpio, flags=re.IGNORECASE)
        
        # Normalizar caracteres Unicode
        texto_limpio = unicodedata.normalize('NFKC', texto_limpio)
        
        return texto_limpio.strip()
    
    @staticmethod
    def normalizar_espacios(texto: str) -> str:
        """Normaliza espacios en blanco múltiples"""
        return re.sub(r'\s+', ' ', texto.strip())
    
    @staticmethod
    def remover_patrones_repetitivos(texto: str, patrones: List[str]) -> str:
        """
        Remueve patrones repetitivos (encabezados, pies de página).
        
        Args:
            texto: Texto completo
            patrones: Lista de patrones a remover
            
        Returns:
            Texto sin patrones repetitivos
        """
        texto_limpio = texto
        
        for patron in patrones:
            # Escapar caracteres especiales de regex
            patron_escapado = re.escape(patron)
            texto_limpio = re.sub(patron_escapado, '', texto_limpio, flags=re.IGNORECASE)
        
        return LimpiadorTexto.normalizar_espacios(texto_limpio)


class AnalizadorComponentes:
    """Analizador de componentes específicos de referencias"""
    
    @staticmethod
    def extraer_autores(referencia: str, estilo: str = "apa") -> List[str]:
        """
        Extrae información de autores de una referencia.
        
        Args:
            referencia: Texto de la referencia
            estilo: Estilo de cita (apa, ieee, mla)
            
        Returns:
            Lista de autores extraídos
        """
        autores = []
        
        if estilo == "apa":
            # Patrón APA: Apellido, I. M.
            patron = r'([A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+),\s*([A-Z]\.(?:\s*[A-Z]\.)?)'
            matches = re.findall(patron, referencia)
            autores = [f"{apellido}, {iniciales}" for apellido, iniciales in matches]
            
        elif estilo == "ieee":
            # Patrón IEEE: I. M. Apellido
            patron = r'([A-Z]\.(?:\s*[A-Z]\.)?)\s*([A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+)'
            matches = re.findall(patron, referencia)
            autores = [f"{iniciales} {apellido}" for iniciales, apellido in matches]
            
        elif estilo == "mla":
            # Patrón MLA: Apellido, Nombre
            patron = r'([A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+),\s*([A-ZÁÉÍÓÚÜ][a-záéíóúüñ\s]+)'
            matches = re.findall(patron, referencia)
            autores = [f"{apellido}, {nombre.strip()}" for apellido, nombre in matches]
        
        return autores
    
    @staticmethod
    def extraer_anio(referencia: str, estilo: str = "apa") -> Optional[str]:
        """
        Extrae el año de publicación de una referencia.
        
        Args:
            referencia: Texto de la referencia
            estilo: Estilo de cita
            
        Returns:
            Año extraído o None si no se encuentra
        """
        patrones_anio = []
        
        if estilo == "apa":
            patrones_anio = [r'\((\d{4}[a-z]?)\)', r'(\d{4}[a-z]?)\.']
        elif estilo == "ieee":
            patrones_anio = [r'([A-Z][a-z]+\.?\s*\d{4})', r'(\d{4})']
        elif estilo == "mla":
            patrones_anio = [r'(\d{1,2}\s*[A-Z][a-z]+\.?\s*\d{4})', r'(\d{4})']
        
        for patron in patrones_anio:
            match = re.search(patron, referencia)
            if match:
                return match.group(1)
        
        return None
    
    @staticmethod
    def extraer_titulo(referencia: str, tipo_publicacion: str = "articulo") -> Optional[str]:
        """
        Extrae el título de una referencia según el tipo de publicación.
        
        Args:
            referencia: Texto de la referencia
            tipo_publicacion: 'articulo', 'libro', 'capitulo', etc.
            
        Returns:
            Título extraído o None
        """
        if tipo_publicacion == "articulo":
            # Títulos de artículos suelen estar entre comillas o ser la primera oración
            patrones = [
                r'"([^"]+)"',  # Entre comillas
                r'([A-ZÁÉÍÓÚÜ][^.]+)\.',  # Primera oración capitalizada
            ]
        elif tipo_publicacion == "libro":
            # Títulos de libros suelen estar en cursiva o capitalizado
            patrones = [
                r'([A-ZÁÉÍÓÚÜ][^.]+)\.',
                r'_([^_]+)_',  # Entre guiones bajos (cursiva en markdown)
            ]
        else:
            patrones = [r'([A-ZÁÉÍÓÚÜ][^.]+)\.']
        
        for patron in patrones:
            match = re.search(patron, referencia)
            if match:
                titulo = match.group(1).strip()
                # Filtrar títulos muy cortos o que sean solo autor
                if len(titulo) > 10 and not re.match(r'^[A-Z]\.\s*[A-Z]', titulo):
                    return titulo
        
        return None
    
    @staticmethod
    def extraer_doi(referencia: str) -> Optional[str]:
        """Extrae DOI de una referencia"""
        patrones_doi = [
            r'https?://doi\.org/(10\.\d+/[^\s]+)',
            r'doi:\s*(10\.\d+/[^\s]+)',
            r'DOI:\s*(10\.\d+/[^\s]+)'
        ]
        
        for patron in patrones_doi:
            match = re.search(patron, referencia)
            if match:
                return match.group(1)
        
        return None
    
    @staticmethod
    def extraer_url(referencia: str) -> List[str]:
        """Extrae URLs de una referencia"""
        patron_url = r'(https?://[^\s]+)'
        urls = re.findall(patron_url, referencia)
        
        # Limpiar URLs (remover puntuación final)
        urls_limpias = []
        for url in urls:
            url_limpia = re.sub(r'[.,;)\]]+$', '', url)
            urls_limpias.append(url_limpia)
        
        return urls_limpias


class ValidadorFormato:
    """Validador específico de formatos según estándares"""
    
    @staticmethod
    def validar_formato_apa(referencia: str) -> Dict[str, bool]:
        """
        Valida el formato específico de APA 7.
        
        Returns:
            Diccionario con validaciones específicas
        """
        validaciones = {
            "autor_formato_correcto": bool(re.search(r'[A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+,\s*[A-Z]\.', referencia)),
            "anio_entre_parentesis": bool(re.search(r'\(\d{4}[a-z]?\)', referencia)),
            "titulo_capitalizado_correcto": ValidadorFormato._validar_capitalizacion_apa(referencia),
            "doi_formato_correcto": ValidadorFormato._validar_doi_apa(referencia),
            "puntuacion_correcta": ValidadorFormato._validar_puntuacion_apa(referencia)
        }
        
        return validaciones
    
    @staticmethod
    def validar_formato_ieee(referencia: str) -> Dict[str, bool]:
        """
        Valida el formato específico de IEEE.
        
        Returns:
            Diccionario con validaciones específicas
        """
        validaciones = {
            "autor_iniciales_primero": bool(re.search(r'[A-Z]\.\s*[A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+', referencia)),
            "titulo_entre_comillas": bool(re.search(r'"[^"]+",', referencia)),
            "abreviacion_revista": ValidadorFormato._validar_abreviacion_ieee(referencia),
            "formato_volumen": bool(re.search(r'vol\.\s*\d+', referencia, re.IGNORECASE)),
            "formato_numero": bool(re.search(r'no\.\s*\d+', referencia, re.IGNORECASE))
        }
        
        return validaciones
    
    @staticmethod
    def _validar_capitalizacion_apa(referencia: str) -> bool:
        """Valida que la capitalización siga las reglas de APA"""
        # Buscar títulos potenciales
        titulos = re.findall(r'[A-ZÁÉÍÓÚÜ][^.]+\.', referencia)
        
        for titulo in titulos:
            # Verificar que solo la primera palabra y nombres propios estén capitalizados
            palabras = titulo.split()
            if len(palabras) > 1:
                # La primera palabra debe estar capitalizada
                if not palabras[0][0].isupper():
                    return False
                
                # Las palabras del medio no deben estar todas capitalizadas
                # (excepto nombres propios, que son difíciles de detectar automáticamente)
                for palabra in palabras[1:-1]:
                    if palabra.isupper() and len(palabra) > 1:
                        return False
        
        return True
    
    @staticmethod
    def _validar_doi_apa(referencia: str) -> bool:
        """Valida que el DOI esté en formato correcto para APA"""
        doi_match = re.search(r'https://doi\.org/10\.\d+/[^\s]+', referencia)
        return doi_match is not None or 'doi' not in referencia.lower()
    
    @staticmethod
    def _validar_puntuacion_apa(referencia: str) -> bool:
        """Valida puntuación básica para APA"""
        # Verificaciones básicas de puntuación
        tiene_punto_final = referencia.strip().endswith('.')
        parentesis_balanceados = referencia.count('(') == referencia.count(')')
        
        return tiene_punto_final and parentesis_balanceados
    
    @staticmethod
    def _validar_abreviacion_ieee(referencia: str) -> bool:
        """Valida que use abreviaciones estándar de IEEE"""
        # Lista de abreviaciones comunes de IEEE
        abreviaciones_ieee = [
            r'IEEE\s+Trans\.',
            r'Proc\.',
            r'J\.',
            r'Lett\.',
            r'Rev\.'
        ]
        
        for patron in abreviaciones_ieee:
            if re.search(patron, referencia):
                return True
        
        # Si no hay abreviaciones, no es necesariamente incorrecto
        return True


# Funciones de utilidad global
def contar_elementos_referencia(referencia: str) -> Dict[str, int]:
    """
    Cuenta elementos básicos de una referencia para análisis estadístico.
    
    Returns:
        Diccionario con conteos de elementos
    """
    return {
        "palabras": len(referencia.split()),
        "caracteres": len(referencia),
        "puntos": referencia.count('.'),
        "comas": referencia.count(','),
        "parentesis": referencia.count('('),
        "urls": len(re.findall(r'https?://[^\s]+', referencia)),
        "numeros": len(re.findall(r'\d+', referencia))
    }


def generar_estadisticas_referencias(referencias: List[str]) -> Dict:
    """
    Genera estadísticas generales sobre un conjunto de referencias.
    
    Args:
        referencias: Lista de referencias a analizar
        
    Returns:
        Diccionario con estadísticas
    """
    if not referencias:
        return {}
    
    estadisticas = {
        "total_referencias": len(referencias),
        "longitud_promedio": sum(len(ref) for ref in referencias) / len(referencias),
        "longitud_minima": min(len(ref) for ref in referencias),
        "longitud_maxima": max(len(ref) for ref in referencias),
        "referencias_con_url": sum(1 for ref in referencias if 'http' in ref),
        "referencias_con_doi": sum(1 for ref in referencias if 'doi' in ref.lower()),
        "tipos_detectados": {}
    }
    
    # Análizar tipos de referencia
    for referencia in referencias:
        tipo = DetectorPatrones.identificar_tipo_referencia(referencia)
        estadisticas["tipos_detectados"][tipo] = estadisticas["tipos_detectados"].get(tipo, 0) + 1
    
    return estadisticas