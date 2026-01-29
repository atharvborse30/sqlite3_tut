import sqlite3

connection = sqlite3.connect('geekforgeeks_student.db')
cursor = connection.cursor()

# create table
cursor.execute("DROP TABLE IF EXISTS STUDENT")
createTable = '''CREATE TABLE STUDENT(
    Student_ID int, First_Name VARCHAR(100),
    Last_Name VARCHAR(100), Age int,
    Department VARCHAR(100)
    )'''
    
cursor.execute(createTable)

# check the database creation data
if cursor:
    print("Database Created Successfully !")
else:
    print("Database Creation Failed !")
    
# insert data into STUDENT table
cursor.execute("INSERT INTO STUDENT VALUES (1, 'Rohit','Pathak', 21, 'IT')")
cursor.execute("INSERT INTO STUDENT VALUES (2, 'Nitin','Biradar', 21, 'IT')")
cursor.execute("INSERT INTO STUDENT VALUES (3, 'Virat','Kohli', 30, 'CIVIL')")
cursor.execute("INSERT INTO STUDENT VALUES (4, 'Rohit','Sharma', 32, 'COMP')")  

# printing the cursor data
if cursor:
    print("Data Inserted")
else:
    print("Data Insertion Failed !")
    
# Retrieve the data of the students whose Department is IT
cursor.execute("SELECT * FROM STUDENT WHERE Department = 'IT'")
# printing the cursor data
print(cursor.fetchall())
print()

# Retrieve the data of the students whose First Name start with 'R'. 
cursor.execute("SELECT * FROM STUDENT WHERE First_name Like'R%'")
print(cursor.fetchall())
print()

# Update the data of student whose Student ID is 2
cursor.execute("UPDATE STUDENT SET Department = 'E&TC' WHERE Student_ID = 2")
cursor.execute("SELECT * FROM STUDENT")
print(cursor.fetchall())
print()

# Delete the data of student whose Age ID is 32
cursor.execute("DELETE FROM STUDENT WHERE AGE = 32")
cursor.execute("SELECT * FROM STUDENT")
print(cursor.fetchall())    

# commit the changes in database and close the connection
connection.commit()
connection.close()