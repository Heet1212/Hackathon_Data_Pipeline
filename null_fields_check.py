import pandas as pd
import json
import sqlite3

def find_null_fields_csv(csv_file_path):
    try:
        df = pd.read_csv(csv_file_path,encoding='unicode_escape')
        print(df)
        null_locations = df.isnull()
        test=rows, cols = null_locations.values.nonzero()
        print( df.isnull().sum())
        return list(zip(rows+2, df.columns[cols]))
        #null_fields = df.columns[df.isnull().any()].tolist()
       # null_rows =  df[df.isnull().any(axis=1)]

       
        return null_fields
    except Exception as e:
        return str(e)

def find_null_fields_json(json_file_path):
    try:
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        
        null_fields = []
        find_null_fields_recursive(data, null_fields)
        return null_fields
    except Exception as e:
        return str(e)

def find_null_fields_recursive(data, null_fields, parent_key=''):
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}.{key}" if parent_key else key
            find_null_fields_recursive(value, null_fields, new_key)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]" if parent_key else f"[{i}]"
            find_null_fields_recursive(item, null_fields, new_key)
    elif data is None:
        null_fields.append(parent_key)

def find_null_fields_sqlite(sqlite_file_path, table_name):
    try:
        conn = sqlite3.connect(sqlite_file_path)
        query = f"PRAGMA table_info({table_name})"
        cursor = conn.execute(query)
        columns = [row[1] for row in cursor.fetchall()]
        
        null_fields = []
        for column in columns:
            query = f"SELECT COUNT(*) FROM {table_name} WHERE {column} IS NULL"
            cursor = conn.execute(query)
            result = cursor.fetchone()
            if result and result[0] > 0:
                null_fields.append(column)
        
        return null_fields
    except Exception as e:
        return str(e)

def find_null_fields_log(log_file_path):
    try:
        # Implement your custom logic to parse log files and find null fields.
        # This will depend on the specific format of your log files.
        # You may need to use regular expressions or other parsing techniques.
        
        # Example:
        with open(log_file_path, 'r') as log_file:
            lines = log_file.readlines()
        
        null_fields = []
        for line in lines:
            # Implement parsing logic here.
            # If a null field is found, add it to the null_fields list.
            pass
        
        return null_fields
    except Exception as e:
        return str(e)

def auto_detect_and_find_null_fields(file_path):
    file_extension = file_path.split('.')[-1].lower()
    
    if file_extension == 'csv':
        return find_null_fields_csv(file_path)
    elif file_extension == 'json':
        return find_null_fields_json(file_path)
    elif file_extension == 'db':
        # You can also check for database-specific file extensions
        return find_null_fields_sqlite(file_path, "your_table_name")
    elif file_extension == 'log':
        return find_null_fields_log(file_path)
    else:
        return "Unsupported file type"

if __name__ == "__main__":
    # Example usage with automatic file type detection
    print("please enter file ")
    file_path = input()  # Replace with your file path
    null_fields = auto_detect_and_find_null_fields(file_path)
    if isinstance(null_fields, list):
        if len(null_fields) > 0:
            print("Null fields found:")
            for field in null_fields:
                print(field)
        else:
            print("No null fields found.")
    else:
        print("Error:", null_fields)
