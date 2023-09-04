import pandas as pd
excel_file_path = input("Enter the path to the Excel file: ")
# excel_file_path ='C:/Project/EmployeeSampleDataChange1.csv'


 
required_columns =['EEID', 'Full Name', 'Job Title', 'Department', 'Business Unit','Bonus %','Gender','Ethnicity','Age','Hire Date','Annual Salary','Country','City','Exit Date']


try:

    df = pd.read_csv(excel_file_path,encoding = "ISO-8859-1")

    # column names from the DataFrame
    columns_present = set(df.columns.tolist())

    # Checking if all required columns are present
    if set(required_columns) == columns_present:
        print("All required columns are present in the Excel file.")
    else:
        print("Not all required columns are present in the Excel file.")
        # Print the missing columns
        missing_columns = set(required_columns).difference(columns_present)
        # missing_columns = set(required_columns - columns_present)
        print("Missing columns:", missing_columns)
        # print(columns_present)
        # print(required_columns)

 

except FileNotFoundError:
    print(f"File '{excel_file_path}' not found.")
except Exception as e:
    print("An error occurred:", str(e))