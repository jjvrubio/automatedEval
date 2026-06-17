#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Integrador TFM-APA - Conexión entre evaluador TFM y validador APA
================================================================================

Módulo que integra el validador APA completo con el sistema de evaluación TFM:
- Análisis bibliográfico como componente de evaluación
- Puntuación APA integrada en rúbrica general
- Reporte unificado TFM + APA
- Configuración flexible para diferentes universidades

Autor: JJVR
Versión: 1.0
Fecha: Octubre 2025
"""

import json
import logging
from pathlib import Path
from typing import Dict, List
from dataclasses import dataclass

# Importar nuestros módulos
from validador_apa_completo import (
    ValidadorAPACompleto,
    ResultadoValidacionAPA,
    generar_reporte_apa_detallado,
)
from validar_citas_openai import (
    validar_citas_integral,
    extraer_referencias_automaticamente,
)

logger = logging.getLogger(__name__)


@dataclass
class ConfiguracionAPA:
    """Configuración para análisis APA según universidad"""

    peso_bibliografico: float = 0.20  # 20% del total TFM
    minimo_referencias: int = 15
    minimo_citas: int = 20
    puntuacion_minima_apa: int = 70
    validacion_openai: bool = True
    modo_estricto: bool = False
    tipos_referencia_requeridos: List[str] = None


@dataclass
class ResultadoIntegracion:
    """Resultado completo TFM + APA"""

    puntuacion_tfm_base: float
    puntuacion_apa: int
    puntuacion_bibliografica: float
    puntuacion_final: float
    resultado_apa_detallado: ResultadoValidacionAPA
    reporte_integrado: str
    recomendaciones_bibliograficas: List[str]
    cumple_requisitos_minimos: bool


class IntegradorTFMAPA:
    """Integrador principal TFM-APA"""

    def __init__(self, config: ConfiguracionAPA = None):
        self.config = config or ConfiguracionAPA()
        self.validador_apa = ValidadorAPACompleto()
        logger.info("🔗 Integrador TFM-APA inicializado")

    def evaluar_componente_bibliografico(
        self, texto_completo: str, archivo_tfm: str = None
    ) -> ResultadoIntegracion:
        """
        Evalúa el componente bibliográfico de un TFM

        Args:
            texto_completo: Contenido completo del TFM
            archivo_tfm: Ruta opcional al archivo TFM

        Returns:
            ResultadoIntegracion con análisis completo
        """
        logger.info("📚 Iniciando evaluación bibliográfica integrada")

        try:
            # 1. Extraer referencias automáticamente
            referencias = extraer_referencias_automaticamente(
                archivo_tfm if archivo_tfm else texto_completo
            )
            logger.info(f"📖 Referencias extraídas: {len(referencias)}")

            # 2. Validación APA completa (local)
            resultado_apa = self.validador_apa.validar_documento_completo(
                texto_completo, referencias
            )

            # 3. Validación OpenAI (opcional, más profunda)
            validacion_openai = None
            if self.config.validacion_openai:
                try:
                    validacion_openai = validar_citas_integral(
                        texto_completo, referencias
                    )
                    logger.info("🤖 Validación OpenAI completada")
                except Exception as e:
                    logger.warning(f"⚠️ Validación OpenAI falló: {e}")

            # 4. Combinar resultados y calcular puntuación bibliográfica
            puntuacion_bibliografica = self._calcular_puntuacion_bibliografica(
                resultado_apa, validacion_openai, len(referencias)
            )

            # 5. Verificar requisitos mínimos
            cumple_requisitos = self._verificar_requisitos_minimos(
                resultado_apa, len(referencias)
            )

            # 6. Generar recomendaciones específicas
            recomendaciones = self._generar_recomendaciones_bibliograficas(
                resultado_apa, len(referencias)
            )

            # 7. Crear resultado integrado (sin puntuación TFM base por ahora)
            resultado = ResultadoIntegracion(
                puntuacion_tfm_base=0.0,  # Se calculará externamente
                puntuacion_apa=resultado_apa.puntuacion_apa,
                puntuacion_bibliografica=puntuacion_bibliografica,
                puntuacion_final=0.0,  # Se calculará al integrar con TFM
                resultado_apa_detallado=resultado_apa,
                reporte_integrado="",  # Se generará después
                recomendaciones_bibliograficas=recomendaciones,
                cumple_requisitos_minimos=cumple_requisitos,
            )

            # 8. Generar reporte integrado
            resultado.reporte_integrado = self._generar_reporte_integrado(
                resultado, validacion_openai
            )

            logger.info(
                f"✅ Evaluación bibliográfica completada - Puntuación: {puntuacion_bibliografica:.1f}/100"
            )
            return resultado

        except Exception as e:
            logger.error(f"❌ Error en evaluación bibliográfica: {e}")
            raise

    def integrar_con_tfm(
        self, resultado_bibliografico: ResultadoIntegracion, puntuacion_tfm_base: float
    ) -> ResultadoIntegracion:
        """
        Integra la puntuación bibliográfica con la evaluación TFM general

        Args:
            resultado_bibliografico: Resultado del análisis bibliográfico
            puntuacion_tfm_base: Puntuación base del TFM (sin componente bibliográfico)

        Returns:
            ResultadoIntegracion actualizado con puntuación final
        """
        logger.info("🔗 Integrando puntuación bibliográfica con evaluación TFM")

        # Actualizar puntuación base
        resultado_bibliografico.puntuacion_tfm_base = puntuacion_tfm_base

        # Calcular puntuación final ponderada
        peso_tfm = 1.0 - self.config.peso_bibliografico
        peso_bibliografico = self.config.peso_bibliografico

        puntuacion_final = (
            puntuacion_tfm_base * peso_tfm
            + resultado_bibliografico.puntuacion_bibliografica * peso_bibliografico
        )

        resultado_bibliografico.puntuacion_final = puntuacion_final

        # Regenerar reporte con puntuación final
        resultado_bibliografico.reporte_integrado = self._generar_reporte_integrado(
            resultado_bibliografico
        )

        logger.info(f"🎯 Puntuación final integrada: {puntuacion_final:.1f}/100")
        return resultado_bibliografico

    def _calcular_puntuacion_bibliografica(
        self,
        resultado_apa: ResultadoValidacionAPA,
        validacion_openai: Dict = None,
        num_referencias: int = 0,
    ) -> float:
        """Calcula puntuación bibliográfica combinando múltiples factores"""

        # Base: puntuación APA local
        puntuacion_base = resultado_apa.puntuacion_apa

        # Bonificación por cantidad de referencias
        if num_referencias >= self.config.minimo_referencias:
            bonus_cantidad = min(
                10, (num_referencias - self.config.minimo_referencias) * 2
            )
        else:
            bonus_cantidad = -20  # Penalización fuerte por pocas referencias

        # Bonificación por calidad OpenAI (si disponible)
        bonus_openai = 0
        if validacion_openai and "analysis" in validacion_openai:
            try:
                # Extraer información de calidad del análisis OpenAI
                analisis = validacion_openai["analysis"]
                if "quality_score" in analisis:
                    bonus_openai = (analisis["quality_score"] - 70) * 0.5  # Normalizar
            except:
                pass

        # Penalización por modo estricto
        penalizacion_estricta = 0
        if self.config.modo_estricto:
            if len(resultado_apa.citas_huerfanas) > 0:
                penalizacion_estricta -= len(resultado_apa.citas_huerfanas) * 5
            if len(resultado_apa.referencias_huerfanas) > 0:
                penalizacion_estricta -= len(resultado_apa.referencias_huerfanas) * 3

        # Calcular puntuación final
        puntuacion_final = (
            puntuacion_base + bonus_cantidad + bonus_openai + penalizacion_estricta
        )

        return max(0, min(100, puntuacion_final))

    def _verificar_requisitos_minimos(
        self, resultado_apa: ResultadoValidacionAPA, num_referencias: int
    ) -> bool:
        """Verifica si se cumplen los requisitos mínimos bibliográficos"""

        requisitos = [
            num_referencias >= self.config.minimo_referencias,
            len(resultado_apa.citas_encontradas) >= self.config.minimo_citas,
            resultado_apa.puntuacion_apa >= self.config.puntuacion_minima_apa,
            len(resultado_apa.citas_huerfanas) == 0,  # No citas sin referencia
        ]

        if self.config.modo_estricto:
            requisitos.extend(
                [
                    len(resultado_apa.referencias_huerfanas)
                    <= 2,  # Máximo 2 referencias no citadas
                    len(resultado_apa.errores_formato) == 0,  # Sin errores de formato
                ]
            )

        return all(requisitos)

    def _generar_recomendaciones_bibliograficas(
        self, resultado_apa: ResultadoValidacionAPA, num_referencias: int
    ) -> List[str]:
        """Genera recomendaciones específicas para mejorar el componente bibliográfico"""
        recomendaciones = []

        # Cantidad de referencias
        if num_referencias < self.config.minimo_referencias:
            faltantes = self.config.minimo_referencias - num_referencias
            recomendaciones.append(
                f"📚 Incluir {faltantes} referencias adicionales (mínimo: {self.config.minimo_referencias})"
            )

        # Cantidad de citas
        if len(resultado_apa.citas_encontradas) < self.config.minimo_citas:
            faltantes = self.config.minimo_citas - len(resultado_apa.citas_encontradas)
            recomendaciones.append(
                f"📖 Incluir {faltantes} citas adicionales (mínimo: {self.config.minimo_citas})"
            )

        # Citas huérfanas (crítico)
        if resultado_apa.citas_huerfanas:
            recomendaciones.append(
                f"🚨 CRÍTICO: {len(resultado_apa.citas_huerfanas)} citas sin referencia correspondiente"
            )

        # Referencias huérfanas
        if resultado_apa.referencias_huerfanas:
            if len(resultado_apa.referencias_huerfanas) > 5:
                recomendaciones.append(
                    f"⚠️ {len(resultado_apa.referencias_huerfanas)} referencias no citadas - considerar citar o eliminar"
                )
            else:
                recomendaciones.append(
                    f"📝 {len(resultado_apa.referencias_huerfanas)} referencias no citadas - revisar necesidad"
                )

        # Calidad APA
        if resultado_apa.puntuacion_apa < self.config.puntuacion_minima_apa:
            recomendaciones.append(
                f"📐 Mejorar formato APA (actual: {resultado_apa.puntuacion_apa}/100, mínimo: {self.config.puntuacion_minima_apa}/100)"
            )

        # Errores específicos
        if resultado_apa.errores_formato:
            recomendaciones.append(
                f"🔧 Corregir {len(resultado_apa.errores_formato)} errores de formato APA"
            )

        # Diversidad de fuentes
        tipos_encontrados = set(
            ref.tipo for ref in resultado_apa.referencias_analizadas
        )
        if len(tipos_encontrados) < 3:
            recomendaciones.append(
                "🌐 Diversificar tipos de fuentes (artículos, libros, web, etc.)"
            )

        return recomendaciones

    def _generar_reporte_integrado(
        self, resultado: ResultadoIntegracion, validacion_openai: Dict = None
    ) -> str:
        """Genera reporte completo TFM + APA"""

        reporte = f"""# 📊 EVALUACIÓN TFM INTEGRADA - COMPONENTE BIBLIOGRÁFICO

## 🎯 Puntuaciones Globales
- **Puntuación TFM Base**: {resultado.puntuacion_tfm_base:.1f}/100
- **Puntuación Bibliográfica**: {resultado.puntuacion_bibliografica:.1f}/100
- **Puntuación Final**: {resultado.puntuacion_final:.1f}/100
- **Peso Bibliográfico**: {self.config.peso_bibliografico * 100:.0f}%

## ✅ Requisitos Mínimos
**Estado**: {"✅ CUMPLE" if resultado.cumple_requisitos_minimos else "❌ NO CUMPLE"}

### 📋 Checklist Bibliográfico:
- Referencias mínimas ({self.config.minimo_referencias}): {"✅" if len(resultado.resultado_apa_detallado.referencias_analizadas) >= self.config.minimo_referencias else "❌"} ({len(resultado.resultado_apa_detallado.referencias_analizadas)})
- Citas mínimas ({self.config.minimo_citas}): {"✅" if len(resultado.resultado_apa_detallado.citas_encontradas) >= self.config.minimo_citas else "❌"} ({len(resultado.resultado_apa_detallado.citas_encontradas)})
- Calidad APA mínima ({self.config.puntuacion_minima_apa}/100): {"✅" if resultado.resultado_apa_detallado.puntuacion_apa >= self.config.puntuacion_minima_apa else "❌"} ({resultado.resultado_apa_detallado.puntuacion_apa}/100)
- Sin citas huérfanas: {"✅" if len(resultado.resultado_apa_detallado.citas_huerfanas) == 0 else "❌"} ({len(resultado.resultado_apa_detallado.citas_huerfanas)} encontradas)

"""

        # Incluir reporte APA detallado
        reporte += generar_reporte_apa_detallado(resultado.resultado_apa_detallado)

        # Validación OpenAI si está disponible
        if validacion_openai:
            reporte += "\n## 🤖 Análisis OpenAI Adicional\n"
            if "summary" in validacion_openai:
                reporte += f"**Resumen**: {validacion_openai['summary']}\n\n"
            if "recommendations" in validacion_openai:
                reporte += "**Recomendaciones IA**:\n"
                for rec in validacion_openai["recommendations"][:3]:
                    reporte += f"- {rec}\n"

        # Recomendaciones bibliográficas
        if resultado.recomendaciones_bibliograficas:
            reporte += "\n## 💡 Recomendaciones Bibliográficas Prioritarias\n"
            for i, rec in enumerate(resultado.recomendaciones_bibliograficas[:5], 1):
                reporte += f"{i}. {rec}\n"

        # Impacto en calificación
        reporte += f"""
## 📈 Impacto en Calificación Final
- **Contribución bibliográfica**: {resultado.puntuacion_bibliografica * self.config.peso_bibliografico:.1f} puntos
- **Contribución TFM base**: {resultado.puntuacion_tfm_base * (1 - self.config.peso_bibliografico):.1f} puntos
- **Total**: {resultado.puntuacion_final:.1f}/100

### 🎓 Equivalencia Calificativa:
"""

        # Equivalencias según puntuación
        if resultado.puntuacion_final >= 90:
            reporte += "**SOBRESALIENTE** (9.0-10.0) 🏆\n"
        elif resultado.puntuacion_final >= 80:
            reporte += "**NOTABLE** (8.0-8.9) 🥈\n"
        elif resultado.puntuacion_final >= 70:
            reporte += "**BIEN** (7.0-7.9) 🥉\n"
        elif resultado.puntuacion_final >= 60:
            reporte += "**APROBADO** (6.0-6.9) ✅\n"
        else:
            reporte += "**SUSPENSO** (<6.0) ❌\n"

        return reporte

    def exportar_resultados(self, resultado: ResultadoIntegracion, ruta_salida: str):
        """Exporta resultados en múltiples formatos"""
        ruta_base = Path(ruta_salida).stem
        directorio = Path(ruta_salida).parent

        # 1. Reporte Markdown
        with open(
            directorio / f"{ruta_base}_reporte_integrado.md", "w", encoding="utf-8"
        ) as f:
            f.write(resultado.reporte_integrado)

        # 2. Datos JSON para procesamiento
        datos_json = {
            "puntuacion_final": resultado.puntuacion_final,
            "puntuacion_tfm_base": resultado.puntuacion_tfm_base,
            "puntuacion_bibliografica": resultado.puntuacion_bibliografica,
            "puntuacion_apa": resultado.puntuacion_apa,
            "cumple_requisitos": resultado.cumple_requisitos_minimos,
            "estadisticas": {
                "num_citas": len(resultado.resultado_apa_detallado.citas_encontradas),
                "num_referencias": len(
                    resultado.resultado_apa_detallado.referencias_analizadas
                ),
                "citas_huerfanas": len(
                    resultado.resultado_apa_detallado.citas_huerfanas
                ),
                "referencias_huerfanas": len(
                    resultado.resultado_apa_detallado.referencias_huerfanas
                ),
                "errores_formato": len(
                    resultado.resultado_apa_detallado.errores_formato
                ),
            },
            "recomendaciones": resultado.recomendaciones_bibliograficas,
            "timestamp": str(Path().cwd()),  # Placeholder para timestamp
        }

        with open(directorio / f"{ruta_base}_datos.json", "w", encoding="utf-8") as f:
            json.dump(datos_json, f, indent=2, ensure_ascii=False)

        logger.info(f"📁 Resultados exportados a {directorio}")


# Configuraciones predefinidas para diferentes universidades
CONFIGS_UNIVERSIDAD = {
    "UNIR": ConfiguracionAPA(
        peso_bibliografico=0.25,
        minimo_referencias=20,
        minimo_citas=25,
        puntuacion_minima_apa=75,
        validacion_openai=True,
        modo_estricto=True,
    ),
    "UAM": ConfiguracionAPA(
        peso_bibliografico=0.20,
        minimo_referencias=15,
        minimo_citas=20,
        puntuacion_minima_apa=70,
        validacion_openai=True,
        modo_estricto=False,
    ),
    "STANDARD": ConfiguracionAPA(
        peso_bibliografico=0.15,
        minimo_referencias=12,
        minimo_citas=15,
        puntuacion_minima_apa=65,
        validacion_openai=False,
        modo_estricto=False,
    ),
}


def crear_integrador_por_universidad(universidad: str = "STANDARD") -> IntegradorTFMAPA:
    """Factory para crear integrador según universidad"""
    config = CONFIGS_UNIVERSIDAD.get(universidad, CONFIGS_UNIVERSIDAD["STANDARD"])
    return IntegradorTFMAPA(config)


def main():
    """Función principal para ejecución directa del integrador"""
    print("🔗 INTEGRADOR TFM-APA")
    print("=" * 30)
    print("ℹ️  Este es un módulo de biblioteca.")
    print("📋 Para ejecutar pruebas, usa:")
    print("   python prueba_integracion_tfm_apa.py")
    print("")
    print("🏫 Configuraciones disponibles:")
    for universidad, config in CONFIGS_UNIVERSIDAD.items():
        print(
            f"   - {universidad}: {config.peso_bibliografico * 100:.0f}% peso bibliográfico"
        )
    print("")
    print("📚 Ejemplo de uso en código:")
    print("""
from integrador_tfm_apa import crear_integrador_por_universidad

# Crear integrador para UNIR
integrador = crear_integrador_por_universidad('UNIR')

# Evaluar componente bibliográfico
resultado = integrador.evaluar_componente_bibliografico(texto, archivo)

# Integrar con puntuación TFM
resultado_final = integrador.integrar_con_tfm(resultado, puntuacion_tfm)
    """)


if __name__ == "__main__":
    main()
