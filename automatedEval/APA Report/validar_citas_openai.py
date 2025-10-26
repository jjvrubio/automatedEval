import json
import os
import docx
import pdfplumber
import logging
from pathlib import Path
from AppKit import NSApplication
from Cocoa import NSOpenPanel

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Funciones de compatibilidad para integración
def seleccionar_archivo_con_dialogo():
    """Función wrapper para compatibilidad con integrador"""
    return select_file(['pdf', 'docx'], "Seleccionar TFM para evaluar")

def extraer_texto_documento(ruta_archivo):
    """Función wrapper para extraer texto de cualquier documento"""
    if not ruta_archivo or not Path(ruta_archivo).exists():
        return None
    
    extension = Path(ruta_archivo).suffix.lower()
    if extension == '.pdf':
        return extract_text_from_pdf(ruta_archivo)
    elif extension == '.docx':
        return extract_text_from_docx(ruta_archivo)
    else:
        logger.error(f"Formato no soportado: {extension}")
        return None

def crear_cliente_openai():
    """Crea cliente OpenAI compatible con v1+ y v0.x"""
    api_key = os.environ.get("MI_CLAVE_API_OPENAI") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("ERROR: No se encontró la variable de entorno MI_CLAVE_API_OPENAI o OPENAI_API_KEY")
    
    try:
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        logger.info("OpenAI client (v1+) inicializado")
        return ("v1", client)
    except ImportError:
        import openai
        openai.api_key = api_key
        logger.info("OpenAI client (v0.x) inicializado")
        return ("v0", openai)

def select_file(allowed_types, title):
    """Selector de archivos con manejo de errores mejorado"""
    try:
        NSApplication.sharedApplication()
        panel = NSOpenPanel.openPanel()
        panel.setAllowedFileTypes_(allowed_types)
        panel.setCanChooseFiles_(True)
        panel.setCanChooseDirectories_(False)
        panel.setTitle_(title)
        if panel.runModal() == 1:
            return panel.URLs()[0].path()
        return None
    except Exception as e:
        logger.error(f"Error en selector de archivos: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    """Extrae texto de PDF con manejo robusto de errores"""
    try:
        logger.info(f"Extrayendo texto de PDF: {pdf_path}")
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for i, page in enumerate(pdf.pages):
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text += f"[P{i+1}]\n{page_text}\n\n"
                except Exception as e:
                    logger.warning(f"Error en página {i+1}: {e}")
                    text += f"[P{i+1}] (Error de extracción)\n\n"
        logger.info(f"Texto extraído: {len(text)} caracteres")
        return text
    except Exception as e:
        logger.error(f"Error extrayendo PDF: {e}")
        return ""

def extract_text_from_docx(docx_path):
    """Extrae texto de DOCX con manejo robusto de errores"""
    try:
        logger.info(f"Extrayendo texto de DOCX: {docx_path}")
        doc = docx.Document(docx_path)
        text_parts = []
        for i, para in enumerate(doc.paragraphs):
            if para.text.strip():
                text_parts.append(para.text)
        text = "\n".join(text_parts)
        logger.info(f"Texto extraído: {len(text)} caracteres")
        return text
    except Exception as e:
        logger.error(f"Error extrayendo DOCX: {e}")
        return ""

def segment_text(text, max_chars=10000):
    """Divide texto largo en segmentos manteniendo contexto"""
    if len(text) <= max_chars:
        return [text]
    
    segments = []
    paragraphs = text.split('\n\n')
    current_segment = ""
    
    for paragraph in paragraphs:
        # Si agregar este párrafo no excede el límite
        if len(current_segment + paragraph + '\n\n') <= max_chars:
            current_segment += paragraph + '\n\n'
        else:
            # Guardar segmento actual si no está vacío
            if current_segment.strip():
                segments.append(current_segment.strip())
            # Comenzar nuevo segmento
            if len(paragraph) <= max_chars:
                current_segment = paragraph + '\n\n'
            else:
                # Si el párrafo es muy largo, dividirlo por frases
                sentences = paragraph.split('. ')
                for sentence in sentences:
                    if len(current_segment + sentence + '. ') <= max_chars:
                        current_segment += sentence + '. '
                    else:
                        if current_segment.strip():
                            segments.append(current_segment.strip())
                        current_segment = sentence + '. '
    
    # Agregar el último segmento
    if current_segment.strip():
        segments.append(current_segment.strip())
    
    logger.info(f"Texto dividido en {len(segments)} segmentos")
    return segments

def extraer_referencias_automaticamente(compat, client, texto_completo):
    """
    Extrae automáticamente las referencias bibliográficas del texto del TFM.
    """
    logger.info("Extrayendo referencias automáticamente del TFM...")
    
    # Buscar sección de referencias (varios nombres posibles)
    posibles_secciones = [
        "referencias bibliográficas", "referencias", "bibliografía", 
        "bibliography", "references", "fuentes bibliográficas",
        "lista de referencias", "fuentes consultadas"
    ]
    
    texto_lower = texto_completo.lower()
    inicio_referencias = -1
    seccion_encontrada = ""
    
    # Buscar donde empiezan las referencias
    for seccion in posibles_secciones:
        pos = texto_lower.find(seccion)
        if pos != -1:
            inicio_referencias = pos
            seccion_encontrada = seccion
            logger.info(f"Sección de referencias encontrada: '{seccion}' en posición {pos}")
            break
    
    if inicio_referencias == -1:
        logger.warning("No se encontró sección de referencias claramente identificada")
        # Intentar con los últimos párrafos del documento
        parrafos = texto_completo.split('\n\n')
        texto_referencias = '\n\n'.join(parrafos[-20:])  # Últimos 20 párrafos
        logger.info("Usando últimos 20 párrafos como posible sección de referencias")
    else:
        # Extraer desde donde empiezan las referencias hasta el final
        texto_referencias = texto_completo[inicio_referencias:]
        # Limitar a una cantidad razonable (evitar anexos, etc.)
        if len(texto_referencias) > 15000:
            texto_referencias = texto_referencias[:15000]
            logger.info("Texto de referencias limitado a 15000 caracteres")
    
    # Usar IA para extraer y estructurar las referencias
    prompt = f"""
Extrae TODAS las referencias bibliográficas del siguiente texto académico.

INSTRUCCIONES:
1. Identifica cada referencia individual en la sección bibliográfica
2. Devuelve SOLO las referencias, una por línea
3. Mantén el formato APA original de cada referencia
4. No incluyas números, viñetas o marcadores adicionales
5. Si hay texto que no son referencias (títulos, párrafos explicativos), ignóralo
6. Cada referencia debe ser una línea separada

TEXTO A ANALIZAR:
---
{texto_referencias}
---

Devuelve solo las referencias extraídas, una por línea, sin numeración ni formato adicional.
"""

    try:
        if compat == "v1":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un experto en extraer referencias bibliográficas de textos académicos."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.1
            )
            referencias_extraidas = response.choices[0].message.content
        else:  # v0.x
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un experto en extraer referencias bibliográficas de textos académicos."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.1
            )
            referencias_extraidas = response["choices"][0]["message"]["content"]
        
        # Procesar las referencias extraídas
        if referencias_extraidas:
            referencias_lista = [ref.strip() for ref in referencias_extraidas.split('\n') 
                               if ref.strip() and len(ref.strip()) > 20]  # Filtrar líneas muy cortas
            
            logger.info(f"Referencias extraídas automáticamente: {len(referencias_lista)}")
            return referencias_lista
        else:
            logger.error("No se pudieron extraer referencias automáticamente")
            return []
            
    except Exception as e:
        logger.error(f"Error extrayendo referencias automáticamente: {e}")
        return []

def guardar_referencias_extraidas(referencias, tfm_file):
    """Guarda las referencias extraídas en un archivo JSON para futura referencia"""
    try:
        output_dir = os.path.dirname(tfm_file)
        base_name = os.path.splitext(os.path.basename(tfm_file))[0]
        json_path = os.path.join(output_dir, f"{base_name}_referencias_extraidas.json")
        
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(referencias, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Referencias guardadas en: {json_path}")
        return json_path
    except Exception as e:
        logger.error(f"Error guardando referencias: {e}")
        return None

def validar_citas_integral(compat, client, texto_completo, referencias):
    """
    Validación integral de citas APA - UNA SOLA llamada optimizada
    """
    logger.info("🚀 Iniciando validación integral (una sola llamada)")
    
    # Extraer solo las partes relevantes del texto para optimizar
    partes_relevantes = extraer_partes_relevantes_para_citas(texto_completo)
    
    prompt = f"""
Eres un experto en normas APA 7. Analiza COMPLETAMENTE el siguiente TFM y sus referencias.

ANÁLISIS REQUERIDO:

1. **EXTRACCIÓN DE CITAS**:
   - Identifica TODAS las citas en el texto (Autor, año), (Autor et al., año), etc.
   - Lista cada cita única encontrada

2. **VERIFICACIÓN CRUZADA**:
   - Para cada cita: ¿existe referencia correspondiente?
   - Para cada referencia: ¿está citada en el texto?

3. **ANÁLISIS DE CALIDAD APA**:
   - Errores de formato en citas
   - Errores de formato en referencias
   - Inconsistencias entre citas y referencias
   - Referencias huérfanas (no citadas)
   - Citas huérfanas (sin referencia)

4. **ESTADÍSTICAS**:
   - Total de citas encontradas
   - Total de referencias proporcionadas
   - Porcentaje de correspondencia
   - Principales problemas detectados

TEXTO DEL TFM (partes relevantes):
---
{partes_relevantes}
---

REFERENCIAS BIBLIOGRÁFICAS:
---
{chr(10).join(referencias[:50])}  
---

Proporciona un análisis COMPLETO y DETALLADO en formato Markdown con todas las secciones solicitadas.
"""

    try:
        if compat == "v1":
            response = client.chat.completions.create(
                model="gpt-4o",  # Modelo más potente para análisis completo
                messages=[
                    {"role": "system", "content": "Eres un experto en normas APA 7 y análisis bibliográfico integral."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=3000,  # Más tokens para análisis completo
                temperature=0.1
            )
            return response.choices[0].message.content
        else:  # v0.x
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "Eres un experto en normas APA 7 y análisis bibliográfico integral."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=3000,
                temperature=0.1
            )
            return response["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"Error en validación integral: {e}")
        return f"**ERROR**: No se pudo completar la validación: {str(e)}"

def extraer_partes_relevantes_para_citas(texto_completo, max_chars=25000):
    """
    Extrae las partes más relevantes del texto para análisis de citas,
    priorizando introducción, desarrollo y conclusiones.
    """
    logger.info("📝 Extrayendo partes relevantes para análisis de citas")
    
    # Si el texto es pequeño, usar todo
    if len(texto_completo) <= max_chars:
        return texto_completo
    
    parrafos = texto_completo.split('\n\n')
    partes_importantes = []
    caracteres_usados = 0
    
    # ESTRATEGIA: Tomar más del principio y final, menos del medio
    total_parrafos = len(parrafos)
    
    # 40% del principio (introducción, marco teórico)
    inicio_hasta = int(total_parrafos * 0.4)
    for i in range(min(inicio_hasta, total_parrafos)):
        if caracteres_usados + len(parrafos[i]) <= max_chars * 0.6:
            partes_importantes.append(parrafos[i])
            caracteres_usados += len(parrafos[i])
        else:
            break
    
    # 30% del final (conclusiones, discusión)
    final_desde = max(inicio_hasta, int(total_parrafos * 0.7))
    for i in range(final_desde, total_parrafos):
        if caracteres_usados + len(parrafos[i]) <= max_chars:
            partes_importantes.append(parrafos[i])
            caracteres_usados += len(parrafos[i])
        else:
            break
    
    # Rellenar con partes del medio si queda espacio
    for i in range(inicio_hasta, final_desde):
        if caracteres_usados + len(parrafos[i]) <= max_chars:
            # Insertar en el medio de la lista
            medio = len(partes_importantes) // 2
            partes_importantes.insert(medio, parrafos[i])
            caracteres_usados += len(parrafos[i])
        else:
            break
    
    texto_optimizado = '\n\n'.join(partes_importantes)
    logger.info(f"Texto optimizado: {len(texto_optimizado)} caracteres de {len(texto_completo)} originales")
    
    return texto_optimizado
    """Valida citas APA usando OpenAI con compatibilidad v1+ y v0.x"""
    prompt = f"""
Eres un experto en normas APA 7 y revisión académica. 

Analiza el siguiente segmento de texto académico ({num_segmento}/{total_segmentos}) y las referencias:

TAREAS:
1. Extrae todas las citas en formato APA que aparecen en el texto
2. Indica para cada cita si existe una referencia correspondiente (por autor y año)
3. Indica para cada referencia si está citada en este segmento
4. Detecta errores de formato o inconsistencias
5. Proporciona recomendaciones específicas de mejora

TEXTO DEL TFM (Segmento {num_segmento}/{total_segmentos}):
---
{texto_segmento}
---

REFERENCIAS APA:
---
{chr(10).join(referencias)}
---

Proporciona un análisis detallado en formato Markdown.
"""

    try:
        if compat == "v1":
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un experto en normas APA 7 y revisión académica."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.2
            )
            return response.choices[0].message.content
        else:  # v0.x
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un experto en normas APA 7 y revisión académica."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.2
            )
            return response["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"Error en validación OpenAI: {e}")
        return f"**ERROR**: No se pudo completar la validación del segmento {num_segmento}: {str(e)}"

def main():
    try:
        logger.info("=== INICIANDO VALIDACIÓN DE CITAS APA ===")
        
        # Crear cliente OpenAI
        compat, client = crear_cliente_openai()
        
        # Seleccionar archivo TFM primero
        tfm_file = select_file(["pdf", "docx", "txt"], "Selecciona el archivo del TFM (PDF, DOCX o TXT)")
        if not tfm_file:
            logger.error("No se seleccionó archivo de TFM.")
            return
        
        # Extraer texto según formato
        ext = os.path.splitext(tfm_file)[-1].lower()
        logger.info(f"Procesando archivo: {tfm_file} (formato: {ext})")
        
        if ext == ".pdf":
            cuerpo = extract_text_from_pdf(tfm_file)
        elif ext == ".docx":
            cuerpo = extract_text_from_docx(tfm_file)
        elif ext == ".txt":
            try:
                with open(tfm_file, encoding='utf-8') as f:
                    cuerpo = f.read()
                logger.info(f"Texto cargado: {len(cuerpo)} caracteres")
            except Exception as e:
                logger.error(f"Error leyendo archivo TXT: {e}")
                return
        else:
            logger.error("Formato no soportado.")
            return
        
        if not cuerpo.strip():
            logger.error("No se pudo extraer texto del archivo.")
            return
        
        # OPCIÓN 1: Referencias automáticas vs OPCIÓN 2: Referencias desde JSON
        print("\n" + "="*60)
        print("OPCIONES PARA OBTENER REFERENCIAS:")
        print("1. Extraer automáticamente del TFM (recomendado)")
        print("2. Cargar desde archivo JSON externo")
        print("="*60)
        
        while True:
            opcion = input("\nSelecciona opción (1 o 2): ").strip()
            if opcion in ["1", "2"]:
                break
            print("Por favor, selecciona 1 o 2")
        
        referencias = []
        
        if opcion == "1":
            # MODO AUTOMÁTICO: Extraer referencias del propio TFM
            logger.info("🤖 Modo automático: extrayendo referencias del TFM...")
            referencias = extraer_referencias_automaticamente(compat, client, cuerpo)
            
            if not referencias:
                logger.error("No se pudieron extraer referencias automáticamente.")
                print("\n❌ No se encontraron referencias. Intenta con la opción 2 (archivo JSON).")
                return
            
            # Guardar referencias extraídas para futura referencia
            json_path = guardar_referencias_extraidas(referencias, tfm_file)
            print(f"\n✅ {len(referencias)} referencias extraídas automáticamente")
            if json_path:
                print(f"📁 Referencias guardadas en: {json_path}")
        
        else:
            # MODO MANUAL: Cargar desde JSON
            logger.info("📂 Modo manual: cargando referencias desde JSON...")
            ref_file = select_file(["json"], "Selecciona el archivo de referencias APA (JSON)")
            if not ref_file:
                logger.error("No se seleccionó archivo de referencias.")
                return
            
            try:
                with open(ref_file, encoding='utf-8') as f:
                    referencias = json.load(f)
                logger.info(f"Referencias cargadas desde JSON: {len(referencias)} elementos")
            except Exception as e:
                logger.error(f"Error cargando referencias: {e}")
                return
        
        if not referencias:
            logger.error("No hay referencias para validar.")
            return
        
        # VALIDACIÓN INTEGRAL - UNA SOLA LLAMADA (MUCHO MÁS RÁPIDO)
        logger.info("🚀 Iniciando validación integral optimizada")
        resultado = validar_citas_integral(compat, client, cuerpo, referencias)
        
        # Consolidar resultados
        contenido_final = f"""# Validación de Citas APA - {Path(tfm_file).name}

**Archivo analizado**: {tfm_file}
**Referencias disponibles**: {len(referencias)}
**Método**: Validación integral optimizada
**Fecha**: {os.popen('date').read().strip()}

---

{resultado}

---

**✅ Validación completada exitosamente**
"""
        
        # Mostrar en consola
        print("\n" + "="*80)
        print("RESULTADO DE LA VALIDACIÓN")
        print("="*80)
        print(contenido_final)
        
        # Guardar resultado
        output_dir = os.path.dirname(tfm_file)
        base_name = os.path.splitext(os.path.basename(tfm_file))[0]
        md_path = os.path.join(output_dir, f"{base_name}_VALIDACION_CITAS.md")
        
        try:
            with open(md_path, "w", encoding="utf-8") as f:
                f.write(contenido_final)
            logger.info(f"Resultado guardado en: {md_path}")
            print(f"\n✅ El resultado también se ha guardado en: {md_path}")
        except Exception as e:
            logger.error(f"Error guardando archivo: {e}")
        
        logger.info("=== VALIDACIÓN COMPLETADA ===")
        
    except Exception as e:
        logger.error(f"Error general en main(): {e}")
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
