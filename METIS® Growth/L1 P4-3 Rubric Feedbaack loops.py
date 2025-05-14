import pandas as pd
import ace_tools as tools

# Create Evaluation Rubric Data
rubric_data = {
    "Criteria": ["Feedback Collection Coverage", "Clarity of Feedback Mechanisms", "Timeliness of Responses", "Actionability of Feedback", "Stakeholder Engagement in Feedback"],
    "1 - Poor": ["Few sources utilized", "No clear process defined", "Responses delayed or ignored", "No follow-up actions taken", "Low participation"],
    "3 - Moderate": ["Some stakeholders contribute", "Some structure but inconsistent", "Some feedback processed in time", "Some issues addressed, but inconsistently", "Some stakeholders engaged"],
    "5 - Excellent": ["Comprehensive multi-source feedback", "Fully standardized process", "Timely, structured responses", "All feedback leads to documented actions", "High participation and continuous engagement"]
}

# Convert to DataFrame
rubric_df = pd.DataFrame(rubric_data)

# Display DataFrame
tools.display_dataframe_to_user(name="Feedback Loops and Responsiveness Rubric", dataframe=rubric_df)
