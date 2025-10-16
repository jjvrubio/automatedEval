#!/usr/bin/env python3
"""
Sistema Modular de Validación de Referencias Bibliográficas
===========================================================

Este módulo independiente permite validar referencias bibliográficas en múltiples
formatos de documentos (PDF, DOCX) y estilos de cita (APA 7, IEEE, MLA).

Uso:
    python referencias_validator.py --archivo documento.pdf --estilo apa
    python referencias_validator.py --archivo documento.docx --estilo ieee --salida informe.json

Características:
- ✅ Extracción automática de referencias desde PDF y DOCX
- ✅ Validación contra múltiples estándares (APA 7, IEEE, MLA)
- ✅ Detección de patrones de encabezados/pies de página
- ✅ Informes detallados en JSON y Markdown
- ✅ Independiente del sistema de evaluación TFM
- ✅ Reutilizable para ensayos, artículos, tesis, etc.

Autor: Sistema de Automatización Académica
Versión: 1.0
Fecha: Octubre 2025
"""

import argparse
import json
import re
import os
import sys
import subprocess
import logging
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum

# Importaciones específicas para manejo de archivos
try:
    import pdfplumber
    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("⚠️  pdfplumber no disponible. Instalar con: pip install pdfplumber")

try:
    import zipfile
    from lxml import etree
    DOCX_AVAILABLE = True
except ImportError:
    DOCX_AVAILABLE = False
    print("⚠️  lxml no disponible. Instalar con: pip install lxml")


# ----------------------------
# Configuraciones específicas para macOS
# ----------------------------
ONEDRIVE_HINTS = ["OneDrive", ".cloud", "DropBox", "Dropbox"]
FORZAR_NFC = True  # Normalización NFC para compatibilidad de archivos

# ----------------------------
# Funciones de utilidad para selección de archivos (copiadas del evaluador TFM)
# ----------------------------

def normalize_path(path: str, nfc: bool = True) -> str:
    """Normaliza rutas para macOS y OneDrive"""
    import unicodedata
    path = os.path.expanduser(path)
    path = os.path.abspath(path)
    if nfc:
        path = unicodedata.normalize("NFC", path)
    return path


def is_onedrive_path(p: str | Path) -> bool:
    """Detecta si es una ruta de OneDrive"""
    s = str(p)
    return any(h in s for h in ONEDRIVE_HINTS)


def _run(cmd: List[str]) -> Tuple[int, str, str]:
    """Ejecuta comando del sistema"""
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def ensure_hydrated(path: str, logger: logging.Logger) -> None:
    """Asegura que archivos de OneDrive estén descargados localmente"""
    try:
        with open(path, "rb") as f:
            _ = f.read(1)
        return
    except Exception:
        if is_onedrive_path(path):
            fpctl = "/usr/bin/fileproviderctl"
            if Path(fpctl).exists():
                rc, out, err = _run([fpctl, "materialize", "-p", path])
                if rc != 0:
                    logger.warning(f"fileproviderctl falló (rc={rc}). {err}")
            else:
                logger.info("'fileproviderctl' no disponible. Intento de lectura directa.")
        # intento final
        try:
            with open(path, "rb") as f:
                _ = f.read(1)
        except Exception as e2:
            logger.warning(f"No se pudo hidratar el archivo: {e2}")


def seleccionar_archivo_referencias(logger: logging.Logger) -> Optional[str]:
    """
    Selector de archivos usando NSOpenPanel de macOS.
    Adaptado específicamente para selección de documentos para validación de referencias.
    """
    try:
        from AppKit import NSApplication, NSOpenPanel  # type: ignore
        NSApp = NSApplication.sharedApplication()
        NSApp.activateIgnoringOtherApps_(True)
        panel = NSOpenPanel.openPanel()
        panel.setCanChooseFiles_(True)
        panel.setCanChooseDirectories_(False)
        panel.setAllowsMultipleSelection_(False)
        panel.setAllowedFileTypes_(["pdf", "docx"])
        panel.setTitle_("Selecciona el documento para validar referencias")
        panel.setMessage_("Elige el archivo PDF o DOCX cuyas referencias quieres validar")
        if panel.runModal() == 1:
            path = panel.URLs()[0].path()
            archivo_seleccionado = normalize_path(path, nfc=FORZAR_NFC)
            # Intentar hidratar el archivo si es de OneDrive
            ensure_hydrated(archivo_seleccionado, logger)
            return archivo_seleccionado
    except ImportError:
        logger.error("❌ AppKit no disponible. Instalar con: pip install pyobjc")
        logger.info("💡 Usando modo fallback de selección manual...")
        return seleccionar_archivo_fallback()
    except Exception as e:
        logger.error(f"Error en selector GUI de AppKit: {e}")
        logger.info("💡 Usando modo fallback de selección manual...")
        return seleccionar_archivo_fallback()
    return None


def seleccionar_archivo_fallback() -> Optional[str]:
    """
    Fallback para selección de archivos cuando AppKit no está disponible.
    Busca archivos en el directorio actual y permite selección manual.
    """
    print("\n🔍 Búsqueda de archivos PDF y DOCX en directorio actual...")
    directorio_actual = Path.cwd()
    archivos_disponibles = []
    
    for extension in [".pdf", ".docx"]:
        archivos_disponibles.extend(directorio_actual.glob(f"*{extension}"))
    
    if archivos_disponibles:
        print(f"\n📁 Archivos encontrados en {directorio_actual}:")
        for i, archivo_disponible in enumerate(archivos_disponibles, 1):
            print(f"   {i}. {archivo_disponible.name}")
        
        print(f"   {len(archivos_disponibles) + 1}. Introducir ruta personalizada")
        
        while True:
            try:
                seleccion = input(f"\n🔢 Selecciona archivo (1-{len(archivos_disponibles) + 1}): ").strip()
                if not seleccion:
                    return None
                
                indice = int(seleccion) - 1
                
                if 0 <= indice < len(archivos_disponibles):
                    return str(archivos_disponibles[indice])
                elif indice == len(archivos_disponibles):
                    archivo = input("📄 Introduce la ruta completa del archivo: ").strip()
                    return archivo if archivo else None
                else:
                    print(f"❌ Selección inválida. Debe ser entre 1 y {len(archivos_disponibles) + 1}")
            except ValueError:
                print("❌ Por favor, introduce un número válido")
    else:
        print("❌ No se encontraron archivos PDF o DOCX en el directorio actual")
        archivo = input("\n📄 Introduce la ruta completa del archivo: ").strip()
        return archivo if archivo else None


# Configurar logging básico
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)


class EstiloCita(Enum):
    """Estilos de cita soportados"""
    APA = "apa"
    IEEE = "ieee"
    MLA = "mla"
    VANCOUVER = "vancouver"


@dataclass
class ReferenciaAnalizada:
    """Estructura para almacenar el análisis de una referencia"""
    texto_original: str
    tiene_autor: bool
    tiene_anio: bool
    tiene_titulo: bool
    tiene_editorial: bool
    tiene_url: bool
    tiene_doi: bool
    es_completa: bool
    errores: List[str]
    sugerencias: List[str]
    puntuacion: float  # 0.0 a 1.0


@dataclass
class InformeValidacion:
    """Estructura del informe completo de validación"""
    archivo_analizado: str
    estilo_validacion: str
    total_referencias: int
    referencias_validas: int
    referencias_con_errores: int
    puntuacion_promedio: float
    referencias: List[ReferenciaAnalizada]
    patrones_detectados: List[str]
    recomendaciones_generales: List[str]


class ExtractorReferencias:
    """Extrae referencias de diferentes tipos de documentos"""
    
    @staticmethod
    def extraer_desde_pdf(ruta_archivo: str) -> Tuple[List[str], List[str]]:
        """Extrae referencias de un archivo PDF"""
        if not PDF_AVAILABLE:
            raise ImportError("pdfplumber no está disponible")
        
        referencias = []
        patrones_detectados = []
        
        try:
            with pdfplumber.open(ruta_archivo) as pdf:
                # Detectar patrones de encabezados/pies
                patrones_detectados = ExtractorReferencias._detectar_patrones_repetitivos(pdf)
                
                # Buscar sección de referencias
                texto_completo = ""
                for pagina in pdf.pages:
                    texto_pagina = pagina.extract_text()
                    if texto_pagina:
                        # Filtrar patrones de encabezado/pie
                        texto_limpio = ExtractorReferencias._limpiar_texto(texto_pagina, patrones_detectados)
                        texto_completo += texto_limpio + "\n"
                
                # Extraer referencias de la sección correspondiente
                referencias = ExtractorReferencias._extraer_referencias_del_texto(texto_completo)
                
        except Exception as e:
            print(f"❌ Error extrayendo referencias del PDF: {e}")
        
        return referencias, patrones_detectados
    
    @staticmethod
    def extraer_desde_docx(ruta_archivo: str) -> Tuple[List[str], List[str]]:
        """Extrae referencias de un archivo DOCX"""
        if not DOCX_AVAILABLE:
            raise ImportError("lxml no está disponible")
        
        referencias = []
        patrones_detectados = []
        
        try:
            with zipfile.ZipFile(ruta_archivo, "r") as docx_zip:
                # Leer document.xml principal
                document_xml = docx_zip.read("word/document.xml")
                tree = etree.XML(document_xml)
                
                # Extraer todos los párrafos
                texto_parrafos = []
                for elemento in tree.xpath("//w:p", namespaces={"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}):
                    texto_parrafo = "".join(
                        t.text for t in elemento.xpath(".//w:t", namespaces={"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}) 
                        if t.text
                    ).strip()
                    if texto_parrafo:
                        texto_parrafos.append(texto_parrafo)
                
                # Unir texto y extraer referencias
                texto_completo = "\n".join(texto_parrafos)
                referencias = ExtractorReferencias._extraer_referencias_del_texto(texto_completo)
                
        except Exception as e:
            print(f"❌ Error extrayendo referencias del DOCX: {e}")
        
        return referencias, patrones_detectados
    
    @staticmethod
    def _detectar_patrones_repetitivos(pdf) -> List[str]:
        """Detecta patrones repetitivos de encabezados/pies de página"""
        from collections import Counter
        
        patrones_texto = Counter()
        total_paginas = len(pdf.pages)
        
        for pagina in pdf.pages:
            texto_pagina = pagina.extract_text()
            if texto_pagina:
                lineas = texto_pagina.splitlines()
                for linea in lineas:
                    linea_limpia = linea.strip()
                    if linea_limpia and len(linea_limpia) < 100:  # Solo líneas cortas
                        patrones_texto[linea_limpia] += 1
        
        # Identificar patrones que aparecen en >80% de las páginas
        patrones_repetitivos = [
            patron for patron, count in patrones_texto.items() 
            if count > 0.8 * total_paginas
        ]
        
        return patrones_repetitivos
    
    @staticmethod
    def _limpiar_texto(texto: str, patrones_a_remover: List[str]) -> str:
        """Limpia el texto removiendo patrones de encabezado/pie"""
        texto_limpio = texto
        
        for patron in patrones_a_remover:
            texto_limpio = texto_limpio.replace(patron, "")
        
        # Remover números de página
        texto_limpio = re.sub(r"^\d+$", "", texto_limpio, flags=re.MULTILINE)
        texto_limpio = re.sub(r"^(Page|Página) \d+$", "", texto_limpio, flags=re.MULTILINE)
        
        return texto_limpio
    
    @staticmethod
    def _extraer_referencias_del_texto(texto: str) -> List[str]:
        """Extrae referencias de la sección bibliográfica del texto"""
        referencias = []
        
        # Detectar idioma y palabras clave
        palabras_clave_es = ["referencias bibliográficas", "bibliografía", "referencias"]
        palabras_clave_en = ["references", "bibliography", "works cited"]
        
        # Buscar sección de referencias
        texto_lower = texto.lower()
        inicio_referencias = -1
        
        # Buscar en español
        for palabra_clave in palabras_clave_es:
            pos = texto_lower.find(palabra_clave)
            if pos != -1:
                inicio_referencias = pos
                break
        
        # Buscar en inglés si no encontró en español
        if inicio_referencias == -1:
            for palabra_clave in palabras_clave_en:
                pos = texto_lower.find(palabra_clave)
                if pos != -1:
                    inicio_referencias = pos
                    break
        
        if inicio_referencias != -1:
            # Extraer texto desde la sección de referencias
            seccion_referencias = texto[inicio_referencias:]
            
            # Dividir en párrafos y filtrar referencias
            parrafos = seccion_referencias.split('\n')
            
            for parrafo in parrafos:
                parrafo_limpio = parrafo.strip()
                
                # Filtros para identificar referencias válidas
                if (len(parrafo_limpio) > 50 and  # Longitud mínima
                    '.' in parrafo_limpio and      # Debe tener puntos
                    not parrafo_limpio.lower().startswith(('referencias', 'bibliografía', 'references')) and  # No es encabezado
                    not re.match(r'^\d+\s*$', parrafo_limpio)):  # No es solo número
                    
                    referencias.append(parrafo_limpio)
        
        return referencias


class ValidadorReferencias:
    """Valida referencias según diferentes estándares"""
    
    def __init__(self, estilo: EstiloCita = EstiloCita.APA):
        self.estilo = estilo
        self.patrones = self._cargar_patrones_validacion(estilo)
    
    def validar_referencia(self, referencia: str) -> ReferenciaAnalizada:
        """Valida una referencia individual"""
        
        # Análisis básico de componentes
        tiene_autor = self._verificar_autor(referencia)
        tiene_anio = self._verificar_anio(referencia)
        tiene_titulo = self._verificar_titulo(referencia)
        tiene_editorial = self._verificar_editorial(referencia)
        tiene_url = self._verificar_url(referencia)
        tiene_doi = self._verificar_doi(referencia)
        
        # Recopilar errores y sugerencias
        errores = []
        sugerencias = []
        
        if not tiene_autor:
            errores.append("Falta información del autor")
            sugerencias.append("Incluir apellido e inicial del nombre del autor")
        
        if not tiene_anio:
            errores.append("Falta año de publicación")
            sugerencias.append("Incluir año entre paréntesis según formato APA")
        
        if not tiene_titulo:
            errores.append("Falta título de la obra")
            sugerencias.append("Incluir título completo de la publicación")
        
        # Validaciones específicas por estilo
        if self.estilo == EstiloCita.APA:
            errores.extend(self._validar_apa_especifico(referencia))
        elif self.estilo == EstiloCita.IEEE:
            errores.extend(self._validar_ieee_especifico(referencia))
        
        # Calcular puntuación
        componentes_totales = 6
        componentes_presentes = sum([tiene_autor, tiene_anio, tiene_titulo, tiene_editorial, tiene_url, tiene_doi])
        puntuacion = componentes_presentes / componentes_totales
        
        # Determinar si es completa
        es_completa = len(errores) == 0 and puntuacion >= 0.7
        
        return ReferenciaAnalizada(
            texto_original=referencia,
            tiene_autor=tiene_autor,
            tiene_anio=tiene_anio,
            tiene_titulo=tiene_titulo,
            tiene_editorial=tiene_editorial,
            tiene_url=tiene_url,
            tiene_doi=tiene_doi,
            es_completa=es_completa,
            errores=errores,
            sugerencias=sugerencias,
            puntuacion=puntuacion
        )
    
    def _cargar_patrones_validacion(self, estilo: EstiloCita) -> Dict:
        """Carga patrones de validación según el estilo"""
        patrones_base = {
            EstiloCita.APA: {
                "autor_patron": r"^[A-ZÁÉÍÓÚ][a-záéíóúñü]+,\s*[A-Z]\.",
                "anio_patron": r"\(\d{4}\)",
                "titulo_patron": r"[A-Z][^.]+\.",
                "url_patron": r"https?://[^\s]+",
                "doi_patron": r"doi:\s*10\.\d+/[^\s]+"
            },
            EstiloCita.IEEE: {
                "autor_patron": r"^[A-Z]\.\s*[A-ZÁÉÍÓÚ][a-záéíóúñü]+",
                "anio_patron": r"\(\d{4}\)",
                "titulo_patron": r'"[^"]+",',
                "url_patron": r"Available:\s*https?://[^\s]+",
                "doi_patron": r"doi:\s*10\.\d+/[^\s]+"
            }
        }
        
        return patrones_base.get(estilo, patrones_base[EstiloCita.APA])
    
    def _verificar_autor(self, referencia: str) -> bool:
        """Verifica presencia de autor"""
        patron = self.patrones.get("autor_patron", r"[A-ZÁÉÍÓÚ][a-záéíóúñü]+")
        return bool(re.search(patron, referencia))
    
    def _verificar_anio(self, referencia: str) -> bool:
        """Verifica presencia de año"""
        patron = self.patrones.get("anio_patron", r"\(\d{4}\)")
        return bool(re.search(patron, referencia))
    
    def _verificar_titulo(self, referencia: str) -> bool:
        """Verifica presencia de título"""
        # Buscar títulos entre comillas o en cursiva
        return bool(re.search(r'["\'][^"\']{10,}["\']', referencia) or 
                   re.search(r'[A-Z][^.]{10,}\.', referencia))
    
    def _verificar_editorial(self, referencia: str) -> bool:
        """Verifica presencia de editorial"""
        editoriales_comunes = ["editorial", "press", "publisher", "ed.", "university"]
        return any(editorial in referencia.lower() for editorial in editoriales_comunes)
    
    def _verificar_url(self, referencia: str) -> bool:
        """Verifica presencia de URL"""
        return bool(re.search(r"https?://[^\s]+", referencia))
    
    def _verificar_doi(self, referencia: str) -> bool:
        """Verifica presencia de DOI"""
        return bool(re.search(r"doi:\s*10\.\d+/[^\s]+", referencia))
    
    def _validar_apa_especifico(self, referencia: str) -> List[str]:
        """Validaciones específicas para estilo APA"""
        errores = []
        
        # Verificar formato de autor (Apellido, I.)
        if not re.search(r"[A-ZÁÉÍÓÚ][a-záéíóúñü]+,\s*[A-Z]\.", referencia):
            errores.append("Formato de autor no cumple APA (debe ser: Apellido, I.)")
        
        # Verificar año entre paréntesis
        if not re.search(r"\(\d{4}\)", referencia):
            errores.append("Año debe estar entre paréntesis en formato APA")
        
        return errores
    
    def _validar_ieee_especifico(self, referencia: str) -> List[str]:
        """Validaciones específicas para estilo IEEE"""
        errores = []
        
        # Verificar formato de autor IEEE (I. Apellido)
        if not re.search(r"[A-Z]\.\s*[A-ZÁÉÍÓÚ][a-záéíóúñü]+", referencia):
            errores.append("Formato de autor no cumple IEEE (debe ser: I. Apellido)")
        
        # Verificar título entre comillas
        if not re.search(r'"[^"]+",', referencia):
            errores.append("Título de artículo debe estar entre comillas en IEEE")
        
        return errores


class GeneradorInformes:
    """Genera informes de validación en diferentes formatos"""
    
    @staticmethod
    def generar_informe_json(informe: InformeValidacion, ruta_salida: str):
        """Genera informe en formato JSON"""
        try:
            with open(ruta_salida, 'w', encoding='utf-8') as archivo:
                json.dump(asdict(informe), archivo, ensure_ascii=False, indent=2)
            print(f"✅ Informe JSON generado: {ruta_salida}")
        except Exception as e:
            print(f"❌ Error generando informe JSON: {e}")
    
    @staticmethod
    def generar_informe_markdown(informe: InformeValidacion, ruta_salida: str):
        """Genera informe en formato Markdown"""
        try:
            contenido = GeneradorInformes._construir_markdown(informe)
            with open(ruta_salida, 'w', encoding='utf-8') as archivo:
                archivo.write(contenido)
            print(f"✅ Informe Markdown generado: {ruta_salida}")
        except Exception as e:
            print(f"❌ Error generando informe Markdown: {e}")
    
    @staticmethod
    def _construir_markdown(informe: InformeValidacion) -> str:
        """Construye el contenido Markdown del informe"""
        lineas = [
            f"# 📚 Informe de Validación de Referencias",
            f"",
            f"**Archivo analizado:** `{informe.archivo_analizado}`",
            f"**Estilo de validación:** {informe.estilo_validacion.upper()}",
            f"**Fecha de análisis:** {GeneradorInformes._obtener_fecha_actual()}",
            f"",
            f"## 📊 Resumen Ejecutivo",
            f"",
            f"- **Total de referencias:** {informe.total_referencias}",
            f"- **Referencias válidas:** {informe.referencias_validas}",
            f"- **Referencias con errores:** {informe.referencias_con_errores}",
            f"- **Puntuación promedio:** {informe.puntuacion_promedio:.2f}/1.00",
            f"- **Porcentaje de cumplimiento:** {(informe.referencias_validas/informe.total_referencias*100):.1f}%",
            f"",
            f"## 🔍 Análisis Detallado de Referencias",
            f""
        ]
        
        for i, ref in enumerate(informe.referencias, 1):
            estado = "✅ VÁLIDA" if ref.es_completa else "❌ CON ERRORES"
            lineas.extend([
                f"### Referencia {i} - {estado}",
                f"",
                f"**Texto original:**",
                f"> {ref.texto_original}",
                f"",
                f"**Componentes detectados:**",
                f"- Autor: {'✅' if ref.tiene_autor else '❌'}",
                f"- Año: {'✅' if ref.tiene_anio else '❌'}",
                f"- Título: {'✅' if ref.tiene_titulo else '❌'}",
                f"- Editorial: {'✅' if ref.tiene_editorial else '❌'}",
                f"- URL: {'✅' if ref.tiene_url else '❌'}",
                f"- DOI: {'✅' if ref.tiene_doi else '❌'}",
                f"",
                f"**Puntuación:** {ref.puntuacion:.2f}/1.00",
                f""
            ])
            
            if ref.errores:
                lineas.extend([
                    f"**❌ Errores detectados:**",
                    *[f"- {error}" for error in ref.errores],
                    f""
                ])
            
            if ref.sugerencias:
                lineas.extend([
                    f"**💡 Sugerencias de mejora:**",
                    *[f"- {sugerencia}" for sugerencia in ref.sugerencias],
                    f""
                ])
            
            lineas.append("---\n")
        
        if informe.recomendaciones_generales:
            lineas.extend([
                f"## 💡 Recomendaciones Generales",
                f"",
                *[f"- {recomendacion}" for recomendacion in informe.recomendaciones_generales],
                f""
            ])
        
        return "\n".join(lineas)
    
    @staticmethod
    def _obtener_fecha_actual() -> str:
        """Obtiene la fecha actual formateada"""
        from datetime import datetime
        return datetime.now().strftime("%d de %B de %Y")


def modo_interactivo():
    """Modo interactivo usando el selector nativo de macOS"""
    print("🔍 VALIDADOR DE REFERENCIAS BIBLIOGRÁFICAS")
    print("=" * 60)
    
    # Usar el selector nativo de macOS
    print("📁 Seleccionando archivo...")
    archivo = seleccionar_archivo_referencias(logger)
    
    if not archivo:
        print("❌ No se seleccionó ningún archivo")
        return None
    
    # Verificar que el archivo existe
    if not Path(archivo).exists():
        print(f"❌ Error: El archivo {archivo} no existe")
        return None
    
    print(f"✅ Archivo seleccionado: {Path(archivo).name}")
    
    # Seleccionar estilo de validación
    print(f"\n📋 Estilos de validación disponibles:")
    estilos = ["apa", "ieee", "mla"]
    for i, estilo in enumerate(estilos, 1):
        descripcion = {
            "apa": "APA 7ª edición (Psicología, Educación)",
            "ieee": "IEEE (Ingeniería, Tecnología)",
            "mla": "MLA (Literatura, Humanidades)"
        }
        print(f"   {i}. {estilo.upper()} - {descripcion[estilo]}")
    
    while True:
        try:
            seleccion_estilo = input(f"\n📝 Selecciona estilo (1-3) [por defecto: APA]: ").strip()
            if not seleccion_estilo:
                estilo = "apa"
                break
            
            indice_estilo = int(seleccion_estilo) - 1
            if 0 <= indice_estilo < len(estilos):
                estilo = estilos[indice_estilo]
                break
            else:
                print("❌ Selección inválida. Debe ser entre 1 y 3")
        except ValueError:
            print("❌ Por favor, introduce un número válido")
    
    # Seleccionar formato de salida
    print(f"\n📄 Formatos de informe:")
    print("   1. Markdown (.md) - Legible y estructurado")
    print("   2. JSON (.json) - Datos estructurados para procesamiento")
    
    while True:
        try:
            seleccion_formato = input(f"\n📊 Selecciona formato (1-2) [por defecto: Markdown]: ").strip()
            if not seleccion_formato:
                formato = "markdown"
                break
            
            indice_formato = int(seleccion_formato) - 1
            if indice_formato == 0:
                formato = "markdown"
                break
            elif indice_formato == 1:
                formato = "json"
                break
            else:
                print("❌ Selección inválida. Debe ser 1 o 2")
        except ValueError:
            print("❌ Por favor, introduce un número válido")
    
    return {
        'archivo': archivo,
        'estilo': estilo,
        'formato': formato,
        'salida': None
    }


def main():
    """Función principal del validador de referencias"""
    parser = argparse.ArgumentParser(
        description="Validador modular de referencias bibliográficas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python referencias_validator.py --archivo documento.pdf --estilo apa
  python referencias_validator.py --archivo tesis.docx --estilo ieee --salida informe.json
  python referencias_validator.py --archivo ensayo.pdf --estilo mla --formato markdown
  python referencias_validator.py --interactivo
        """
    )
    
    parser.add_argument("--archivo", "-a", help="Archivo a analizar (PDF o DOCX)")
    parser.add_argument("--estilo", "-e", choices=["apa", "ieee", "mla"], default="apa", help="Estilo de cita a validar")
    parser.add_argument("--salida", "-s", help="Archivo de salida para el informe")
    parser.add_argument("--formato", "-f", choices=["json", "markdown"], default="markdown", help="Formato del informe")
    parser.add_argument("--interactivo", "-i", action="store_true", help="Modo interactivo para seleccionar archivo y opciones")
    
    args = parser.parse_args()
    
    # Modo interactivo
    if args.interactivo:
        config = modo_interactivo()
        if not config:
            sys.exit(1)
        
        archivo = config['archivo']
        estilo = config['estilo']
        formato = config['formato']
        salida = config['salida']
    else:
        # Si no se proporciona archivo, usar selector nativo de macOS
        archivo = args.archivo
        if not archivo:
            print("🔍 VALIDADOR DE REFERENCIAS BIBLIOGRÁFICAS")
            print("=" * 50)
            print("📁 Abriendo selector de archivos de macOS...")
            archivo = seleccionar_archivo_referencias(logger)
            
            if not archivo:
                print("❌ Error: No se seleccionó ningún archivo")
                print("💡 Usa: python referencias_validator.py --archivo documento.pdf")
                print("💡 O usa: python referencias_validator.py --interactivo")
                sys.exit(1)
            
            print(f"✅ Archivo seleccionado: {Path(archivo).name}")
        
        estilo = args.estilo
        formato = args.formato
        salida = args.salida
    
    # Verificar que el archivo existe
    if not Path(archivo).exists():
        print(f"❌ Error: El archivo {archivo} no existe")
        
        # Sugerir archivos PDF/DOCX en el directorio actual
        directorio_actual = Path.cwd()
        archivos_disponibles = []
        
        for extension in [".pdf", ".docx"]:
            archivos_disponibles.extend(directorio_actual.glob(f"*{extension}"))
        
        if archivos_disponibles:
            print(f"\n💡 Archivos disponibles en {directorio_actual}:")
            for i, archivo_disponible in enumerate(archivos_disponibles, 1):
                print(f"   {i}. {archivo_disponible.name}")
            
            print(f"\n🔄 Reinicia el script con:")
            print(f"   python referencias_validator.py --archivo \"nombre_archivo.pdf\"")
        
        sys.exit(1)
    
    # Determinar formato del archivo
    extension = Path(archivo).suffix.lower()
    
    print(f"🔍 Analizando: {archivo}")
    print(f"📋 Estilo: {estilo.upper()}")
    print(f"📄 Formato: {extension}")
    print("=" * 50)
    
    try:
        # Extraer referencias según el tipo de archivo
        if extension == ".pdf":
            if not PDF_AVAILABLE:
                print("❌ Error: pdfplumber no está instalado. Ejecutar: pip install pdfplumber")
                sys.exit(1)
            referencias, patrones = ExtractorReferencias.extraer_desde_pdf(archivo)
        elif extension == ".docx":
            if not DOCX_AVAILABLE:
                print("❌ Error: lxml no está instalado. Ejecutar: pip install lxml")
                sys.exit(1)
            referencias, patrones = ExtractorReferencias.extraer_desde_docx(archivo)
        else:
            print(f"❌ Error: Formato de archivo {extension} no soportado")
            print("💡 Formatos soportados: .pdf, .docx")
            sys.exit(1)
        
        print(f"📚 Referencias extraídas: {len(referencias)}")
        
        if not referencias:
            print("⚠️  No se encontraron referencias en el documento")
            sys.exit(0)
        
        # Validar referencias
        estilo_enum = EstiloCita(estilo)
        validador = ValidadorReferencias(estilo_enum)
        
        referencias_analizadas = []
        referencias_validas = 0
        
        for referencia in referencias:
            analisis = validador.validar_referencia(referencia)
            referencias_analizadas.append(analisis)
            if analisis.es_completa:
                referencias_validas += 1
        
        # Generar recomendaciones generales
        recomendaciones = []
        if referencias_validas / len(referencias) < 0.8:
            recomendaciones.append("Revisar formato general de las referencias según el estilo seleccionado")
        if any(not ref.tiene_doi for ref in referencias_analizadas):
            recomendaciones.append("Considerar incluir DOI cuando esté disponible")
        if any(not ref.tiene_url for ref in referencias_analizadas):
            recomendaciones.append("Incluir URLs de acceso para recursos digitales")
        
        # Crear informe
        puntuacion_promedio = sum(ref.puntuacion for ref in referencias_analizadas) / len(referencias_analizadas)
        
        informe = InformeValidacion(
            archivo_analizado=archivo,
            estilo_validacion=estilo,
            total_referencias=len(referencias),
            referencias_validas=referencias_validas,
            referencias_con_errores=len(referencias) - referencias_validas,
            puntuacion_promedio=puntuacion_promedio,
            referencias=referencias_analizadas,
            patrones_detectados=patrones,
            recomendaciones_generales=recomendaciones
        )
        
        # Generar archivo de salida
        if salida:
            ruta_salida = salida
        else:
            nombre_base = Path(archivo).stem
            extension_salida = "json" if formato == "json" else "md"
            ruta_salida = f"informe_referencias_{nombre_base}.{extension_salida}"
        
        if formato == "json":
            GeneradorInformes.generar_informe_json(informe, ruta_salida)
        else:
            GeneradorInformes.generar_informe_markdown(informe, ruta_salida)
        
        # Mostrar resumen en consola
        print(f"\n📊 RESUMEN DE VALIDACIÓN:")
        print(f"   ✅ Referencias válidas: {referencias_validas}/{len(referencias)}")
        print(f"   ❌ Referencias con errores: {len(referencias) - referencias_validas}")
        print(f"   📈 Puntuación promedio: {puntuacion_promedio:.2f}/1.00")
        print(f"   📋 Cumplimiento: {(referencias_validas/len(referencias)*100):.1f}%")
        print(f"   📄 Informe guardado: {ruta_salida}")
        
    except Exception as e:
        print(f"❌ Error durante el análisis: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()