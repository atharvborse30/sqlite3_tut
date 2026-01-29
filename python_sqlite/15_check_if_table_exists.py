# import required module
import sqlite3

# connect to database
con = sqlite3.connect('g4gdata.db')

# create cursor object
cur = con.cursor()

# create tables
cur.execute(
  """CREATE TABLE EMPLOYEE(FIRST_NAME VARCHAR(255),
  LAST_NAME VARCHAR(255),AGE int, SEX CHAR(1), INCOME int);""")
print('EMPLOYEE table created')

cur.execute(
  """CREATE TABLE STUDENT(NAME VARCHAR(255),AGE int, SEX CHAR(1));""")
print('STUDENT table created')

cur.execute(
  """CREATE TABLE STAFF(NAME VARCHAR(255), INCOME int);""")
print('STAFF table created')
print()

# check if table exists
print('Check if STUDENT table exists in the database:')
listOfTables = cur.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='STUDENT'; """).fetchall()

if listOfTables == []:
    print('Table not found!')
else:
    print('Table found!')

# check if table exists
print('Check if TEACHER table exists in the database:')
listOfTables = cur.execute(
  """SELECT name FROM sqlite_master WHERE type='table' 
  AND name='TEACHER'; """).fetchall()

if listOfTables == []:
    print('Table not found!')
else:
    print('Table found!')

# commit changes
con.commit()

# terminate the connection
con.close()