#!/usr/bin/env python3
"""
Ejemplos de Uso del Sistema de Validación de Referencias
======================================================

Este script demuestra diferentes formas de usar el sistema modular
de validación de referencias bibliográficas.
"""

import os
import sys
from pathlib import Path

# Añadir el directorio actual al path para importar módulos
sys.path.append(str(Path(__file__).parent))

try:
    from referencias_validator import (
        ExtractorReferencias, ValidadorReferencias, GeneradorInformes,
        EstiloCita, ReferenciaAnalizada, InformeValidacion
    )
    from utils_referencias import DetectorPatrones, LimpiadorTexto, AnalizadorComponentes
    from config_referencias import ESTILOS_CONFIGURACION, UMBRALES_VALIDACION
except ImportError as e:
    print(f"❌ Error importando módulos: {e}")
    print("Asegúrate de que todos los archivos estén en el mismo directorio")
    sys.exit(1)


def ejemplo_validacion_referencias_texto():
    """Ejemplo de validación de referencias desde texto directo"""
    print("📚 EJEMPLO 1: Validación de referencias desde texto")
    print("=" * 60)
    
    # Referencias de ejemplo (algunas correctas, otras con errores)
    referencias_ejemplo = [
        # APA correcto
        "García, J. M. (2023). Efectos del cambio climático en la biodiversidad marina. Revista de Ecología, 45(3), 123-145. https://doi.org/10.1038/eco2023.123",
        
        # APA con errores
        "MARTÍNEZ, ANTONIO (2022) INTELIGENCIA ARTIFICIAL EN EDUCACIÓN. TECNOLOGÍA EDUCATIVA, VOL. 12, 67-89.",
        
        # Referencia incompleta
        "Smith, J. Machine learning applications. 2021.",
        
        # Referencia web correcta
        "López, M. A. (2023). Guía completa de Python para ciencia de datos. DataScience Blog. https://www.datascienceblog.com/python-guide",
        
        # Libro con formato correcto
        "Pérez, R., & González, L. (2022). Metodologías de investigación cualitativa (3ª ed.). Editorial Académica."
    ]
    
    # Crear validador APA
    validador = ValidadorReferencias(EstiloCita.APA)
    
    referencias_analizadas = []
    print(f"Analizando {len(referencias_ejemplo)} referencias en formato APA...\n")
    
    for i, referencia in enumerate(referencias_ejemplo, 1):
        print(f"🔍 Referencia {i}:")
        print(f"   Texto: {referencia[:80]}{'...' if len(referencia) > 80 else ''}")
        
        # Analizar la referencia
        analisis = validador.validar_referencia(referencia)
        referencias_analizadas.append(analisis)
        
        # Mostrar resultados
        estado = "✅ VÁLIDA" if analisis.es_completa else "❌ CON ERRORES"
        print(f"   Estado: {estado}")
        print(f"   Puntuación: {analisis.puntuacion:.2f}/1.00")
        
        if analisis.errores:
            print(f"   Errores: {', '.join(analisis.errores[:2])}")
        
        print()
    
    # Estadísticas generales
    referencias_validas = sum(1 for ref in referencias_analizadas if ref.es_completa)
    puntuacion_promedio = sum(ref.puntuacion for ref in referencias_analizadas) / len(referencias_analizadas)
    
    print(f"📊 RESUMEN:")
    print(f"   Referencias válidas: {referencias_validas}/{len(referencias_ejemplo)}")
    print(f"   Puntuación promedio: {puntuacion_promedio:.2f}/1.00")
    print(f"   Porcentaje de cumplimiento: {(referencias_validas/len(referencias_ejemplo)*100):.1f}%")


def ejemplo_analisis_componentes():
    """Ejemplo de análisis detallado de componentes de referencias"""
    print("\n🔬 EJEMPLO 2: Análisis detallado de componentes")
    print("=" * 60)
    
    referencia_compleja = """García-López, J. M., Rodríguez, A. P., & Smith, K. L. (2023). 
    Machine learning applications in climate change prediction: A comprehensive review. 
    Nature Climate Change, 13(8), 456-472. https://doi.org/10.1038/nclimate2023.456"""
    
    print(f"📖 Referencia a analizar:")
    print(f"   {referencia_compleja}")
    print()
    
    # Análisis de componentes específicos
    print("🔍 ANÁLISIS DE COMPONENTES:")
    
    # Extraer autores
    autores = AnalizadorComponentes.extraer_autores(referencia_compleja, "apa")
    print(f"   👥 Autores detectados: {len(autores)}")
    for autor in autores:
        print(f"      - {autor}")
    
    # Extraer año
    anio = AnalizadorComponentes.extraer_anio(referencia_compleja, "apa")
    print(f"   📅 Año: {anio}")
    
    # Extraer título
    titulo = AnalizadorComponentes.extraer_titulo(referencia_compleja, "articulo")
    print(f"   📄 Título: {titulo}")
    
    # Extraer DOI
    doi = AnalizadorComponentes.extraer_doi(referencia_compleja)
    print(f"   🔗 DOI: {doi}")
    
    # Extraer URLs
    urls = AnalizadorComponentes.extraer_url(referencia_compleja)
    print(f"   🌐 URLs: {urls}")
    
    # Detectar tipo de publicación
    tipo = DetectorPatrones.identificar_tipo_referencia(referencia_compleja)
    print(f"   📚 Tipo detectado: {tipo}")


def ejemplo_comparacion_estilos():
    """Ejemplo de validación en diferentes estilos de cita"""
    print("\n📋 EJEMPLO 3: Comparación entre estilos de cita")
    print("=" * 60)
    
    # La misma referencia en diferentes estilos
    referencias_estilos = {
        "APA": "García, J. M. (2023). Machine learning in education. Journal of Educational Technology, 45(3), 123-145.",
        "IEEE": 'J. M. García, "Machine learning in education," Journal of Educational Technology, vol. 45, no. 3, pp. 123-145, 2023.',
        "MLA": 'García, Juan Manuel. "Machine learning in education." Journal of Educational Technology, vol. 45, no. 3, 2023, pp. 123-145.'
    }
    
    for estilo_nombre, referencia in referencias_estilos.items():
        print(f"🎯 Estilo {estilo_nombre}:")
        print(f"   Referencia: {referencia}")
        
        # Validar según el estilo correspondiente
        if estilo_nombre == "APA":
            validador = ValidadorReferencias(EstiloCita.APA)
        elif estilo_nombre == "IEEE":
            validador = ValidadorReferencias(EstiloCita.IEEE)
        else:  # MLA
            validador = ValidadorReferencias(EstiloCita.MLA)
        
        analisis = validador.validar_referencia(referencia)
        estado = "✅ VÁLIDA" if analisis.es_completa else "❌ CON ERRORES"
        
        print(f"   Estado: {estado}")
        print(f"   Puntuación: {analisis.puntuacion:.2f}/1.00")
        
        if analisis.errores:
            print(f"   Errores: {', '.join(analisis.errores)}")
        
        print()


def ejemplo_deteccion_idioma():
    """Ejemplo de detección automática de idioma"""
    print("\n🌐 EJEMPLO 4: Detección de idioma")
    print("=" * 60)
    
    textos_ejemplo = {
        "Español": """
        Referencias Bibliográficas
        
        García, J. (2023). Efectos del cambio climático. Revista de Ecología, 45(3), 123-145.
        López, M. (2022). Metodología de investigación. Editorial Universidad.
        """,
        
        "English": """
        References
        
        Smith, J. K. (2023). Climate change effects on biodiversity. Ecology Journal, 45(3), 123-145.
        Johnson, A. (2022). Research methodology handbook. Academic Press.
        """,
        
        "Mixto": """
        Referencias / References
        
        García, J. (2023). Análisis de datos. Data Analysis Journal, 12(1), 45-67.
        Smith, J. (2022). Machine learning applications. AI Review, 8(2), 123-134.
        """
    }
    
    for tipo, texto in textos_ejemplo.items():
        idioma_detectado = DetectorPatrones.detectar_idioma_documento(texto)
        print(f"📝 Documento {tipo}:")
        print(f"   Idioma detectado: {idioma_detectado}")
        
        # Extraer sección de referencias
        seccion_refs, posicion = DetectorPatrones.extraer_seccion_referencias(texto)
        if posicion != -1:
            print(f"   Sección encontrada en posición: {posicion}")
            print(f"   Primeros 100 caracteres: {seccion_refs[:100]}...")
        else:
            print("   ⚠️ No se encontró sección de referencias")
        
        print()


def ejemplo_generacion_informe():
    """Ejemplo de generación de informe completo"""
    print("\n📊 EJEMPLO 5: Generación de informe completo")
    print("=" * 60)
    
    # Simular análisis completo
    referencias_prueba = [
        "García, J. M. (2023). Inteligencia artificial en educación. Revista Educativa, 45(3), 123-145.",
        "SMITH, JOHN (2022) MACHINE LEARNING BASICS. TECH JOURNAL.",  # Con errores
        "López, A. (2021). Análisis de datos con Python. Editorial Técnica. https://doi.org/10.1234/example"
    ]
    
    validador = ValidadorReferencias(EstiloCita.APA)
    referencias_analizadas = []
    
    for referencia in referencias_prueba:
        analisis = validador.validar_referencia(referencia)
        referencias_analizadas.append(analisis)
    
    # Crear informe
    referencias_validas = sum(1 for ref in referencias_analizadas if ref.es_completa)
    puntuacion_promedio = sum(ref.puntuacion for ref in referencias_analizadas) / len(referencias_analizadas)
    
    informe = InformeValidacion(
        archivo_analizado="ejemplo_referencias.txt",
        estilo_validacion="APA",
        total_referencias=len(referencias_prueba),
        referencias_validas=referencias_validas,
        referencias_con_errores=len(referencias_prueba) - referencias_validas,
        puntuacion_promedio=puntuacion_promedio,
        referencias=referencias_analizadas,
        patrones_detectados=[],
        recomendaciones_generales=[
            "Revisar formato de autores según estándar APA",
            "Incluir DOI cuando esté disponible",
            "Verificar capitalización de títulos"
        ]
    )
    
    # Generar informes
    try:
        GeneradorInformes.generar_informe_markdown(informe, "ejemplo_informe.md")
        GeneradorInformes.generar_informe_json(informe, "ejemplo_informe.json")
        
        print("✅ Informes generados exitosamente:")
        print("   📄 ejemplo_informe.md")
        print("   📄 ejemplo_informe.json")
        
    except Exception as e:
        print(f"❌ Error generando informes: {e}")


def mostrar_configuracion_disponible():
    """Muestra la configuración disponible del sistema"""
    print("\n⚙️ CONFIGURACIÓN DEL SISTEMA")
    print("=" * 60)
    
    print("📋 Estilos de cita soportados:")
    for estilo, config in ESTILOS_CONFIGURACION.items():
        print(f"   • {estilo.upper()}: {config['nombre_completo']}")
    
    print(f"\n🎯 Umbrales de validación:")
    for umbral, valor in UMBRALES_VALIDACION.items():
        print(f"   • {umbral}: {valor}")
    
    print(f"\n📁 Archivos del sistema:")
    archivos_sistema = [
        "referencias_validator.py - Módulo principal",
        "config_referencias.py - Configuración",
        "utils_referencias.py - Utilidades",
        "requirements_referencias.txt - Dependencias"
    ]
    for archivo in archivos_sistema:
        print(f"   • {archivo}")


def main():
    """Función principal que ejecuta todos los ejemplos"""
    print("🚀 SISTEMA DE VALIDACIÓN DE REFERENCIAS - EJEMPLOS")
    print("=" * 80)
    print("Este script demuestra las capacidades del sistema modular")
    print("de validación de referencias bibliográficas.\n")
    
    try:
        # Ejecutar ejemplos
        ejemplo_validacion_referencias_texto()
        ejemplo_analisis_componentes()
        ejemplo_comparacion_estilos()
        ejemplo_deteccion_idioma()
        ejemplo_generacion_informe()
        mostrar_configuracion_disponible()
        
        print("\n🎉 EJEMPLOS COMPLETADOS EXITOSAMENTE")
        print("=" * 80)
        print("Para usar el sistema con tus propios archivos:")
        print("   python referencias_validator.py --archivo tu_documento.pdf --estilo apa")
        print("   python referencias_validator.py --archivo tu_tesis.docx --estilo ieee")
        
    except Exception as e:
        print(f"\n❌ Error ejecutando ejemplos: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()