# Physical POS Research Agent

Este agente responde a una pregunta concreta:

> ¿Cuántas compañías del CSV venden a través de tiendas o puntos de venta físicos?

Clasifica cada empresa en:

- `yes_owned_physical_pos`: tiendas, salones, clínicas, showrooms o puntos físicos propios.
- `yes_third_party_physical_pos`: venta en tiendas, farmacias, salones, cadenas o distribuidores físicos de terceros.
- `yes_mixed_physical_pos`: ambos casos.
- `no_ecommerce_or_b2b_only`: no hay evidencia de canal físico.
- `unclear`: no hay suficiente evidencia fiable.

El conteo principal suma las tres categorías `yes_*`.

## Ejecutar

```bash
python3 -m pip install openai
export OPENAI_API_KEY="tu_api_key"
python3 "02_Profesional/0201_Convercus/Automatizaciones/Agencies Playbook/physical_pos_research_agent.py" --limit 10
```

Por defecto usa llamadas HTTPS directas a la API de OpenAI, así que no depende del SDK `openai`. Si quieres forzar el SDK:

```bash
python3 "02_Profesional/0201_Convercus/Automatizaciones/Agencies Playbook/physical_pos_research_agent.py" --transport sdk --limit 10
```

Cuando el lote de prueba sea correcto:

```bash
python3 "02_Profesional/0201_Convercus/Automatizaciones/Agencies Playbook/physical_pos_research_agent.py"
```

## Salidas

- `physical-pos-research-results.csv`: clasificación por compañía, evidencia y fuentes.
- `physical-pos-research-results.jsonl`: respuesta completa por compañía.
- `physical-pos-research-summary.json`: conteo agregado y porcentaje.

El script es reanudable: si existe el CSV de resultados, omite compañías con `status=ok`.
