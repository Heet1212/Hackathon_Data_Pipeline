import pandas as pd
from datetime import datetime

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

file_path = 'EmployeeSampleData.xlsx' 
date_column_name = 'Hire Date' 

try:
    df = pd.read_excel(file_path)
except Exception as e:
    print(f"Error reading the Excel file: {str(e)}")
    exit()

for index, row in df.iterrows():
    date_column = str(row[date_column_name])
    if not is_valid_date(date_column):
        print(f"Row {index + 2}: {date_column} has an invalid date format in the 'Hire Date' column")
