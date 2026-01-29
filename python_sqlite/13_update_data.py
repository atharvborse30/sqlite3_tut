import sqlite3

connection = sqlite3.connect('gfg1.db')
cursor = connection.cursor()

# Creating table
table = """CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(255), 
LAST_NAME VARCHAR(255),AGE int, SEX VARCHAR(255), INCOME int);"""
cursor.execute(table)

# Queries to INSERT records.
cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Anand', 'Choubey', 25, 'M', 10000)''')

cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
    VALUES ('Mukesh', 'Sharma', 20, 'M', 9000)''')

cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Ankit', 'Pandey', 24, 'M', 6300)''')

cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Subhdra ', 'Singh', 26, 'F', 8000)''')

cursor.execute(
    '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
    VALUES ('Tanu', 'Mishra', 24, 'F', 6500)''')

# Display data inserted
print("EMPLOYEE Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)  
print()

# Updating - set the income of employees to 5000 whose age is less than 25
cursor.execute('''UPDATE EMPLOYEE SET INCOME = 5000 WHERE Age<25;''')
print('\nAfter Updating...\n')

# Display data
print("EMPLOYEE Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)
print()


# update - assign the age of female employees to 0
cursor.execute('''UPDATE EMPLOYEE SET AGE = 0 WHERE SEX='F';''')
print('\nAfer Updating...\n')

# Display data
print("EMPLOYEE Table: ")
data = cursor.execute('''SELECT * FROM EMPLOYEE''')
for row in data:
    print(row)
print()


# update multiple columns - create a STAFF table and insert values into it. Then update all columns. i.e all the attributes of the staff whose department is Computer
# Creating table
table ="""CREATE TABLE STAFF(NAME VARCHAR(255), AGE int,
DEPARTMENT VARCHAR(255));"""
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STAFF VALUES('Anand', 45, 'Chemistry')''')
cursor.execute('''INSERT INTO STAFF VALUES('Ravi', 32, 'Physics')''')
cursor.execute('''INSERT INTO STAFF VALUES('Chandini', 32, 'Computer')''')
cursor.execute('''INSERT INTO STAFF VALUES('Latika', 40, 'Maths')''')

# Display data inserted
print("STAFF Table: ")
data=cursor.execute('''SELECT * FROM STAFF''')
for row in data:
    print(row)

# Updating    
cursor.execute('''UPDATE STAFF SET NAME = 'Ram', AGE = 30, 
DEPARTMENT = 'Biology' WHERE DEPARTMENT = 'Computer';''')
print('\nAfter Updating...\n')

# Display data 
print("STAFF Table: ")
data=cursor.execute('''SELECT * FROM STAFF''')
for row in data:
    print(row)
    
print()


# update the name and age of the staff whose department is Chemistry
# Display data inserted
print("STAFF Table: ")
data=cursor.execute('''SELECT * FROM STAFF''')
for row in data:
    print(row)

# Updating    
cursor.execute('''UPDATE STAFF SET NAME = 'Chandini', 
AGE = 32 WHERE DEPARTMENT = 'Chemistry';''')
print('\nAfter Updating...\n')

# Display data 
print("STAFF Table: ")
data=cursor.execute('''SELECT * FROM STAFF''')
for row in data:
    print(row)
print()


# update statement without the WHERE  statement. we create STUDENT table and insert values into it.
# after that , update the SECTION column of all the students by assigning it to X.
# Creating table
table ="""CREATE TABLE STUDENT(NAME VARCHAR(255), CLASS VARCHAR(255),
SECTION VARCHAR(255));"""
cursor.execute(table)

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju', '7th', 'A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''')

# Display data inserted
print("STUDENT Table: ")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Updating    
cursor.execute('''UPDATE STUDENT SET SECTION = 'X';''')
print('\nAfter Updating...\n')

# Display data 
print("STUDENT Table: ")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)
print()


# update all the data into it using only UPDATE and SET query.
# Updating    
cursor.execute('''UPDATE STUDENT SET NAME = 'X',
CLASS = 'Y', SECTION = 'Z';''')
print('\nAfter Updating...\n')

# Display data 
print("STUDENT Table: ")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)
    
# Commit your changes in the database    
connection.commit()

# Closing the connection
connection.close()