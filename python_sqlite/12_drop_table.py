import sqlite3

connection = sqlite3.connect('geeks_database.db')


connection.execute('''CREATE TABLE customer_address
                   (ID INT PRIMARY KEY NOT NULL,
                   NAME TEXT NOT NULL,
                   AGE INT NOT NULL,
                   ADDRESS CHAR(50)); ''')

# insert records into table
connection.execute(
    "INSERT INTO customer_address VALUES (1, 'nikhil teja', 22, 'hyderabad' )")

connection.execute(
    "INSERT INTO customer_address VALUES (2, 'karthik', 25, 'khammam')")

connection.execute(
    "INSERT INTO customer_address VALUES (3, 'sravan', 22, 'ponnur' )")

connection.execute(
    "INSERT INTO customer_address VALUES (4, 'deepika', 25, 'chebrolu' )")

connection.execute(
    "INSERT INTO customer_address VALUES (5, 'jyothika', 22, 'noida')")

# drop table
connection.execute("DROP TABLE customer_address")

print("data dropped successfully !")

connection.close()