from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import sqlite3
from typing import List
import schemas # Import schemas
from schemas import ItemBase, ItemCreate, ItemUpdate, Item

app = FastAPI()

DATABASE_FILE = "inventory.db"

# Dependency to get a database connection
def get_db():
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row   # Access columns by name
    return connection

# Function to create the table if it doesn't exist
def create_table():
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS inventory (
                       item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       item_name TEXT NOT NULL,
                       quantity INTEGER NOT NULL,
                       price REAL,
                       description TEXT
                   )
                   """)
    connection.commit()
    connection.close()
    
create_table()


# API Endpoints

@app.get("/items", response_model=List[Item])
async def get_items(db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory")
    items = [Item(**row) for row in cursor.fetchall()]  # convert rows to Item objects
    return items

@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id : int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM inventory WHERE item_id = ?", (item_id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return Item(**row)

@app.post("/items", response_model=Item)
async def create_item(item : ItemCreate, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO inventory (item_name, quantity, price, description) VALUES (?,?,?,?)",
        (item.item_name, item.quantity, item.price, item.description),
    )
    db.commit()
    item_id = cursor.lastrowid
    new_item = Item(item_id = item_id, item_name=item.item_name, quantity=item.quantity, price=item.price, description=item.description)
    return new_item


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id : int, item : ItemUpdate, dp=Depends(get_db)):
    cursor = db.cursor()
    # Build the update query dynamically based on provided fields
    update_fields = []
    params = []
    if item.item_name is not None:
        update_fields.append("item_name = ?")
        params.append(item.item_name)
    if item.quantity is not None:
        update_fields.append("quantity = ?")
        params.append(item.quantity)
    if item.price is not None:
        update_fields.append("price = ?")
        params.append(item.price)
    if item.description is not None:
        update_fields.append("description = ?")
        params.append(item.description)
        
    if not update_fields:
        raise HTTPException(status_code=400, detail="No fields to update provided")
    
    query = "UPDATE inventory SET " + ", ".join(update_fields) + " WHERE item_id = ?"
    params.append(item_id)
    
    cursor.execute(query, tuple(params))
    db.commit()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    
    updated_item = get_item(item_id, db)  # retrieve the updated item
    return updated_item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int, db=Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM inventory WHERE item_id = ?", (item_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message" : "Item deleted"}