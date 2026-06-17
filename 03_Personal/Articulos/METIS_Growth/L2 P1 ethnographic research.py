import pandas as pd


def create_ethnographic_report():
    # Create DataFrame for observations
    data = {
        "Theme": ["Shopping Behavior", "Media Consumption", "Social Interactions"],
        "Observation": [
            "Consumers shop on weekends.",
            "WhatsApp is widely used.",
            "Decisions influenced by family advice.",
        ],
        "Implication": [
            "Launch weekend promotions.",
            "Use WhatsApp campaigns.",
            "Highlight family testimonials.",
        ],
    }
    df = pd.DataFrame(data)

    # Export to Excel
    writer = pd.ExcelWriter("EthnographicResearchReport.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="Ethnographic Insights", index=False)
    writer.close()


create_ethnographic_report()
