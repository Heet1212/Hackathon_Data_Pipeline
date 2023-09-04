import os
import sys
import pandas as pd
import time

#Checking whether the files in the folder that are available or not

Necessarty_files = ['a1.xlsx', 'a2.xlsx', 'a3.xlsx']
folder_path = 'C:\Project\Project_Excel _files'

l_files = os.listdir(folder_path)

file_count = len(l_files)

if len(l_files) >= 3:
    
    for i in range(len(Necessarty_files)):
        if Necessarty_files[i] not in l_files :
             print("This file is not available:",l_files[i])
             sys.exit(1)
else:
    print("Thge file count in this folder is less than 3")

print("All file are Available:",Necessarty_files)

#Checking whether the Tables in the Mysql DB that are available or not

import mysql.connector

host = "localhost"
user = "root"
password = "Rajesh@8865"
database = "demo"

# Establish the database connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

Tables_available_in_Mysql=[]
check_tables = ['account', 'branch', 'customer',]

cursor = connection.cursor()

tables = "SHOW TABLES;"


cursor.execute(tables)
results = cursor.fetchall()
for i in range(len(results)):
    Tables_available_in_Mysql.append(results[i][0])
    
print(Tables_available_in_Mysql)

for i in range(len(check_tables)):
    if  check_tables[i] not in Tables_available_in_Mysql:
        print("Table is not there in MySql:",Tables_available_in_Mysql[i])


print("All tables are present")

#Checking the latency of the file

folder_path1 = r'C:\Project\Project_Excel _files\ages_dataset.csv' 
   
str_tm = time.time()
df = pd.read_csv(folder_path1)

df.iloc[100000]
end_time = time.time()
print(float(end_time-str_tm))

str_tm1 = time.time()
df1 = pd.read_csv(folder_path1)

df1.iloc[100]
end_time1 = time.time()
print(float(end_time1-str_tm1))
print(end_time1)



