import mysql.connector

 

host = "localhost"
user = "root"
password = "MBVbgm137$$$"
database = "practiceck"

 

# Establish the database connection

connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
cursor = connection.cursor()


Tables_available_in_Mysql=[]
check_tables = ['employeedata']

table_name = "employeedata"
column_name = "ExitDate"
query = "SELECT EEID,FullName FROM employeedata WHERE ExitDate IS  NULL"
   


EEID='E023875'
FullName='Emily Davis'
ExitDate=None




cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
#print(tables)

##for testing Table Exist or not
print('Check for Existance of Table')
for table in tables:
    if list(table) == check_tables:
        print("Table Exist")
print('*'*50)    
##for testing exitdate is null
print('Check for ExitDate IS  NULL')
cursor.execute(query)
null_rows = cursor.fetchall()
if null_rows:
    print(f"Rows with null values in {column_name}:")
    for row in null_rows:
        print(row)
else:
    print(f"No null values found in {column_name}.")
print('*'*50)  

print('Check for Data Error')
insert_query = "INSERT INTO {} (EEID, FullName, ExitDate) VALUES (%d, %s, %s)".format(table_name)
data = (EEID, FullName, ExitDate)
try:
    cursor.execute(insert_query, data)
    connection.commit()
    print("Data inserted successfully!")
except mysql.connector.Error as error:
    print("Error while inserting data:", error)

print('*'*50)  

print('Check for Duplicates')
query1 = f"select distinct EEID, FullName, count(*) FROM {table_name} GROUP BY  EEID, FullName HAVING COUNT(*) > 1"
cursor.execute(query1)
duplicate_rows = cursor.fetchall()
if duplicate_rows:
    print("Duplicate rows:")
    for row in duplicate_rows:
        print(row)
else:
    print("No duplicate rows found.")		
