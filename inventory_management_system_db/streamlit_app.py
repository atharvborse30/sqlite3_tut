import streamlit as st
import requests
import pandas as pd

# API URL
API_URL = 'http://127.0.0.1:8000'

# Function to fetch items from the API
def get_items():
    response = requests.get(f"{API_URL}/items")
    response.raise_for_status()
    return response.json()

# Function to fetch a single item from the API
def get_item(item_id):
    response = requests.get(f"{API_URL}/items/{item_id}")
    response.raise_for_status()
    return response.json()

# Function to add a new item to the API
def add_item(item_data):
    response = requests.post(f"{API_URL}/items", json=item_data)
    response.raise_for_status()
    return response.json()

# Function to update an existing item in the API
def update_item(item_id, item_data):
    response = requests.put(f"{API_URL}/items/{item_id}",json=item_data)
    response.raise_for_status()
    return response.json()

# Function to delete an item from the API
def delete_item(item_id):
    response = requests.delete(f"{API_URL}/items/{item_id}")
    response.raise_for_status()
    return response

# Streamlit app
st.title("Simple Inventory Management")

# Display inventory items
items = get_items()
df = pd.DataFrame(items)
st.dataframe(df)

# Add new item form 
with st.form("add_item"):
    st.subheader("Add new Item")
    item_name = st.text_input("Item Name")
    quantity = st.number_input("Quantity", min_value=0, step=1)
    price = st.number_input("Price",min_value=0.0)
    description = st.text_area("Description (optional)")
    submitted = st.form_submit_button("Add Item")
    
    if submitted:
        new_item = {
            "item_name" : item_name,
            "quantity" : quantity,
            "price" : price,
            "description" : description
        }
        try:
            add_item(new_item)
            st.success("Item added successfully")
            # Refresh the inventory
            items = get_items()
            df = pd.DataFrame(items)
            st.dataframe(df)
        except requests.exceptions.RequestException as e:
            st.error(f"Error adding item: {e}")
            
# Edit existing item form
st.subheader("Edit Item")
item_id_to_edit = st.number_input("Enter Item ID to Edit", min_value=1, step=1)
if st.button("Edit"):
    try:
        item = get_item(item_id_to_edit)
        with st.form("edit_item"):
            item_name = st.text_input("Item Name", item["item_name"])
            quantity = st.number_input("Quantity", min_value=0, step=1, value=item["quanityt"])
            price = st.number_input("Price", min_value=0.0, value=item["price"])
            description = st.text_area("Description (optional)", value=item["description"])
            submitted = st.form_submit_button("Update Item")
            
            if submitted:
                update_item = {
                    "item_name" : item_name,
                    "quantity" : quantity,
                    "price" : price,
                    "description" : description
                }
                update_item(item_id_to_edit, update_item)
                st.success("Item update successfully")
                items = get_items()
                df = pd.DataFrame(items)
                st.dataframe(df)
                
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching or updating item: {e}")
        
# Delete Item
st.subheader("Delete Item")
item_id_to_delete = st.number_input("Enter Item ID to Delete", min_value=1, step=1)
if st.button("Delete"):
    try:
        delete_item(item_id_to_delete)
        st.success("Item deleted successfully")
        items = get_items()
        df = pd.DataFrame(df)
        st.dataframe(df)
    except requests.exceptions.RequestException as e:
        st.error(f"Error deleting item: {e}")        