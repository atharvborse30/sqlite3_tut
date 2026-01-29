import sqlite3

# Connecting to sqlite
connection_obj = sqlite3.connect('geek.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")

# Creating table
table = """ CREATE TABLE GEEK (
            Email VARCHAR(255) NOT NULL,
            Name CHAR(25) NOT NULL,
            Score INT
        ); """

cursor_obj.execute(table)

# Inserting data into geek table
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk1@gmail.com","Geek1",25)""")
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk2@gmail.com","Geek2",15)""")
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk3@gmail.com","Geek3",36)""")
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk4@gmail.com","Geek4",27)""")
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk5@gmail.com","Geek5",40)""")
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk6@gmail.com","Geek6",14)""")
connection_obj.execute(
    """INSERT INTO GEEK (Email,Name,Score) VALUES ("geekk7@gmail.com","Geek7",10)""")

# Display table
data = cursor_obj.execute("""SELECT * FROM GEEK""")
print('GEEK Table:')
for row in data:
    print(row)
print()

    
# now we add a new column "UserName"
new_column = "ALTER TABLE GEEK ADD COLUMN UserName CHAR(25)"

# display table
data = cursor_obj.execute("SELECT * FROM GEEK")
print("GEEK Table: ")
for row in data:
    print(row)
print()


# change the name of the table
# select from sqlite_master
cursor_obj.execute("SELECT * FROM sqlite_master")

table = cursor_obj.fetchall()
print("Before changing the name of Table")
print("The name of the table:", table[0][2])

# Rename the SQLite Table
renameTable = "ALTER TABLE GEEK RENAME TO GFG"
cursor_obj.execute(renameTable)


# select from sqlite_master
cursor_obj.execute("SELECT * FROM sqlite_master")

table = cursor_obj.fetchall()

print("After changing the name of Table")
print("The name of the table:", table[0][2])


connection_obj.commit()

# Close the connection
connection_obj.close()