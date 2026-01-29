import sqlite3

# Function to Convert Binary data to human readable format
def convertToBinaryData(filename):
    
    # convert binary format to images or files data
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(name, photo):
    try:
        # Using connect method for establishing a connection
        sqliteConnection = sqlite3.connect('SQLite_Retrieving_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        
        # insert query
        sqlite_insert_blob_query = """INSERT INTO Student (name, img) VALUES (?,?)"""
        
        # converting human readable file into binary data
        empPhoto = convertToBinaryData(photo)
        
        # convert data into tuple format
        data_tuple = (name, empPhoto)
        
        # using cursor object executing our query
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and ile inserted successfully as a BLOB into a table")
        cursor.close()
        
    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
        
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")
            
insertBLOB("Smith", "sqli_image.jpeg")
