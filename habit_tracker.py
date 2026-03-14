import pandas as pd
from datetime import datetime, timedelta

# 1. Dashboard and Log setup
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)
date_range = pd.date_range(start_date, end_date)

data = {
    'Date': date_range.strftime('%Y-%m-%d'),
    'Day': date_range.strftime('%A'),
    'Fajr': '❌', 'Dhuhr': '❌', 'Asr': '❌', 'Maghrib': '❌', 'Isha': '❌',
    'Gym': '❌',
    'DSA_Solved': 0,
    'JS_Hrs': 0, 'TS_Hrs': 0, 'React_Hrs': 0, 'Next_Hrs': 0, 'GSAP_3JS_Hrs': 0,
    'Total_Study_Hrs': 0,
    'Daily_Score_%': 0
}

df = pd.DataFrame(data)

# 2. Save to Excel with formatting
file_name = "Premium_Habit_Tracker_2026.xlsx"
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Daily_Log', index=False)

workbook  = writer.book
worksheet = writer.sheets['Daily_Log']

# 3. Premium Styling (Dark Theme Vibes)
header_format = workbook.add_format({
    'bold': True, 'text_wrap': True, 'valign': 'top',
    'fg_color': '#1E1E1E', 'font_color': '#00FF00', 'border': 1
})

# Apply formatting to headers
for col_num, value in enumerate(df.columns.values):
    worksheet.write(0, col_num, value, header_format)

# 4. Conditional Formatting (The Heatmap Logic)
green_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

# Dropdown for ✅/❌
worksheet.data_validation('C2:H366', {'validate': 'list', 'source': ['✅', '❌']})

writer.close()
print(f"🔥 Boom! '{file_name}' toiri hoye geche. Google Colab-er file section theke download korun.")