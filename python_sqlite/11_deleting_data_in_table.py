import sqlite3

connection = sqlite3.connect('geek.db')

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS GEEK")

# create the GEEK table
table = """CREATE TABLE GEEK (
    Email VARCHAR(255) NOT NULL,
    Name CHAR(25) NOT NULL,
    Score INT);
    """
    
cursor.execute(table)

# Insert some data into the GEEK table
data = [
    ("geekk1@gmail.com", "Geek1", 25),
    ("geekk2@gmail.com", "Geek2", 15),
    ("geekk3@gmail.com", "Geek3", 36),
    ("geekk4@gmail.com", "Geek4", 27),
    ("geekk5@gmail.com", "Geek5", 40),
    ("geekk6@gmail.com", "Geek6", 14),
    ("geekk7@gmail.com", "Geek7", 10),
]

cursor.executemany("INSERT INTO GEEK (Email, Name, Score) VALUES (?, ?, ?)", data)
print()

# Deleting data from the table
# 1. Delete Rows with condition
cursor.execute("DELETE FROM GEEK WHERE Score < 15")

# 2. Delete all Rows
# display all data before deletion
cursor.execute("SELECT * FROM GEEK")
print("Data before Deletion: ")
print(cursor.fetchall())
print()

# delete all rows to the database
cursor.execute("DELETE FROM GEEK")

# display all data after deletion
cursor.execute("SELECT * FROM GEEK")
print("\nData after deletion: ")
print(cursor.fetchall())


connection.commit()
connection.close()