import pyodbc

string_connection = (
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-KDB6CJ2;'
    'DATABASE=charity_organization;'
    'TRUSTED_CONNECTION=YES;'
)
try:
    CONN = pyodbc.connect(string_connection)
    print('Connected successfully')
    cursor = CONN.cursor()
    
    cursor.execute('SELECT * FROM donor')
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    cursor.close()
    CONN.close()
except pyodbc.Error as e:
    print(f"Error: {e}")


