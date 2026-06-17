#!/usr/bin/env python3
"""
Configuración del Sistema de Validación de Referencias
=====================================================

Este archivo contiene configuraciones específicas para la validación
de referencias bibliográficas en diferentes estilos y idiomas.
"""

# Configuración de estilos de cita
ESTILOS_CONFIGURACION = {
    "apa": {
        "nombre_completo": "American Psychological Association (APA) 7th Edition",
        "patrones": {
            "autor": {
                "formato": "Apellido, I. M.",
                "regex": r"^[A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+,\s*[A-Z]\.(?:\s*[A-Z]\.)?",
                "ejemplos": ["García, J.", "Martínez, A. M.", "Smith, J. K."],
            },
            "anio": {
                "formato": "(YYYY)",
                "regex": r"\(\d{4}[a-z]?\)",
                "ejemplos": ["(2023)", "(2021a)", "(2020)"],
            },
            "titulo_articulo": {
                "formato": "Título del artículo.",
                "regex": r"[A-ZÁÉÍÓÚÜ][^.]+\.",
                "ejemplos": [
                    "Efectos del cambio climático.",
                    "Machine learning applications.",
                ],
            },
            "titulo_revista": {
                "formato": "Título de la Revista",
                "regex": r"[A-ZÁÉÍÓÚÜ][^,]+",
                "ejemplos": ["Nature", "Revista de Psicología", "Journal of Science"],
            },
            "volumen": {
                "formato": "Vol(Num)",
                "regex": r"\b\d+\(\d+\)",
                "ejemplos": ["45(3)", "12(1)", "89(12)"],
            },
            "paginas": {
                "formato": "pp. 123-456",
                "regex": r"pp?\.\s*\d+-\d+",
                "ejemplos": ["pp. 123-145", "p. 67", "pp. 890-912"],
            },
            "doi": {
                "formato": "https://doi.org/10.1000/xxx",
                "regex": r"https?://doi\.org/10\.\d+/[^\s]+",
                "ejemplos": ["https://doi.org/10.1038/nature12373"],
            },
            "url": {
                "formato": "https://www.ejemplo.com",
                "regex": r"https?://[^\s]+",
                "ejemplos": ["https://www.nature.com/articles/123"],
            },
        },
        "reglas_especiales": [
            "El apellido del autor debe ir primero, seguido de las iniciales",
            "El año debe estar entre paréntesis inmediatamente después del autor",
            "Solo la primera letra del título y nombres propios van en mayúscula",
            "El nombre de la revista debe estar en cursiva (o capitalizado)",
            "Incluir DOI cuando esté disponible",
        ],
    },
    "ieee": {
        "nombre_completo": "Institute of Electrical and Electronics Engineers (IEEE)",
        "patrones": {
            "autor": {
                "formato": "I. M. Apellido",
                "regex": r"[A-Z]\.\s*(?:[A-Z]\.\s*)?[A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+",
                "ejemplos": ["J. García", "A. M. Martínez", "J. K. Smith"],
            },
            "titulo_articulo": {
                "formato": '"Título del artículo,"',
                "regex": r'"[^"]+",',
                "ejemplos": [
                    '"Machine learning applications,"',
                    '"Efectos del clima,"',
                ],
            },
            "titulo_revista": {
                "formato": "Título de la Revista",
                "regex": r"[A-ZÁÉÍÓÚÜ][^,]+",
                "ejemplos": ["IEEE Trans. Pattern Anal.", "Nature Communications"],
            },
            "volumen": {
                "formato": "vol. 45, no. 3",
                "regex": r"vol\.\s*\d+,\s*no\.\s*\d+",
                "ejemplos": ["vol. 45, no. 3", "vol. 12, no. 1"],
            },
            "paginas": {
                "formato": "pp. 123-456",
                "regex": r"pp\.\s*\d+-\d+",
                "ejemplos": ["pp. 123-145", "pp. 890-912"],
            },
            "anio": {
                "formato": "Mes YYYY",
                "regex": r"[A-Z][a-z]+\.?\s*\d{4}",
                "ejemplos": ["Jan. 2023", "December 2021", "Mar. 2020"],
            },
        },
        "reglas_especiales": [
            "Las iniciales van antes del apellido",
            "Los títulos de artículos van entre comillas",
            "Usar abreviaciones estándar para nombres de revistas",
            "El formato de fecha incluye mes y año",
            "Numeración secuencial [1], [2], etc.",
        ],
    },
    "mla": {
        "nombre_completo": "Modern Language Association (MLA) 8th Edition",
        "patrones": {
            "autor": {
                "formato": "Apellido, Nombre",
                "regex": r"[A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+,\s*[A-ZÁÉÍÓÚÜ][a-záéíóúüñ]+",
                "ejemplos": ["García, Juan", "Smith, John", "Martínez, Ana María"],
            },
            "titulo_articulo": {
                "formato": '"Título del Artículo."',
                "regex": r'"[^"]+\."',
                "ejemplos": [
                    '"Machine Learning Applications."',
                    '"Efectos del Cambio Climático."',
                ],
            },
            "titulo_revista": {
                "formato": "Título de la Revista,",
                "regex": r"[A-ZÁÉÍÓÚÜ][^,]+,",
                "ejemplos": ["Nature,", "Revista de Psicología,"],
            },
            "fecha": {
                "formato": "DD Mes YYYY",
                "regex": r"\d{1,2}\s*[A-Z][a-z]+\.?\s*\d{4}",
                "ejemplos": ["15 Mar. 2023", "3 December 2021"],
            },
        },
        "reglas_especiales": [
            "Nombre completo del autor (no solo iniciales)",
            "Títulos de artículos entre comillas",
            "Títulos de publicaciones en cursiva",
            "Fecha completa cuando esté disponible",
            "URL y fecha de acceso para fuentes web",
        ],
    },
}

# Configuración de idiomas
IDIOMAS_CONFIGURACION = {
    "español": {
        "palabras_clave_referencias": [
            "referencias bibliográficas",
            "bibliografía",
            "referencias",
            "fuentes consultadas",
            "obras citadas",
        ],
        "indicadores_autor": ["por", "de", "autor:", "autores:"],
        "indicadores_fecha": ["año", "fecha", "publicado"],
        "editoriales_comunes": [
            "editorial",
            "ediciones",
            "ed.",
            "editores",
            "universidad",
            "instituto",
            "centro",
        ],
    },
    "english": {
        "palabras_clave_referencias": [
            "references",
            "bibliography",
            "works cited",
            "literature cited",
            "sources",
        ],
        "indicadores_autor": ["by", "author:", "authors:"],
        "indicadores_fecha": ["year", "date", "published"],
        "editoriales_comunes": [
            "press",
            "publisher",
            "publications",
            "university",
            "institute",
            "center",
            "foundation",
            "society",
        ],
    },
}

# Configuración de tipos de publicación
TIPOS_PUBLICACION = {
    "articulo_revista": {
        "componentes_requeridos": [
            "autor",
            "anio",
            "titulo_articulo",
            "titulo_revista",
            "volumen",
            "paginas",
        ],
        "componentes_opcionales": ["doi", "url"],
        "peso_validacion": 1.0,
    },
    "libro": {
        "componentes_requeridos": ["autor", "anio", "titulo", "editorial", "ciudad"],
        "componentes_opcionales": ["isbn", "url"],
        "peso_validacion": 0.9,
    },
    "capitulo_libro": {
        "componentes_requeridos": [
            "autor",
            "anio",
            "titulo_capitulo",
            "editor",
            "titulo_libro",
            "editorial",
            "paginas",
        ],
        "componentes_opcionales": ["isbn"],
        "peso_validacion": 0.8,
    },
    "tesis": {
        "componentes_requeridos": [
            "autor",
            "anio",
            "titulo",
            "tipo_tesis",
            "institucion",
        ],
        "componentes_opcionales": ["url", "repositorio"],
        "peso_validacion": 0.7,
    },
    "web": {
        "componentes_requeridos": [
            "autor_o_organizacion",
            "anio_o_fecha",
            "titulo",
            "url",
        ],
        "componentes_opcionales": ["fecha_acceso"],
        "peso_validacion": 0.6,
    },
}

# Configuración de errores comunes y sugerencias
ERRORES_COMUNES = {
    "apa": {
        "falta_parentesis_anio": {
            "descripcion": "El año no está entre paréntesis",
            "sugerencia": "Colocar el año entre paréntesis: (2023)",
            "gravedad": "media",
        },
        "formato_autor_incorrecto": {
            "descripcion": "El formato del autor no sigue el estándar APA",
            "sugerencia": "Usar formato: Apellido, I. M.",
            "gravedad": "alta",
        },
        "titulo_mayusculas": {
            "descripcion": "El título tiene mayúsculas incorrectas",
            "sugerencia": "Solo la primera letra y nombres propios en mayúscula",
            "gravedad": "media",
        },
        "falta_doi": {
            "descripcion": "Falta el DOI cuando está disponible",
            "sugerencia": "Incluir DOI en formato: https://doi.org/10.xxxx/xxxx",
            "gravedad": "baja",
        },
    },
    "ieee": {
        "orden_autor_incorrecto": {
            "descripcion": "Las iniciales deben ir antes del apellido",
            "sugerencia": "Usar formato: I. M. Apellido",
            "gravedad": "alta",
        },
        "titulo_sin_comillas": {
            "descripcion": "El título del artículo debe estar entre comillas",
            "sugerencia": 'Formato: "Título del artículo,"',
            "gravedad": "media",
        },
    },
}

# Configuración de umbrales de validación
UMBRALES_VALIDACION = {
    "puntuacion_minima_aprobado": 0.7,
    "puntuacion_minima_excelente": 0.9,
    "porcentaje_referencias_validas_minimo": 80,
    "longitud_minima_referencia": 30,
    "longitud_maxima_referencia": 1000,
}

# Configuración de salida de informes
CONFIGURACION_INFORMES = {
    "incluir_ejemplos": True,
    "incluir_sugerencias_detalladas": True,
    "incluir_estadisticas": True,
    "incluir_graficos": False,  # Para futuras implementaciones
    "formato_fecha": "%d de %B de %Y",
    "idioma_informe": "español",
}
