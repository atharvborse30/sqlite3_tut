import sqlite3

connection = sqlite3.connect('hotel_data.db')
cursor = connection.cursor()

# create a new table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS hotel (
                   FIND INTEGER PRIMARY KEY NOT NULL,
                   FNAME TEXT NOT NULL,
                   COST INTEGER NOT NULL,
                   WEIGHT INTEGER
                   )'''
                )

    
connection.close()