import pandas as pd
import os
import mysql.connector
import csv

# Open the CSV file for reading
temp = r'C:\Users\rahulb\Desktop\Employee_Sample_Data.CSV'
with open(temp, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Create a list to store data from the CSV
    data = []

    # Read and store data from the CSV file
    for row in csv_reader:
        data.append(row)


file_path = temp  # Replace with the correct file path
if os.path.exists(file_path):
    print(f"The file '{file_path}' exits.")
else:
    print(f"The file '{file_path}' does not exist.")

# Replace 'your_file.csv' with the actual path to your CSV file
df = pd.read_csv(temp)
duplicate_rows = df[df.duplicated()]

# Display the duplicate rows
print("Duplicate Rows:")
print(duplicate_rows)
# Remove duplicate rows and update the DataFrame
df = df.drop_duplicates()

# Optionally, you can save the updated DataFrame to a new CSV file
df.to_csv('updated_file.csv', index=False)
# Define the MySQL connection parameters
host = "localhost"       # Replace with your MySQL server host
user = "root"             # Replace with your MySQL username
password = "Mario123$"   # Replace with your MySQL password
database = "demo"         # Replace with your target database


# Establish the database connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

Tables_available_in_Mysql = []
check_tables = ['emp', 'loan', 'dept']

cursor = connection.cursor()

tables = "SHOW TABLES;"

cursor.execute(tables)
results = cursor.fetchall()
for i in range(len(results)):
    Tables_available_in_Mysql.append(results[i][0])

print(Tables_available_in_Mysql)

for i in range(len(check_tables)):
    if check_tables[i] not in Tables_available_in_Mysql:
        print("Table is not there in MySql:", Tables_available_in_Mysql[i])

print("All tables are present")
folder_path1 = r(temp)

df = pd.read_csv(folder_path1)
