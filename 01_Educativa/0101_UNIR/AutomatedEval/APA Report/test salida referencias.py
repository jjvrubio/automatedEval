import re
import json

# Input JSON with split references
references = [
    "8. REFERENCIAS",
    "ACAN, Asociación Clúster de Automoción de Navarra. (10 de 2017). La industria 4.0.",
    "Tecnologías habilitadoras. Blog / Industria 4.0:",
    "https://clusterautomocionnavarra.com/wp-content/uploads/2017/10/ACAN-",
    "Tecnolog%C3%ADas_habilitadoras.pdf",
    "Atrio Agencia S.A.S. (12 de 2 de 2024). Las 7 Tendencias de Consumo que Dominarán el 2024:",
    "Preparando a las Marcas para el Futuro. linkedin:",
    "https://www.linkedin.com/pulse/las-7-tendencias-de-consumo-que-",
    "dominar%C3%A1n-el-2024-0t7ee/",
    "Bengochea, D. (07 de 2022). 16 KPIs obligatorios para medir el rendimiento de un",
    "eCommerce. Outvio / Blog: https://outvio.com/es/blog/kpi-ecommerce/",
    "Benítez Aranda, S. (2009). La Artesanía latinoamericana como Factor de Desarrollo",
    "Económico, Social y Cultural: a la luz de los nuevos conceptos de cultura y desarrollo.",
    "(UNESCO, Ed.) Revista Cultura y Desarrollo, 1-19.",
    "http://documentacion.cidap.gob.ec/cgi-bin/koha/opac-detail.pl?biblionumber=5865",
    "Bustos Flores, C. (2009). La producción artesanal. (U. d. Andes, Ed.) Visión Gerencial(1), 37-",
    "52. https://www.redalyc.org/pdf/4655/465545880009.pdf",
    "CAMTIC, Cámara de Tecnologías de Información y Comunicación. (2022). Informe de",
    "Chequeo Digital ofrece recomendaciones para transformación digital de empresas.",
    "Actualidad TIC: https://www.camtic.org/actualidad-tic/informe-de-chequeo-digital-",
    "ofrece-recomendaciones-para-transformacion-digital-de-empresas/",
    "Centro de Comercio Internacional. (2020). Artesanías. Nuestro trabajo>Temas>Bienes y",
    "servicios: https://intracen.org/es/nuestra-labor/temas/bienes-y-servicios/artesanias",
    "Cibrián Barredo, I. (2018). Marketing digital. Mide, analiza y mejora (1ra. ed.). Madrid: ESIC",
    "Editorial.",
    'CIDAP. (2019). Expediente "Cuenca ciudad artesanal", para la designación de Cuenca como',
    "Ciudad Mundial de las Artesanías. Repositorio Digital CIDAP:",
    "http://documentacion.cidap.gob.ec:8080/handle/cidap/2107",
    "Colombia.com. (20 de 11 de 2013). Etno-Artesanía, Neo-Artesanía y Eco-Artesanía",
    "tendencias que marcan la historia. Colombia.com - Tecnología:",
    "https://www.colombia.com/tecnologia/eventos/sdi/75320/etno-artesania-neo-",
    "artesania-y-eco-artesania-tendencias-que-marcan-la-historia",
    "Consejería de Transformación Económica, Industria, Conocimiento y Universidades de la",
    "Junta de Andalucía. (2021). Modelo de madurez digital. Programa Empresa Digital:",
    "https://www.programaempresadigital.es/documents/20182/0/Modelo+de+Empresa",
    "+Digital/27cb798a-e165-42c5-a86b-1d003c6e9ee3",
    "Cordero Merchán, A., & Urgilés Figueroa, D. (2019). Propuesta de aplicación de una",
    "plataforma de comercio electrónico para la internacionalización de artesanías",
    "tradicionales del Azuay hacia la Unión Europea. Trabajo de graduación, Universidad",
    "del Azuay, Facultad de Ciencias Jurídicas.",
    "https://dspace.uazuay.edu.ec/handle/datos/8807",
    "Czaplewski, M. (2018). The use of e-commerce in the promotion and sale of hand made",
    "products. Management, 22(1), 154-162. https://doi.org/10.2478/manment-2018-",
    "0011.",
    "D’artesano. (8 de 5 de 2020). Interiorismo Artesanal, una Tendencia en Aumento. Tendencia",
    "emergente: El interiorismo artesanal como estilo sustentable. blogs/blog-dartesano:",
    "https://dartesano.com.mx/blogs/blog-dartesano/interiorismo-artesanal-una-",
    "tendencia-en-aumento",
    "Diaz, D. (05 de 2020). KPI Ecommerce: 20 métricas importantes para analizar. Nirvine KPI /",
    "Blog: https://nirvine.com/blog/kpi-ecommerce/",
    "Elósegui, T., & Muñoz, G. (2015). Marketing Analytics (1ra. ed.). Madrid: Anaya Multimedia.",
    "EMR, Expert Market Research. (2023). Visión General del Mercado de Artesanías. Bienes de",
    "Consumo y Servicios/ Muebles y accesorios para el hogar/Mercado de Artesanía:",
    "https://www.informesdeexpertos.com/informes/mercado-de-artesania",
    "Etienne-Nugue, J. (01 de 2009). Háblame de la... Artesanía. (UNESCO, Ed.) París.",
    "https://unesdoc.unesco.org/ark:/48223/pf0000181443",
    "Euromonitor. (1 de 2018). Las 10 principales tendencias globales de consumo para 2018.",
    "Insights/Whitepapers: https://go.euromonitor.com/white-paper-economies-",
    "consumers-2018-global-consumer-trends-",
    "SP.html?utm_campaign=CT_WP_18_01_16_Top%252010%2520GCT25202018%2520",
    "SP&utm_medium=Blog&utm_source=Blog&utm_content=&utm_term=",
    "Euromonitor. (1 de 2019). Las 10 principales tendencias globales de consumo para 2019.",
    "Insights/Whitepapers: https://go.euromonitor.com/white-paper-EC_2019-10-",
    "principales-tendencias-globales-de-consumo-para-",
    "2019.html?utm_source=blog&utm_medium=blog&utm_campaign=CT_WP_19_01_1",
    "5_Top2010%20GCT202019%20SP&utm_content=organic",
    "Everything Tienda. (26 de 6 de 2023). El movimiento Slow Fashion. Artesanía y sostenibilidad.",
    "Moda: https://everythingtienda.com/el-movimiento-slow-fashion-artesania-y-",
    "sostenibilidad/",
    "EY Latin America North. (2022). Estudio de Madurez Digital 2022. Transformación de la",
    "tecnología: https://www.ey.com/es_ec/transformacion-con-sentido/nuevo-ritmo-de-",
    "madurez-digital",
    "Ferro Monroy, D. (2017). Identidad, cultura e innovación en las artesanías: un camino para el",
    "desarrollo sustentable y el Buen Vivir. (U. A. Bolívar, Ed.) Estudios de la Gestión:",
    "revista internacional de administración(1), 95-116.",
    "https://repositorio.uasb.edu.ec/handle/10644/5477",
    "Forbes, Newsletter. (22 de 03 de 2023). Los consumidores cada vez valoran más los",
    "productos sostenibles, artesanales y de proximidad. Actualidad:",
    "https://forbes.es/actualidad/251889/los-consumidores-cada-vez-valoran-mas-los-",
    "productos-sostenibles-artesanales-y-de-proximidad/",
    "Genwords. (05 de 2024). Los Mejores KPIs para eCommerce. Genwords / Blog:",
    "https://www.genwords.com/blog/mejores-kpis-para-ecommerce",
    "González Varona, J. (2021). Retos para la Transformación Digital de las PYMES: Competencia",
    "Organizacional para la Transformación Digital. Tesis Doctoral, Universidad de",
    "Valladolid, Escuela de Doctorado, Valladolid.",
    "https://www.researchgate.net/publication/353828728_Retos_para_la_Transformaci",
    "on_Digital_de_las_PYMES_Competencia_Organizacional_para_la_Transformacion_Di",
    "gital",
    "Granda, M., & Campoverde, J. (2022). ¿Cuál es el nivel de digitalización de las empresas en",
    "Ecuador? Una aproximación a través de la herramienta Chequeo Digital. Reporte",
    "2020-2021. (E. d. ESPAE, Ed.) ESPAE Escuela de Negocios > Blog > Publicaciones >",
    "Reportes de Investigación: https://www.espae.edu.ec/maria-granda-",
    "publicaciones/cual-es-el-nivel-de-digitalizacion-de-las-empresas-en-ecuador-una-",
    "aproximacion-a-traves-de-la-herramienta-chequeo-digital-reporte-2020-2021/",
    "Grupo Atico34. (2024). Stakeholders: Qué son, tipos y ejemplos. Blog / Compliance:",
    "https://protecciondatos-lopd.com/empresas/stakeholders/",
    "Hernández, L. (13 de 01 de 2024). Análisis de datos para artesanos: Comprende tus métricas",
    "y optimiza tus estrategias. Producción Artesanal Digital/Comercio Digital:",
    "https://produccionartesanal.net/comercio-digital/analisis-datos-artesanos-",
    "comprende-tus-metricas-optimiza-tus-estrategias/",
    "IBM. (05 de 2024). ¿Qué es la Industria 4.0? Topics / What is Industry 4.0 and how does it",
    "work?: https://www.ibm.com/es-es/topics/industry-4-0",
    "Inesdi. (11 de 10 de 2023). Super apps: qué son y cómo cambiarán el mundo digital.",
    "Bolg/Tech: https://www.inesdi.com/blog/super-apps/",
    "Inesdi, & Three Points. (2023). Think Digital Report 2021 y 2022. Think Digital Summit:",
    "https://thinkdigitalsummit.online/think-digital-report/",
    "Jalil Vélez, N., Roque Doval, Y., Garcés González, R., & Naranjo Flores, C. (2021). El papel de",
    "la artesanía en los procesos de reconversión económica rural en Ecuador. Estudios",
    "Del Desarrollo Social: Cuba Y América Latina, 9(Especial 2).",
    "https://revistas.uh.cu/revflacso/article/view/3771",
    "Junta de Andalucía. (2021). Modelo de Madurez Digital. Transformación digital de la pyme:",
    "https://www.programaempresadigital.es/web/guest/autodiagnostico-digital",
    "Kaushik, A. (2010). Analítica Web 2.0 (1ra. ed.). Barcelona: Gestión 2000.",
    "Ken , A. (08 de 2023). Los mejores KPIs para tu eCommerce. Blog / Marketing:",
    "https://www.gluo.mx/blog/los-mejores-kpis-para-tu-ecommerce",
    "La Caja Company. (2024). Tendencias de Consumo 2024: ¿Cúales tendencias de Consumidor",
    "impulsarán el marketing? Blog/Tendencias de marketing:",
    "https://lacaja.company/blog/tendencias-de-consumo-2024-la-evolucion-de-la-",
    "experiencia-del-consumidor/",
    "Landívar Andrade, M. (2088). La artesanías en el Ecuador: definiciones, políticas y",
    "perspectivas. Universidad Politécnica Salesiana, Desarrollo Local, Quito.",
    "https://dspace.ups.edu.ec/handle/123456789/16705",
    "López, J. (06 de 2017). Tecnologías habilitadoras de la Industria 4.0. Factoría del Futuro /",
    "Blog: https://www.factoriadelfuturo.com/tecnologias-habilitadoras/",
    "Lorenzo, O. (2016). Modelos de Madurez Digital: ¿en qué consisten y qué podemos aprender",
    "de ellos? Boletín de Estudios Económicos, LXXI(219), 573-590.",
    "https://www.researchgate.net/publication/313798566_Modelos_de_Madurez_Digit",
    "al_en_que_consisten_y_que_podemos_aprender_de_ellos/related",
    "Mendoza Ríos, V. H. (2023). Qué son los stakeholders y métodos para su análisis. (U. A.",
    "Hidalgo, Editor) Divulgacion de la ciencia: https://www.uaeh.edu.mx/divulgacion-",
    "ciencia/stakeholders-metodos/",
    "Miranda Daconte, A. (2022). Plataforma web para consumo colaborativo de artesanías en",
    "Colombia. Trabajo Fin de Máster, Universidad Internacional de La Rioja , Escuela",
    "Superior de Ingeniería y Tecnología, Barraquilla.",
    "https://reunir.unir.net/handle/123456789/14002",
    "Navarro-Hoyos, S. (2015). Como la artesanía entra al mundo de la comercialización y sus",
    "características. silvananavarro.com/post:",
    "https://www.silvananavarro.com/post/2015-1-23-como-la-artesan%C3%ADa-entra-",
    "al-mundo-de-la-comercializaci%C3%B3n-y-sus-caracter%C3%ADsticas",
    "Orna, A. (29 de 4 de 2024). Cinco tendencias de decoración para el 2024. (I. M. La Metro,",
    "Editor) MetroNews: https://lametro.edu.ec/cinco-tendencias-de-decoracion-para-el-",
    "2024/",
    "Oyarzún, G. (24 de 01 de 2024). Estudio de mercado de artesanías: estructura, proyección y",
    "demanda. (EspacioEmpresa, Editor) espacioempresa.com/emprendedores/:",
    "https://espacioempresa.com/emprendedores/estudio-mercado-artesanias/",
    "PROCOLOMBIA. (13 de 12 de 2019). Alemania, Francia y Reino Unido, encabezaron compras",
    "de artesanías colombianas. procolombia.co/noticias:",
    "https://prensa.procolombia.co/alemania-francia-y-reino-unido-encabezaron-",
    "compras-de-artesanias-colombianas",
    "PROECUADOR. (11 de 06 de 2017). Artesanías ecuatorianas cautivan a empresa",
    "estadounidense. proecuador.gob.ec/Noticias:",
    "https://www.proecuador.gob.ec/artesanias-ecuatorianas-cautivan-a-empresa-",
    "estadounidense/",
    "PROECUADOR. (1 de 05 de 2024). Tratado de Libre Comercio entre Ecuador y China entrará",
    "en vigencia el 01 de mayo. Noticias: https://www.produccion.gob.ec/tratado-de-",
    "libre-comercio-entre-ecuador-y-china-entrara-en-vigencia-el-01-de-mayo/",
    "Reset. (12 de 2023). Tendencias del mercado y hábitos del consumidor para 2024.",
    "(Bancolombia, Editor) Marketing Digital:",
    "https://resetmarketingdigital.com/tendencias-mercado-habitos-consumidor-2024",
    "Rivera, C. (26 de 12 de 2023). Conquistando la Red: Estrategias de Marketing Digital para",
    "Artesanos Modernos. Producción Artesanal Digital/Comercio Digital:",
    "https://produccionartesanal.net/comercio-digital/conquistando-red-estrategias-",
    "marketing-digital-artesanos-modernos/",
    "Rivera, C. (22 de 12 de 2023). Redes Sociales Nicho: Dónde Promocionar Artesanías Fuera de",
    "los Canales Convencionales. Producción Artesanal Digital/Comercio Digital:",
    "https://produccionartesanal.net/comercio-digital/redes-sociales-nicho-donde-",
    "promocionar-artesanias-fuera-canales-convenciona/",
    "Sánchez Sisa, C. (2022). El proceso de comercialización de productos artesanales y la",
    "permanencia en el mercado de la asociación de Artesanos Productores en Arte y",
    "Artesanías. Universidad Técnica del Norte, Facultad de Ciencias Administrativas y",
    "Económicas, Ibarra. https://repositorio.utn.edu.ec/handle/123456789/12053",
    "SAP. (03 de 2024). ¿Qué es la industria 4.0? Soluciones de SAP para la Industria 4.0:",
    "https://www.sap.com/latinamerica/products/scm/industry-4-0/what-is-industry-4-",
    "0.html#:~:text=Definici%C3%B3n%20de%20Industria%204.0&text=Abarca%20un%20",
    "conjunto%20de%20tecnolog%C3%ADas,la%20creaci%C3%B3n%20de%20f%C3%A1bri",
    "cas%20inteligentes.",
    "Sheykin, H. (3 de 04 de 2024). Top 7 Estrategias de rentabilidad para el mercado artesanal:",
    "¡aumente sus ventas! finmodelslab.com/es/blogs/:",
    "https://finmodelslab.com/es/blogs/profitability/artisan-marketplace-profitability",
    "Shopify. (01 de 2014). 32 indicadores clave de rendimiento (KPIs) para el comercio",
    "electrónico. Shopify / Blog / Ecommerce:",
    "https://www.shopify.com/es/blog/11925985-32-indicadores-clave-de-rendimiento-",
    "kpis-para-el-comercio-electronico",
    "Suárez Hernández, F. (15 de 1 de 2024). Top 10 de tendencias y acciones sostenibles que",
    "deberían avanzar más en 2024. Portada / Red Forbes /:",
    "https://www.forbes.com.mx/top-10-de-tendencias-y-acciones-sostenibles-que-",
    "deberian-avanzar-mas-en-2024/",
    "Tableau, S. (05 de 2024). Guía de visualización de datos: definición, ejemplos y recursos de",
    "aprendizaje. Tableau / Artículos: https://www.tableau.com/es-es/learn/articles/data-",
    "visualization",
    "UADIN, Business School. (05 de 2024). Tecnologías habilitadoras de la Industria 4.0: ¿Cuáles",
    "son? UADIN Business School / Blog: https://www.uadin.com/noticias/tecnologias-",
    "habilitadoras-industria-40-cuales-son/",
    "UNESCO. (2003). ¿Qué es el patrimonio cultural inmaterial? UNESCO/Cultura/Patrimonio",
    "inmaterial/Convención/¿Qué es el patrimonio inmaterial?:",
    "https://ich.unesco.org/es/que-es-el-patrimonio-inmaterial-00003",
    "UNESCO. (2003). Técnicas artesanales tradicionales. UNESCO/Cultura/Patrimonio",
    "inmaterial/Convención/Ámbitos del patrimonio inmaterial/Técnicas artesanales",
    "tradicionales: https://ich.unesco.org/es/tcnicas-artesanales-tradicionales-00057",
    "Verbo, J. (05 de 2024). 12 tecnologías habilitadoras dentro del marco de la Industria 4.0 para",
    "la generación de nuevos modelos de negocio. Grupo Cibernos / Blog:",
    "https://www.grupocibernos.com/blog/12-tecnologias-habilitadoras-dentro-del-",
    "marco-de-la-industria-4-0",
    "Villalba Chamorro, A. (2023). La Economía Circular desde las experiencias de las Artesanas",
    "textiles de la ciudad de Pilar, Paraguay. Ciencia Latina Revista Científica",
    "Multidisciplinar, 7(4), 6943-6965.",
    "https://doi.org/https://doi.org/10.37811/cl_rcm.v7i4.7454",
    "Westerman, G., Bonnet, D., & McAfee, A. (2012). The Advantages of Digital Maturity. MIT",
    "Sloan Management Review. https://sloanreview.mit.edu/article/the-advantages-of-",
    "digital-maturity/",
]


# Utility function for debug output
def debug_output(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# Step 0: Detector and splitter for embedded references
def detect_and_split_embedded_references(references):
    embedded_indices = []
    split_references = []
    author_year_pattern = r"[A-Za-z0-9.,&\s]+\.?\s*\((\d{4}|s\.f\.|s\.f)\)\s*"

    for i, line in enumerate(references):
        matches = list(re.finditer(author_year_pattern, line))
        if len(matches) > 1:  # Multiple references found in the same line
            embedded_indices.append(i)
            last_start = 0

            for j, match in enumerate(matches):
                start, end = match.span()

                if j == 0:  # First match
                    split_references.append(
                        line[:start].strip() + line[start:end].strip()
                    )
                else:  # Subsequent matches
                    split_references.append(
                        line[last_start:start].strip() + line[start:end].strip()
                    )

                last_start = end

            if last_start < len(line):
                split_references.append(
                    line[last_start:].strip()
                )  # Remaining text after the last match
        else:
            split_references.append(line)

    # Debug output for embedded references and split results
    debug_output(
        "detected_embedded_references.json",
        {"embedded_indices": embedded_indices, "split_references": split_references},
    )
    return split_references


# Step 1A: Identify offending lines
def identify_offending_lines(references):
    author_year_pattern = r"^[A-Za-z0-9.,&\s]+\.?\s*\((\d{4}|s\.f\.|s\.f)\)\s*"
    offending_indices = []

    for i, line in enumerate(references):
        if not re.match(author_year_pattern, line):
            offending_indices.append(i)

    # Debug output for offending lines
    debug_output(
        "identify_offending_lines.json", [references[i] for i in offending_indices]
    )
    return offending_indices


# Step 1B: Merge offending lines with the previous line
def merge_offending_lines(references, offending_indices):
    merged_references = []
    current_ref = ""

    for i, line in enumerate(references):
        if i in offending_indices:  # Merge with the previous line
            current_ref += " " + line.strip()
        else:
            if current_ref:  # Finalize the current merged reference
                merged_references.append(current_ref.strip())
            current_ref = line.strip()

    if current_ref:  # Append the last reference if it exists
        merged_references.append(current_ref.strip())

    # Debug output for merged references
    debug_output("merge_offending_lines.json", merged_references)
    return merged_references


# Main orchestration function
def main():
    # Step 0: Detect and split embedded references
    split_references = detect_and_split_embedded_references(references)

    # Step 1A: Identify offending lines
    offending_indices = identify_offending_lines(split_references)

    # Step 1B: Merge offending lines
    merged_references = merge_offending_lines(split_references, offending_indices)

    print("Processing completed. Debug outputs saved for each step.")


# Run the main function
if __name__ == "__main__":
    main()
