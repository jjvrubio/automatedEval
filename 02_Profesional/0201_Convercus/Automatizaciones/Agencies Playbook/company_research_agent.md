# Company Research Agent

Este agente lee `apollo-accounts-export.csv`, toma los nombres de la primera columna (`Company Name`) e investiga cada compañía con IA y búsqueda web. Genera dos salidas:

- `company-research-results.csv`: tabla filtrable para priorizar compañías.
- `company-research-results.jsonl`: registros completos con el resultado estructurado y la respuesta cruda de la API.

## Requisitos

```bash
python3 -m pip install openai
export OPENAI_API_KEY="tu_api_key"
```

## Prueba recomendada

Primero revisa qué compañías va a procesar:

```bash
python3 "02_Profesional/0201_Convercus/Automatizaciones/Agencies Playbook/company_research_agent.py" --dry-run --limit 10
```

Después ejecuta un lote pequeño:

```bash
python3 "02_Profesional/0201_Convercus/Automatizaciones/Agencies Playbook/company_research_agent.py" --limit 5
```

Si el resultado tiene el nivel de detalle correcto, lanza el resto:

```bash
python3 "02_Profesional/0201_Convercus/Automatizaciones/Agencies Playbook/company_research_agent.py"
```

## Opciones útiles

- `--limit 20`: procesa solo 20 compañías.
- `--start 100`: empieza en la compañía 101 del CSV.
- `--force`: vuelve a investigar compañías que ya tienen `status=ok`.
- `--model gpt-5.5`: usa un modelo más potente para investigaciones más profundas.
- `--sleep 1`: espera 1 segundo entre compañías.

El script es reanudable: si ya existe `company-research-results.csv`, omite las compañías completadas con `status=ok`.
