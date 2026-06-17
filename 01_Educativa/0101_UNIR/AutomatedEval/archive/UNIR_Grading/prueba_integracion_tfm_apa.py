#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prueba de Integración TFM-APA - Script de testing completo
================================================================================

Script para probar la integración completa del sistema TFM-APA:
- Análisis bibliográfico completo
- Validación APA local + OpenAI
- Integración con evaluación TFM
- Generación de reportes unificados

Uso:
    python prueba_integracion_tfm_apa.py [ruta_tfm] [universidad]

Autor: JJVR
Versión: 1.0
Fecha: Octubre 2025
"""

import sys
import logging
from pathlib import Path
import time

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("integracion_tfm_apa.log", encoding="utf-8"),
    ],
)

logger = logging.getLogger(__name__)

# Importar nuestros módulos
try:
    from integrador_tfm_apa import crear_integrador_por_universidad, CONFIGS_UNIVERSIDAD
    from validar_citas_openai import (
        extraer_texto_documento,
        seleccionar_archivo_con_dialogo,
    )
except ImportError as e:
    logger.error(f"❌ Error importando módulos: {e}")
    sys.exit(1)


def prueba_completa_integracion(archivo_tfm: str = None, universidad: str = "UNIR"):
    """Prueba completa del sistema integrado TFM-APA"""

    logger.info("🚀 INICIANDO PRUEBA DE INTEGRACIÓN TFM-APA")
    logger.info(f"📍 Universidad: {universidad}")

    inicio = time.time()

    try:
        # 1. Seleccionar archivo si no se proporciona
        if not archivo_tfm:
            logger.info("📁 Seleccionando archivo TFM...")
            archivo_tfm = seleccionar_archivo_con_dialogo()
            if not archivo_tfm:
                logger.error("❌ No se seleccionó archivo")
                return

        logger.info(f"📄 Archivo seleccionado: {Path(archivo_tfm).name}")

        # 2. Extraer texto del documento
        logger.info("📖 Extrayendo texto del documento...")
        texto_completo = extraer_texto_documento(archivo_tfm)

        if not texto_completo:
            logger.error("❌ No se pudo extraer texto del documento")
            return

        logger.info(f"📊 Texto extraído: {len(texto_completo):,} caracteres")

        # 3. Crear integrador para la universidad especificada
        logger.info(f"🔧 Configurando integrador para {universidad}...")
        integrador = crear_integrador_por_universidad(universidad)

        # Mostrar configuración
        config = integrador.config
        logger.info("⚙️ Configuración aplicada:")
        logger.info(f"   - Peso bibliográfico: {config.peso_bibliografico * 100:.0f}%")
        logger.info(f"   - Mínimo referencias: {config.minimo_referencias}")
        logger.info(f"   - Mínimo citas: {config.minimo_citas}")
        logger.info(f"   - Puntuación mínima APA: {config.puntuacion_minima_apa}/100")
        logger.info(
            f"   - Validación OpenAI: {'✅' if config.validacion_openai else '❌'}"
        )
        logger.info(f"   - Modo estricto: {'✅' if config.modo_estricto else '❌'}")

        # 4. Evaluar componente bibliográfico
        logger.info("📚 Evaluando componente bibliográfico...")
        resultado = integrador.evaluar_componente_bibliografico(
            texto_completo, archivo_tfm
        )

        # 5. Simular puntuación TFM base (en caso real vendría del evaluador principal)
        puntuacion_tfm_simulada = 82.5  # Ejemplo: Notable
        logger.info(f"🎯 Simulando puntuación TFM base: {puntuacion_tfm_simulada}/100")

        # 6. Integrar con evaluación TFM
        logger.info("🔗 Integrando con evaluación TFM...")
        resultado_final = integrador.integrar_con_tfm(
            resultado, puntuacion_tfm_simulada
        )

        # 7. Mostrar resultados clave
        logger.info("\n" + "=" * 60)
        logger.info("📊 RESULTADOS FINALES")
        logger.info("=" * 60)
        logger.info(f"🎯 Puntuación Final: {resultado_final.puntuacion_final:.1f}/100")
        logger.info(
            f"📚 Puntuación Bibliográfica: {resultado_final.puntuacion_bibliografica:.1f}/100"
        )
        logger.info(f"📖 Puntuación APA: {resultado_final.puntuacion_apa}/100")
        logger.info(
            f"✅ Cumple requisitos: {'SÍ' if resultado_final.cumple_requisitos_minimos else 'NO'}"
        )

        # Estadísticas rápidas
        stats = resultado_final.resultado_apa_detallado
        logger.info("📈 Estadísticas:")
        logger.info(f"   - Citas encontradas: {len(stats.citas_encontradas)}")
        logger.info(f"   - Referencias analizadas: {len(stats.referencias_analizadas)}")
        logger.info(f"   - Citas huérfanas: {len(stats.citas_huerfanas)}")
        logger.info(f"   - Referencias huérfanas: {len(stats.referencias_huerfanas)}")
        logger.info(f"   - Errores formato: {len(stats.errores_formato)}")

        # 8. Exportar resultados
        ruta_salida = (
            Path(archivo_tfm).parent / f"evaluacion_integrada_{universidad.lower()}"
        )
        logger.info(f"💾 Exportando resultados a: {ruta_salida}")
        integrador.exportar_resultados(resultado_final, str(ruta_salida))

        # 9. Mostrar recomendaciones principales
        if resultado_final.recomendaciones_bibliograficas:
            logger.info("\n📝 RECOMENDACIONES PRINCIPALES:")
            for i, rec in enumerate(
                resultado_final.recomendaciones_bibliograficas[:3], 1
            ):
                logger.info(f"   {i}. {rec}")

        # 10. Tiempo total
        tiempo_total = time.time() - inicio
        logger.info(f"\n⏱️ Tiempo total: {tiempo_total:.2f} segundos")

        # 11. Mostrar archivos generados
        logger.info("\n📁 Archivos generados:")
        logger.info(f"   - {ruta_salida}_reporte_integrado.md")
        logger.info(f"   - {ruta_salida}_datos.json")
        logger.info("   - integracion_tfm_apa.log")

        logger.info("\n✅ PRUEBA DE INTEGRACIÓN COMPLETADA EXITOSAMENTE")

        return resultado_final

    except Exception as e:
        logger.error(f"❌ Error en prueba de integración: {e}")
        logger.exception("Detalles del error:")
        return None


def mostrar_configuraciones_disponibles():
    """Muestra las configuraciones disponibles por universidad"""
    print("\n🏫 CONFIGURACIONES DISPONIBLES POR UNIVERSIDAD:")
    print("=" * 50)

    for universidad, config in CONFIGS_UNIVERSIDAD.items():
        print(f"\n📍 {universidad}:")
        print(f"   Peso bibliográfico: {config.peso_bibliografico * 100:.0f}%")
        print(f"   Mínimo referencias: {config.minimo_referencias}")
        print(f"   Mínimo citas: {config.minimo_citas}")
        print(f"   Puntuación mínima APA: {config.puntuacion_minima_apa}/100")
        print(f"   Validación OpenAI: {'✅' if config.validacion_openai else '❌'}")
        print(f"   Modo estricto: {'✅' if config.modo_estricto else '❌'}")


def main():
    """Función principal"""

    # Mostrar banner
    print("🎓 SISTEMA INTEGRADO TFM-APA v1.0")
    print("=" * 40)
    print("📚 Evaluación bibliográfica completa")
    print("🔗 Integración con evaluador TFM")
    print("📊 Reportes unificados")
    print("=" * 40)

    # Parsear argumentos
    archivo_tfm = None
    universidad = "UNIR"

    if len(sys.argv) > 1:
        if sys.argv[1] in ["--help", "-h"]:
            print("\nUso:")
            print("  python prueba_integracion_tfm_apa.py [archivo_tfm] [universidad]")
            print("\nArgumentos:")
            print("  archivo_tfm    Ruta al archivo TFM (opcional, se abrirá diálogo)")
            print("  universidad    UNIR, UAM, STANDARD (por defecto: UNIR)")
            print("\nEjemplos:")
            print("  python prueba_integracion_tfm_apa.py")
            print("  python prueba_integracion_tfm_apa.py mi_tfm.pdf UNIR")
            print("  python prueba_integracion_tfm_apa.py mi_tfm.docx UAM")
            mostrar_configuraciones_disponibles()
            return

        archivo_tfm = sys.argv[1]

        if len(sys.argv) > 2:
            universidad = sys.argv[2].upper()
            if universidad not in CONFIGS_UNIVERSIDAD:
                print(f"⚠️ Universidad '{universidad}' no reconocida. Usando UNIR.")
                universidad = "UNIR"

    # Mostrar configuración seleccionada
    print(f"\n🎯 Configuración seleccionada: {universidad}")
    if archivo_tfm:
        print(f"📄 Archivo: {archivo_tfm}")
    else:
        print("📁 Se abrirá diálogo para seleccionar archivo")

    # Ejecutar prueba
    resultado = prueba_completa_integracion(archivo_tfm, universidad)

    if resultado:
        print(
            f"\n🎉 Evaluación completada. Puntuación final: {resultado.puntuacion_final:.1f}/100"
        )
    else:
        print("\n❌ La evaluación no se pudo completar")


if __name__ == "__main__":
    main()
