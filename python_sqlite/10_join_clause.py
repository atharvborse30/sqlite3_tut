import sqlite3

connection = sqlite3.connect('Geeks.db')

# create cursor object
cursor = connection.cursor()

"""two tables Advisor(AdvisorID, AdvisorName) and Student(StudentID,StudentName,AdvisorID)
   where AdvisorID of the Student table is the foreign key referencing AdvisorID of the Advisor table"""
# create and populate tables
cursor.executescript('''
                     CREATE TABLE Advisor(
                         AdvisorID INTEGER NOT NULL,
                         AdvisorName TEXT NOT NULL,
                         PRIMARY KEY(AdvisorID)
                     );
                     
                     CREATE TABLE Student(
                         StudentID NUMERIC NOT NULL,
                         StudentName NUMERIC NOT NULL,
                         AdvisorID INTEGER,
                         FOREIGN KEY(AdvisorID) REFERENCES Advisor(AdvisorID),
                         PRIMARY KEY(StudentID)
                     );
                     
                     INSERT INTO Advisor(AdvisorID, AdvisorName) VALUES
                     (1, "John Paul"),
                     (2, "Anthony Roy"),
                     (3, "Raj Shetty"),
                     (4, "Sam Reeds"),
                     (5, "Arthur Clintwood");
                     
                     INSERT INTO Student(StudentID, StudentName, AdvisorID) VALUES
                     (501, "Geek1", 1),
                     (502, "Geek2", 1),
                     (503, "Geek3", 3),
                     (504, "Geek4", 2),
                     (505, "Geek5", 4),
                     (506, "Geek6", 2),
                     (507, "Geek7", 2),
                     (508, "Geek8", 3),
                     (509, "Geek9", NULL),
                     (510, "Geek10", 1);
                     ''')

# INNER JOIN - records that have common attributes in both tables
sql = '''SELECT StudentID, StudentName, AdvisorName FROM Student INNER JOIN Advisor ON Student.AdvisorID = Advisor.AdvisorID;'''
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

print()
    
    
# LEFT JOIN - given all records from the table, and only common records from the right table
sql = '''SELECT StudentID, StudentName, AdvisorName 
FROM Student 
LEFT JOIN Advisor
USING(AdvisorID) ;'''
# Executing the query
cursor.execute(sql)
# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)

print()


# RIGHT JOIN 
sql = '''SELECT StudentID, StudentName, AdvisorName 
FROM Advisor 
LEFT JOIN Student
USING(AdvisorID);'''
# Executing the query
cursor.execute(sql)
# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)
    
print()

# FULL OUTER JOIN
sql = '''SELECT StudentID, StudentName, AdvisorName 
FROM Student 
LEFT JOIN Advisor
USING(AdvisorID)
UNION ALL
SELECT StudentID, StudentName, AdvisorName 
FROM Advisor 
LEFT JOIN Student
USING(AdvisorID)
WHERE Student.AdvisorID IS NULL;'''
# Executing the query
cursor.execute(sql)
# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)
    
print()


# CROSS JOIN
sql = '''SELECT StudentID, StudentName, AdvisorName 
FROM Student 
CROSS JOIN Advisor;'''
# Executing the query
cursor.execute(sql)
# Fetching rows from the result table
result = cursor.fetchall()
for row in result:
    print(row)

connection.commit()

connection.close()