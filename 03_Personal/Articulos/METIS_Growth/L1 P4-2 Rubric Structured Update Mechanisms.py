import pandas as pd
import ace_tools as tools

# Create Evaluation Rubric Data
rubric_data = {
    "Criteria": [
        "Definition of Objectives",
        "Frequency of Updates",
        "Standardization",
        "Responsibility Assignment",
    ],
    "1 - Poor": [
        "No clear purpose",
        "Random or inconsistent",
        "No templates used",
        "No ownership defined",
    ],
    "3 - Moderate": [
        "Some updates aligned",
        "Some structure but not uniform",
        "Some updates standardized",
        "Some roles assigned",
    ],
    "5 - Excellent": [
        "Fully aligned with goals",
        "Clear, scheduled updates",
        "Fully structured update formats",
        "Fully accountable update structure",
    ],
}

# Convert to DataFrame
rubric_df = pd.DataFrame(rubric_data)

# Display DataFrame
tools.display_dataframe_to_user(
    name="Structured Update Mechanisms Rubric", dataframe=rubric_df
)
