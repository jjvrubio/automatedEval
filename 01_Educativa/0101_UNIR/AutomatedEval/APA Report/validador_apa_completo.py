#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador APA Completo - Módulo especializado en análisis exhaustivo APA 7
================================================================================

Módulo que implementa validación completa de normas APA 7:
- Estructura y formato de referencias
- Validación de citas en texto
- Correspondencia citas-referencias
- Análisis de calidad bibliográfica
- Integración con evaluador TFM principal

Autor: JJVR
Versión: 1.0
Fecha: Octubre 2025
"""

import re
import logging
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class CitaEncontrada:
    """Representa una cita encontrada en el texto"""

    texto_cita: str
    autores: List[str]
    año: str
    pagina: str = ""
    tipo: str = ""  # 'directa', 'indirecta', 'multiple'
    posicion: int = 0


@dataclass
class ReferenciaAnalizada:
    """Representa una referencia analizada"""

    texto_completo: str
    autores: List[str]
    año: str
    titulo: str
    tipo: str  # 'articulo', 'libro', 'web', 'tesis'
    errores: List[str]
    calidad_apa: int  # 0-10


@dataclass
class ResultadoValidacionAPA:
    """Resultado completo de validación APA"""

    citas_encontradas: List[CitaEncontrada]
    referencias_analizadas: List[ReferenciaAnalizada]
    correspondencias: Dict[str, bool]
    referencias_huerfanas: List[str]
    citas_huerfanas: List[str]
    errores_formato: List[str]
    puntuacion_apa: int  # 0-100
    recomendaciones: List[str]


class ValidadorAPACompleto:
    """Validador completo de normas APA 7"""

    def __init__(self):
        self.patrones_cita = self._definir_patrones_cita()
        self.patrones_referencia = self._definir_patrones_referencia()
        self.reglas_apa = self._cargar_reglas_apa()

    def _definir_patrones_cita(self) -> Dict[str, str]:
        """Define patrones regex para detectar citas APA"""
        return {
            "cita_simple": r"\(([A-Za-záéíóúñü\s&,]+),?\s*(\d{4}[a-z]?)\)",
            "cita_pagina": r"\(([A-Za-záéíóúñü\s&,]+),?\s*(\d{4}[a-z]?),?\s*p\.?\s*(\d+)\)",
            "cita_multiple": r"\(([A-Za-záéíóúñü\s&,;]+),?\s*(\d{4}[a-z]?)[^)]*\)",
            "cita_et_al": r"\(([A-Za-záéíóúñü\s]+)\s+et\s+al\.?,?\s*(\d{4}[a-z]?)\)",
            "cita_narrativa": r"([A-Za-záéíóúñü\s]+)\s*\((\d{4}[a-z]?)\)",
        }

    def _definir_patrones_referencia(self) -> Dict[str, str]:
        """Define patrones para analizar referencias"""
        return {
            "articulo": r"([^.]+)\.\s*\((\d{4})\)\.\s*([^.]+)\.\s*([^,]+)",
            "libro": r"([^.]+)\.\s*\((\d{4})\)\.\s*([^.]+)\.\s*([^:]+):?\s*([^.]+)",
            "web": r"([^.]+)\.\s*\((\d{4})\)\.\s*([^.]+)\.\s*Recuperado de",
            "tesis": r"([^.]+)\.\s*\((\d{4})\)\.\s*([^.]+)\.\s*\(Tesis",
        }

    def _cargar_reglas_apa(self) -> Dict[str, Any]:
        """Carga reglas específicas APA 7"""
        return {
            "estructura_referencia": {
                "autor_obligatorio": True,
                "año_obligatorio": True,
                "titulo_obligatorio": True,
                "formato_año": r"\(\d{4}[a-z]?\)",
                "separador_autores": r"[,&]",
                "punto_final_obligatorio": True,
            },
            "formato_citas": {
                "parentesis_obligatorios": True,
                "separador_autor_año": r",\s*",
                "et_al_minimo": 3,  # 3+ autores requieren et al.
                "pagina_formato": r"p\.\s*\d+",
            },
            "errores_comunes": {
                "año_sin_parentesis": r"\b\d{4}\b(?!\))",
                "separador_incorrecto": r"[;:](?!\s)",
                "mayusculas_incorrectas": r"\b[a-z]+\s+[A-Z]",
                "espaciado_incorrecto": r"\(\s+|\s+\)",
                "punto_y_coma_incorrecto": r";\s*&",
            },
        }

    def validar_documento_completo(
        self, texto_completo: str, referencias: List[str]
    ) -> ResultadoValidacionAPA:
        """
        Validación completa de documento según normas APA 7
        """
        logger.info("🔍 Iniciando validación APA completa")

        # 1. Extraer y analizar citas
        citas = self._extraer_citas(texto_completo)
        logger.info(f"📖 Citas encontradas: {len(citas)}")

        # 2. Analizar referencias
        refs_analizadas = self._analizar_referencias(referencias)
        logger.info(f"📚 Referencias analizadas: {len(refs_analizadas)}")

        # 3. Verificar correspondencias
        correspondencias = self._verificar_correspondencias(citas, refs_analizadas)

        # 4. Identificar huérfanas
        refs_huerfanas, citas_huerfanas = self._identificar_huerfanas(
            citas, refs_analizadas
        )

        # 5. Detectar errores de formato
        errores_formato = self._detectar_errores_formato(texto_completo, referencias)

        # 6. Calcular puntuación APA
        puntuacion = self._calcular_puntuacion_apa(
            citas, refs_analizadas, correspondencias, errores_formato
        )

        # 7. Generar recomendaciones
        recomendaciones = self._generar_recomendaciones(
            citas, refs_analizadas, errores_formato
        )

        resultado = ResultadoValidacionAPA(
            citas_encontradas=citas,
            referencias_analizadas=refs_analizadas,
            correspondencias=correspondencias,
            referencias_huerfanas=refs_huerfanas,
            citas_huerfanas=citas_huerfanas,
            errores_formato=errores_formato,
            puntuacion_apa=puntuacion,
            recomendaciones=recomendaciones,
        )

        logger.info(f"✅ Validación APA completada - Puntuación: {puntuacion}/100")
        return resultado

    def _extraer_citas(self, texto: str) -> List[CitaEncontrada]:
        """Extrae todas las citas del texto usando patrones APA"""
        citas = []

        for tipo_cita, patron in self.patrones_cita.items():
            matches = re.finditer(patron, texto, re.IGNORECASE)
            for match in matches:
                if tipo_cita == "cita_pagina":
                    cita = CitaEncontrada(
                        texto_cita=match.group(0),
                        autores=[match.group(1).strip()],
                        año=match.group(2),
                        pagina=match.group(3) if len(match.groups()) > 2 else "",
                        tipo=tipo_cita,
                        posicion=match.start(),
                    )
                else:
                    cita = CitaEncontrada(
                        texto_cita=match.group(0),
                        autores=[match.group(1).strip()],
                        año=match.group(2),
                        tipo=tipo_cita,
                        posicion=match.start(),
                    )
                citas.append(cita)

        # Eliminar duplicados y ordenar por posición
        citas_unicas = {}
        for cita in citas:
            key = f"{cita.autores[0]}_{cita.año}"
            if key not in citas_unicas or cita.tipo == "cita_pagina":
                citas_unicas[key] = cita

        return sorted(citas_unicas.values(), key=lambda x: x.posicion)

    def _analizar_referencias(
        self, referencias: List[str]
    ) -> List[ReferenciaAnalizada]:
        """Analiza cada referencia según normas APA"""
        referencias_analizadas = []

        for ref_texto in referencias:
            if not ref_texto.strip():
                continue

            ref_analizada = ReferenciaAnalizada(
                texto_completo=ref_texto,
                autores=[],
                año="",
                titulo="",
                tipo="desconocido",
                errores=[],
                calidad_apa=0,
            )

            # Detectar tipo de referencia
            ref_analizada.tipo = self._detectar_tipo_referencia(ref_texto)

            # Extraer elementos básicos
            ref_analizada.autores, ref_analizada.año, ref_analizada.titulo = (
                self._extraer_elementos_referencia(ref_texto)
            )

            # Validar formato APA
            ref_analizada.errores = self._validar_formato_referencia(ref_texto)

            # Calcular calidad APA (0-10)
            ref_analizada.calidad_apa = self._calcular_calidad_referencia(ref_analizada)

            referencias_analizadas.append(ref_analizada)

        return referencias_analizadas

    def _detectar_tipo_referencia(self, referencia: str) -> str:
        """Detecta el tipo de referencia (artículo, libro, web, etc.)"""
        ref_lower = referencia.lower()

        if any(term in ref_lower for term in ["doi:", "doi.org", "journal", "revista"]):
            return "articulo"
        elif any(term in ref_lower for term in ["recuperado de", "http", "www", "url"]):
            return "web"
        elif "tesis" in ref_lower or "dissertation" in ref_lower:
            return "tesis"
        elif any(term in ref_lower for term in ["editorial", "ed.", "publisher"]):
            return "libro"
        else:
            return "desconocido"

    def _extraer_elementos_referencia(
        self, referencia: str
    ) -> Tuple[List[str], str, str]:
        """Extrae autores, año y título de una referencia"""
        autores = []
        año = ""
        titulo = ""

        # Buscar año en formato (YYYY)
        año_match = re.search(r"\((\d{4}[a-z]?)\)", referencia)
        if año_match:
            año = año_match.group(1)

        # Extraer autores (antes del año)
        if año_match:
            texto_autores = referencia[: año_match.start()].strip()
            # Separar autores por comas y &
            autores_raw = re.split(r"[,&]", texto_autores)
            autores = [
                autor.strip().rstrip(".") for autor in autores_raw if autor.strip()
            ]

        # Extraer título (después del año, antes del punto o journal)
        if año_match:
            resto_texto = referencia[año_match.end() :].strip()
            titulo_match = re.search(r"^\.?\s*([^.]+)", resto_texto)
            if titulo_match:
                titulo = titulo_match.group(1).strip()

        return autores, año, titulo

    def _validar_formato_referencia(self, referencia: str) -> List[str]:
        """Valida el formato APA de una referencia"""
        errores = []

        # Verificar punto final
        if not referencia.strip().endswith("."):
            errores.append("Falta punto final")

        # Verificar formato de año
        if not re.search(r"\(\d{4}[a-z]?\)", referencia):
            errores.append("Año no está en formato (YYYY)")

        # Verificar espaciado después de puntos
        if re.search(r"\.[A-Za-z]", referencia):
            errores.append("Falta espacio después de punto")

        # Verificar mayúsculas en título
        if re.search(r"\.\s*[a-z]", referencia):
            errores.append("Título no inicia con mayúscula")

        return errores

    def _calcular_calidad_referencia(self, referencia: ReferenciaAnalizada) -> int:
        """Calcula calidad APA de 0-10"""
        puntuacion = 10

        # Restar por errores
        puntuacion -= len(referencia.errores) * 2

        # Restar si faltan elementos esenciales
        if not referencia.autores:
            puntuacion -= 3
        if not referencia.año:
            puntuacion -= 3
        if not referencia.titulo:
            puntuacion -= 2

        return max(0, puntuacion)

    def _verificar_correspondencias(
        self, citas: List[CitaEncontrada], referencias: List[ReferenciaAnalizada]
    ) -> Dict[str, bool]:
        """Verifica correspondencia entre citas y referencias"""
        correspondencias = {}

        for cita in citas:
            clave_cita = f"{cita.autores[0]}_{cita.año}"
            correspondencias[clave_cita] = False

            for ref in referencias:
                if ref.autores and ref.año:
                    # Comparación flexible de autores
                    autor_cita = cita.autores[0].lower().strip()
                    autor_ref = ref.autores[0].lower().strip()

                    # Verificar si coinciden autor y año
                    if (
                        autor_cita in autor_ref or autor_ref in autor_cita
                    ) and cita.año == ref.año:
                        correspondencias[clave_cita] = True
                        break

        return correspondencias

    def _identificar_huerfanas(
        self, citas: List[CitaEncontrada], referencias: List[ReferenciaAnalizada]
    ) -> Tuple[List[str], List[str]]:
        """Identifica referencias y citas huérfanas"""
        refs_huerfanas = []
        citas_huerfanas = []

        # Referencias sin citar
        for ref in referencias:
            if ref.autores and ref.año:
                encontrada = False
                for cita in citas:
                    if ref.año == cita.año and any(
                        autor.lower() in ref.autores[0].lower()
                        for autor in cita.autores
                    ):
                        encontrada = True
                        break
                if not encontrada:
                    refs_huerfanas.append(f"{ref.autores[0]} ({ref.año})")

        # Citas sin referencia
        for cita in citas:
            encontrada = False
            for ref in referencias:
                if ref.año == cita.año and any(
                    cita.autores[0].lower() in autor.lower() for autor in ref.autores
                ):
                    encontrada = True
                    break
            if not encontrada:
                citas_huerfanas.append(f"{cita.autores[0]} ({cita.año})")

        return refs_huerfanas, citas_huerfanas

    def _detectar_errores_formato(
        self, texto: str, referencias: List[str]
    ) -> List[str]:
        """Detecta errores comunes de formato APA"""
        errores = []

        # Verificar errores en citas
        for patron_nombre, patron_regex in self.reglas_apa["errores_comunes"].items():
            matches = re.findall(patron_regex, texto)
            if matches:
                errores.append(f"{patron_nombre}: {len(matches)} ocurrencias")

        return errores

    def _calcular_puntuacion_apa(
        self,
        citas: List[CitaEncontrada],
        referencias: List[ReferenciaAnalizada],
        correspondencias: Dict[str, bool],
        errores: List[str],
    ) -> int:
        """Calcula puntuación APA global 0-100"""
        if not citas and not referencias:
            return 0

        puntuacion = 100

        # Penalizar por correspondencias fallidas
        if correspondencias:
            correspondencias_exitosas = sum(1 for v in correspondencias.values() if v)
            tasa_correspondencia = correspondencias_exitosas / len(correspondencias)
            puntuacion *= tasa_correspondencia

        # Penalizar por errores de formato
        puntuacion -= len(errores) * 5

        # Penalizar por calidad baja de referencias
        if referencias:
            calidad_promedio = sum(ref.calidad_apa for ref in referencias) / len(
                referencias
            )
            puntuacion *= calidad_promedio / 10

        return max(0, int(puntuacion))

    def _generar_recomendaciones(
        self,
        citas: List[CitaEncontrada],
        referencias: List[ReferenciaAnalizada],
        errores: List[str],
    ) -> List[str]:
        """Genera recomendaciones específicas para mejorar"""
        recomendaciones = []

        if errores:
            recomendaciones.append(
                f"Corregir {len(errores)} errores de formato detectados"
            )

        refs_baja_calidad = [ref for ref in referencias if ref.calidad_apa < 7]
        if refs_baja_calidad:
            recomendaciones.append(
                f"Revisar formato de {len(refs_baja_calidad)} referencias con calidad baja"
            )

        if len(citas) == 0:
            recomendaciones.append(
                "El documento carece de citas. Incluir respaldo bibliográfico."
            )
        elif len(citas) < 10:
            recomendaciones.append(
                "Considerar incluir más citas para mayor sustento teórico"
            )

        if len(referencias) == 0:
            recomendaciones.append("Incluir lista de referencias bibliográficas")

        return recomendaciones


def generar_reporte_apa_detallado(resultado: ResultadoValidacionAPA) -> str:
    """Genera reporte detallado en formato Markdown"""
    reporte = f"""# 📊 REPORTE APA COMPLETO

## 🎯 Puntuación General: {resultado.puntuacion_apa}/100

### 📈 Estadísticas Generales
- **Citas encontradas**: {len(resultado.citas_encontradas)}
- **Referencias analizadas**: {len(resultado.referencias_analizadas)}
- **Correspondencias exitosas**: {sum(1 for v in resultado.correspondencias.values() if v)}/{len(resultado.correspondencias)}
- **Referencias huérfanas**: {len(resultado.referencias_huerfanas)}
- **Citas huérfanas**: {len(resultado.citas_huerfanas)}

### 📖 Análisis de Citas
"""

    # Tabla de citas
    if resultado.citas_encontradas:
        reporte += "\n| Cita | Año | Tipo | ✓ Referencia |\n|------|-----|------|---------------|\n"
        for cita in resultado.citas_encontradas[:10]:  # Primeras 10
            clave = f"{cita.autores[0]}_{cita.año}"
            tiene_ref = "✅" if resultado.correspondencias.get(clave, False) else "❌"
            reporte += (
                f"| {cita.autores[0]} | {cita.año} | {cita.tipo} | {tiene_ref} |\n"
            )

    # Referencias problemáticas
    reporte += "\n### 📚 Análisis de Referencias\n"
    refs_problematicas = [
        ref for ref in resultado.referencias_analizadas if ref.errores
    ]
    if refs_problematicas:
        reporte += "\n**Referencias con errores:**\n"
        for ref in refs_problematicas[:5]:
            reporte += f"- {ref.autores[0] if ref.autores else 'Sin autor'} ({ref.año}): {', '.join(ref.errores)}\n"

    # Huérfanas
    if resultado.referencias_huerfanas:
        reporte += f"\n### 🔍 Referencias no citadas ({len(resultado.referencias_huerfanas)}):\n"
        for ref in resultado.referencias_huerfanas[:5]:
            reporte += f"- {ref}\n"

    if resultado.citas_huerfanas:
        reporte += (
            f"\n### 🔍 Citas sin referencia ({len(resultado.citas_huerfanas)}):\n"
        )
        for cita in resultado.citas_huerfanas[:5]:
            reporte += f"- {cita}\n"

    # Recomendaciones
    if resultado.recomendaciones:
        reporte += "\n### 💡 Recomendaciones:\n"
        for rec in resultado.recomendaciones:
            reporte += f"- {rec}\n"

    return reporte
