#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Evaluador TFM - SafeFix

Objetivo:
- No tocar la versión en Git.
- Mantener `temperature=0.0` (determinismo), pero garantizar que el prompt
  incorpora elementos únicos del documento (hash, frases clave) para que
  respuestas idénticas no se deban a prompts idénticos por error.
- Limpiar variables globales usadas por el script original.
- Añadir logging detallado de selección/lectura/prompt-hash.
- Usar los YAML de configuración existentes.

Uso:
  /Users/juanjo/.../venv_arm64/bin/python Evaluador_TFM_SafeFix.py

"""

from __future__ import annotations

import os
import sys
import json
import hashlib
import time
import re
import subprocess
import plistlib
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

# Rutas relativas basadas en la ubicación del script
ROOT_AUTOMATED = Path(__file__).resolve().parents[2]
TFM_PACKAGE = ROOT_AUTOMATED / "TFM_Evaluator_Prompt_Package"

CONFIG_SISTEMA = TFM_PACKAGE / "configuracion_sistema_tfm.yaml"
CONFIG_PROMPT = TFM_PACKAGE / "TFM_Evaluator_Prompt.yaml"
CONFIG_CAPACIDADES = TFM_PACKAGE / "capacidades_rubricas.yaml"

# Carpeta para resultados propia (no sobrescribe original)
DIR_SELF = Path(__file__).resolve().parent
RESULTS_DIR = DIR_SELF / "resultados_safe"
RESULTS_DIR.mkdir(exist_ok=True)

UTF8_ENV = dict(os.environ)
UTF8_ENV.setdefault("LC_ALL", "en_US.UTF-8")
UTF8_ENV.setdefault("LANG", "en_US.UTF-8")


def _normalize_for_matching(text: str) -> str:
    if not text:
        return ""
    normalized = unicodedata.normalize("NFKD", str(text))
    filtered_chars: List[str] = []
    for ch in normalized:
        if unicodedata.combining(ch):
            continue
        if ch.isalnum() or ch.isspace():
            filtered_chars.append(ch)
    stripped = "".join(filtered_chars).lower()
    return " ".join(stripped.split())


def _prompt_config(config: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(config, dict):
        return {}
    prompt_cfg = config.get("prompt")
    if isinstance(prompt_cfg, dict):
        return prompt_cfg
    prompt_cfg = config.get("evaluador")
    if isinstance(prompt_cfg, dict):
        return prompt_cfg
    return {}


def _default_metodologias(config: Dict[str, Any]) -> Dict[str, Any]:
    prompt_cfg = _prompt_config(config)
    instrucciones_cfg = (
        prompt_cfg.get("instrucciones_metodologicas", {})
        if prompt_cfg
        else {}
    )
    defaults_cfg = instrucciones_cfg.get("defaults") if isinstance(instrucciones_cfg, dict) else {}
    if isinstance(defaults_cfg, dict) and defaults_cfg:
        return defaults_cfg

    return {
        "analisis_externo": (
            "Analiza si el TFM desarrolla de forma secuencial el PESTEL, las 5 Fuerzas "
            "de Porter, los grupos estrategicos, el ciclo de vida sectorial, el perfil "
            "de competidores, el estudio de mercado y clientes, la vigilancia tecnologica, "
            "el mapeo de stakeholders y la sintesis MEFE/DAFO. Evalua calidad de datos, "
            "uso de indicadores, hallazgos accionables y coherencia entre modelos."
        ),
        "analisis_interno": (
            "Comprueba si se realiza auditoria de recursos, cadena de valor, analisis "
            "financiero y organizacional, core competences, benchmarking interno y matriz "
            "VRIO. Valora profundidad, evidencia cuantitativa y si se vinculan hallazgos "
            "con la MEFI y conclusiones estrategicas."
        ),
        "procesos_fabricacion_operativos": {
            "generico": (
                "Verifica si el TFM aplica Lean, Six Sigma/DMAIC, Value Stream Mapping o "
                "Teoria de Restricciones para redisenyar procesos, eliminar desperdicios y "
                "estabilizar la operacion. Exige que se cuantifiquen tiempos de ciclo, "
                "inventario, capacidad y calidad, que se definan indicadores lider/rezagados "
                "y que se describa el sistema de seguimiento (tableros, responsables y "
                "cadencia). Evalua la coherencia entre diagnostico, contramedidas propuestas, "
                "gestion del cambio y mitigacion de riesgos operativos."
            ),
            "regulado": (
                "Desarrolla el analisis enfatizando la alineacion con GMP/FDA/EMA y marcos "
                "regulatorios afines. Conecta Lean, Six Sigma, VSM o TOC con ALCOA+, Quality Risk "
                "Management (ICH Q9/Q10), planes de validacion/revalidacion y control de cambios. "
                "Exige evidencias de trazabilidad documental, control de proveedores, stock de "
                "seguridad y programas de formacion obligatoria. Cita guias FDA, EMA, PIC/S y "
                "Quality by Design cuando falten salvaguardas regulatorias."
            ),
            "servicios_publicos": (
                "Evalua la mejora de procesos en Administraciones Publicas o servicios ciudadanos. "
                "Comprueba que se modelen flujos con SIPOC/BPMN, se midan tiempos de tramitacion, "
                "cargas de trabajo y cuellos de botella, y que se vinculen las acciones a la Ley "
                "39/2015, Ley 40/2015, ENS/ENI, proteccion de datos y principios de simplificacion "
                "administrativa. Solicita indicadores de experiencia ciudadana, ROI social, "
                "gobernanza y gestion del cambio en funcionarios (formacion, roles, cuadros de "
                "mando)."
            ),
            "fabricacion_continua": (
                "Analiza procesos de flujo continuo asegurando control estadistico, estabilidad "
                "de parametros criticos (temperatura, presion, velocidad) y monitorizacion en tiempo "
                "real. Exige indicadores de OEE, SPC, alarmas que activen planes CAPA y coordinacion "
                "con mantenimiento predictivo."
            ),
            "fabricacion_discreta": (
                "Verifica balanceo de linea, takt time, SMED, Kanban y gestion de cuellos. "
                "Exige datos de tiempo ciclo estandar, rendimiento por celda, retrabajos y capacidad "
                "instalada. Evalua integracion con plan maestro y digitalizacion (MES, Andon, "
                "trazabilidad de componentes)."
            ),
            "cadena_suministro": (
                "Conecta la mejora operativa con plan maestro, S&OP, inventarios y gestion de demanda. "
                "Pide evaluar sincronizacion proveedor-planta-cliente, politicas de stock, buffers "
                "dinamicos y mitigacion de riesgos de abastecimiento."
            ),
            "logistica": (
                "Relaciona la intervencion con layout de almacenes, slotting, productividad pick-pack, "
                "uso de WMS/TMS y seguridad operativa. Revisa analisis de tiempos, capacidad por franja "
                "y uso de indicadores OTIF, fill-rate y coste por envio."
            ),
            "distribucion": (
                "Evalua la coherencia del redisenyo con la gestion de canales, estrategias omnicanal y "
                "promesas de servicio. Solicita indicadores de nivel de servicio, coste por canal, "
                "devoluciones y experiencia cliente."
            ),
        },
        "procesos_logisticos_cadena_suministro": {
            "generico": (
                "Analiza si se utilizan marcos SCOR, analisis ABC de inventarios y diagnostico de "
                "ultima milla para priorizar mejoras en la cadena de suministro y los KPI logisticos."
            ),
            "cadena_suministro": (
                "Comprueba la integracion S&OP, planeacion de demanda, segmentacion ABC/XYZ y diseno de "
                "red (nodos, capacidad, costos). Exige simulaciones de escenarios, planes de contingencia "
                "y metricas de resiliencia."
            ),
            "logistica": (
                "Evalua layout, slotting, uso de WMS/TMS, productividades pick-pack, dimensionamiento de "
                "flota y control OTIF. Pide evidencia de analisis de capacidad, tiempos muertos y "
                "estrategias de cross-docking o parcel hubs."
            ),
            "distribucion": (
                "Examina la gestion de canales (retail, B2B, ecommerce), acuerdos de nivel de servicio, "
                "ultima milla y devoluciones. Solicita cuadros de mando por canal, margen contribucion, "
                "fill-rate y estrategias omnicanal."
            ),
        },
        "procesos_administrativos_servicios": (
            "Comprueba si los procesos administrativos o de servicio se modelan con "
            "SIPOC, BPMN o swimlanes, se cuantifican tiempos de ciclo y se plantean "
            "indicadores de servicio tras el redisenyo."
        ),
        "procesos_causa_raiz": (
            "Revisa si se mapean procesos y causas raiz con SIPOC, Ishikawa, Pareto o "
            "FMEA, y si se priorizan acciones con datos cuantificados."
        ),
        "analisis_financiero": (
            "Exige un modelo financiero con flujo de caja descontado, VAN, TIR, payback, "
            "ROI, ratio beneficio/coste y coste total de propiedad (TCO). Solicita "
            "documentar supuestos de inflacion, estructura de financiacion y analisis de "
            "sensibilidad con escenarios base/optimista/pesimista."
        ),
    }


DEFAULT_DOMAIN_CONFIG: Dict[str, Any] = {
    "orden_prioridad": ["generico"],
    "definiciones": {
        "generico": {
            "keywords": [
                "lean",
                "six sigma",
                "dmaic",
                "kaizen",
                "procesos",
            ],
            "alias": [
                "operaciones_genericas",
                "operaciones",
            ],
        },
    },
}


def _domain_config(config: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    base_config = {
        "orden_prioridad": list(
            DEFAULT_DOMAIN_CONFIG.get("orden_prioridad", [])
        ),
        "definiciones": {
            clave: dict(valor)
            for clave, valor in DEFAULT_DOMAIN_CONFIG.get("definiciones", {}).items()
            if isinstance(valor, dict)
        },
    }

    prompt_cfg = _prompt_config(config or {})
    dominios_cfg = (
        prompt_cfg.get("dominios_operativos", {}) if prompt_cfg else {}
    )
    if isinstance(dominios_cfg, dict):
        prioridad_cfg = dominios_cfg.get("orden_prioridad")
        if isinstance(prioridad_cfg, list) and prioridad_cfg:
            base_config["orden_prioridad"] = [
                str(item).strip().lower().replace(" ", "_")
                for item in prioridad_cfg
                if str(item).strip()
            ]

        definiciones_cfg = dominios_cfg.get("definiciones")
        if isinstance(definiciones_cfg, dict):
            for clave, valor in definiciones_cfg.items():
                if not isinstance(valor, dict):
                    continue
                clave_norm = str(clave).strip().lower().replace(" ", "_")
                destino = base_config["definiciones"].setdefault(clave_norm, {})
                for attr, dato in valor.items():
                    if attr == "alias" and isinstance(dato, (list, tuple, set)):
                        existentes = destino.get("alias", [])
                        combinados = list(existentes) if isinstance(existentes, list) else []
                        for item in dato:
                            if item:
                                combinados.append(item)
                        destino["alias"] = list(dict.fromkeys(combinados))
                    else:
                        destino[attr] = dato

    for clave, datos in list(base_config["definiciones"].items()):
        if not isinstance(datos, dict):
            datos = {}
            base_config["definiciones"][clave] = datos
        alias_cfg = datos.get("alias", [])
        alias_normalizados: set[str] = set()
        if isinstance(alias_cfg, (list, tuple, set)):
            for item in alias_cfg:
                if not item:
                    continue
                alias_normalizados.add(
                    str(item).strip().lower().replace(" ", "_")
                )
        if clave == "generico":
            alias_normalizados.update({"operaciones_genericas", "operaciones"})
        datos["_alias_normalizados"] = alias_normalizados

    return base_config


def _normalizar_entorno(
    dominio: Optional[str], config: Optional[Dict[str, Any]] = None
) -> str:
    if not dominio:
        return "generico"

    dominio_norm = str(dominio).strip().lower().replace(" ", "_")
    if not dominio_norm:
        return "generico"

    dominio_cfg = _domain_config(config)
    definiciones = dominio_cfg.get("definiciones", {})

    if dominio_norm in definiciones:
        return "generico" if dominio_norm == "operaciones_genericas" else dominio_norm

    for clave, datos in definiciones.items():
        if not isinstance(datos, dict):
            continue
        alias_set = datos.get("_alias_normalizados") or set()
        if dominio_norm in alias_set:
            return "generico" if clave == "operaciones_genericas" else clave

    if dominio_norm in {"operaciones_genericas", "operaciones"}:
        return "generico"

    return "generico"

def _texto_operaciones_por_entorno(
    dominio: Optional[str], fuente: Optional[Any] = None, config: Optional[Dict[str, Any]] = None
) -> str:
    dominio_norm = _normalizar_entorno(dominio, config)

    if isinstance(fuente, dict):
        claves_a_probar = [dominio_norm]
        if dominio_norm != "generico":
            claves_a_probar.append("generico")
        else:
            claves_a_probar.append("operaciones_genericas")
        claves_a_probar.append("default")

        for clave in claves_a_probar:
            if clave and clave in fuente:
                texto_dict = fuente.get(clave)
                if texto_dict:
                    return str(texto_dict).strip()

    if isinstance(fuente, str) and fuente.strip():
        return fuente.strip()

    dominio_cfg = _domain_config(config)
    definiciones = dominio_cfg.get("definiciones", {})
    texto_por_defecto = str(
        definiciones.get(dominio_norm, {}).get("texto_operaciones")
        or definiciones.get("generico", {}).get("texto_operaciones")
        or ""
    ).strip()
    return texto_por_defecto


def _filtrar_palabras_operaciones(
    palabras: Optional[List[str]], dominio: Optional[str], config: Optional[Dict[str, Any]] = None
) -> List[str]:
    if not palabras:
        return []
    dominio_norm = _normalizar_entorno(dominio, config)
    if dominio_norm == "regulado":
        return [p for p in palabras if p]
    dominio_cfg = _domain_config(config)
    definiciones = dominio_cfg.get("definiciones", {})
    regulado_cfg = definiciones.get("regulado", {})
    palabras_fuente = regulado_cfg.get("keywords", [])
    if not isinstance(palabras_fuente, (list, tuple, set)):
        palabras_fuente = []
    palabras_regulado = {
        _normalize_for_matching(p)
        for p in palabras_fuente
        if p
    }
    filtradas: List[str] = []
    vistos: set[str] = set()
    for palabra in palabras:
        if not palabra:
            continue
        norm = _normalize_for_matching(palabra)
        if norm in palabras_regulado:
            continue
        if palabra in vistos:
            continue
        vistos.add(palabra)
        filtradas.append(palabra)
    return filtradas


def _ajustar_comentario_metodologico(
    clave: str,
    comentario_original: str,
    dominio: Optional[str],
    detectado: bool,
    config: Optional[Dict[str, Any]] = None,
) -> str:
    if clave != "procesos_fabricacion_operativos":
        return comentario_original
    dominio_norm = _normalizar_entorno(dominio, config)
    dominio_cfg = _domain_config(config)
    definiciones = dominio_cfg.get("definiciones", {})
    comentarios_cfg = definiciones.get(dominio_norm, {}).get("comentario_operaciones")
    if detectado:
        comentario = (
            comentarios_cfg.get("detectado")
            if isinstance(comentarios_cfg, dict)
            else None
        )
        if comentario:
            return str(comentario)
    else:
        comentario = (
            comentarios_cfg.get("falta")
            if isinstance(comentarios_cfg, dict)
            else None
        )
        if comentario:
            return str(comentario)

    # Fallbacks: utilizar la configuración genérica si existe, o el comentario original
    generico_cfg = definiciones.get("generico", {}).get("comentario_operaciones")
    if isinstance(generico_cfg, dict):
        comentario = generico_cfg.get("detectado" if detectado else "falta")
        if comentario:
            return str(comentario)

    return comentario_original


def _ajustar_estado_por_entorno(
    clave: str,
    estado: Optional[Dict[str, Any]],
    dominio: Optional[str],
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    if not isinstance(estado, dict):
        return {}
    ajustado = dict(estado)
    if clave != "procesos_fabricacion_operativos":
        return ajustado
    ajustado["palabras_encontradas"] = _filtrar_palabras_operaciones(
        ajustado.get("palabras_encontradas"), dominio, config
    )
    ajustado["palabras_faltantes"] = _filtrar_palabras_operaciones(
        ajustado.get("palabras_faltantes"), dominio, config
    )
    ajustado["comentario_evaluacion"] = _ajustar_comentario_metodologico(
        clave,
        str(ajustado.get("comentario_evaluacion", "")),
        dominio,
        True,
        config,
    )
    ajustado["comentario_falta"] = _ajustar_comentario_metodologico(
        clave,
        str(ajustado.get("comentario_falta", "")),
        dominio,
        False,
        config,
    )
    return ajustado


def _inferir_entorno_procesos(
    texto: Optional[str],
    metadata_estado: Optional[Dict[str, Dict[str, Any]]] = None,
    config: Optional[Dict[str, Any]] = None,
) -> str:
    texto_norm = _normalize_for_matching(texto) if texto else ""
    metadata_estado = metadata_estado or {}
    dominio_cfg = _domain_config(config)
    definiciones = dominio_cfg.get("definiciones", {})
    prioridad = dominio_cfg.get("orden_prioridad", [])

    keywords_normalizados: Dict[str, set[str]] = {}
    for dominio, datos in definiciones.items():
        if not isinstance(datos, dict):
            continue
        palabras = datos.get("keywords", [])
        if not isinstance(palabras, (list, tuple, set)):
            continue
        keywords_normalizados[dominio] = {
            _normalize_for_matching(p)
            for p in palabras
            if p
        }

    metadata_detectada: Dict[str, set[str]] = {}
    for clave, estado in metadata_estado.items():
        if not isinstance(estado, dict) or not estado.get("detectado"):
            continue
        encontrados = estado.get("palabras_encontradas") or []
        metadata_detectada[clave] = {
            _normalize_for_matching(p)
            for p in encontrados
            if p
        }

    candidatos: set[str] = set()
    for dominio, datos in definiciones.items():
        if not isinstance(datos, dict):
            continue

        coincidencia = False
        keywords = keywords_normalizados.get(dominio, set())
        if texto_norm and keywords:
            for palabra_norm in keywords:
                if palabra_norm and palabra_norm in texto_norm:
                    coincidencia = True
                    break

        if not coincidencia:
            metadata_keys = datos.get("metadata_detectada", [])
            if isinstance(metadata_keys, (list, tuple, set)):
                for clave in metadata_keys:
                    palabras_encontradas = metadata_detectada.get(str(clave))
                    if not palabras_encontradas:
                        continue
                    requeridas = datos.get("palabras_metadata", [])
                    if isinstance(requeridas, (list, tuple, set)) and requeridas:
                        for palabra in requeridas:
                            palabra_norm = _normalize_for_matching(palabra)
                            if (
                                palabra_norm
                                and palabra_norm in palabras_encontradas
                            ):
                                coincidencia = True
                                break
                    else:
                        coincidencia = True
                    if coincidencia:
                        break

        if coincidencia:
            candidatos.add(dominio)

    if candidatos:
        for dominio in prioridad:
            if dominio in candidatos:
                return _normalizar_entorno(dominio, config)
        dominio_elegido = next(iter(candidatos))
        return _normalizar_entorno(dominio_elegido, config)

    # Fallback heuristics conservan compatibilidad con configuraciones previas
    keywords_regulado = keywords_normalizados.get("regulado", set())
    keywords_servicios = keywords_normalizados.get("servicios_publicos", set())
    keywords_generico = keywords_normalizados.get("operaciones_genericas") or (
        keywords_normalizados.get("generico") or set()
    )

    estado_fab = metadata_estado.get("procesos_fabricacion_operativos")
    if estado_fab and estado_fab.get("detectado"):
        encontrados = {
            _normalize_for_matching(p)
            for p in estado_fab.get("palabras_encontradas", [])
            if p
        }
        if keywords_regulado and (encontrados & keywords_regulado):
            return "regulado"

    if texto_norm and keywords_regulado and any(
        term and term in texto_norm for term in keywords_regulado
    ):
        return "regulado"

    if texto_norm and keywords_servicios and any(
        term and term in texto_norm for term in keywords_servicios
    ):
        return "servicios_publicos"

    estado_admin = metadata_estado.get("procesos_administrativos_servicios")
    if estado_admin and estado_admin.get("detectado") and not (
        estado_fab and estado_fab.get("detectado")
    ):
        return "servicios_publicos"

    if estado_fab and estado_fab.get("detectado"):
        return "generico"

    if texto_norm and keywords_generico and any(
        term and term in texto_norm for term in keywords_generico
    ):
        return "generico"

    return "generico"


def _obtener_texto_metodologia(
    clave: str,
    metodologias_cfg: Dict[str, Any],
    defaults: Dict[str, Any],
    dominio_operativo: Optional[str],
    config: Optional[Dict[str, Any]] = None,
) -> str:
    override = (
        metodologias_cfg.get(clave)
        if isinstance(metodologias_cfg, dict)
        else None
    )
    if clave == "procesos_fabricacion_operativos":
        base_dict: Dict[str, Any] = {}
        default_val = defaults.get(clave)
        if isinstance(default_val, dict):
            base_dict.update(default_val)

        if isinstance(override, dict):
            base_dict.update({str(k): v for k, v in override.items()})
            return _texto_operaciones_por_entorno(dominio_operativo, base_dict, config)

        if override is not None:
            return _texto_operaciones_por_entorno(dominio_operativo, override, config)

        if base_dict:
            return _texto_operaciones_por_entorno(dominio_operativo, base_dict, config)

        return _texto_operaciones_por_entorno(dominio_operativo, default_val, config)

    if isinstance(override, dict):
        dominio_norm = _normalizar_entorno(dominio_operativo, config)
        texto = (
            override.get(dominio_norm)
            or override.get("generico")
            or override.get("default")
        )
        if texto:
            return str(texto).strip()
    elif isinstance(override, str) and override.strip():
        return override.strip()

    default_val = defaults.get(clave)
    if isinstance(default_val, dict):
        dominio_norm = _normalizar_entorno(dominio_operativo, config)
        texto = (
            default_val.get(dominio_norm)
            or default_val.get("generico")
            or default_val.get("default")
        )
        if texto:
            return str(texto).strip()
    elif isinstance(default_val, str):
        return default_val

    return ""

def _category_display_names(config: Dict[str, Any]) -> Dict[str, str]:
    prompt_cfg = _prompt_config(config)
    resultado: Dict[str, str] = {}
    if prompt_cfg:
        categorias_cfg = prompt_cfg.get("categorias", {})
        display_cfg = (
            categorias_cfg.get("display_names")
            if isinstance(categorias_cfg, dict)
            else {}
        )
        if isinstance(display_cfg, dict):
            for clave, valor in display_cfg.items():
                if clave is None or valor is None:
                    continue
                clave_str = str(clave)
                resultado[clave_str] = str(valor)
        if resultado:
            return resultado

    candidatos: List[str] = []
    if prompt_cfg:
        estructura_cfg = prompt_cfg.get("estructura_superior", {})
        if isinstance(estructura_cfg, dict):
            keywords_cfg = estructura_cfg.get("keywords_por_categoria", {})
            if isinstance(keywords_cfg, dict):
                for clave in keywords_cfg.keys():
                    if clave is not None:
                        candidatos.append(str(clave))

    nombres: Dict[str, str] = {}
    for clave in candidatos:
        clave_norm = str(clave).strip()
        if not clave_norm:
            continue
        nombres[clave_norm] = clave_norm.replace("_", " ").strip().capitalize()
    return nombres


def _criterio_extendido_instrucciones(config: Dict[str, Any]) -> Dict[str, str]:
    prompt_cfg = _prompt_config(config)
    if prompt_cfg:
        categorias_cfg = prompt_cfg.get("categorias", {})
        instrucciones_cfg = (
            categorias_cfg.get("instrucciones_criterio_extendido")
            if isinstance(categorias_cfg, dict)
            else {}
        )
        if isinstance(instrucciones_cfg, dict) and instrucciones_cfg:
            result: Dict[str, str] = {}
            for clave, valor in instrucciones_cfg.items():
                if clave is None or valor is None:
                    continue
                result[str(clave)] = str(valor)
            if result:
                return result
    return {}


def _presentar_metodologia(clave: str) -> str:
    if not clave:
        return ""
    texto = clave.replace("_", " ").strip()
    if not texto:
        return ""
    return texto.capitalize()


def _clasificar_criterio_extendido(criterio: str) -> str:
    crit = (criterio or "").lower()
    if any(word in crit for word in ["formato", "lenguaje", "estilo"]):
        return "formato"
    if any(word in crit for word in ["portada", "resumen", "abstract", "índice", "indice"]):
        return "portada"
    if any(word in crit for word in ["introdu", "objetivo", "justificacion", "justificación"]):
        return "introduccion"
    if any(word in crit for word in ["estructura", "apartados", "contenido"]):
        return "estructura"
    if "conclus" in crit:
        return "conclusiones"
    if any(word in crit for word in ["limitacion", "amenaza", "riesgo"]):
        return "limitaciones"
    if any(word in crit for word in ["referencia", "bibliograf", "fuente"]):
        return "referencias"
    if any(word in crit for word in ["proyecto", "solucion", "solución", "desarrollo"]):
        return "proyecto"
    return "general"


def _segmentar_capitulos_superiores(texto: str) -> List[Dict[str, Any]]:
    if not texto:
        return []
    lines = texto.splitlines()
    offsets: List[int] = []
    position = 0
    for line in lines:
        offsets.append(position)
        position += len(line) + 1
    pattern = re.compile(r"^\s*(\d+)\.\s+(.+)$")
    secciones: List[Dict[str, Any]] = []
    for idx, line in enumerate(lines):
        match = pattern.match(line)
        if not match:
            continue
        numero = match.group(1).strip()
        titulo = match.group(2).strip().rstrip(". ")
        secciones.append(
            {
                "numero": numero,
                "titulo": titulo,
                "titulo_norm": _normalize_for_matching(titulo),
                "start": offsets[idx],
            }
        )

    if not secciones:
        return []

    total_len = len(texto)
    for idx, seccion in enumerate(secciones):
        start = seccion.get("start", 0)
        end = secciones[idx + 1]["start"] if idx + 1 < len(secciones) else total_len
        seccion["texto"] = texto[start:end].strip()
    return secciones


def _mapear_secciones_por_categoria(
    texto: str,
    config: Dict[str, Any],
    rubrica_activa: Optional[str],
) -> Tuple[Dict[str, str], List[Dict[str, Any]]]:
    secciones = _segmentar_capitulos_superiores(texto)
    prompt_cfg = _prompt_config(config)
    estructura_cfg = (
        prompt_cfg.get("estructura_superior", {})
        if prompt_cfg
        else {}
    )
    keywords_cfg = (
        estructura_cfg.get("keywords_por_categoria", {})
        if isinstance(estructura_cfg, dict)
        else {}
    )
    mapeo_por_rubrica = (
        estructura_cfg.get("mapeo_por_rubrica", {})
        if isinstance(estructura_cfg, dict)
        else {}
    )
    rubrica_norm = _normalize_for_matching(rubrica_activa) if rubrica_activa else ""
    mapping_cfg = {}
    if isinstance(mapeo_por_rubrica, dict):
        if rubrica_norm:
            for clave, valores in mapeo_por_rubrica.items():
                clave_norm = _normalize_for_matching(clave)
                if clave_norm and rubrica_norm == clave_norm:
                    mapping_cfg = valores if isinstance(valores, dict) else {}
                    break
        if not mapping_cfg:
            mapping_cfg = mapeo_por_rubrica.get("default", {}) if isinstance(mapeo_por_rubrica.get("default"), dict) else {}

    mapping: Dict[str, List[str]] = {}

    if isinstance(keywords_cfg, dict):
        for alias, keywords in keywords_cfg.items():
            if isinstance(keywords, (list, tuple)):
                mapping[str(alias)] = [str(k) for k in keywords if k]

    if isinstance(mapping_cfg, dict):
        for alias, keywords in mapping_cfg.items():
            if isinstance(keywords, (list, tuple)):
                mapping[str(alias)] = [str(k) for k in keywords if k]

    if not mapping:
        for categoria in _category_display_names(config).keys():
            mapping[categoria] = []
        if not mapping:
            mapping["general"] = []

    resultado: Dict[str, str] = {}
    if not secciones:
        resultado["general"] = texto
        return resultado, secciones

    for alias, keywords in mapping.items():
        if not keywords:
            continue
        keywords_norm = [
            _normalize_for_matching(keyword) for keyword in keywords if keyword
        ]
        textos: List[str] = []
        for seccion in secciones:
            titulo_norm = seccion.get("titulo_norm") or ""
            if any(kw and kw in titulo_norm for kw in keywords_norm):
                fragmento = seccion.get("texto") or ""
                if fragmento:
                    textos.append(fragmento)
        if textos:
            resultado[alias] = "\n\n".join(textos)

    if "general" not in resultado:
        resultado["general"] = texto

    return resultado, secciones


def _orden_categorias(
    config: Dict[str, Any], rubrica_activa: Optional[str]
) -> List[str]:
    prompt_cfg = _prompt_config(config)
    estructura_cfg = (
        prompt_cfg.get("estructura_superior", {})
        if prompt_cfg
        else {}
    )
    mapeo_por_rubrica = (
        estructura_cfg.get("mapeo_por_rubrica", {})
        if isinstance(estructura_cfg, dict)
        else {}
    )
    rubrica_norm = _normalize_for_matching(rubrica_activa) if rubrica_activa else ""
    mapping_cfg = None
    if isinstance(mapeo_por_rubrica, dict):
        if rubrica_norm:
            for clave, valores in mapeo_por_rubrica.items():
                if _normalize_for_matching(clave) == rubrica_norm and isinstance(valores, dict):
                    mapping_cfg = valores
                    break
        if mapping_cfg is None and isinstance(mapeo_por_rubrica.get("default"), dict):
            mapping_cfg = mapeo_por_rubrica.get("default")

    orden: List[str] = []
    if isinstance(mapping_cfg, dict):
        orden.extend([str(k) for k in mapping_cfg.keys()])
    display_names = _category_display_names(config)
    for categoria in display_names:
        if categoria not in orden:
            orden.append(categoria)
    return orden


def _extraer_fragmentos_relevantes(
    texto: str,
    palabras: List[str],
    max_length: int = 6000,
    ventana: int = 1200,
) -> str:
    if not texto:
        return ""
    if not palabras:
        return texto[:max_length]

    texto_lower = texto.lower()
    longitud = len(texto)
    rangos: List[Tuple[int, int]] = []

    for palabra in palabras:
        if not palabra:
            continue
        clave = str(palabra).strip().lower()
        if not clave:
            continue
        inicio = texto_lower.find(clave)
        while inicio != -1:
            fin = inicio + len(clave)
            ventana_inicio = max(0, inicio - ventana // 2)
            ventana_fin = min(longitud, fin + ventana // 2)
            rangos.append((ventana_inicio, ventana_fin))
            inicio = texto_lower.find(clave, fin)

    if not rangos:
        return texto[:max_length]

    rangos.sort()
    combinados: List[List[int]] = []
    for inicio, fin in rangos:
        if not combinados or inicio > combinados[-1][1] + 80:
            combinados.append([inicio, fin])
        else:
            combinados[-1][1] = max(combinados[-1][1], fin)

    fragmentos: List[str] = []
    acumulado = 0
    for inicio, fin in combinados:
        fragmento = texto[inicio:fin]
        fragmentos.append(fragmento)
        acumulado += fin - inicio
        if acumulado >= max_length:
            break

    combinado = "\n...\n".join(fragmentos)
    if len(combinado) > max_length:
        combinado = combinado[:max_length]
    return combinado or texto[:max_length]


def _palabras_clave_para_metodologias(
    metodologias: List[str],
    metadata_estado: Optional[Dict[str, Dict[str, Any]]],
    config: Dict[str, Any],
) -> List[str]:
    if not metodologias:
        return []
    prompt_cfg = _prompt_config(config)
    metodologias_section = (
        prompt_cfg.get("instrucciones_metodologicas", {})
        if prompt_cfg
        else {}
    )
    metadata_cfg = metodologias_section.get("metadata", {})
    palabras: set[str] = set()

    for clave in metodologias:
        clave_norm = clave or ""
        if metadata_estado and clave_norm in metadata_estado:
            encontradas = metadata_estado[clave_norm].get("palabras_encontradas") or []
            for palabra in encontradas:
                if palabra:
                    palabras.add(str(palabra))
        info = metadata_cfg.get(clave_norm, {}) if isinstance(metadata_cfg, dict) else {}
        base = info.get("palabras_clave") or []
        for palabra in base:
            if palabra:
                palabras.add(str(palabra))

    return [p for p in palabras if p]


def _extraer_citas_metodologicas(
    texto: str,
    palabras: List[str],
    max_snippets: int = 4,
    ventana: int = 600,
) -> List[Tuple[str, str]]:
    if not texto or not palabras:
        return []

    texto_lower = texto.lower()
    longitud = len(texto)
    snippets: List[Tuple[str, str]] = []
    visitadas: set[Tuple[int, int]] = set()

    for palabra in palabras:
        clave = str(palabra).strip().lower()
        if not clave:
            continue
        inicio_busqueda = 0
        while True:
            idx = texto_lower.find(clave, inicio_busqueda)
            if idx == -1:
                break
            fin = idx + len(clave)
            ventana_inicio = max(0, idx - ventana // 2)
            ventana_fin = min(longitud, fin + ventana // 2)
            par = (ventana_inicio, ventana_fin)
            if par not in visitadas:
                fragmento = texto[ventana_inicio:ventana_fin].strip()
                if fragmento:
                    snippets.append((str(palabra).strip(), fragmento))
                    visitadas.add(par)
                    if len(snippets) >= max_snippets:
                        return snippets
            inicio_busqueda = fin
    return snippets


def _evaluar_cobertura_metodologica(
    texto_completo: str, config: Dict[str, Any]
) -> Dict[str, Dict[str, Any]]:
    prompt_cfg = _prompt_config(config)
    metodologias_section = (
        prompt_cfg.get("instrucciones_metodologicas", {})
        if prompt_cfg
        else {}
    )
    metadata_cfg = metodologias_section.get("metadata", {})
    if not isinstance(metadata_cfg, dict) or not metadata_cfg:
        return {}

    texto_norm = _normalize_for_matching(texto_completo)
    resultados: Dict[str, Dict[str, Any]] = {}

    for clave, info in metadata_cfg.items():
        if not isinstance(info, dict):
            continue
        palabras = info.get("palabras_clave", []) or []
        palabras_encontradas: List[str] = []
        palabras_faltantes: List[str] = []
        for palabra in palabras:
            palabra_norm = _normalize_for_matching(palabra)
            if not palabra_norm:
                continue
            if palabra_norm and palabra_norm in texto_norm:
                palabras_encontradas.append(str(palabra).strip())
            else:
                palabras_faltantes.append(str(palabra).strip())

        detectado = bool(palabras_encontradas)
        resultados[clave] = {
            "detectado": detectado,
            "critico": bool(info.get("critico", False)),
            "palabras_encontradas": palabras_encontradas,
            "palabras_faltantes": palabras_faltantes,
            "comentario_evaluacion": str(info.get("comentario_evaluacion", "")).strip(),
            "comentario_falta": str(info.get("comentario_falta", "")).strip(),
        }

    return resultados


def _extra_instrucciones_metodologicas(
    criterio: str,
    config: Dict[str, Any],
    texto_completo: Optional[str] = None,
    metadata_estado: Optional[Dict[str, Dict[str, Any]]] = None,
    dominio_operativo: Optional[str] = None,
) -> tuple[str, List[str]]:
    texto: List[str] = []
    added: set[str] = set()
    orden: List[str] = []
    crit = criterio or ""
    crit_lower = crit.lower()
    crit_norm = _normalize_for_matching(crit)
    prompt_cfg = _prompt_config(config)
    metodologias_section = (
        prompt_cfg.get("instrucciones_metodologicas", {})
        if prompt_cfg
        else {}
    )
    metodologias_cfg = {
        key: value
        for key, value in metodologias_section.items()
        if key not in {"mapeo_criterios", "metodologias_forzadas", "metadata"}
        and isinstance(value, (str, dict))
    }
    aliases_cfg = metodologias_section.get("mapeo_criterios", {})
    forced_cfg = metodologias_section.get("metodologias_forzadas", {})
    defaults = _default_metodologias(config)
    if not dominio_operativo:
        dominio_operativo = _inferir_entorno_procesos(
            texto_completo,
            metadata_estado,
            config,
        )

    def _append(clave: str) -> None:
        if clave in added:
            return
        if clave not in defaults:
            return
        piezas: List[str] = []
        texto_metodologia = _obtener_texto_metodologia(
            clave,
            metodologias_cfg,
            defaults,
            dominio_operativo,
            config,
        )
        if texto_metodologia:
            piezas.append(texto_metodologia)
        if metadata_estado and clave in metadata_estado:
            estado = metadata_estado[clave]
            comentario = (
                estado.get("comentario_evaluacion")
                if estado.get("detectado")
                else estado.get("comentario_falta")
            )
            if comentario:
                piezas.append(comentario)
            if not estado.get("detectado"):
                faltantes = [
                    palabra
                    for palabra in estado.get("palabras_faltantes", [])
                    if palabra
                ]
                if faltantes:
                    piezas.append(
                        "No se identifican evidencias de: "
                        + ", ".join(sorted({f.strip() for f in faltantes}))
                    )
                if estado.get("critico"):
                    piezas.append(
                        "Marca la ausencia como desviacion critica y propone un plan para cubrirla."
                    )
        if piezas:
            texto.append("\n".join(piezas))
        added.add(clave)
        orden.append(clave)

    if any(key in crit_lower for key in ["extern", "pestel", "porter", "entorno"]):
        _append("analisis_externo")
    if any(key in crit_lower for key in ["intern", "vrio", "cadena", "recursos"]):
        _append("analisis_interno")
    if any(
        key in crit_lower
        for key in [
            "proceso",
            "operac",
            "product",
            "fabric",
            "lean",
            "gmp",
            "fda",
            "six sigma",
            "dmaic",
            "dmac",
            "vsm",
            "value stream",
            "ishikawa",
            "fmea",
        ]
    ):
        _append("procesos_fabricacion_operativos")
    if any(
        key in crit_lower
        for key in ["logist", "sumin", "supply", "scor", "invent", "ultima milla"]
    ):
        _append("procesos_logisticos_cadena_suministro")
    if any(
        key in crit_lower
        for key in ["administr", "servicio", "sipoc", "bpm", "swimlane", "blueprint"]
    ):
        _append("procesos_administrativos_servicios")
    if any(
        key in crit_lower
        for key in ["financ", "inversion", "roi", "van", "tir", "payback", "flujo"]
    ):
        _append("analisis_financiero")

    if isinstance(aliases_cfg, dict):
        for clave, alias_list in aliases_cfg.items():
            if clave in added:
                continue
            if not isinstance(alias_list, (list, tuple)):
                continue
            alias_norm = [
                _normalize_for_matching(alias)
                for alias in alias_list
                if isinstance(alias, str) and alias.strip()
            ]
            for alias_value in alias_norm:
                if not alias_value:
                    continue
                if crit_norm and (
                    alias_value in crit_norm or crit_norm in alias_value
                ):
                    _append(clave)
                    break

    for clave, valor in forced_cfg.items():
        if not valor:
            continue
        if clave in added:
            continue
        alias_list = aliases_cfg.get(clave)
        if not alias_list:
            continue
        alias_norm = [
            _normalize_for_matching(alias)
            for alias in alias_list
            if isinstance(alias, str) and alias.strip()
        ]
        if any(alias_value and alias_value in crit_norm for alias_value in alias_norm):
            _append(clave)

    return "\n".join(texto), orden


def _is_onedrive_path(path: Path) -> bool:
    text = str(path)
    return ("OneDrive" in text) or ("/Library/CloudStorage/" in text and "OneDrive-" in text)


def _hydrate_if_needed(path: Path, logger: Any) -> None:
    try:
        with open(path, "rb", buffering=0) as handler:
            _ = handler.read(65536)
    except Exception as exc:
        if logger is not None:
            logger.warning("No se pudo hidratar el archivo para leer etiquetas: %s", exc)


def _mdls_plist(path: Path) -> Optional[Any]:
    try:
        result = subprocess.run(
            ["mdls", "-name", "kMDItemUserTags", "-plist", str(path)],
            capture_output=True,
            env=UTF8_ENV,
            check=False,
        )
    except FileNotFoundError:
        return None

    if result.returncode != 0 or not result.stdout:
        return None

    try:
        data = plistlib.loads(result.stdout)
    except Exception:
        return None

    if isinstance(data, dict):
        value = data.get("kMDItemUserTags")
        if value is not None:
            return value
    if isinstance(data, list):
        if data and isinstance(data[0], dict):
            value = data[0].get("kMDItemUserTags")
            if value is not None:
                return value
        if all(isinstance(item, str) for item in data):
            return data
    if isinstance(data, tuple) and all(isinstance(item, str) for item in data):
        return list(data)
    return None


def _xattr_finder_tags(path: Path) -> Optional[Any]:
    existing = path.exists()
    try:
        result = subprocess.run(
            ["xattr", "-p", "com.apple.metadata:_kMDItemUserTags", str(path)],
            capture_output=True,
            env=UTF8_ENV,
            check=False,
        )
    except FileNotFoundError:
        return None

    if result.returncode != 0 or not result.stdout:
        if result.returncode != 0 and existing and result.stderr:
            stderr_text = result.stderr.decode("utf-8", errors="ignore").strip()
            if stderr_text:
                print("xattr stderr:", stderr_text)
        return None

    try:
        return plistlib.loads(result.stdout)
    except Exception:
        return None


def _mdls_raw_tags(path: Path) -> Optional[List[str]]:
    try:
        result = subprocess.run(
            ["mdls", "-name", "kMDItemUserTags", "-raw", str(path)],
            capture_output=True,
            env=UTF8_ENV,
            check=False,
        )
    except FileNotFoundError:
        return None

    if result.returncode != 0:
        return None

    text = result.stdout.decode("utf-8", errors="ignore").strip()
    if not text or text in {"(null)", "<null>", "null"}:
        return None

    if text.startswith("(") and text.endswith(")"):
        inner = text[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip() for p in inner.split(",")]
        tags: List[str] = []
        for part in parts:
            clean = part.strip()
            if clean.startswith('"') and clean.endswith('"'):
                clean = clean[1:-1]
            elif clean.startswith("'") and clean.endswith("'"):
                clean = clean[1:-1]
            if clean:
                tags.append(clean)
        return tags

    if text.startswith('"') and text.endswith('"') and len(text) >= 2:
        return [text[1:-1]]

    return [text]


def _coerce_existing_path(path: Path) -> Path:
    candidates = [str(path)]
    for form in ("NFC", "NFD", "NFKC", "NFKD"):
        candidates.append(unicodedata.normalize(form, str(path)))

    for cand in candidates:
        candidate_path = Path(cand).expanduser()
        if candidate_path.exists():
            try:
                return candidate_path.resolve()
            except Exception:
                return candidate_path
    return Path(unicodedata.normalize("NFC", str(path))).expanduser()


def _normalize_finder_tag(value: str) -> str:
    if not value:
        return ""
    normalized = unicodedata.normalize("NFC", str(value))
    head = normalized.split("\n", 1)[0]
    head = head.split("(", 1)[0]
    head = head.strip()
    if not head:
        return ""
    if " " in head:
        head = head.split(" ", 1)[0]
    match = re.match(r"([A-Za-z0-9_-]+)", head)
    if match:
        head = match.group(1)
    return head.strip().upper()


def obtener_etiquetas_finder(ruta: str, logger: Any) -> List[str]:
    if not ruta:
        return []

    try:
        path_obj = _coerce_existing_path(Path(ruta))
    except Exception:
        if logger is not None:
            logger.error("No se pudo normalizar la ruta para leer etiquetas: %s", ruta)
        return []

    if not path_obj.exists():
        if logger is not None:
            logger.warning("No existe el archivo para leer etiquetas: %s", path_obj)
        return []

    if _is_onedrive_path(path_obj):
        _hydrate_if_needed(path_obj, logger)

    raw_tags: Optional[Any] = None
    source = ""
    for nombre, extractor in (
        ("mdls-plist", _mdls_plist),
        ("xattr", _xattr_finder_tags),
        ("mdls-raw", _mdls_raw_tags),
    ):
        try:
            resultado = extractor(path_obj)
        except Exception as exc:  # noqa: PERF203 (depuración)
            resultado = None
            if logger is not None:
                logger.warning(
                    "Extractor de etiquetas %s falló para %s: %s",
                    nombre,
                    path_obj,
                    exc,
                )
        if resultado is not None:
            raw_tags = resultado
            source = nombre
            if isinstance(resultado, (list, tuple, set)):
                if len(resultado) > 0:
                    break
            elif resultado:
                break

    if raw_tags is None:
        raw_tags = []
        if logger is not None and getattr(logger, "_null_logger", False):
            print("No se obtuvieron etiquetas Finder via mdls/xattr para:", path_obj)

    tags: List[str] = []
    raw_display: List[str] = []
    if isinstance(raw_tags, (list, tuple)):
        for raw in raw_tags:
            raw_text = str(raw)
            raw_display.append(raw_text)
            tag = _normalize_finder_tag(raw_text)
            if tag:
                tags.append(tag)
    elif isinstance(raw_tags, str):
        raw_display.append(raw_tags)
        tag = _normalize_finder_tag(raw_tags)
        if tag:
            tags.append(tag)

    if logger is not None:
        if raw_display:
            logger.info(
                "Etiquetas Finder (raw, %s): %s",
                source or "desconocido",
                ", ".join(raw_display),
            )
            if getattr(logger, "_null_logger", False):
                print(
                    "Etiquetas Finder (raw,",
                    source or "desconocido",
                    "):",
                    ", ".join(raw_display),
                )
        elif source:
            logger.info(
                "Extractor de etiquetas %s no devolvió valores para el archivo.",
                source,
            )
            if getattr(logger, "_null_logger", False):
                print(
                    "Extractor de etiquetas",
                    source,
                    "no devolvió valores para el archivo.",
                )
        if tags:
            logger.info("Etiquetas Finder (normalizadas): %s", ", ".join(tags))
            if getattr(logger, "_null_logger", False):
                print("Etiquetas Finder (normalizadas):", ", ".join(tags))
        else:
            logger.info("No se detectaron etiquetas Finder en el archivo seleccionado.")
            if getattr(logger, "_null_logger", False):
                print("No se detectaron etiquetas Finder en el archivo seleccionado.")

    return tags


def ajustar_rubrica_por_config(
    df, rubrica_key: str, config: Dict[str, Any], logger: Any
):
    if logger is None:
        logger = configurar_logger()

    rubricas_cfg = (
        (config.get("sistema", {}) if config else {}).get("rubricas_config", {})
    )
    exclusiones_cfg = rubricas_cfg.get("exclusiones", {}) if rubricas_cfg else {}
    conf = exclusiones_cfg.get(rubrica_key)
    if not conf:
        return df

    df = df.copy()
    total = len(df)
    indices_a_eliminar: set[int] = set()

    numeros = conf.get("criterios_excluir")
    if isinstance(numeros, (list, tuple)):
        for numero in numeros:
            try:
                idx = int(numero) - 1
            except (TypeError, ValueError):
                continue
            if 0 <= idx < total:
                indices_a_eliminar.add(idx)

    formula = str(conf.get("criterios_excluir_formula") or "").lower()
    if formula.startswith("ultimo"):
        match = re.search(r"(\d+)", formula)
        if match:
            cantidad = int(match.group(1))
            for idx in range(max(total - cantidad, 0), total):
                indices_a_eliminar.add(idx)

    if indices_a_eliminar:
        df = df.drop(df.index[sorted(indices_a_eliminar)])
        df = df.reset_index(drop=True)
        logger.info(
            "Se excluyeron %d criterios de la rúbrica %s: %s",
            len(indices_a_eliminar),
            rubrica_key,
            ", ".join(str(i + 1) for i in sorted(indices_a_eliminar)),
        )

    esperado = conf.get("numero_criterios")
    minimo = conf.get("numero_criterios_min")
    maximo = conf.get("numero_criterios_max")
    final = len(df)

    if esperado is not None:
        try:
            esperado_int = int(esperado)
            if final != esperado_int:
                logger.warning(
                    "La rúbrica %s tiene %d criterios tras exclusiones, pero se esperaba %d.",
                    rubrica_key,
                    final,
                    esperado_int,
                )
        except (TypeError, ValueError):
            logger.warning(
                "valor numero_criterios inválido en configuración de la rúbrica %s: %s",
                rubrica_key,
                esperado,
            )
    else:
        if minimo is not None:
            try:
                minimo_int = int(minimo)
                if final < minimo_int:
                    logger.warning(
                        "La rúbrica %s quedó con %d criterios, por debajo del mínimo configurado %d.",
                        rubrica_key,
                        final,
                        minimo_int,
                    )
            except (TypeError, ValueError):
                logger.warning(
                    "valor numero_criterios_min inválido en configuración de la rúbrica %s: %s",
                    rubrica_key,
                    minimo,
                )
        if maximo is not None:
            try:
                maximo_int = int(maximo)
                if final > maximo_int:
                    logger.warning(
                        "La rúbrica %s quedó con %d criterios, por encima del máximo configurado %d.",
                        rubrica_key,
                        final,
                        maximo_int,
                    )
            except (TypeError, ValueError):
                logger.warning(
                    "valor numero_criterios_max inválido en configuración de la rúbrica %s: %s",
                    rubrica_key,
                    maximo,
                )

    runtime = config.setdefault("_runtime", {}) if config is not None else {}
    runtime.setdefault("criterios_excluidos", {})[rubrica_key] = sorted(i + 1 for i in indices_a_eliminar)
    runtime.setdefault("criterios_totales", {})[rubrica_key] = final

    return df


# Globals we will reset to avoid cross-run contamination
def reset_globals():
    globals_to_reset = ["_contador_llamadas", "_patrones_usados"]
    for g in globals_to_reset:
        if g in globals():
            try:
                del globals()[g]
            except Exception:
                globals()[g] = None


# Logger
def configurar_logger():
    """Devuelve un logger nulo (no hace nada). Eliminamos uso de logs para simplificar.
    Mantener la función para compatibilidad con llamadas existentes.
    """

    class NullLogger:
        def __init__(self):
            self._null_logger = True

        def info(self, *args, **kwargs):
            return None

        def error(self, *args, **kwargs):
            return None

        def exception(self, *args, **kwargs):
            return None

        def warning(self, *args, **kwargs):
            return None

    return NullLogger()



# --- Rulepacks: carga y resolución (modular) ---------------------------------
def _load_yaml_file(path: Path, logger: Any = None) -> Dict[str, Any]:
    """Carga un YAML devolviendo dict. En caso de error, devuelve {}.
    Se usa para rulepacks y configuraciones auxiliares.
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return data if isinstance(data, dict) else {}
    except Exception as exc:
        if logger:
            logger.warning("No se pudo cargar YAML: %s (%s)", path, exc)
        return {}


def _resolve_rulepacks(cfg: Dict[str, Any], base_dir: Path, logger: Any = None) -> None:
    """Resuelve rulepacks declarados en el YAML del evaluador.

    Convención:
      - cfg['evaluador']['rulepacks'] es un dict de packs.
      - cada pack puede tener: enabled, strict_mode, rules_file (relativo a base_dir o absoluto).
      - el contenido del pack se inyecta en cfg['evaluador']['rulepacks'][name]['rules'].

    Además, si no existe 'rulepacks' pero existe un ruleset por defecto en el paquete,
    se crea una entrada mínima para evitar que el sistema dependa del orden/edición manual.
    """
    evaluador = cfg.get("evaluador")
    if not isinstance(evaluador, dict):
        return

    # Autoregistro del pack por defecto si existe el archivo y aún no se declara nada.
    default_rules_path = (base_dir / "rules_analisis_externo.yaml").resolve()
    if "rulepacks" not in evaluador and default_rules_path.exists():
        evaluador["rulepacks"] = {
            "analisis_externo": {
                "enabled": True,
                "strict_mode": True,
                "rules_file": "rules_analisis_externo.yaml",
                "version": "1.0",
                "output_expectations": {
                    "require_gate_reporting": True,
                    "require_block_diagnostics": True,
                    "require_cross_check_reporting": True,
                },
            }
        }

    rulepacks = evaluador.get("rulepacks")
    if not isinstance(rulepacks, dict):
        return

    for name, pack_cfg in rulepacks.items():
        if not isinstance(pack_cfg, dict):
            continue
        if not pack_cfg.get("enabled", False):
            continue

        rules_file = pack_cfg.get("rules_file") or pack_cfg.get("rules_path")
        # Si el YAML declara 'rules_file' vacío, intentamos convención por nombre del pack.
        if not rules_file and name == "analisis_externo":
            rules_file = "rules_analisis_externo.yaml"

        rules_path: Optional[Path] = None
        if isinstance(rules_file, str) and rules_file.strip():
            candidate = Path(rules_file).expanduser()
            if candidate.is_absolute():
                rules_path = candidate
            else:
                rules_path = (base_dir / candidate).resolve()

        # Fallback: si el path no existe y es el pack esperado, usar el default.
        if (not rules_path) or (not rules_path.exists()):
            if name == "analisis_externo" and default_rules_path.exists():
                rules_path = default_rules_path

        if rules_path and rules_path.exists():
            pack_cfg["rules"] = _load_yaml_file(rules_path, logger=logger)
            pack_cfg.setdefault("resolved_rules_path", str(rules_path))
        else:
            pack_cfg.setdefault("rules", {})
            if logger:
                logger.warning("Rulepack '%s' habilitado pero no se encontró rules_file: %s", name, rules_file)




def _capabilities_cfg(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Devuelve la configuración de capacidades (si existe) cargada desde capacidades_rubricas.yaml."""
    cap = cfg.get("capabilities") if isinstance(cfg, dict) else None
    return cap if isinstance(cap, dict) else {}


def _merge_rulepacks_from_capabilities(cfg: Dict[str, Any], logger: Any = None) -> None:
    """Añade rulepacks desde capacidades_rubricas.yaml a cfg['evaluador']['rulepacks'] sin sobrescribir.

    Esto permite que los rulepacks apunten a capacidades canónicas en un YAML separado,
    manteniendo el YAML principal del prompt más limpio y evitando hardcode por rúbrica.
    """
    if not isinstance(cfg, dict):
        return
    cap_cfg = _capabilities_cfg(cfg)
    rp_src = cap_cfg.get("rulepacks")
    if not isinstance(rp_src, dict) or not rp_src:
        return

    evaluador = cfg.setdefault("evaluador", {})
    if not isinstance(evaluador, dict):
        return
    rp_dst = evaluador.setdefault("rulepacks", {})
    if not isinstance(rp_dst, dict):
        evaluador["rulepacks"] = {}
        rp_dst = evaluador["rulepacks"]

    added: List[str] = []
    for name, pack in rp_src.items():
        if name in rp_dst:
            continue
        if isinstance(pack, dict):
            rp_dst[name] = pack
            added.append(name)

    if logger and added:
        logger.info("Rulepacks añadidos desde capacidades_rubricas.yaml: %s", ", ".join(sorted(added)))


def _resolve_rulepack_targets_for_active_rubric(cfg: Dict[str, Any], rubrica_df, logger: Any = None) -> None:
    """Resuelve apply_to_capacidades -> apply_to_criterios (títulos reales) para la rúbrica activa.

    - Se apoya en capacidades_rubricas.yaml:
        rubricas[<RUBRICA_ID>].capability_to_criterios (ids internos)
        rubricas[<RUBRICA_ID>].criterios[*].match (regex para localizar títulos reales en Excel)
    - Inyecta en cada rulepack:
        pack_cfg['_resolved_apply_to_criterios'] = [<títulos reales>]
        pack_cfg['_resolved_target_criterio_ids'] = [<ids internos>]
    """
    if not isinstance(cfg, dict) or rubrica_df is None:
        return
    runtime = cfg.setdefault("_runtime", {})
    rubric_key = runtime.get("rubrica_activa")
    if not rubric_key:
        return

    # Evitar recomputar (útil cuando se evalúan muchos criterios)
    if runtime.get("_resolved_rulepack_targets_for") == rubric_key:
        return

    cap_cfg = _capabilities_cfg(cfg)
    rub_cfg = (cap_cfg.get("rubricas") or {}).get(str(rubric_key))
    if not isinstance(rub_cfg, dict):
        return

    criterios_defs = rub_cfg.get("criterios") or []
    cap_to_ids = rub_cfg.get("capability_to_criterios") or {}
    if not isinstance(criterios_defs, list) or not isinstance(cap_to_ids, dict):
        return

    # Lista de títulos reales disponibles en la rúbrica (primer columna del Excel)
    criterios_reales: List[str] = []
    try:
        for _, row in rubrica_df.iterrows():
            c = str(row.iloc[0]).strip()
            if not c or c.lower() in {"nan", "none"}:
                continue
            criterios_reales.append(c)
    except Exception:
        return

    # Resolver id interno -> títulos reales usando regex 'match'
    id_to_titles: Dict[str, List[str]] = {}
    for item in criterios_defs:
        if not isinstance(item, dict):
            continue
        cid = item.get("id")
        rex = item.get("match")
        if not cid or not rex:
            continue
        try:
            hits = [t for t in criterios_reales if re.search(str(rex), t)]
        except Exception:
            hits = []
        if hits:
            id_to_titles[str(cid)] = hits

    rulepacks = (cfg.get("evaluador") or {}).get("rulepacks") if isinstance(cfg.get("evaluador"), dict) else {}
    if not isinstance(rulepacks, dict) or not rulepacks:
        return

    for pack_name, pack_cfg in rulepacks.items():
        if not isinstance(pack_cfg, dict):
            continue
        cap_list = pack_cfg.get("apply_to_capacidades") or pack_cfg.get("apply_to_capabilities")
        if not isinstance(cap_list, (list, tuple)) or not cap_list:
            continue

        criterio_ids: List[str] = []
        for cap in cap_list:
            if not isinstance(cap, str) or not cap.strip():
                continue
            ids = cap_to_ids.get(cap.strip())
            if isinstance(ids, (list, tuple)):
                criterio_ids.extend([str(x) for x in ids if x])

        resolved_titles: List[str] = []
        for cid in criterio_ids:
            resolved_titles.extend(id_to_titles.get(cid, []))

        # Deduplicar preservando orden
        seen = set()
        resolved_titles = [t for t in resolved_titles if t and not (t in seen or seen.add(t))]

        pack_cfg["_resolved_target_criterio_ids"] = list(dict.fromkeys(criterio_ids))
        pack_cfg["_resolved_apply_to_criterios"] = resolved_titles

        if logger and not resolved_titles:
            logger.warning(
                "Rulepack '%s': apply_to_capacidades=%s pero no se resolvieron criterios reales para la rúbrica '%s'.",
                pack_name,
                cap_list,
                rubric_key,
            )

    runtime["_resolved_rulepack_targets_for"] = rubric_key


# --- Rulepacks: heurísticas mínimas (gates/caps) -----------------------------
def _should_apply_rulepack(criterio: str, pack_cfg: Dict[str, Any]) -> bool:
    """Decide si aplicar un rulepack a un criterio concreto.

    Soporta:
      - pack_cfg['_resolved_apply_to_criterios']: lista de títulos reales ya resueltos (vía capacidades canónicas)
      - pack_cfg['apply_to_criterios']: lista de substrings o nombres (modo legacy)
      - heurística por defecto: criterios tipo 'introducción/objetivos/justificación' y 'proyecto'
    """
    crit = (criterio or "").strip()
    crit_norm = _normalize_for_matching(crit)

    apply_list = (
        pack_cfg.get("_resolved_apply_to_criterios")
        or pack_cfg.get("apply_to_criterios")
    )
    if isinstance(apply_list, (list, tuple)) and apply_list:
        for item in apply_list:
            if not isinstance(item, str) or not item.strip():
                continue
            token_norm = _normalize_for_matching(item.strip())
            if token_norm and token_norm in crit_norm:
                return True
        return False

    # Heurística por defecto (conservadora)
    return any(
        key in crit_norm
        for key in [
            "introdu",
            "objetiv",
            "justific",
            "proyecto",
            "entorno",
            "analisis externo",
            "análisis externo",
        ]
    )


def _normalize_text_for_rules(texto: str) -> str:
    return _normalize_for_matching(texto or "")


def _find_first(patterns: List[str], text_norm: str) -> Optional[int]:
    for pat in patterns:
        try:
            m = re.search(pat, text_norm)
            if m:
                return m.start()
        except re.error:
            continue
    return None


def _window(text: str, start: int, length: int = 2000) -> str:
    if start < 0:
        start = 0
    return text[start : start + length]


def _evidence_counts(sample: str) -> Dict[str, int]:
    # Indicadores: números, porcentajes, moneda, años.
    indicators = len(re.findall(r"(?:\b\d{1,3}(?:[\.,]\d+)?\b|%|€|\b20\d{2}\b)", sample))
    # Fuentes: patrones APA aproximados, URL, DOI o referencias tipo [1]
    sources = len(re.findall(r"(?:\(.*?,\s*(?:19|20)\d{2}\)|https?://|www\.|doi:|\[\d+\])", sample, flags=re.IGNORECASE))
    return {"indicators": indicators, "sources": sources}


def _has_implication(sample: str) -> bool:
    return bool(
        re.search(
            r"(por tanto|por ello|implica|se traduce|requiere|debe\b|condiciona|obliga|en consecuencia)",
            sample,
            flags=re.IGNORECASE,
        )
    )


def _detect_core_blocks(texto: str) -> Dict[str, Dict[str, Any]]:
    """Detección mínima de bloques. No pretende ser perfecta, sino estable y explicable."""
    raw = texto or ""
    norm = _normalize_text_for_rules(raw)

    patterns = {
        "pestel": [r"\bpestel\b"],
        "porter_5f": [r"porter", r"cinco\s+fuerzas", r"\b5\s*fuerzas\b"],
        "mercado_cliente": [r"segment", r"\bmercado\b", r"\bcliente\b", r"\busuario\b", r"drivers", r"barrera"],
        "competidores_alternativas": [r"compet", r"benchmark", r"alternativ", r"sustitut"],
        "stakeholders": [r"stakeholder", r"grupos\s+de\s+inter", r"poder\s*-?\s*inter", r"matriz\s+poder"],
        "sintesis_mefe_dafo": [r"\bmefe\b", r"\befe\b", r"\bdafo\b", r"\bfoda\b", r"factores\s+extern"],
    }

    results: Dict[str, Dict[str, Any]] = {}
    for block, pats in patterns.items():
        pos = _find_first(pats, norm)
        present = pos is not None
        sample = _window(raw, pos if pos is not None else 0, 2500) if present else ""
        ev = _evidence_counts(sample) if present else {"indicators": 0, "sources": 0}
        results[block] = {
            "present": present,
            "pos": pos,
            "evidence": ev,
            "has_implication": _has_implication(sample) if present else False,
        }

    # Síntesis requiere MEFE/EFE y DAFO en conjunto (más estricto que un match simple).
    has_mefe = bool(re.search(r"\bmefe\b|\befe\b|factores\s+extern", norm))
    has_dafo = bool(re.search(r"\bdafo\b|\bfoda\b", norm))
    results["sintesis_mefe_dafo"]["present"] = has_mefe and has_dafo

    return results


def _analisis_externo_gate_report(
    texto: str, rules: Dict[str, Any]
) -> Dict[str, Any]:
    """Evalúa gates principales del rulepack de análisis externo con heurística mínima.

    Devuelve:
      - missing_blocks
      - gate_failures
      - cap_level (nivel máximo permitido)
      - per_block (diagnóstico mínimo)
    """
    per_block = _detect_core_blocks(texto)
    required_blocks = [
        "pestel",
        "porter_5f",
        "mercado_cliente",
        "competidores_alternativas",
        "stakeholders",
        "sintesis_mefe_dafo",
    ]
    missing_blocks = [b for b in required_blocks if not per_block.get(b, {}).get("present")]

    gate_failures: List[str] = []
    cap_level = 4

    # Gate G1
    if len(missing_blocks) >= 2:
        gate_failures.append("G1_core_blocks_missing_2_or_more")
        cap_level = min(cap_level, 1)
    if "sintesis_mefe_dafo" in missing_blocks:
        gate_failures.append("G1_missing_synthesis")
        cap_level = min(cap_level, 2)

    # Gate G2: evidencia mínima por bloque presente (aproximación)
    any_no_evidence = False
    for b in required_blocks:
        info = per_block.get(b, {})
        if not info.get("present"):
            continue
        ev = info.get("evidence") or {}
        if (ev.get("indicators", 0) < 1) or (ev.get("sources", 0) < 1):
            any_no_evidence = True
            break
    if any_no_evidence:
        gate_failures.append("G2_min_evidence_failed")
        cap_level = min(cap_level, 2)

    # Gate G3: implicaciones en PESTEL y Porter
    pestel_imp = per_block.get("pestel", {}).get("has_implication", False)
    porter_imp = per_block.get("porter_5f", {}).get("has_implication", False)
    if not (pestel_imp and porter_imp):
        gate_failures.append("G3_implications_missing_pestel_or_porter")
        cap_level = min(cap_level, 2)

    return {
        "missing_blocks": missing_blocks,
        "gate_failures": gate_failures,
        "cap_level": cap_level,
        "per_block": per_block,
    }


def _format_rulepack_addendum(pack_name: str, report: Dict[str, Any], pack_cfg: Dict[str, Any]) -> str:
    """Texto breve para insertar en el prompt (auditable, no verboso)."""
    cap = report.get("cap_level", 4)
    missing = report.get("missing_blocks", [])
    failures = report.get("gate_failures", [])
    resolved = pack_cfg.get("resolved_rules_path") or pack_cfg.get("rules_file") or ""
    return (
        f"\n[Rulepack:{pack_name}] strict_mode={bool(pack_cfg.get('strict_mode', True))}; "
        f"ruleset={resolved}; cap_level={cap}. "
        f"Missing_blocks={missing}. Gate_failures={failures}.\n"
        "Debes respetar el cap_level (nivel máximo) y justificar la decisión citando evidencia del texto.\n"
        "Si el cap_level < 4, prioriza 'areas_mejora' con acciones concretas para cumplir los gates.\n"
    )




def _detect_internal_blocks(raw: str) -> Dict[str, Dict[str, Any]]:
    """Detección mínima de bloques de análisis interno (heurística).

    La detección es deliberadamente conservadora: busca presencia + evidencia mínima (indicadores/fuentes)
    para apoyar gates/caps en modo ultraestricto.
    """
    texto = raw or ""
    norm = _normalize_text_for_rules(texto)

    patterns = {
        "procesos_cadena_valor": [
            r"cadena\s+de\s+valor",
            r"value\s+chain",
            r"\bbpmn\b",
            r"mapa\s+de\s+proces",
            r"\bvsm\b",
            r"sipoc",
            r"as\s*-?\s*is",
            r"to\s*-?\s*be",
        ],
        "recursos_capacidades": [
            r"\bvrio\b",
            r"recurs",
            r"capacidades",
            r"competenc",
        ],
        "causa_raiz_priorizacion": [
            r"causa\s+ra[ií]z",
            r"\b5\s*porqu",
            r"ishikawa",
            r"diagrama\s+de\s+causa",
            r"pareto",
            r"principio\s+80\s*/\s*20",
        ],
        "sintesis_mefi": [
            r"\bmefi\b",
            r"\bife\b",
            r"factores\s+intern",
            r"matriz\s+de\s+evaluaci[oó]n\s+de\s+factores\s+internos",
        ],
        "coso": [r"\bcoso\b", r"control\s+interno", r"ambiente\s+de\s+control", r"evaluaci[oó]n\s+de\s+riesgos"],
        "fmea": [
            r"\bfmea\b",
            r"\bpfmea\b",
            r"modo\s+de\s+fallo",
            r"rpn",
            r"severidad",
            r"ocurrencia",
            r"detec",
        ],
    }

    results: Dict[str, Dict[str, Any]] = {}
    for block, pats in patterns.items():
        pos = _find_first(pats, norm)
        present = pos is not None
        sample = _window(texto, pos if pos is not None else 0, 2500) if present else ""
        ev = _evidence_counts(sample) if sample else {"indicators": 0, "sources": 0}
        results[block] = {"present": present, "pos": pos, "evidence": ev}
    return results


def _analisis_interno_gate_report(texto: str, rules: Dict[str, Any], dominio_operativo: Optional[str] = None) -> Dict[str, Any]:
    """Evalúa gates principales del rulepack de análisis interno con heurística mínima.

    Devuelve:
      - missing_blocks
      - gate_failures
      - cap_level (nivel máximo permitido)
      - per_block (diagnóstico mínimo)
    """
    per_block = _detect_internal_blocks(texto)

    # Permite que un rules_file redefina exigencias (si existe)
    required_blocks = rules.get("required_blocks")
    required_any_of = rules.get("required_any_of")

    # Defaults ultraestrictos y transversales
    if not isinstance(required_blocks, list) or not required_blocks:
        required_blocks = ["procesos_cadena_valor", "recursos_capacidades", "causa_raiz_priorizacion", "sintesis_mefi"]

    if not isinstance(required_any_of, list):
        required_any_of = []

    # En dominios regulados, reforzar control/riesgo si el propio TFM lo declara (o si el ruleset lo exige)
    # (No lo hacemos universalmente obligatorio para no penalizar TFMs puramente conceptuales.)
    if dominio_operativo:
        dom = _normalize_for_matching(dominio_operativo)
        if any(k in dom for k in ["salud", "gobierno", "public", "administr", "aliment", "farm", "industr", "bodeg", "cadena de frio", "frio"]):
            # Solo elevar si hay alguna señal de controles/riesgos en el texto o el ruleset lo pide.
            if per_block.get("coso", {}).get("present") or per_block.get("fmea", {}).get("present") or rules.get("require_control_riesgo"):
                if "coso" not in required_blocks:
                    required_blocks = list(required_blocks) + ["coso"]
                if "fmea" not in required_blocks:
                    required_blocks = list(required_blocks) + ["fmea"]

    missing_blocks = [b for b in required_blocks if not per_block.get(b, {}).get("present")]

    gate_failures: List[str] = []
    cap_level = 4

    # Gate I1: faltan 2+ bloques troncales
    if len(missing_blocks) >= 2:
        gate_failures.append("I1_core_blocks_missing_2_or_more")
        cap_level = min(cap_level, 1)

    # Gate I2: falta síntesis MEFI (o equivalente)
    if "sintesis_mefi" in missing_blocks:
        gate_failures.append("I2_missing_internal_synthesis_mefi")
        cap_level = min(cap_level, 2)

    # Gate I3: falta causalidad/priorización (causa raíz)
    if "causa_raiz_priorizacion" in missing_blocks:
        gate_failures.append("I3_missing_root_cause_or_prioritization")
        cap_level = min(cap_level, 2)

    # Gate I4: evidencia mínima en bloques presentes
    any_no_evidence = False
    for b in required_blocks:
        info = per_block.get(b, {})
        if not info.get("present"):
            continue
        ev = info.get("evidence") or {}
        if (ev.get("indicators", 0) < 1) or (ev.get("sources", 0) < 1):
            any_no_evidence = True
            break
    if any_no_evidence:
        gate_failures.append("I4_min_evidence_failed")
        cap_level = min(cap_level, 2)

    # Gate I5: reglas 'any_of' (si el ruleset las define)
    # Formato esperado: [["bloque_a","bloque_b"], ["x","y","z"]]
    if required_any_of:
        try:
            for group in required_any_of:
                if not isinstance(group, (list, tuple)) or not group:
                    continue
                if not any(per_block.get(g, {}).get("present") for g in group):
                    gate_failures.append("I5_required_any_of_missing:" + ",".join([str(x) for x in group]))
                    cap_level = min(cap_level, 2)
        except Exception:
            pass

    return {
        "missing_blocks": missing_blocks,
        "gate_failures": gate_failures,
        "cap_level": cap_level,
        "per_block": per_block,
    }


def _run_rulepack_gate_report(pack_name: str, texto: str, rules: Dict[str, Any], dominio_operativo: Optional[str] = None) -> Dict[str, Any]:
    """Despacha la evaluación de gates por nombre de pack."""
    if pack_name == "analisis_externo":
        return _analisis_externo_gate_report(texto, rules)
    if pack_name == "analisis_interno":
        return _analisis_interno_gate_report(texto, rules, dominio_operativo=dominio_operativo)
    return {}
def _enforce_cap_level(parsed: Dict[str, Any], cap_level: int, report: Dict[str, Any]) -> None:
    """Aplica un techo de nivel de forma determinista (ultraestricto)."""
    try:
        nivel_value = parsed.get("nivel")
        if nivel_value is None:
            return
        nivel = int(nivel_value)
    except Exception:
        return
    if cap_level and isinstance(cap_level, int) and nivel > cap_level:
        parsed["nivel_original_modelo"] = nivel
        parsed["nivel"] = cap_level
        # Anclar la razón en la justificación de forma transparente.
        j = (parsed.get("justificacion") or "").strip()
        motivo = (
            f"[Ajuste ultraestricto] Se aplica cap_level={cap_level} por gates fallidos: "
            f"{report.get('gate_failures', [])}; missing_blocks={report.get('missing_blocks', [])}."
        )
        parsed["justificacion"] = (j + " " + motivo).strip()

# Carga configuración YAML mínima
def cargar_config_yaml() -> Dict[str, Any]:
    cfg = {}
    for key, path in (
        ("sistema", CONFIG_SISTEMA),
        ("evaluador", CONFIG_PROMPT),
        ("capabilities", CONFIG_CAPACIDADES),
    ):
        try:
            with open(path, "r", encoding="utf-8") as f:
                cfg[key] = yaml.safe_load(f) or {}
        except Exception:
            cfg[key] = {}

    
    # Añadir rulepacks definidos en capacidades_rubricas.yaml (sin sobrescribir los del prompt)
    try:
        _merge_rulepacks_from_capabilities(cfg)
    except Exception:
        pass

# Resolver rulepacks (si existen) sin acoplarse al orden del YAML
    try:
        _resolve_rulepacks(cfg, TFM_PACKAGE)
    except Exception:
        pass

    return cfg


def validar_config_minima(cfg: Dict[str, Any]) -> None:
    """Verifica que existan las secciones esenciales en los YAML. Si falta, lanza RuntimeError.
    Requisito: al menos la sección 'sistema' y 'evaluador' deben contener datos.
    """
    sistema = cfg.get("sistema") or {}
    evaluador = cfg.get("evaluador") or {}
    if not sistema or not evaluador:
        raise RuntimeError(
            "Faltan archivos YAML de configuración o están vacíos. Se requiere 'sistema' y 'evaluador'."
        )


# Selector (AppKit NSOpenPanel) - funciona sólo en macOS
def seleccionar_archivo_pdf_docx(logger: Any) -> Optional[str]:
    if logger is None:
        logger = configurar_logger()
    try:
        from AppKit import NSOpenPanel, NSModalResponseOK  # type: ignore
    except ImportError as e:
        logger.error(
            "AppKit no disponible: selección de archivo no funcionará aquí. Error: %s",
            e,
        )
        if getattr(logger, "_null_logger", False):
            print(
                "AppKit no disponible: selección de archivo no funcionará aquí. Error:",
                e,
            )
        return None
    panel = NSOpenPanel.openPanel()
    panel.setAllowedFileTypes_(["pdf", "docx"])  # <--- corregido: lista de extensiones
    panel.setAllowsMultipleSelection_(False)
    panel.setMessage_("Selecciona el TFM (PDF o DOCX)")
    if panel.runModal() == NSModalResponseOK:
        url = panel.URLs()[0]
        path = url.path()
        logger.info(f"Archivo seleccionado: {path}")
        if getattr(logger, "_null_logger", False):
            print("Archivo seleccionado:", path)
        return path
    return None


# Lectura PDF/DOCX con hash
def leer_tfm(path: str, logger: Any) -> str:
    if logger is None:
        logger = configurar_logger()
    if not os.path.exists(path):
        logger.error("No existe archivo: %s", path)
        return ""
    ext = Path(path).suffix.lower()
    contenido = ""
    try:
        if ext == ".pdf":
            import pdfplumber

            with pdfplumber.open(path) as pdf:
                logger.info("Páginas PDF: %s", len(pdf.pages))
                for i, page in enumerate(pdf.pages, 1):
                    text = page.extract_text() or ""
                    if text.strip():
                        contenido += f"[P{i}] " + text + "\n"
        elif ext == ".docx":
            from docx import Document

            doc = Document(path)
            logger.info("Párrafos DOCX: %s", len(doc.paragraphs))
            for p in doc.paragraphs:
                if p.text.strip():
                    contenido += p.text + "\n"
        else:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                contenido = f.read()
    except Exception as e:
        logger.exception("Error extrayendo texto: %s", e)
        return ""

    h = hashlib.md5(contenido.encode("utf-8")).hexdigest()
    logger.info("MD5 contenido: %s | longitud: %d", h, len(contenido))
    logger.info("Primeros 200 chars: %s", repr(contenido[:200]))
    return contenido


# Extracción rápida de frases clave (n-grams simples)
def extraer_frases_clave(texto: str, n: int = 5) -> List[str]:
    tokens = re.findall(r"\w+", texto.lower())
    frec: Dict[str, int] = {}
    for t in tokens:
        if len(t) > 3:
            frec[t] = frec.get(t, 0) + 1
    items = sorted(frec.items(), key=lambda x: -x[1])[:n]
    return [w for w, _ in items]


# Helper para calcular rutas de exportación (intenta crear subcarpeta en la carpeta del TFM)
def paths_para_exportar(
    ruta_tfm: Optional[str], ts: str, config: Optional[Dict[str, Any]] = None
):
    """Devuelve rutas de salida para csv/json/md.
    Si la configuración YAML contiene `sistema.archivos_config.nombres_salida`, se usan
    los nombres definidos allí. En otro caso, se usan los nombres por defecto.
    Siempre escribe directamente en la carpeta del TFM (sin subcarpeta).
    """
    if not ruta_tfm:
        raise RuntimeError("No se proporcionó ruta del TFM para exportar")

    tfm_dir = Path(ruta_tfm).resolve().parent

    # Valores por defecto (coinciden con convención existente)
    default_names = {
        "csv": "evaluacion_tfm_resultado.csv",
        "json": "evaluacion_tfm_informe.json",
        "markdown": "evaluacion_tfm_informe.md",
    }

    try:
        nombres = (
            (config or {})
            .get("sistema", {})
            .get("archivos_config", {})
            .get("nombres_salida", {})
        )
        csv_name = nombres.get("csv") or default_names["csv"]
        json_name = nombres.get("json") or default_names["json"]
        md_name = nombres.get("markdown") or default_names["markdown"]
    except Exception:
        csv_name = default_names["csv"]
        json_name = default_names["json"]
        md_name = default_names["markdown"]

    csv_direct = tfm_dir / csv_name
    json_direct = tfm_dir / json_name
    md_direct = tfm_dir / md_name
    return csv_direct, json_direct, md_direct


# Construir prompt incluyendo hash y frases clave para diferenciación
def construir_prompt(
    criterio: str,
    instrucciones: str,
    texto_relevante: str,
    doc_hash: str,
    phrases: List[str],
) -> str:
    sample = texto_relevante[:6000]
    prompt = (
        f"Eres un evaluador académico. Criterio: {criterio}\n"
        f"Instrucciones: {instrucciones}\n"
        f"Documento hash: {doc_hash}\n"
        f"Frases clave: {', '.join(phrases)}\n"
        f"Texto relevante (recorte):\n{sample}\n"
        "Responde en formato JSON con campos: criterio, nivel(1-4), justificacion, areas_mejora, evidencias."
    )
    return prompt


# Llamada a OpenAI (compatible con distintas versiones)
def obtener_respuesta_openai(
    prompt: str,
    config: Dict[str, Any],
    logger: Any,
    max_tokens_override: Optional[int] = None,
) -> str:
    if logger is None:
        logger = configurar_logger()
    openai_cfg = config.get("sistema", {}).get("openai_config", {})
    variables_api = openai_cfg.get(
        "variables_api_key", ["MI_CLAVE_API_OPENAI", "OPENAI_API_KEY"]
    )
    api_key = None
    for v in variables_api:
        api_key = os.getenv(v)
        if api_key:
            break
    if not api_key:
        raise RuntimeError(
            f"No API key encontrada en variables de entorno: {variables_api}"
        )

    temperatura = openai_cfg.get("temperatura_por_defecto", 0.0)
    if max_tokens_override is not None:
        max_tokens_eval = int(max_tokens_override)
    else:
        max_tokens_eval = openai_cfg.get("max_tokens_evaluacion", 900)
    modelo = openai_cfg.get("modelo_por_defecto", "gpt-4o-mini")

    try:
        import openai
        client = openai.OpenAI(api_key=api_key)
        logger.info(
            "Usando cliente openai.OpenAI, modelo=%s temp=%s", modelo, temperatura
        )
        resp = client.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperatura,
            max_tokens=max_tokens_eval,
        )
        content = getattr(resp.choices[0].message, "content", None)
        if content is None:
            content = resp.choices[0].message.content
        return str(content) if content is not None else ""
    except Exception as e:
        logger.exception("Error llamando OpenAI: %s", e)
        raise


def obtener_api_key_desde_config(config: Dict[str, Any]) -> str:
    """Devuelve la API key encontrada en entorno según las variables configuradas en YAML.
    Lanza RuntimeError si no encuentra ninguna clave.
    """
    openai_cfg = config.get("sistema", {}).get("openai_config", {})
    variables_api = openai_cfg.get(
        "variables_api_key", ["MI_CLAVE_API_OPENAI", "OPENAI_API_KEY"]
    )
    for v in variables_api:
        val = os.getenv(v)
        if val:
            return val
    raise RuntimeError(
        f"No API key encontrada en variables de entorno: {variables_api}"
    )


# Evaluación minimalista usando rúbrica en xlsx
def cargar_rubrica_por_defecto(
    config: Dict[str, Any], logger: Any, ruta_tfm: Optional[str] = None
):
    if logger is None:
        logger = configurar_logger()
    rubricas = config.get("sistema", {}).get("rutas_sistema", {}).get("rubricas", {})
    if not rubricas:
        logger.error("No hay rúbricas configuradas en YAML")
        return None

    selected_key: Optional[str] = None
    selected_path: Optional[str] = None
    tags_detectadas: List[str] = []

    if ruta_tfm:
        try:
            tags_detectadas = obtener_etiquetas_finder(ruta_tfm, logger)
        except Exception as exc:
            logger.warning("No se pudieron leer etiquetas Finder: %s", exc)
            tags_detectadas = []

        normalized_tags_upper = [
            _normalize_finder_tag(tag).upper() for tag in tags_detectadas
        ]
        normalized_tags_upper = [tag for tag in normalized_tags_upper if tag]
        for key, path in rubricas.items():
            key_normalized = _normalize_finder_tag(key)
            if key_normalized in normalized_tags_upper:
                selected_key = key
                selected_path = path
                break

    if not selected_path:
        selected_key, selected_path = next(iter(rubricas.items()))
        if tags_detectadas:
            logger.warning(
                "Las etiquetas Finder %s no coinciden con rúbricas registradas; usando rúbrica por defecto %s.",
                tags_detectadas,
                selected_key,
            )
            if getattr(logger, "_null_logger", False):
                print(
                    "Las etiquetas Finder",
                    tags_detectadas,
                    "no coinciden con rúbricas registradas; usando rúbrica por defecto",
                    selected_key,
                )
        else:
            logger.info(
                "No se detectaron etiquetas Finder; usando rúbrica por defecto %s.",
                selected_key,
            )
            if getattr(logger, "_null_logger", False):
                print(
                    "No se detectaron etiquetas Finder; usando rúbrica por defecto",
                    selected_key,
                )
    else:
        logger.info(
            "Rúbrica seleccionada por etiqueta: %s -> %s",
            selected_key,
            selected_path,
        )
        if getattr(logger, "_null_logger", False):
            print("Rúbrica seleccionada por etiqueta:", selected_key, "->", selected_path)

    rubrica_path = Path(str(selected_path)).expanduser()
    if _is_onedrive_path(rubrica_path):
        _hydrate_if_needed(rubrica_path, logger)

    if not rubrica_path.exists():
        logger.error("La rúbrica seleccionada no existe: %s", rubrica_path)
        return None

    try:
        import pandas as pd

        df = pd.read_excel(rubrica_path)
        df = ajustar_rubrica_por_config(df, selected_key, config, logger) # pyright: ignore[reportArgumentType]
        logger.info(
            "Rúbrica cargada (%s): %s (filas=%d)",
            selected_key,
            rubrica_path,
            len(df),
        )
        runtime = config.setdefault("_runtime", {})
        runtime["rubrica_activa"] = selected_key
        runtime["etiquetas_detectadas"] = tags_detectadas
        runtime["ruta_rubrica"] = str(rubrica_path)
        return df
    except Exception as e:
        logger.exception("Error cargando rúbrica: %s", e)
        return None


def generar_analisis_extendido(
    criterio: str,
    metodologias_relacionadas: List[str],
    citas_formateadas: List[str],
    texto_original: str,
    palabras_clave: List[str],
    doc_hash: str,
    phrases: List[str],
    metadata_estado: Optional[Dict[str, Dict[str, Any]]],
    dominio_operativo: Optional[str],
    config: Dict[str, Any],
    logger: Any,
) -> str:
    sistema_cfg = config.get("sistema", {}) if isinstance(config, dict) else {}
    ext_cfg = sistema_cfg.get("analisis_extendido", {}) if sistema_cfg else {}
    if not ext_cfg or not ext_cfg.get("habilitado"):
        return ""

    criterios_objetivo = ext_cfg.get("criterios_objetivo") or []
    crit_norm = _normalize_for_matching(criterio)
    if criterios_objetivo:
        coincide = False
        for objetivo in criterios_objetivo:
            obj_norm = _normalize_for_matching(objetivo)
            if not obj_norm:
                continue
            if obj_norm in crit_norm or crit_norm in obj_norm:
                coincide = True
                break
        if not coincide:
            return ""

    instrucciones_generales = str(ext_cfg.get("instrucciones_generales", "")).strip()
    metodologia_por_defecto = str(ext_cfg.get("metodologia_por_defecto", "")).strip()
    metodologia_cfg = ext_cfg.get("metodologias_especificas", {})
    defaults_metodologias = _default_metodologias(config)
    dominio_resuelto = dominio_operativo or _inferir_entorno_procesos(
        texto_original,
        metadata_estado,
        config,
    )
    instrucciones_metodologia: List[str] = []
    if isinstance(metodologia_cfg, dict):
        for clave in metodologias_relacionadas:
            texto_met = _obtener_texto_metodologia(
                clave,
                metodologia_cfg,
                defaults_metodologias,
                dominio_resuelto,
                config,
            )
            if texto_met:
                if texto_met not in instrucciones_metodologia:
                    instrucciones_metodologia.append(texto_met)
    if not instrucciones_metodologia and metodologia_por_defecto:
        instrucciones_metodologia.append(metodologia_por_defecto)

    prompt_partes: List[str] = [
        "Actua como miembro del tribunal evaluador del TFM. Redacta un informe extendido que complemente la nota y refleje el análisis crítico detallado.",
        f"Criterio evaluado: {criterio}",
    ]
    if instrucciones_generales:
        prompt_partes.append(instrucciones_generales)
    categoria = _clasificar_criterio_extendido(criterio)
    instrucciones_categoria = _criterio_extendido_instrucciones(config)
    categoria_instr = instrucciones_categoria.get(categoria)
    if categoria_instr:
        prompt_partes.append(categoria_instr)
    if instrucciones_metodologia:
        prompt_partes.append("\n\n".join(instrucciones_metodologia))
    prompt_partes.append(
        "Evita repetir observaciones ya mencionadas en otros criterios del informe y céntrate en aspectos exclusivos de este criterio."
    )
    if citas_formateadas:
        prompt_partes.append(
            "Fragmentos etiquetados para analizar:\n" + "\n---\n".join(citas_formateadas)
        )
    palabras_referencia = list({p.strip().lower(): None for p in (palabras_clave or []) if p})
    palabras_referencia.append(criterio)
    palabras_referencia = [p for p in palabras_referencia if p]
    texto_para_analisis = texto_original or ""
    if texto_para_analisis:
        recorte = _extraer_fragmentos_relevantes(
            texto_para_analisis,
            palabras_referencia,
            max_length=7000,
            ventana=1200,
        )
        prompt_partes.append(
            "Texto de referencia (selección relevante):\n" + recorte
        )
    if phrases:
        prompt_partes.append("Frases clave del documento: " + ", ".join(phrases))
    prompt_partes.append(f"Documento hash: {doc_hash}")
    prompt_partes.append(
        "Entrega un texto narrativo estructurado con párrafos completos, conclusiones accionables y sin JSON ni listas simples."
    )

    prompt_extendido = "\n\n".join(part for part in prompt_partes if part)
    max_tokens_ext = (
        sistema_cfg.get("openai_config", {}).get("max_tokens_extendido")
        if isinstance(sistema_cfg, dict)
        else None
    )

    try:
        respuesta = obtener_respuesta_openai(
            prompt_extendido,
            config,
            logger,
            max_tokens_override=max_tokens_ext,
        )
    except Exception as exc:
        logger.warning("No se pudo obtener informe extendido: %s", exc)
        return ""

    return str(respuesta or "").strip()


def evaluar_tfm_minimal(
    texto_tfm: str, rubrica_df, config: Dict[str, Any], logger: Any
) -> List[Dict[str, Any]]:
    resultados = []
    if logger is None:
        logger = configurar_logger()
    if rubrica_df is None or not texto_tfm.strip():
        return resultados
    doc_hash = hashlib.md5(texto_tfm.encode("utf-8")).hexdigest()
    phrases = extraer_frases_clave(texto_tfm, n=6)
    instrucciones = (
        config.get("evaluador", {}).get("context")
        or "Evalúa el criterio con rigor académico."
    )
    metadata_original = _evaluar_cobertura_metodologica(texto_tfm, config)
    dominio_operativo = _inferir_entorno_procesos(
        texto_tfm,
        metadata_original,
        config,
    )
    metadata_estado = {
        clave: _ajustar_estado_por_entorno(clave, estado, dominio_operativo)
        for clave, estado in (metadata_original or {}).items()
    }
    runtime = config.setdefault("_runtime", {})
    runtime["dominio_operativo"] = dominio_operativo
    runtime["cobertura_metodologias"] = metadata_estado
    runtime["metodologias_no_detectadas"] = [
        clave for clave, estado in (metadata_estado or {}).items() if not estado.get("detectado")
    ]
    runtime["metodologias_detectadas"] = [
        clave for clave, estado in (metadata_estado or {}).items() if estado.get("detectado")
    ]
    metodologias_usadas: set[str] = set()

    rubrica_activa = runtime.get("rubrica_activa")
    # Resolver targets de rulepacks (apply_to_capacidades -> criterios reales) para la rúbrica activa
    try:
        _resolve_rulepack_targets_for_active_rubric(config, rubrica_df, logger)
    except Exception:
        pass
    secciones_categoria, secciones_lista = _mapear_secciones_por_categoria(
        texto_tfm,
        config,
        rubrica_activa,
    )
    runtime["secciones_superiores"] = secciones_lista

    if metadata_estado and logger is not None:
        for clave, estado in metadata_estado.items():
            if estado.get("detectado"):
                continue
            nombre = _presentar_metodologia(clave)
            pendientes = ", ".join(estado.get("palabras_faltantes", [])) or "sin pistas"
            logger.warning(
                "Metodologia %s ausente%s. Palabras pendientes: %s",
                nombre,
                " (CRITICA)" if estado.get("critico") else "",
                pendientes,
            )

    def _enrich_result(destino: Dict[str, Any], claves_relacionadas: List[str]) -> None:
        if not isinstance(destino, dict):
            return
        metodologias_legibles = [
            _presentar_metodologia(clave) for clave in claves_relacionadas if clave
        ]
        if metodologias_legibles:
            destino["metodologias_relacionadas"] = ", ".join(metodologias_legibles)
        else:
            destino.setdefault("metodologias_relacionadas", "")

        comentarios: List[str] = []
        alertas: List[str] = []
        hallazgos: List[str] = []

        for clave in claves_relacionadas:
            estado = metadata_estado.get(clave, {}) if metadata_estado else {}
            if not estado:
                continue
            nombre = _presentar_metodologia(clave)
            comentario_base = (
                estado.get("comentario_evaluacion")
                if estado.get("detectado")
                else estado.get("comentario_falta")
            )
            if comentario_base:
                comentarios.append(f"{nombre}: {comentario_base}")
            if estado.get("palabras_encontradas"):
                hallazgos.append(
                    f"{nombre}: "
                    + ", ".join(sorted({p for p in estado["palabras_encontradas"] if p}))
                )
            if not estado.get("detectado"):
                faltantes = [
                    palabra for palabra in estado.get("palabras_faltantes", []) if palabra
                ]
                faltantes_msg = (
                    " (faltan evidencias de: "
                    + ", ".join(sorted({f for f in faltantes}))
                    + ")"
                    if faltantes
                    else ""
                )
                pref = "CRITICO - " if estado.get("critico") else ""
                alerta = (
                    f"{pref}{nombre}: {comentario_base or 'Sin evidencia metodologica.'}{faltantes_msg}"
                )
                alertas.append(alerta)

        if comentarios:
            destino["comentario_metodologico"] = " || ".join(comentarios)
        else:
            destino.setdefault("comentario_metodologico", "")

        if alertas:
            destino["alertas_metodologicas"] = " || ".join(alertas)
        else:
            destino.setdefault("alertas_metodologicas", "")

        if hallazgos:
            destino["palabras_metodologicas_encontradas"] = " || ".join(hallazgos)
        else:
            destino.setdefault("palabras_metodologicas_encontradas", "")

    for _, row in rubrica_df.iterrows():
        criterio = str(row.iloc[0]).strip()
        if not criterio or criterio.lower() in {"nan", "none", ""}:
            continue
        # Intentar extraer las 4 descripciones de nivel desde la rúbrica
        descripcion_niveles: List[str] = []
        try:
            # Si la rúbrica tiene al menos 5 columnas, asumimos: [criterio, nivel1, nivel2, nivel3, nivel4, ...]
            if len(row) >= 5:
                # Tomar las siguientes 4 columnas tras la primera
                descripcion_niveles = [str(x).strip() for x in row.iloc[1:5]]
            else:
                # Intentar buscar columnas cuyo nombre sugiera 'nivel' o 'level'
                cols = list(rubrica_df.columns)
                cand = []
                for c in cols[1:]:
                    if isinstance(c, str) and re.search(
                        r"nivel|level|score|descriptor", c, re.I
                    ):
                        cand.append(c)
                if cand:
                    for c in cand[:4]:
                        descripcion_niveles.append(str(row[c]).strip())
        except Exception:
            descripcion_niveles = []

        instrucciones_completas = instrucciones
        _, metodologias_relacionadas = _extra_instrucciones_metodologicas(
            criterio,
            config,
            texto_completo=texto_tfm,
            metadata_estado=metadata_estado,
            dominio_operativo=dominio_operativo,
        )
        metodologias_usadas.update(metodologias_relacionadas)

        categoria_criterio = _clasificar_criterio_extendido(criterio)
        texto_categoria = (
            secciones_categoria.get(categoria_criterio)
            if secciones_categoria
            else None
        )
        if not texto_categoria:
            texto_categoria = secciones_categoria.get("general") if secciones_categoria else None
        if not texto_categoria:
            texto_categoria = texto_tfm

        # --- Rulepacks (gates/caps) -----------------------------------------
        rulepack_addendum = ""
        rulepack_reports: Dict[str, Dict[str, Any]] = {}
        rulepack_caps: Dict[str, int] = {}

        rulepacks_cfg = (
            (config.get("evaluador") or {}).get("rulepacks", {})
            if isinstance(config, dict)
            else {}
        )
        if isinstance(rulepacks_cfg, dict) and rulepacks_cfg:
            for pack_name, pack_cfg in rulepacks_cfg.items():
                if not isinstance(pack_cfg, dict) or not pack_cfg.get("enabled", False):
                    continue
                if not _should_apply_rulepack(criterio, pack_cfg):
                    continue
                rules_value = pack_cfg.get("rules")
                rules: Dict[str, Any] = rules_value if isinstance(rules_value, dict) else {}
                report = _run_rulepack_gate_report(
                    str(pack_name),
                    texto_categoria,
                    rules,
                    dominio_operativo=dominio_operativo,
                )
                if not isinstance(report, dict) or not report:
                    continue
                try:
                    cap = int(report.get("cap_level", 4) or 4)
                except Exception:
                    cap = 4
                rulepack_reports[str(pack_name)] = report
                rulepack_caps[str(pack_name)] = cap
                try:
                    rulepack_addendum += _format_rulepack_addendum(str(pack_name), report, pack_cfg)
                except Exception:
                    pass

        if metodologias_relacionadas and metadata_estado:
            cobertura_lines: List[str] = []
            for clave in metodologias_relacionadas:
                estado = metadata_estado.get(clave, {})
                nombre = _presentar_metodologia(clave)
                if not estado:
                    cobertura_lines.append(f"{nombre}: sin datos de deteccion")
                    continue
                if estado.get("detectado"):
                    encontradas = ", ".join(
                        sorted({p for p in estado.get("palabras_encontradas", []) if p})
                    )
                    if encontradas:
                        cobertura_lines.append(
                            f"{nombre}: evidencias detectadas en el texto -> {encontradas}"
                        )
                    else:
                        cobertura_lines.append(
                            f"{nombre}: marca presencia metodologica pero sin palabras clave listadas"
                        )
                else:
                    faltantes = ", ".join(
                        sorted({p for p in estado.get("palabras_faltantes", []) if p})
                    )
                    if not faltantes:
                        faltantes = "sin palabras clave registradas"
                    prefijo = "CRITICO - " if estado.get("critico") else ""
                    cobertura_lines.append(
                        f"{prefijo}{nombre}: no se hallaron evidencias. Faltan -> {faltantes}"
                    )

            if cobertura_lines:
                instrucciones_completas += (
                    "\nCobertura metodologica detectada en el documento:\n- "
                    + "\n- ".join(cobertura_lines)
                )

        # Construir prompt incluyendo las descripciones numeradas si existen
        if descripcion_niveles and len(descripcion_niveles) == 4:
            niveles_text = "\n".join(
                [f"{i + 1}. {d}" for i, d in enumerate(descripcion_niveles)]
            )
            prompt_extra = (
                "A continuación se proporcionan 4 descripciones de niveles para este criterio. "
                "Responde indicando únicamente el número (1-4) que mejor describe el trabajo, y justifica la elección.\n"
                f"Descripciones:\n{niveles_text}\n"
            )
        else:
            prompt_extra = "Indica el nivel del trabajo (1-4) y justifica la elección."

        prompt_extra += (
            " La justificacion debe citar evidencia textual o numerica del TFM y detallar brechas o malas aplicaciones "
            "de los modelos requeridos."
        )

        # Añadir directiva de rulepack (si aplica) sin ensuciar el prompt base
        if rulepack_addendum:
            prompt_extra += rulepack_addendum

        palabras_metodo = _palabras_clave_para_metodologias(
            metodologias_relacionadas,
            metadata_estado,
            config,
        )
        palabras_metodo.extend([criterio])
        palabras_metodo = list({p.strip(): None for p in palabras_metodo if p and p.strip()})
        enviar_completo = (
            config.get("sistema", {})
            .get("evaluacion_config", {})
            .get("enviar_documento_completo", False)
        )

        if enviar_completo:
            texto_relevante = texto_tfm
        else:
            texto_relevante = _extraer_fragmentos_relevantes(
                texto_categoria,
                palabras_metodo,
                max_length=6000,
                ventana=1400,
            )
            if not texto_relevante:
                texto_relevante = texto_tfm[:6000]

        citas_metodologicas = _extraer_citas_metodologicas(
            texto_categoria,
            palabras_metodo,
            max_snippets=4,
            ventana=800,
        )

        citas_formateadas: List[str] = []
        if citas_metodologicas:
            for idx, (clave_cita, fragmento_cita) in enumerate(
                citas_metodologicas, start=1
            ):
                etiqueta = clave_cita or "metodologia"
                fragmento_limpio = fragmento_cita.strip().replace("\n", " ")
                citas_formateadas.append(
                    f"[Fragmento {idx} - {etiqueta}] {fragmento_limpio}"
                )

            prompt_extra += (
                "\nAnaliza cada fragmento etiquetado (Fragmento 1, Fragmento 2, etc.) "
                "explicando si evidencia una aplicacion correcta, parcial o ausente de la metodologia."
            )

        citas_texto = ""
        if citas_formateadas:
            citas_texto = (
                "\nFragmentos relevantes detectados:\n"
                + "\n---\n".join(citas_formateadas)
            )

        prompt = construir_prompt(
            criterio,
            instrucciones_completas + "\n" + prompt_extra + citas_texto,
            texto_relevante,
            doc_hash,
            phrases,
        )
        prompt_hash = hashlib.md5(prompt.encode("utf-8")).hexdigest()
        logger.info("Evaluando criterio: %s | prompt_hash: %s", criterio, prompt_hash)
        resp = obtener_respuesta_openai(prompt, config, logger)
        informe_extendido = generar_analisis_extendido(
            criterio,
            metodologias_relacionadas,
            citas_formateadas,
            texto_categoria,
            palabras_metodo,
            doc_hash,
            phrases,
            metadata_estado,
            dominio_operativo,
            config,
            logger,
        )
        # Intentar parsear JSON, fallback básico
        if not resp:
            logger.error("Respuesta vacía para criterio: %s", criterio)
            continue
        resp_cand = resp.strip()
        try:
            # Some models return ```json blocks
            if resp_cand.startswith("```json"):
                resp_cand = resp_cand[7:]
                if resp_cand.endswith("```"):
                    resp_cand = resp_cand[:-3]
            elif resp_cand.startswith("```"):
                resp_cand = resp_cand[3:]
                if resp_cand.endswith("```"):
                    resp_cand = resp_cand[:-3]
            parsed = json.loads(resp_cand)
            # Normalizar: asegurarnos de que existe 'descripcion_nivel' con el texto correspondiente
            nivel_elegido = parsed.get("nivel")
            nivel_idx: Optional[int] = None
            try:
                if nivel_elegido is not None and nivel_elegido != "":
                    nivel_int = int(nivel_elegido)
                    nivel_idx = nivel_int - 1
            except (TypeError, ValueError):
                nivel_idx = None
            if (
                nivel_idx is not None
                and descripcion_niveles
                and 0 <= nivel_idx < len(descripcion_niveles)
            ):
                parsed.setdefault("descripcion_nivel", descripcion_niveles[nivel_idx])
            else:
                # Si no pudimos deducir, dejar descripcion_nivel vacía o tomar la que venga en parsed
                parsed.setdefault(
                    "descripcion_nivel", parsed.get("descripcion_nivel") or ""
                )

            # Añadir las descripciones de los 4 niveles al resultado para que JSON y CSV contengan
            # las mismas columnas/valores y sea posible sincronizarlos.
            for i in range(4):
                key = f"nivel_{i + 1}"
                parsed.setdefault(
                    key, descripcion_niveles[i] if i < len(descripcion_niveles) else ""
                )
            # Aplicar caps deterministas de rulepacks (si corresponde)
            if rulepack_reports:
                for rp_name, rp_report in rulepack_reports.items():
                    safe_name = re.sub(r"[^0-9a-zA-Z_]+", "_", str(rp_name)).strip("_")
                    key_base = f"rulepack_{safe_name}" if safe_name else "rulepack"
                    try:
                        parsed[key_base] = json.dumps(rp_report, ensure_ascii=False)
                    except Exception:
                        parsed[key_base] = str(rp_report)
                    cap = rulepack_caps.get(str(rp_name))
                    if cap is None:
                        try:
                            cap = int(rp_report.get("cap_level", 4) or 4)
                        except Exception:
                            cap = 4
                    parsed[key_base + "_cap_level"] = cap
                    _enforce_cap_level(parsed, int(cap), rp_report)

            _enrich_result(parsed, metodologias_relacionadas)
            if citas_formateadas:
                parsed["citas_metodologicas"] = " || ".join(citas_formateadas)
            if informe_extendido:
                parsed["informe_extendido"] = informe_extendido

            resultados.append(parsed)
            logger.info(
                "Parse OK criterio %s -> nivel %s", criterio, parsed.get("nivel")
            )
        except Exception:
            logger.exception("No se pudo parsear JSON. Respuesta: %s", resp)
            # Guardar fallback
            fallback = {
                "criterio": criterio,
                "nivel": None,
                "justificacion": resp_cand,
                "descripcion_nivel": "",
            }
            _enrich_result(fallback, metodologias_relacionadas)
            if citas_formateadas:
                fallback["citas_metodologicas"] = " || ".join(citas_formateadas)
            if informe_extendido:
                fallback["informe_extendido"] = informe_extendido
            resultados.append(fallback)
        time.sleep(0.5)

    runtime["metodologias_referenciadas_en_criterios"] = sorted(metodologias_usadas)
    return resultados


# Exportar resultados
def _generar_markdown(
    resultados: List[Dict[str, Any]],
    categorias_ordenadas: List[str],
    config: Optional[Dict[str, Any]] = None,
) -> str:
    """Genera un informe en Markdown agrupando los criterios por capítulo superior."""
    lines = ["# Informe de Evaluación TFM", ""]

    agrupados: Dict[str, List[Dict[str, Any]]] = {}
    for r in resultados:
        categoria = (r.get("categoria_superior") or "general").strip() or "general"
        agrupados.setdefault(categoria, []).append(r)

    orden_final: List[str] = []
    for cat in categorias_ordenadas:
        if cat in agrupados and cat not in orden_final:
            orden_final.append(cat)
    for cat in agrupados:
        if cat not in orden_final:
            orden_final.append(cat)

    display_names = _category_display_names(config or {})
    for cat in orden_final:
        criterios_cat = agrupados.get(cat)
        if not criterios_cat:
            continue
        titulo_cat = display_names.get(
            cat, cat.replace("_", " ").title()
        )
        lines.append(f"## {titulo_cat}")
        lines.append("")
        for r in criterios_cat:
            criterio = r.get("criterio") or ""
            nivel = r.get("nivel") or ""
            just = r.get("justificacion") or ""
            evid = r.get("evidencias") or ""
            areas = r.get("areas_mejora") or ""
            informe_ext = r.get("informe_extendido") or ""
            lines.append(f"### {criterio}")
            lines.append(f"- **Nivel alcanzado**: {nivel}")
            if just:
                lines.append(f"- **Justificación**: {just}")
            if evid:
                lines.append(f"- **Evidencias**: {evid}")
            if areas:
                lines.append(f"- **Áreas de mejora**: {areas}")
            if informe_ext:
                lines.append("\n#### Informe extendido\n")
                lines.append(informe_ext.strip())
            lines.append("")

    lines.append("## Tabla de Evaluación")
    lines.append("")
    lines.append("| Criterio | Nivel |")
    lines.append("|----------|-------|")

    resumen_ordenado: List[Dict[str, Any]] = []
    for cat in orden_final:
        resumen_ordenado.extend(agrupados.get(cat, []))

    for r in resumen_ordenado:
        criterio = (r.get("criterio") or "").replace("\n", " ")
        nivel = r.get("nivel") or ""
        lines.append(f"| {criterio} | {nivel} |")
    lines.append("")
    return "\n".join(lines)


def exportar(
    resultados: List[Dict[str, Any]],
    texto_tfm: str,
    ruta_tfm: Optional[str],
    config: Optional[Dict[str, Any]],
    logger: Any,
) -> None:
    # No hay fallback: se escriben directamente en la carpeta del TFM o se lanza excepción
    csv_path, json_path, md_path = paths_para_exportar(
        ruta_tfm, time.strftime("%Y%m%d_%H%M%S"), config
    )
    # CSV
    import pandas as pd

    try:
        # Normalizar y ordenar columnas: intentar imponer un esquema útil y estable
        df = pd.DataFrame(resultados)
        # Columnas preferidas en el CSV para compatibilidad con automatización externa
        preferred = [
            "criterio",
            "nivel",
            "descripcion_nivel",
            "nivel_1",
            "nivel_2",
            "nivel_3",
            "nivel_4",
            "justificacion",
            "areas_mejora",
            "evidencias",
            "metodologias_relacionadas",
            "comentario_metodologico",
            "alertas_metodologicas",
            "palabras_metodologicas_encontradas",
            "citas_metodologicas",
        ]
        # Añadir columnas faltantes con cadena vacía
        for c in preferred:
            if c not in df.columns:
                df[c] = ""
        df = df[preferred + [c for c in df.columns if c not in preferred]]
        df.to_csv(csv_path, index=False, encoding="utf-8")
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar CSV en {csv_path}: {e}")
    # JSON
    try:
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(resultados, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar JSON en {json_path}: {e}")
    # MD
    try:
        rubrica_activa = (
            config.get("_runtime", {}).get("rubrica_activa")
            if isinstance(config, dict)
            else None
        )
        categorias_ordenadas = _orden_categorias(config or {}, rubrica_activa)
        md_content = _generar_markdown(resultados, categorias_ordenadas, config or {})
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)
    except Exception as e:
        raise RuntimeError(f"No se pudo guardar MD en {md_path}: {e}")


# Main
def main() -> int:
    reset_globals()
    logger = configurar_logger()
    config = cargar_config_yaml()

    logger.info("=== Evaluador TFM SafeFix (no modifica Git) ===")
    # Validar que los YAML mínimos existan y contengan datos
    try:
        validar_config_minima(config)
    except RuntimeError as e:
        logger.error(str(e))
        print(f"ERROR: {e}")
        return 1

    # Validar que exista API key para OpenAI antes de comenzar
    try:
        _ = obtener_api_key_desde_config(config)
    except RuntimeError as e:
        logger.error(str(e))
        print(f"ERROR: {e}")
        return 1

    ruta = seleccionar_archivo_pdf_docx(logger)
    if not ruta:
        logger.error("No se seleccionó archivo. Abortando.")
        return 1
    texto = leer_tfm(ruta, logger)
    if not texto.strip():
        logger.error("Texto vacío después de leer. Abortando.")
        return 1
    rubrica = cargar_rubrica_por_defecto(config, logger, ruta)
    if rubrica is None:
        logger.error("No se pudo cargar rúbrica. Abortando.")
        return 1
    resultados = evaluar_tfm_minimal(texto, rubrica, config, logger)

    exportar(resultados, texto, ruta, config, logger)
    logger.info("Evaluación completada. Archivos guardados en la carpeta del TFM.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
