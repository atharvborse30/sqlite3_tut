import sqlite3

connection = sqlite3.connect('geek.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS GEEK")

table_creation_query = """
    CREATE TABLE GEEK (
        Email VARCHAR(255) NOT NULL,
        First_Name CHAR(25) NOT NULL,
        Last_Name CHAR(25),
        Score INT
    );
"""

# execute the table creation query
cursor.execute(table_creation_query)

# confirm that the table has been created
print("Table is Ready")

# Closing the connection to the database
connection.close()