# Esta función no tiene sentido ontológico.

**def** generar_preguntas_respaldo(resultados: List[Dict], num_preguntas: int) -> List[str]:

​    """

​    Sistema de respaldo cuando falla el análisis profundo.

​    """

​    preguntas_respaldo = [

​        "El trabajo presenta metodología declarada que no se alinea completamente con la implementación práctica observada. ¿Cómo se justifica esta desconexión metodológica y qué implicaciones tiene para la validez de los resultados obtenidos?",

​        

​        "Los resultados se presentan sin análisis suficiente de factores confusores o variables intervinientes que podrían explicar los hallazgos. ¿Por qué no se controlan estas variables y cómo afecta esta omisión a la robustez de las conclusiones?",

​        

​        "Las conclusiones del estudio exceden el alcance de los datos presentados y la metodología aplicada. ¿Qué fundamenta estas generalizaciones y por qué no se reconocen explícitamente las limitaciones del diseño utilizado?"

​    ]

​    

​    return preguntas_respaldo[:num_preguntas]



# Esto debería apoyarse en el YAML



datos = {
        "numeros_y_porcentajes": [],
        "metodologias_mencionadas": [],
        "nombres_herramientas": [],
        "empresas_organizaciones": [],
        "indicadores_problemas": [],
        "frases_contradictorias": [],
        "datos_temporales": [],
        "valores_financieros": [],
        "conceptos_teoricos": [],
        "variables_estudiadas": [],
        "hipotesis_planteadas": [],
        "resultados_cuantitativos": [],
        "fuentes_citadas": [],
        "limitaciones_reconocidas": [],
        "conclusiones_clave": [],
        "recomendaciones": [],
        "sectores_industrias": [],
        "terminos_tecnicos": [],
        "escalas_medicion": [],
        # NUEVOS CAMPOS FINANCIEROS ESPECÍFICOS
​        "ratios_financieros": [],
​        "indicadores_financieros": [],
​        "metricas_rendimiento": [],
​        "analisis_financiero_tipo": [],
​        "proyecciones_financieras": [],
​        "criterios_inversion": []
​    }
​    
​    if not texto_tfm:
​        if logger:
​            logger.warning("No hay texto del TFM disponible para extracción específica")
​        return datos
​    
    # 1. Números, porcentajes y valores numéricos (EXPANDIDO PARA FINANZAS)
​    datos["numeros_y_porcentajes"] = re.findall(r'\d+(?:\.\d+)?%', texto_tfm)
​    
    # Valores financieros ampliados
​    datos["valores_financieros"] = re.findall(r'[€$£¥S/]\s*\d+(?:,\d{3})*(?:\.\d+)?', texto_tfm)
​    
    # Ratios financieros específicos
​    ratios_pattern = r'(?:ratio|índice|coeficiente)\s+(?:de\s+)?([a-záéíóúñü\s]+?):\s*(\d+(?:\.\d+)?)'
​    ratios_encontrados = re.findall(ratios_pattern, texto_tfm, re.IGNORECASE)
​    datos["ratios_financieros"] = [f"{ratio.strip()}: {valor}" for ratio, valor in ratios_encontrados]
​    
    # Indicadores financieros clave
​    indicadores_financieros = [
​        r'ROI[:=]\s*(\d+(?:\.\d+)?%?)',
​        r'VAN[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
​        r'NPV[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
​        r'TIR[:=]\s*(\d+(?:\.\d+)?%)',
​        r'IRR[:=]\s*(\d+(?:\.\d+)?%)',
​        r'WACC[:=]\s*(\d+(?:\.\d+)?%)',
​        r'EVA[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
​        r'EBITDA[:=]\s*([€$£¥S/]?\s*\d+(?:,\d{3})*(?:\.\d+)?)',
​        r'payback[:=]\s*(\d+(?:\.\d+)?)\s*(?:años?|meses?)',
​        r'punto de equilibrio[:=]\s*(\d+(?:,\d{3})*)',
​        r'break\s*even[:=]\s*(\d+(?:,\d{3})*)'
​    ]
​    
​    datos["indicadores_financieros"] = []
​    for patron in indicadores_financieros:
​        matches = re.findall(patron, texto_tfm, re.IGNORECASE)
​        datos["indicadores_financieros"].extend(matches)
​    
​    datos["resultados_cuantitativos"] = re.findall(r'\d+(?:\.\d+)?\s*(?:puntos|grados|unidades|casos|participantes|muestras)', texto_tfm, re.IGNORECASE)
​    datos["datos_temporales"] = re.findall(r'\b(?:20\d{2}|2\d{3})\b', texto_tfm)
​    
    # 2. Metodologías y herramientas (ampliado para CUALQUIER DOMINIO)
​    metodologias_amplias = [
        # Estratégicas
​        'PESTEL', 'PORTER', 'DAFO', 'SWOT', 'VRIO', 'CANVAS', 'BALANCED SCORECARD',
​        'MEFE', 'MEFI', 'MATRIZ BCG', 'CINCO FUERZAS', 'CADENA DE VALOR',
​        'CORE COMPETENCE', 'BENCHMARKING', 'ANALISIS DE COMPETIDORES',
        # Financieras y Económicas
​        'ROI', 'VAN', 'NPV', 'TIR', 'IRR', 'PAYBACK', 'EVA', 'EBITDA', 'WACC',
​        'RATIO DE LIQUIDEZ', 'RATIO DE SOLVENCIA', 'RATIO DE RENTABILIDAD',
​        'ANALISIS VERTICAL', 'ANALISIS HORIZONTAL', 'DUPONT', 'Z-SCORE',
​        'CAPM', 'BETA', 'COEFICIENTE DE VARIACION', 'ANALISIS DE SENSIBILIDAD',
​        'MONTE CARLO', 'ARBOL DE DECISION', 'VALOR PRESENTE NETO', 'TASA INTERNA',
​        'FLUJO DE CAJA', 'CASH FLOW', 'PUNTO DE EQUILIBRIO', 'BREAK EVEN',
​        'ANALISIS COSTO-BENEFICIO', 'ABC COSTING', 'MARGEN CONTRIBUCION',
        # Operacionales y Mejora
​        'LEAN', 'SIX SIGMA', 'SCRUM', 'KANBAN', 'ISHIKAWA', 'KAIZEN',
​        'JUST IN TIME', 'TOC', 'TEORIA DE RESTRICCIONES', 'ANALISIS DE PARETO',
​        'FMEA', 'CAUSA RAIZ', '5 PORQUES', 'MAPEO DE PROCESOS',
        # Investigación científica
​        'ENCUESTA', 'ENTREVISTA', 'OBSERVACIÓN', 'FOCUS GROUP', 'DELPHI',
​        'ANÁLISIS FACTORIAL', 'REGRESIÓN', 'CORRELACIÓN', 'CHI-CUADRADO', 'ANOVA',
​        'CRONBACH', 'KAISER', 'BARTLETT', 'LIKERT', 'SPSS', 'R STUDIO',
​        'ANALISIS MULTIVARIANTE', 'REGRESION LOGISTICA', 'CLUSTER ANALYSIS',
        # Tecnológicas
​        'MACHINE LEARNING', 'BIG DATA', 'BLOCKCHAIN', 'IOT', 'INTELIGENCIA ARTIFICIAL',
​        'CRM', 'ERP', 'API', 'UX', 'UI', 'DEVOPS', 'CLOUD COMPUTING',
​        'BUSINESS INTELLIGENCE', 'DATA MINING', 'ANALYTICS', 'DASHBOARD',
        # Educativas
​        'CONSTRUCTIVISMO', 'CONDUCTISMO', 'COGNITIVISMO', 'BLOOM', 'KIRKPATRICK',
​        'ADDIE', 'MOODLE', 'LMS', 'E-LEARNING', 'FLIPPED CLASSROOM',
        # Salud
​        'ENSAYO CONTROLADO', 'PLACEBO', 'DOBLE CIEGO', 'META-ANÁLISIS', 'REVISIÓN SISTEMÁTICA',
        # Marketing
​        'SEM', 'SEO', 'SOCIAL MEDIA', 'INBOUND', 'FUNNEL', 'KPI', 'CTR', 'CAC', 'LTV',
        # Psicología/Sociología
​        'GROUNDED THEORY', 'FENOMENOLOGÍA', 'ETNOGRAFÍA', 'ANÁLISIS DE CONTENIDO'
​    ]
​    