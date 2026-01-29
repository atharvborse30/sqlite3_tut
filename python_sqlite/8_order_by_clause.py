import sqlite3

connection = sqlite3.connect('geeks_database.db')


connection.execute('''CREATE TABLE customer_address(
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    AGE INT NOT NULL,
    ADDRESS CHAR(50)
);''')

# insert 5 records into the customer_address table
connection.execute("INSERT INTO customer_address VALUES (1, 'nikhil teja', 22, 'hyderabad')")
connection.execute("INSERT INTO customer_address VALUES (2, 'karthik', 25, 'khammam')")
connection.execute("INSERT INTO customer_address VALUES (3, 'sravan', 22, 'ponnur')")
connection.execute("INSERT INTO customer_address VALUES (4, 'deepika', 25, 'chebrolu')")
connection.execute("INSERT INTO customer_address VALUES (5, 'jyothika', 22, 'noida')")

# display all details from the table in ascending order based on address
cursor = connection.execute("SELECT ADDRESS, ID FROM customer_address ORDER BY ADDRESS")
for i in cursor:
    print(i)

print()

# display address and id based on the address in descending order
cursor = connection.execute("SELECT ADDRESS, ID FROM customer_address ORDER BY ADDRESS DESC")
for i in cursor:
    print(i)
print()
    
# display name and id based on name in descending order
cursor = connection.execute("SELECT NAME, ID  from customer_address ORDER BY NAME DESC")
for i in cursor:
    print(i)

connection.close()