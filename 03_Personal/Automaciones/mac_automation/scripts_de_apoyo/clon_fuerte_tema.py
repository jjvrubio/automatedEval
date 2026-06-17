#!/usr/bin/env python3
from __future__ import annotations

import argparse
import posixpath
import re
import tempfile
import unicodedata
import xml.etree.ElementTree as ET
from copy import deepcopy
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


DEFAULT_TEMAS = Path(
    "/Users/juanjo/Library/CloudStorage/OneDrive-KALEIDAGEOGRAFIAS&MERCADOSSL/"
    "UNIR/Actualización de Contenidos/Ecosistema Digital y Tecnologías Disruptivas/"
    "Curso 2026/TEMAS"
)

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_PR = "http://schemas.openxmlformats.org/package/2006/relationships"
NS_WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS_CT = "http://schemas.openxmlformats.org/package/2006/content-types"
NS = {"w": NS_W, "r": NS_R, "pr": NS_PR, "wp": NS_WP, "ct": NS_CT}

PARTES_RELACIONADAS_TEMPLATE = (
    "word/styles.xml",
    "word/theme/theme1.xml",
    "word/fontTable.xml",
    "word/settings.xml",
    "word/webSettings.xml",
)

TEXTOS_PRELIMINARES = {
    "indice",
    "índice",
    "table of contents",
    "lista de figuras",
    "lista de tablas",
    "esquema",
    "ideas clave",
    "key ideas",
    "resumen",
    "summary",
}

TEXTOS_SUFFIX_TEMPLATE = {
    "a fondo",
    "test",
}

SINONIMOS_ESTILO: dict[str, list[str]] = {
    "author": ["textoindependiente", "normal"],
    "date": ["textoindependiente", "normal"],
    "firstparagraph": ["textoindependiente", "normal"],
    "blocktext": ["textoindependiente", "normal"],
    "title": ["ttulo1", "textoindependiente", "normal"],
    "tocheading": ["ttulo1", "normal"],
}

PPR_LAYOUT_TAGS = (
    "spacing",
    "ind",
    "jc",
    "tabs",
    "contextualSpacing",
    "mirrorIndents",
)

HEADING_STYLE_IDS = ("Ttulo1", "Ttulo2", "Ttulo3")
TOC2_STYLE_IDS = {"TDC2", "TOC2", "toc2"}
TOC2_TITLE_LEFT = 5240
TOC2_HANGING = "419"
TOC2_LEFT = str(TOC2_TITLE_LEFT + int(TOC2_HANGING))
TOC2_PAGE_TAB = "9822"
REL_TYPE_HEADER = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"
REL_TYPE_FOOTER = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer"
CONTENT_TYPE_HEADER = "application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"
CONTENT_TYPE_FOOTER = "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"
REV_TEMA_RE = re.compile(r"tema_(\d+)_rev\.docx$", re.IGNORECASE)


def normalizar_texto(texto: str) -> str:
    t = " ".join(texto.split()).strip().lower()
    t = "".join(ch for ch in unicodedata.normalize("NFKD", t) if not unicodedata.combining(ch))
    return t


def normalizar_nombre_estilo(texto: str) -> str:
    return "".join(ch for ch in normalizar_texto(texto) if ch.isalnum())


def qn_w(tag: str) -> str:
    return f"{{{NS_W}}}{tag}"


def qn_r(tag: str) -> str:
    return f"{{{NS_R}}}{tag}"


def leer_zip(path: Path) -> dict[str, bytes]:
    with ZipFile(str(path), "r") as zf:
        return {name: zf.read(name) for name in zf.namelist()}


def parse_xml(blobs: dict[str, bytes], part: str) -> ET.Element | None:
    data = blobs.get(part)
    if data is None:
        return None
    return ET.fromstring(data)


def obtener_style_id_parrafo(parrafo: ET.Element) -> str:
    pstyle = parrafo.find("./w:pPr/w:pStyle", NS)
    if pstyle is None:
        return ""
    return pstyle.attrib.get(qn_w("val"), "")


def definir_style_id_parrafo(parrafo: ET.Element, style_id: str) -> None:
    if not style_id:
        return

    ppr = parrafo.find("w:pPr", NS)
    if ppr is None:
        ppr = ET.Element(qn_w("pPr"))
        parrafo.insert(0, ppr)

    pstyle = ppr.find("w:pStyle", NS)
    if pstyle is None:
        pstyle = ET.Element(qn_w("pStyle"))
        ppr.insert(0, pstyle)
    pstyle.attrib[qn_w("val")] = style_id


def asegurar_ppr(parrafo: ET.Element) -> ET.Element:
    ppr = parrafo.find("w:pPr", NS)
    if ppr is None:
        ppr = ET.Element(qn_w("pPr"))
        parrafo.insert(0, ppr)
    return ppr


def extraer_estilos_por_id(styles_root: ET.Element | None) -> dict[str, str]:
    if styles_root is None:
        return {}

    estilos: dict[str, str] = {}
    for estilo in styles_root.findall("w:style", NS):
        sid = estilo.attrib.get(qn_w("styleId"), "")
        if not sid:
            continue
        nombre = estilo.find("w:name", NS)
        estilos[sid] = nombre.attrib.get(qn_w("val"), "") if nombre is not None else ""
    return estilos


def es_parrafo_heading(parrafo: ET.Element, styles_map: dict[str, str]) -> bool:
    style_id = obtener_style_id_parrafo(parrafo)
    style_name = styles_map.get(style_id, "")
    joined = f"{style_name} {style_id}".lower()
    candidatos = (
        "heading 1",
        "heading 2",
        "heading 3",
        "heading1",
        "heading2",
        "heading3",
        "título 1",
        "título 2",
        "título 3",
        "titulo 1",
        "titulo 2",
        "titulo 3",
        "ttulo1",
        "ttulo2",
        "ttulo3",
    )
    return any(c in joined for c in candidatos)


def texto_parrafo(parrafo: ET.Element) -> str:
    return "".join(node.text or "" for node in parrafo.findall(".//w:t", NS))


def asignar_texto_parrafo(parrafo: ET.Element, texto: str) -> None:
    text_nodes = parrafo.findall(".//w:t", NS)
    if text_nodes:
        text_nodes[0].text = texto
        for node in text_nodes[1:]:
            node.text = ""
        return

    run = parrafo.find("w:r", NS)
    if run is None:
        run = ET.SubElement(parrafo, qn_w("r"))
    ET.SubElement(run, qn_w("t")).text = texto


def es_texto_preliminar(texto: str) -> bool:
    return normalizar_texto(texto) in TEXTOS_PRELIMINARES


def iter_body_children(root: ET.Element) -> list[ET.Element]:
    body = root.find("w:body", NS)
    if body is None:
        return []
    return list(body)


def contiene_objeto_anclado(node: ET.Element) -> bool:
    return node.find(".//w:pict", NS) is not None or node.find(".//wp:anchor", NS) is not None


def crear_parrafo_portador_anclas() -> ET.Element:
    parrafo = ET.Element(qn_w("p"))
    ppr = ET.SubElement(parrafo, qn_w("pPr"))
    ET.SubElement(
        ppr,
        qn_w("spacing"),
        {
            qn_w("before"): "0",
            qn_w("after"): "0",
            qn_w("line"): "1",
            qn_w("lineRule"): "exact",
        },
    )
    rpr = ET.SubElement(ppr, qn_w("rPr"))
    ET.SubElement(rpr, qn_w("sz"), {qn_w("val"): "1"})
    ET.SubElement(rpr, qn_w("szCs"), {qn_w("val"): "1"})
    return parrafo


def extraer_anclas_de_tdc2(root: ET.Element) -> None:
    def procesar_contenedor(contenedor: ET.Element) -> None:
        for child in list(contenedor):
            procesar_contenedor(child)

            if child.tag != qn_w("p") or obtener_style_id_parrafo(child) not in TOC2_STYLE_IDS:
                continue

            runs_anclados = [
                run
                for run in list(child)
                if run.tag == qn_w("r") and contiene_objeto_anclado(run)
            ]
            if not runs_anclados:
                continue

            portador = crear_parrafo_portador_anclas()
            for run in runs_anclados:
                child.remove(run)
                portador.append(run)

            contenedor.insert(list(contenedor).index(child), portador)

    procesar_contenedor(root)


def parrafos_por_estilo(root: ET.Element, style_id: str) -> list[ET.Element]:
    return [
        parrafo
        for parrafo in root.findall(".//w:p", NS)
        if obtener_style_id_parrafo(parrafo) == style_id
    ]


def indice_bloque_toc_en_contenedor(contenedor: ET.Element) -> tuple[int, int] | None:
    children = list(contenedor)
    inicio = None
    for i, child in enumerate(children):
        if child.tag == qn_w("p") and obtener_style_id_parrafo(child) in {"TDC1", "TDC2"}:
            inicio = i
            break
    if inicio is None:
        return None

    fin = inicio
    for i in range(inicio, len(children)):
        child = children[i]
        if child.tag != qn_w("p"):
            break

        sid = obtener_style_id_parrafo(child)
        texto = normalizar_texto(texto_parrafo(child))
        if i > inicio and sid not in {"TDC1", "TDC2"} and texto not in {"", "© universidad internacional de la rioja (unir)"}:
            break
        fin = i
        if sid == "TDC1" and texto.startswith("test"):
            break
    return inicio, fin


def encontrar_contenedor_toc(root: ET.Element) -> tuple[ET.Element, int, int] | None:
    span = indice_bloque_toc_en_contenedor(root)
    if span is not None:
        return root, span[0], span[1]

    for child in list(root):
        encontrado = encontrar_contenedor_toc(child)
        if encontrado is not None:
            return encontrado
    return None


def sincronizar_parrafos_indice(dest_root: ET.Element, front_root: ET.Element) -> None:
    dest_encontrado = encontrar_contenedor_toc(dest_root)
    front_encontrado = encontrar_contenedor_toc(front_root)
    if dest_encontrado is None or front_encontrado is None:
        return

    dest_container, dest_start, dest_end = dest_encontrado
    front_container, front_start, front_end = front_encontrado

    for child in list(dest_container)[dest_start : dest_end + 1]:
        dest_container.remove(child)

    insert_at = dest_start
    for child in list(front_container)[front_start : front_end + 1]:
        dest_container.insert(insert_at, deepcopy(child))
        insert_at += 1


def sincronizar_textos_portada(dest_root: ET.Element, front_root: ET.Element) -> None:
    dest_parrafos = dest_root.findall(".//w:p", NS)
    front_parrafos = front_root.findall(".//w:p", NS)

    pares_indices = ((3, 3), (17, 17), (19, 19))
    for dest_idx, src_idx in pares_indices:
        if dest_idx < len(dest_parrafos) and src_idx < len(front_parrafos):
            texto = texto_parrafo(front_parrafos[src_idx])
            if normalizar_texto(texto):
                asignar_texto_parrafo(dest_parrafos[dest_idx], texto)

    # Tema 2 has the cover subtitle split across two paragraphs; keep the base layout single-line.
    if len(front_parrafos) > 20 and len(dest_parrafos) > 19:
        segunda_linea = texto_parrafo(front_parrafos[20])
        if normalizar_texto(segunda_linea):
            texto = f"{texto_parrafo(front_parrafos[19])} {segunda_linea}".strip()
            asignar_texto_parrafo(dest_parrafos[19], texto)


def sincronizar_rotulo_esquema(dest_root: ET.Element, front_root: ET.Element) -> None:
    front_textos = [
        texto_parrafo(parrafo)
        for parrafo in front_root.findall(".//w:p", NS)
        if normalizar_texto(texto_parrafo(parrafo)).startswith("tema ")
        and normalizar_texto(texto_parrafo(parrafo)).endswith(". esquema")
    ]
    if not front_textos:
        return

    texto_front = front_textos[0]
    for parrafo in dest_root.findall(".//w:p", NS):
        texto = normalizar_texto(texto_parrafo(parrafo))
        if texto.startswith("tema ") and texto.endswith(". esquema"):
            asignar_texto_parrafo(parrafo, texto_front)
            return


def indice_inicio_suffix(children: list[ET.Element], styles_map: dict[str, str]) -> int | None:
    for i, child in enumerate(children):
        if child.tag != qn_w("p"):
            continue
        if not es_parrafo_heading(child, styles_map):
            continue
        if normalizar_texto(texto_parrafo(child)) in TEXTOS_SUFFIX_TEMPLATE:
            return i
    return None


def indice_fin_sin_sectpr(children: list[ET.Element]) -> int:
    if children and children[-1].tag == qn_w("sectPr"):
        return len(children) - 1
    return len(children)


def aplicar_formato_importado(
    nodes: list[ET.Element],
    estilos_template: dict[str, str],
    estilos_origen: dict[str, str],
    arquetipos: dict[str, ET.Element],
    heading_ppr: dict[str, ET.Element],
    heading_rpr: dict[str, ET.Element],
) -> None:
    remapeo_estilos = construir_remapeo_estilos(estilos_template, estilos_origen, nodes)
    for node in nodes:
        aplicar_remapeo_estilos(node, remapeo_estilos)
        if node.tag != qn_w("p"):
            continue

        if es_parrafo_heading(node, estilos_template):
            sid = obtener_style_id_parrafo(node)
            aplicar_arquetipo_parrafo(node, heading_ppr.get(sid))
            aplicar_rpr_arquetipo_a_runs(node, heading_rpr.get(sid))
            continue

        style_id = obtener_style_id_parrafo(node)
        force_style = None
        if style_id in {"", "Normal", "Textoindependiente"}:
            force_style = "Textoindependiente"
        elif style_id in {"FirstParagraph", "BlockText", "BodyText"}:
            force_style = "Textoindependiente"

        clave = "lista" if es_parrafo_lista(node) else "cuerpo"
        aplicar_arquetipo_parrafo(node, arquetipos.get(clave), force_style_id=force_style)


def sincronizar_suffix_frontmatter(
    dest_root: ET.Element,
    front_root: ET.Element,
    estilos_template: dict[str, str],
    estilos_frontmatter: dict[str, str],
    arquetipos: dict[str, ET.Element],
    heading_ppr: dict[str, ET.Element],
    heading_rpr: dict[str, ET.Element],
) -> list[ET.Element]:
    body_dest = dest_root.find("w:body", NS)
    body_front = front_root.find("w:body", NS)
    if body_dest is None or body_front is None:
        return []

    dest_children = list(body_dest)
    front_children = list(body_front)
    dest_start = indice_inicio_suffix(dest_children, estilos_template)
    front_start = indice_inicio_suffix(front_children, estilos_frontmatter)
    if dest_start is None or front_start is None:
        return []

    dest_end = indice_fin_sin_sectpr(dest_children)
    front_end = indice_fin_sin_sectpr(front_children)
    bloque_front = [deepcopy(node) for node in front_children[front_start:front_end]]
    if not bloque_front:
        return []

    aplicar_formato_importado(
        bloque_front,
        estilos_template,
        estilos_frontmatter,
        arquetipos,
        heading_ppr,
        heading_rpr,
    )

    for node in dest_children[dest_start:dest_end]:
        body_dest.remove(node)

    insert_at = dest_start
    for node in bloque_front:
        body_dest.insert(insert_at, node)
        insert_at += 1

    return bloque_front


def sincronizar_frontmatter(dest_root: ET.Element, front_root: ET.Element) -> None:
    sincronizar_textos_portada(dest_root, front_root)
    sincronizar_parrafos_indice(dest_root, front_root)
    sincronizar_rotulo_esquema(dest_root, front_root)


def normalizar_tdc2(root: ET.Element) -> None:
    for parrafo in root.findall(".//w:p", NS):
        if obtener_style_id_parrafo(parrafo) not in TOC2_STYLE_IDS:
            continue

        ppr = asegurar_ppr(parrafo)
        num_pr = ppr.find("w:numPr", NS)
        if num_pr is not None:
            ppr.remove(num_pr)

        ind = ppr.find("w:ind", NS)
        if ind is None:
            ind = ET.Element(qn_w("ind"))
            ppr.append(ind)

        ind.attrib.pop(qn_w("firstLine"), None)
        ind.attrib[qn_w("left")] = TOC2_LEFT
        ind.attrib[qn_w("hanging")] = TOC2_HANGING

        tabs = ppr.find("w:tabs", NS)
        if tabs is None:
            tabs = ET.Element(qn_w("tabs"))
            ppr.append(tabs)
        for tab in list(tabs):
            tabs.remove(tab)
        tabs.append(
            ET.Element(
                qn_w("tab"),
                {
                    qn_w("val"): "left",
                    qn_w("pos"): TOC2_PAGE_TAB,
                },
            )
        )


def indice_inicio_revisado(children: list[ET.Element], styles_map: dict[str, str]) -> int:
    for i, child in enumerate(children):
        if child.tag != qn_w("p"):
            continue
        if es_parrafo_heading(child, styles_map) and normalizar_texto(texto_parrafo(child)):
            return i
    return 0


def indice_fin_revisado(children: list[ET.Element], styles_map: dict[str, str], start: int) -> int:
    primer_heading = ""
    for child in children[start:]:
        if child.tag != qn_w("p"):
            continue
        if es_parrafo_heading(child, styles_map):
            primer_heading = normalizar_texto(texto_parrafo(child))
            break

    if not primer_heading:
        return len(children)

    for i, child in enumerate(children[start + 1 :], start=start + 1):
        if child.tag != qn_w("p"):
            continue
        if not es_parrafo_heading(child, styles_map):
            continue
        if normalizar_texto(texto_parrafo(child)) == primer_heading:
            return i

    return len(children)


def indice_inicio_template(children: list[ET.Element], styles_map: dict[str, str]) -> int:
    vio_preliminar = False
    for i, child in enumerate(children):
        if child.tag != qn_w("p"):
            continue
        texto = texto_parrafo(child)
        if not normalizar_texto(texto):
            continue
        if es_texto_preliminar(texto):
            vio_preliminar = True
            continue
        if vio_preliminar and es_parrafo_heading(child, styles_map):
            return i

    for i, child in enumerate(children):
        if child.tag != qn_w("p"):
            continue
        texto = texto_parrafo(child)
        if normalizar_texto(texto) and es_parrafo_heading(child, styles_map):
            return i
    return 0


def indice_fin_template(children: list[ET.Element], styles_map: dict[str, str]) -> int:
    for i, child in enumerate(children):
        if child.tag != qn_w("p"):
            continue
        if not es_parrafo_heading(child, styles_map):
            continue
        if normalizar_texto(texto_parrafo(child)) in TEXTOS_SUFFIX_TEMPLATE:
            return i
    return len(children)


def extraer_ids_num_usados(nodes: list[ET.Element]) -> set[str]:
    usados: set[str] = set()
    for node in nodes:
        for num_id in node.findall(".//w:numPr/w:numId", NS):
            valor = num_id.attrib.get(qn_w("val"))
            if valor:
                usados.add(valor)
    return usados


def es_parrafo_lista(parrafo: ET.Element) -> bool:
    ppr = parrafo.find("w:pPr", NS)
    if ppr is None:
        return False
    if ppr.find("w:numPr", NS) is not None:
        return True
    ind = ppr.find("w:ind", NS)
    return ind is not None and qn_w("hanging") in ind.attrib


def construir_remapeo_estilos(
    estilos_template: dict[str, str],
    estilos_revisado: dict[str, str],
    nodes: list[ET.Element],
) -> dict[str, str]:
    usados: set[str] = set()
    for node in nodes:
        for tag in (".//w:pStyle", ".//w:rStyle", ".//w:tblStyle"):
            for style in node.findall(tag, NS):
                valor = style.attrib.get(qn_w("val"))
                if valor:
                    usados.add(valor)

    faltantes = {sid for sid in usados if sid not in estilos_template}
    por_nombre_template: dict[str, str] = {}
    for sid, nombre in estilos_template.items():
        clave_sid = normalizar_nombre_estilo(sid)
        if clave_sid:
            por_nombre_template[clave_sid] = sid
        clave = normalizar_nombre_estilo(nombre)
        if clave:
            por_nombre_template[clave] = sid

    remapeo: dict[str, str] = {}
    for sid in sorted(faltantes):
        candidatos = []
        nombre_rev = estilos_revisado.get(sid, "")
        clave_rev = normalizar_nombre_estilo(nombre_rev)
        if clave_rev:
            candidatos.append(clave_rev)
        candidatos.append(normalizar_nombre_estilo(sid))
        candidatos.extend(SINONIMOS_ESTILO.get(normalizar_nombre_estilo(sid), []))
        elegido = next((por_nombre_template[c] for c in candidatos if c in por_nombre_template), "")
        if not elegido and "Normal" in estilos_template:
            elegido = "Normal"
        if elegido:
            remapeo[sid] = elegido
    return remapeo


def aplicar_remapeo_estilos(node: ET.Element, remapeo: dict[str, str]) -> None:
    if not remapeo:
        return
    for tag in (".//w:pStyle", ".//w:rStyle", ".//w:tblStyle"):
        for style in node.findall(tag, NS):
            valor = style.attrib.get(qn_w("val"))
            if valor in remapeo:
                style.attrib[qn_w("val")] = remapeo[valor]


def ppr_arquetipo(parrafo: ET.Element) -> ET.Element | None:
    ppr = parrafo.find("w:pPr", NS)
    if ppr is None:
        return None

    nuevo = ET.Element(qn_w("pPr"))
    for child in list(ppr):
        if child.tag.split("}")[-1] in PPR_LAYOUT_TAGS:
            nuevo.append(deepcopy(child))
    return nuevo if list(nuevo) else None


def rpr_arquetipo_heading(parrafo: ET.Element) -> ET.Element | None:
    fallback: ET.Element | None = None
    for run in parrafo.findall("w:r", NS):
        rpr = run.find("w:rPr", NS)
        if rpr is not None and list(rpr):
            if rpr.find("w:color", NS) is not None:
                return deepcopy(rpr)
            if fallback is None:
                fallback = deepcopy(rpr)
    return fallback


def construir_arquetipos_parrafo(
    template_children: list[ET.Element],
    styles_map: dict[str, str],
    start_tpl: int,
    end_tpl: int,
) -> dict[str, ET.Element]:
    arquetipos: dict[str, ET.Element] = {}

    for child in template_children[start_tpl:end_tpl]:
        if child.tag != qn_w("p"):
            continue
        texto = normalizar_texto(texto_parrafo(child))
        if not texto or es_parrafo_heading(child, styles_map):
            continue

        arq = ppr_arquetipo(child)
        if arq is None:
            continue

        clave = "lista" if es_parrafo_lista(child) else "cuerpo"
        if clave not in arquetipos:
            arquetipos[clave] = arq
        if "cuerpo" in arquetipos and "lista" in arquetipos:
            break

    if "lista" not in arquetipos and "cuerpo" in arquetipos:
        arquetipos["lista"] = deepcopy(arquetipos["cuerpo"])
    return arquetipos


def construir_arquetipos_heading(
    template_children: list[ET.Element],
) -> tuple[dict[str, ET.Element], dict[str, ET.Element]]:
    ppr_map: dict[str, ET.Element] = {}
    rpr_map: dict[str, ET.Element] = {}

    for child in template_children:
        if child.tag != qn_w("p"):
            continue
        sid = obtener_style_id_parrafo(child)
        if sid not in HEADING_STYLE_IDS:
            continue
        if normalizar_texto(texto_parrafo(child)):
            if sid not in ppr_map:
                arq = ppr_arquetipo(child)
                if arq is not None:
                    ppr_map[sid] = arq
            if sid not in rpr_map:
                rpr = rpr_arquetipo_heading(child)
                if rpr is not None:
                    rpr_map[sid] = rpr
        if len(ppr_map) == len(HEADING_STYLE_IDS) and len(rpr_map) == len(HEADING_STYLE_IDS):
            break

    return ppr_map, rpr_map


def aplicar_arquetipo_parrafo(
    parrafo: ET.Element,
    arquetipo: ET.Element | None,
    force_style_id: str | None = None,
) -> None:
    if arquetipo is None and not force_style_id:
        return

    ppr = parrafo.find("w:pPr", NS)
    if ppr is None:
        ppr = ET.Element(qn_w("pPr"))
        parrafo.insert(0, ppr)

    keepers: list[ET.Element] = []
    for child in list(ppr):
        local = child.tag.split("}")[-1]
        if local in {"pStyle", "numPr", "outlineLvl", "keepNext", "keepLines", "pageBreakBefore", "sectPr"}:
            keepers.append(deepcopy(child))
        ppr.remove(child)

    for child in keepers:
        ppr.append(child)

    if force_style_id:
        definir_style_id_parrafo(parrafo, force_style_id)
        ppr = parrafo.find("w:pPr", NS)
        assert ppr is not None

    if arquetipo is not None:
        existing = {child.tag for child in ppr}
        for child in list(arquetipo):
            if child.tag not in existing:
                ppr.append(deepcopy(child))


def aplicar_rpr_arquetipo_a_runs(parrafo: ET.Element, rpr_arquetipo: ET.Element | None) -> None:
    if rpr_arquetipo is None:
        return

    for run in parrafo.findall("w:r", NS):
        rpr = run.find("w:rPr", NS)
        if rpr is None:
            rpr = ET.Element(qn_w("rPr"))
            run.insert(0, rpr)
        existing = {child.tag for child in rpr}
        for child in list(rpr_arquetipo):
            if child.tag not in existing:
                rpr.append(deepcopy(child))


def merge_numbering(
    template_blobs: dict[str, bytes],
    revisado_blobs: dict[str, bytes],
    used_num_ids: set[str],
    base_numbering_xml: bytes | None = None,
) -> bytes | None:
    if not used_num_ids:
        return base_numbering_xml if base_numbering_xml is not None else template_blobs.get("word/numbering.xml")

    tpl_root = (
        ET.fromstring(base_numbering_xml)
        if base_numbering_xml is not None
        else parse_xml(template_blobs, "word/numbering.xml")
    )
    src_root = parse_xml(revisado_blobs, "word/numbering.xml")
    if tpl_root is None or src_root is None:
        return base_numbering_xml if base_numbering_xml is not None else template_blobs.get("word/numbering.xml")

    nums_tpl = {node.attrib.get(qn_w("numId"), ""): node for node in tpl_root.findall("w:num", NS)}
    abstract_tpl = {
        node.attrib.get(qn_w("abstractNumId"), ""): node for node in tpl_root.findall("w:abstractNum", NS)
    }
    nums_src = {node.attrib.get(qn_w("numId"), ""): node for node in src_root.findall("w:num", NS)}
    abstract_src = {
        node.attrib.get(qn_w("abstractNumId"), ""): node for node in src_root.findall("w:abstractNum", NS)
    }

    def insertar_abstract_num(node: ET.Element) -> None:
        children = list(tpl_root)
        first_num_idx = next(
            (idx for idx, child in enumerate(children) if child.tag == qn_w("num")),
            len(children),
        )
        tpl_root.insert(first_num_idx, node)

    changed = False
    for num_id in sorted(used_num_ids):
        if num_id in nums_tpl:
            continue
        src_num = nums_src.get(num_id)
        if src_num is None:
            continue

        abs_node = src_num.find("w:abstractNumId", NS)
        abs_id = abs_node.attrib.get(qn_w("val"), "") if abs_node is not None else ""
        if abs_id and abs_id not in abstract_tpl and abs_id in abstract_src:
            nuevo_abstract = deepcopy(abstract_src[abs_id])
            insertar_abstract_num(nuevo_abstract)
            abstract_tpl[abs_id] = nuevo_abstract

        nuevo_num = deepcopy(src_num)
        tpl_root.append(nuevo_num)
        nums_tpl[num_id] = nuevo_num
        changed = True

    if not changed:
        return base_numbering_xml if base_numbering_xml is not None else template_blobs.get("word/numbering.xml")
    return ET.tostring(tpl_root, encoding="utf-8", xml_declaration=True)


def parse_relationships(data: bytes | None) -> ET.Element | None:
    if data is None:
        return None
    return ET.fromstring(data)


def next_rid(existing: set[str]) -> str:
    max_num = 0
    for rid in existing:
        if rid.startswith("rId") and rid[3:].isdigit():
            max_num = max(max_num, int(rid[3:]))
    return f"rId{max_num + 1}"


def qn_ct(tag: str) -> str:
    return f"{{{NS_CT}}}{tag}"


def crear_header_xml(texto: str = "") -> bytes:
    root = ET.Element(qn_w("hdr"))
    p = ET.SubElement(root, qn_w("p"))
    ppr = ET.SubElement(p, qn_w("pPr"))
    ET.SubElement(ppr, qn_w("jc"), {qn_w("val"): "right"})
    r = ET.SubElement(p, qn_w("r"))
    rpr = ET.SubElement(r, qn_w("rPr"))
    ET.SubElement(rpr, qn_w("rFonts"), {qn_w("ascii"): "Calibri Light", qn_w("hAnsi"): "Calibri Light"})
    ET.SubElement(rpr, qn_w("color"), {qn_w("val"): "777777"})
    ET.SubElement(rpr, qn_w("sz"), {qn_w("val"): "18"})
    ET.SubElement(rpr, qn_w("szCs"), {qn_w("val"): "18"})
    ET.SubElement(r, qn_w("t")).text = texto
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def crear_footer_xml(texto: str = "Ecosistema Digital y Tecnologías Disruptivas") -> bytes:
    root = ET.Element(qn_w("ftr"))
    p = ET.SubElement(root, qn_w("p"))
    ppr = ET.SubElement(p, qn_w("pPr"))
    ET.SubElement(ppr, qn_w("jc"), {qn_w("val"): "right"})

    r = ET.SubElement(p, qn_w("r"))
    rpr = ET.SubElement(r, qn_w("rPr"))
    ET.SubElement(rpr, qn_w("rFonts"), {qn_w("ascii"): "Calibri Light", qn_w("hAnsi"): "Calibri Light"})
    ET.SubElement(rpr, qn_w("color"), {qn_w("val"): "777777"})
    ET.SubElement(rpr, qn_w("sz"), {qn_w("val"): "20"})
    ET.SubElement(rpr, qn_w("szCs"), {qn_w("val"): "20"})
    ET.SubElement(r, qn_w("t")).text = f"{texto}   "

    field = ET.SubElement(p, qn_w("fldSimple"), {qn_w("instr"): "PAGE"})
    fr = ET.SubElement(field, qn_w("r"))
    frpr = ET.SubElement(fr, qn_w("rPr"))
    ET.SubElement(frpr, qn_w("rFonts"), {qn_w("ascii"): "Calibri Light", qn_w("hAnsi"): "Calibri Light"})
    ET.SubElement(frpr, qn_w("color"), {qn_w("val"): "0097CD"})
    ET.SubElement(frpr, qn_w("sz"), {qn_w("val"): "20"})
    ET.SubElement(frpr, qn_w("szCs"), {qn_w("val"): "20"})
    ET.SubElement(fr, qn_w("t")).text = "1"
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def crear_footer_vacio_xml() -> bytes:
    root = ET.Element(qn_w("ftr"))
    ET.SubElement(root, qn_w("p"))
    return ET.tostring(root, encoding="utf-8", xml_declaration=True)


def agregar_override_content_type(root: ET.Element, part_name: str, content_type: str) -> None:
    for override in root.findall("ct:Override", NS):
        if override.attrib.get("PartName") == part_name:
            override.attrib["ContentType"] = content_type
            return
    ET.SubElement(root, qn_ct("Override"), {"PartName": part_name, "ContentType": content_type})


def agregar_relacion_parte(root: ET.Element, rel_id: str, rel_type: str, target: str) -> None:
    ET.SubElement(
        root,
        f"{{{NS_PR}}}Relationship",
        {
            "Id": rel_id,
            "Type": rel_type,
            "Target": target,
        },
    )


def definir_referencias_seccion(sect_pr: ET.Element, header_rid: str, footer_rid: str) -> None:
    for child in list(sect_pr):
        if child.tag in {qn_w("headerReference"), qn_w("footerReference")}:
            sect_pr.remove(child)

    header_ref = ET.Element(qn_w("headerReference"), {qn_w("type"): "default", qn_r("id"): header_rid})
    footer_ref = ET.Element(qn_w("footerReference"), {qn_w("type"): "default", qn_r("id"): footer_rid})
    sect_pr.insert(0, footer_ref)
    sect_pr.insert(0, header_ref)


def crear_parrafo_salto_seccion(sect_pr_base: ET.Element, header_rid: str, footer_rid: str) -> ET.Element:
    parrafo = ET.Element(qn_w("p"))
    ppr = ET.SubElement(parrafo, qn_w("pPr"))
    sect_pr = deepcopy(sect_pr_base)
    tipo = sect_pr.find("w:type", NS)
    if tipo is None:
        tipo = ET.Element(qn_w("type"), {qn_w("val"): "continuous"})
        sect_pr.insert(0, tipo)
    else:
        tipo.attrib[qn_w("val")] = "continuous"
    definir_referencias_seccion(sect_pr, header_rid, footer_rid)
    ppr.append(sect_pr)
    return parrafo


def gather_relationship_ids(node: ET.Element) -> set[str]:
    ids: set[str] = set()
    for elem in node.iter():
        for attr, value in elem.attrib.items():
            if attr.startswith(f"{{{NS_R}}}") and value:
                ids.add(value)
    return ids


def resolve_target_path(target: str) -> str:
    if target.startswith("/"):
        return target.lstrip("/")
    return posixpath.normpath(posixpath.join("word", target))


def relative_target_from_word(path: str) -> str:
    return posixpath.relpath(path, "word")


def copiar_relaciones_y_partes(
    nodes: list[ET.Element],
    template_blobs: dict[str, bytes],
    revisado_blobs: dict[str, bytes],
) -> tuple[bytes | None, dict[str, bytes]]:
    tpl_rels_root = parse_relationships(template_blobs.get("word/_rels/document.xml.rels"))
    src_rels_root = parse_relationships(revisado_blobs.get("word/_rels/document.xml.rels"))
    if tpl_rels_root is None or src_rels_root is None:
        return template_blobs.get("word/_rels/document.xml.rels"), {}

    src_rel_by_id = {
        rel.attrib.get("Id", ""): rel for rel in src_rels_root.findall("pr:Relationship", NS)
    }
    existing_ids = {rel.attrib.get("Id", "") for rel in tpl_rels_root.findall("pr:Relationship", NS)}
    existing_by_signature = {
        (
            rel.attrib.get("Type", ""),
            rel.attrib.get("Target", ""),
            rel.attrib.get("TargetMode", ""),
        ): rel.attrib.get("Id", "")
        for rel in tpl_rels_root.findall("pr:Relationship", NS)
    }

    extra_parts: dict[str, bytes] = {}
    rid_map: dict[str, str] = {}

    for node in nodes:
        for rid in sorted(gather_relationship_ids(node)):
            if rid in rid_map:
                continue
            src_rel = src_rel_by_id.get(rid)
            if src_rel is None:
                continue

            rel_type = src_rel.attrib.get("Type", "")
            target = src_rel.attrib.get("Target", "")
            target_mode = src_rel.attrib.get("TargetMode", "")

            if target_mode != "External" and target:
                part_path = resolve_target_path(target)
                if part_path in revisado_blobs:
                    src_blob = revisado_blobs[part_path]
                    if part_path in template_blobs and template_blobs[part_path] != src_blob:
                        stem, ext = posixpath.splitext(part_path)
                        suffix = 1
                        new_part_path = f"{stem}_src{suffix}{ext}"
                        while new_part_path in template_blobs or new_part_path in extra_parts:
                            suffix += 1
                            new_part_path = f"{stem}_src{suffix}{ext}"
                        part_path = new_part_path
                    extra_parts[part_path] = src_blob
                    target = relative_target_from_word(part_path)

            signature = (rel_type, target, target_mode)
            if signature in existing_by_signature:
                rid_map[rid] = existing_by_signature[signature]
                continue

            new_rid = rid if rid not in existing_ids else next_rid(existing_ids)
            rel_attrib = {
                "Id": new_rid,
                "Type": rel_type,
                "Target": target,
            }
            if target_mode:
                rel_attrib["TargetMode"] = target_mode
            tpl_rels_root.append(ET.Element(f"{{{NS_PR}}}Relationship", rel_attrib))
            existing_ids.add(new_rid)
            existing_by_signature[signature] = new_rid
            rid_map[rid] = new_rid

    if rid_map:
        for node in nodes:
            for elem in node.iter():
                for attr, value in list(elem.attrib.items()):
                    if attr.startswith(f"{{{NS_R}}}") and value in rid_map:
                        elem.attrib[attr] = rid_map[value]

    return ET.tostring(tpl_rels_root, encoding="utf-8", xml_declaration=True), extra_parts


def aplicar_cabecera_pie_central(
    document_xml: bytes,
    document_rels_xml: bytes | None,
    content_types_xml: bytes,
) -> tuple[bytes, bytes | None, bytes, dict[str, bytes]]:
    if document_rels_xml is None:
        return document_xml, document_rels_xml, content_types_xml, {}

    doc_root = ET.fromstring(document_xml)
    body = doc_root.find("w:body", NS)
    if body is None:
        return document_xml, document_rels_xml, content_types_xml, {}

    rels_root = parse_relationships(document_rels_xml)
    if rels_root is None:
        return document_xml, document_rels_xml, content_types_xml, {}

    existing_ids = {rel.attrib.get("Id", "") for rel in rels_root.findall("pr:Relationship", NS)}
    header_rid = next_rid(existing_ids)
    existing_ids.add(header_rid)
    footer_rid = next_rid(existing_ids)
    existing_ids.add(footer_rid)
    blank_header_rid = next_rid(existing_ids)
    existing_ids.add(blank_header_rid)
    blank_footer_rid = next_rid(existing_ids)
    existing_ids.add(blank_footer_rid)

    parts = {
        "word/header_clon_fuerte1.xml": crear_header_xml("© Universidad Internacional de La Rioja (UNIR)"),
        "word/footer_clon_fuerte1.xml": crear_footer_xml(),
        "word/header_clon_fuerte_blank.xml": crear_header_xml(""),
        "word/footer_clon_fuerte_blank.xml": crear_footer_vacio_xml(),
    }

    agregar_relacion_parte(rels_root, header_rid, REL_TYPE_HEADER, "header_clon_fuerte1.xml")
    agregar_relacion_parte(rels_root, footer_rid, REL_TYPE_FOOTER, "footer_clon_fuerte1.xml")
    agregar_relacion_parte(rels_root, blank_header_rid, REL_TYPE_HEADER, "header_clon_fuerte_blank.xml")
    agregar_relacion_parte(rels_root, blank_footer_rid, REL_TYPE_FOOTER, "footer_clon_fuerte_blank.xml")

    children = list(body)
    a_fondo_idx = next(
        (
            idx
            for idx, child in enumerate(children)
            if child.tag == qn_w("p") and normalizar_texto(texto_parrafo(child)) == "a fondo"
        ),
        -1,
    )
    if a_fondo_idx == -1:
        return document_xml, document_rels_xml, content_types_xml, {}

    following_sect = next(
        (
            sect
            for child in children[a_fondo_idx:]
            for sect in [child.find("./w:pPr/w:sectPr", NS)]
            if sect is not None
        ),
        None,
    )
    previous_sect = next(
        (
            sect
            for child in reversed(children[:a_fondo_idx])
            for sect in [child.find("./w:pPr/w:sectPr", NS)]
            if sect is not None
        ),
        None,
    )
    sect_base = following_sect if following_sect is not None else previous_sect
    if sect_base is None:
        return document_xml, document_rels_xml, content_types_xml, {}

    body.insert(a_fondo_idx, crear_parrafo_salto_seccion(sect_base, header_rid, footer_rid))

    # Prevent later template sections from inheriting the central native header/footer.
    for child in list(body)[a_fondo_idx + 1 :]:
        sect = child.find("./w:pPr/w:sectPr", NS)
        if sect is not None:
            definir_referencias_seccion(sect, blank_header_rid, blank_footer_rid)

    content_root = ET.fromstring(content_types_xml)
    agregar_override_content_type(content_root, "/word/header_clon_fuerte1.xml", CONTENT_TYPE_HEADER)
    agregar_override_content_type(content_root, "/word/footer_clon_fuerte1.xml", CONTENT_TYPE_FOOTER)
    agregar_override_content_type(content_root, "/word/header_clon_fuerte_blank.xml", CONTENT_TYPE_HEADER)
    agregar_override_content_type(content_root, "/word/footer_clon_fuerte_blank.xml", CONTENT_TYPE_FOOTER)

    return (
        ET.tostring(doc_root, encoding="utf-8", xml_declaration=True),
        ET.tostring(rels_root, encoding="utf-8", xml_declaration=True),
        ET.tostring(content_root, encoding="utf-8", xml_declaration=True),
        parts,
    )


def construir_documento(
    template_root: ET.Element,
    revisado_root: ET.Element,
    estilos_template: dict[str, str],
    estilos_revisado: dict[str, str],
    frontmatter_root: ET.Element | None = None,
    estilos_frontmatter: dict[str, str] | None = None,
) -> tuple[list[ET.Element], list[ET.Element]]:
    body_tpl = template_root.find("w:body", NS)
    body_src = revisado_root.find("w:body", NS)
    if body_tpl is None or body_src is None:
        raise ValueError("No se pudo localizar el cuerpo del documento DOCX.")

    children_tpl = list(body_tpl)
    children_src = list(body_src)

    start_tpl = indice_inicio_template(children_tpl, estilos_template)
    end_tpl = indice_fin_template(children_tpl, estilos_template)
    start_src = indice_inicio_revisado(children_src, estilos_revisado)
    end_src = indice_fin_revisado(children_src, estilos_revisado, start_src)

    if start_tpl >= end_tpl:
        raise ValueError("No se pudo localizar un bloque central reemplazable en la plantilla.")

    bloque_src = [deepcopy(node) for node in children_src[start_src:end_src] if node.tag != qn_w("sectPr")]
    if not bloque_src:
        raise ValueError("El documento revisado no contiene un bloque de contenido útil.")

    arquetipos = construir_arquetipos_parrafo(children_tpl, estilos_template, start_tpl, end_tpl)
    heading_ppr, heading_rpr = construir_arquetipos_heading(children_tpl)
    aplicar_formato_importado(
        bloque_src,
        estilos_template,
        estilos_revisado,
        arquetipos,
        heading_ppr,
        heading_rpr,
    )

    for node in children_tpl[start_tpl:end_tpl]:
        body_tpl.remove(node)

    insert_at = start_tpl
    for node in bloque_src:
        body_tpl.insert(insert_at, node)
        insert_at += 1

    suffix_frontmatter: list[ET.Element] = []
    if frontmatter_root is not None:
        sincronizar_frontmatter(template_root, frontmatter_root)
        suffix_frontmatter = sincronizar_suffix_frontmatter(
            dest_root=template_root,
            front_root=frontmatter_root,
            estilos_template=estilos_template,
            estilos_frontmatter=estilos_frontmatter or {},
            arquetipos=arquetipos,
            heading_ppr=heading_ppr,
            heading_rpr=heading_rpr,
        )

    normalizar_tdc2(template_root)
    extraer_anclas_de_tdc2(template_root)

    return bloque_src, suffix_frontmatter


def inferir_frontmatter(revisado: Path) -> Path | None:
    match = REV_TEMA_RE.match(revisado.name)
    if not match:
        return None
    candidato = revisado.with_name(f"TEMA {int(match.group(1))}.docx")
    return candidato if candidato.exists() else None


def clonar_fuerte(
    plantilla: Path,
    revisado: Path,
    salida: Path,
    frontmatter: Path | None = None,
) -> tuple[int, int]:
    if not plantilla.exists():
        raise FileNotFoundError(f"No existe plantilla: {plantilla}")
    if not revisado.exists():
        raise FileNotFoundError(f"No existe revisado: {revisado}")

    template_blobs = leer_zip(plantilla)
    revisado_blobs = leer_zip(revisado)
    frontmatter_blobs = leer_zip(frontmatter) if frontmatter is not None and frontmatter.exists() else None

    template_root = parse_xml(template_blobs, "word/document.xml")
    revisado_root = parse_xml(revisado_blobs, "word/document.xml")
    if template_root is None or revisado_root is None:
        raise ValueError("No se pudo abrir word/document.xml en uno de los DOCX.")
    frontmatter_root = (
        parse_xml(frontmatter_blobs, "word/document.xml") if frontmatter_blobs is not None else None
    )

    estilos_template = extraer_estilos_por_id(parse_xml(template_blobs, "word/styles.xml"))
    estilos_revisado = extraer_estilos_por_id(parse_xml(revisado_blobs, "word/styles.xml"))
    estilos_frontmatter = (
        extraer_estilos_por_id(parse_xml(frontmatter_blobs, "word/styles.xml"))
        if frontmatter_blobs is not None
        else {}
    )

    inserted_nodes, frontmatter_nodes = construir_documento(
        template_root=template_root,
        revisado_root=revisado_root,
        estilos_template=estilos_template,
        estilos_revisado=estilos_revisado,
        frontmatter_root=frontmatter_root,
        estilos_frontmatter=estilos_frontmatter,
    )

    numbering_xml = merge_numbering(
        template_blobs=template_blobs,
        revisado_blobs=revisado_blobs,
        used_num_ids=extraer_ids_num_usados(inserted_nodes),
    )
    if frontmatter_blobs is not None and frontmatter_nodes:
        numbering_xml = merge_numbering(
            template_blobs=template_blobs,
            revisado_blobs=frontmatter_blobs,
            used_num_ids=extraer_ids_num_usados(frontmatter_nodes),
            base_numbering_xml=numbering_xml,
        )

    document_rels_xml, extra_parts = copiar_relaciones_y_partes(
        nodes=inserted_nodes,
        template_blobs=template_blobs,
        revisado_blobs=revisado_blobs,
    )
    if frontmatter_blobs is not None and frontmatter_nodes:
        rels_base_blobs = dict(template_blobs)
        if document_rels_xml is not None:
            rels_base_blobs["word/_rels/document.xml.rels"] = document_rels_xml
        rels_base_blobs.update(extra_parts)
        document_rels_xml, extra_parts_front = copiar_relaciones_y_partes(
            nodes=frontmatter_nodes,
            template_blobs=rels_base_blobs,
            revisado_blobs=frontmatter_blobs,
        )
        extra_parts.update(extra_parts_front)

    document_xml = ET.tostring(template_root, encoding="utf-8", xml_declaration=True)
    content_types_xml = template_blobs.get("[Content_Types].xml")
    header_footer_parts: dict[str, bytes] = {}
    if content_types_xml is not None:
        document_xml, document_rels_xml, content_types_xml, header_footer_parts = aplicar_cabecera_pie_central(
            document_xml=document_xml,
            document_rels_xml=document_rels_xml,
            content_types_xml=content_types_xml,
        )

    fd, tmp_name = tempfile.mkstemp(suffix=".docx")
    Path(tmp_name).unlink(missing_ok=True)
    salida_tmp = Path(tmp_name)
    _ = fd

    salida.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(str(salida_tmp), "w", compression=ZIP_DEFLATED) as z_out:
        for name, blob in template_blobs.items():
            if name == "[Content_Types].xml" and content_types_xml is not None:
                z_out.writestr(name, content_types_xml)
                continue
            if name == "word/document.xml":
                z_out.writestr(name, document_xml)
                continue
            if name == "word/numbering.xml" and numbering_xml is not None:
                z_out.writestr(name, numbering_xml)
                continue
            if name == "word/_rels/document.xml.rels" and document_rels_xml is not None:
                z_out.writestr(name, document_rels_xml)
                continue
            z_out.writestr(name, blob)

        for name in PARTES_RELACIONADAS_TEMPLATE:
            if name not in template_blobs and name in revisado_blobs:
                z_out.writestr(name, revisado_blobs[name])

        for name, blob in extra_parts.items():
            if name not in template_blobs:
                z_out.writestr(name, blob)

        for name, blob in header_footer_parts.items():
            if name not in template_blobs:
                z_out.writestr(name, blob)

    salida_tmp.replace(salida)
    return len(inserted_nodes), len(extra_parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Clon fuerte de formato: conserva la carcasa del template y reemplaza "
            "el bloque central por el contenido revisado."
        )
    )
    parser.add_argument(
        "--plantilla",
        type=Path,
        default=DEFAULT_TEMAS / "TEMA 1.docx",
        help="DOCX base con estructura y formato final.",
    )
    parser.add_argument(
        "--revisado",
        type=Path,
        default=DEFAULT_TEMAS / "tema_1_rev.docx",
        help="DOCX origen del bloque central de contenido.",
    )
    parser.add_argument(
        "--salida",
        type=Path,
        default=DEFAULT_TEMAS / "TEMA 1_CLON_FUERTE.docx",
        help="DOCX de salida.",
    )
    parser.add_argument(
        "--frontmatter",
        type=Path,
        default=None,
        help="DOCX opcional del que copiar portada, índice, rótulos preliminares y secciones finales.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    frontmatter = args.frontmatter if args.frontmatter is not None else inferir_frontmatter(args.revisado)
    inserted_nodes, extra_parts = clonar_fuerte(
        plantilla=args.plantilla,
        revisado=args.revisado,
        salida=args.salida,
        frontmatter=frontmatter,
    )

    print(f"Plantilla: {args.plantilla}")
    print(f"Revisado:  {args.revisado}")
    print(f"Frontmatter: {frontmatter if frontmatter is not None else '—'}")
    print(f"Salida:    {args.salida}")
    print(f"Nodos insertados desde revisado: {inserted_nodes}")
    print(f"Partes adicionales copiadas:     {extra_parts}")
    print("Nota: se conserva la carcasa del template y se sustituye el bloque central y la cola final.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
