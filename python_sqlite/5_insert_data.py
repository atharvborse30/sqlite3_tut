import sqlite3

connection = sqlite3.connect('geek.db')
cursor = connection.cursor()

# There are two main methods for inserting data:
# 1. Only Values : Inserting data by specifying the values without column names
# 2. Column names and values : Specifying both column names and their corresponding values for insertion


# USING 1. OPTION only values
# Create table
cursor.execute("""
               CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255), SECTION VARCHAR(255))""")

# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')")
cursor.execute("INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')")

# or OPTION 2.
# Insert data into the table using column names
# cursor.execute("INSERT INTO STUDENT (CLASS, SECTION, NAME) VALUES ('7th', 'A', 'Raju')")
# cursor.execute("INSERT INTO STUDENT (SECTION, NAME, CLASS) VALUES ('B', 'Shyam', '8th')")
# cursor.execute("INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES ('Baburao', '9th', 'C')")

# Display inserted data
print("Data Inserted in the table: ")
cursor.execute("SELECT * FROM STUDENT")
for row in cursor.fetchall():
    print(row)
    
# Commit changes and close connection
connection.commit()
connection.close()