'''
Explanation of the Code
    Workbook Creation : A new Excel workbook is created using Workbook() from openpyxl.
    Sheets : Four sheets are added for each template: KPI Definition Document, KPI Tracking Report, Stakeholder Feedback Analysis Report, and Iteration Plan.
    Headers : The create_header function formats the header row with bold font, background color, and centered alignment.
    Content Addition : The add_row function adds data to each row while ensuring text wraps for readability.
    Data : Predefined data for each template is included as examples. You can modify or extend this data as needed.
    Styling : Borders, alignments, and colors are applied to enhance readability.
    File Saving : The workbook is saved as Communication_Templates.xlsx.

Output
Running the script will generate an Excel file named Communication_Templates.xlsx with four tabs:
    KPI Definition Document : Lists KPIs with definitions, measurement methods, and targets.
    KPI Tracking Report : Tracks KPI performance with current status, trends, and actions taken.
    Stakeholder Feedback Analysis Report : Summarizes feedback themes, summaries, and examples.
    Iteration Plan : Outlines proposed changes with descriptions, timelines, and responsible parties.
'''

from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

# Function to create a styled header row
def create_header(ws, headers):
    for col_num, header in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num, value=header)
        cell.font = Font(bold=True, size=12)
        cell.fill = PatternFill(start_color="D9EAD3", end_color="D9EAD3", fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center")
        ws.column_dimensions[chr(64 + col_num)].width = 25

# Function to add content to rows
def add_row(ws, row_data, row_num):
    for col_num, value in enumerate(row_data, 1):
        cell = ws.cell(row=row_num, column=col_num, value=value)
        cell.alignment = Alignment(wrap_text=True)

# Create a new workbook
wb = Workbook()

# Template 1: KPI Definition Document
ws1 = wb.create_sheet("KPI Definition Document", 0)
headers_kpi_def = ["KPI Name", "Definition", "Measurement Method", "Target"]
create_header(ws1, headers_kpi_def)

kpi_data = [
    ["Response Time", "Average time taken to respond to stakeholder inquiries.", "Track timestamps of incoming and outgoing communications.", "Reduce average response time by 20% within six months."],
    ["Engagement Level", "Percentage of stakeholders actively participating in discussions.", "Analyze participation rates in meetings and surveys.", "Increase engagement by 15% quarterly."]
]

for idx, row in enumerate(kpi_data, start=2):
    add_row(ws1, row, idx)

# Template 2: KPI Tracking Report
ws2 = wb.create_sheet("KPI Tracking Report", 1)
headers_kpi_track = ["KPI Name", "Current Status", "Trend", "Actions Taken"]
create_header(ws2, headers_kpi_track)

kpi_tracking_data = [
    ["Response Time", "2 hours", "Decreased by 15%", "Implemented automated alerts for urgent inquiries."],
    ["Engagement Level", "85%", "Increased by 10%", "Introduced interactive sessions in meetings."]
]

for idx, row in enumerate(kpi_tracking_data, start=2):
    add_row(ws2, row, idx)

# Template 3: Stakeholder Feedback Analysis Report
ws3 = wb.create_sheet("Stakeholder Feedback Analysis Report", 2)
headers_feedback = ["Theme", "Feedback Summary", "Examples"]
create_header(ws3, headers_feedback)

feedback_data = [
    ["Frequency of Communication", "Stakeholders appreciate regular updates but suggest bi-weekly summaries.", "Some stakeholders mentioned they receive too many daily updates."],
    ["Clarity of Communication", "Some stakeholders find technical jargon confusing.", "One stakeholder noted difficulty understanding a recent email about project milestones."],
    ["Responsiveness", "High satisfaction with response times, with minor suggestions for improvement.", "A few stakeholders suggested setting up an after-hours contact method."]
]

for idx, row in enumerate(feedback_data, start=2):
    add_row(ws3, row, idx)

# Template 4: Iteration Plan
ws4 = wb.create_sheet("Iteration Plan", 3)
headers_iteration = ["Change", "Description", "Timeline", "Responsible Party"]
create_header(ws4, headers_iteration)

iteration_data = [
    ["Simplify Language in Emails", "Revise email templates to eliminate technical jargon and simplify language.", "Immediate", "Communication Manager"],
    ["Introduce Bi-Weekly Summary Reports", "Develop and distribute bi-weekly summary reports to stakeholders.", "Next quarter", "Project Coordinator"]
]

for idx, row in enumerate(iteration_data, start=2):
    add_row(ws4, row, idx)

# Save the workbook
wb.save("Communication_Templates.xlsx")
print("Templates created successfully in 'Communication_Templates.xlsx'")