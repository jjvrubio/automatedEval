import pandas as pd

def create_channel_mapping_document():
    # Create DataFrame for channel inventory
    data = {
        'Channel': ['Facebook', 'Instagram', 'Print Media'],
        'Penetration (%)': [80, 60, 20],
        'Engagement Rate (%)': [2.5, 4.2, 1.0],
        'Preferred Content Format': ['Videos/Infographics', 'Images/Stories', 'Articles']
    }
    df = pd.DataFrame(data)
    
    # Export to Excel
    writer = pd.ExcelWriter('ChannelMappingDocument.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Channel Insights', index=False)
    writer.close()

create_channel_mapping_document()