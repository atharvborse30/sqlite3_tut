import sqlite3

connection = sqlite3.connect('hotel_data.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM hotel")

# Fetch all records
rows = cursor.fetchall()

print("All Food Items:\n")
for row in rows:
    print(f"Food ID: {row[0]}, Name: {row[1]}, Cost: {row[2]}, Weight: {row[3]}")
    
cursor.close()