import sqlite3

connection = sqlite3.connect('ship_database.db')  # Provide a database filename

connection.execute('''CREATE TABLE ship (ship_id INT, ship_name TEXT NOT NULL, ship_destination CHAR(50) NOT NULL);''')
print("ship table created successfully!")

# insert query to insert values
connection.execute("INSERT INTO ship  VALUES (1, 'tata-hitachi','noida' )")
connection.execute("INSERT INTO ship  VALUES (2, 'tata-mumbai','mumbai' )")
connection.execute("INSERT INTO ship  VALUES (3, 'tata-express','hyderabad' )")

# query to display all data in the table
cursor = connection.execute("SELECT * from ship")
print("Actual data")

# display row by row
for row in cursor:
    print(row)

# query to delete all data where ship_id = 2
connection.execute("DELETE from ship where ship_id=2")

print("After  deleting ship id = 2 row")

# display row by row
cursor = connection.execute("SELECT * from ship")
for row in cursor:
    print(row)
print()


# delete data where the ship address is hyderabad on the same table
connection.execute("DELETE from ship where ship_destination='hyderabad'")
print("After deleting ship address = hyderabad row")
cursor = connection.execute("SELECT * from ship")
for row in cursor:
    print(row)

# close the connection
connection.close()