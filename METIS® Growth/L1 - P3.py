
import pandas as pd

# Define rubric data
rubric_data = {
    "Aspect": ["Frequency Appropriateness", "Channel Suitability", "Content Clarity", "Accountability", "Transparency"],
    "1 (Poor)": ["Rarely aligned", "Poorly suited", "Unclear", "No clear responsibility", "Lacks honesty"],
    "2 (Fair)": ["Occasionally aligned", "Minimally suitable", "Somewhat clear", "Vague assignment", "Minimal honesty"],
    "3 (Good)": ["Generally aligned", "Moderately suitable", "Clear with minor inconsistencies", "Clearly assigned", "Adequate honesty"],
    "4 (Very Good)": ["Consistently aligned", "Highly suitable", "Very clear and consistent", "Well-enforced assignments", "High level of honesty"],
    "5 (Excellent)": ["Perfectly aligned", "Extremely suitable", "Exceptionally clear and consistent", "Fully enforced with documentation", "Exceptional honesty"]
}

# Create DataFrame
df = pd.DataFrame(rubric_data)

# Export to Excel
df.to_excel("Evaluation_Rubric_Regular_Updates.xlsx", index=False)

print("Excel file generated successfully!")
