import sqlite3

connection = sqlite3.connect('geek.db')
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS GEEK")

connection.execute("""CREATE TABLE GEEK(
    Email varchar(255),
    Name varchar(50),
    Score int
    );
""")

connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk1@gmail.com','Geek1',21)""")
connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk2@gmail.com','Geek2',22)""")
connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk3@gmail.com','Geek3',23)""")
connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk4@gmail.com','Geek4',24)""")
connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk5@gmail.com','Geek5',25)""")
connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk6@gmail.com','Geek6',26)""")
connection.execute("""INSERT INTO GEEK (Email, Name, Score) VALUES ('geekk7@gmail.com','Geek7',27)""")

# to select all column we will use
statement = '''SELECT * FROM GEEK'''

cursor.execute(statement)

print('All the data...')
output = cursor.fetchall()
for row in output:
    print(row)

# Reset the cursor to the beginning of the result set to read some rows
cursor.execute(statement)  # Re-execute the query

print("Limited data...")
limited_output = cursor.fetchmany(5)
for row in limited_output:
    print(row)

# Reset the cursor again to read only one row
cursor.execute(statement)  # Re-execute the query

print("Only one data...")
one_row_output = cursor.fetchone()
print(one_row_output)

connection.commit()

# close the connection
connection.close()