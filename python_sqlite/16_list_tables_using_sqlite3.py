import sqlite3

try:
    connection = sqlite3.connect('SQLite_Retrieving_data.db')
    print("Connected to SQLite")

    sql_query = """SELECT  name FROM sqlite_master WHERE type='table';"""

    cursor = connection.cursor()

    cursor.execute(sql_query)
    print("List of Tables\n")

    print(cursor.fetchall())

except sqlite3.Error as error:
    print("Failed to execute the above query", error)
    
finally:
    if connection:
        connection.close()
        print("The sqlite connection is closed")
