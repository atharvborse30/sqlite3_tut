from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    item_name : str
    quantity : int
    price : float
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    item_id : int
    description : Optional[str] = None
    
class ItemUpdate(BaseModel):
    item_name : Optional[str] = None
    quantity : Optional[int] = None
    price : Optional[float] = None
    description : Optional[str] = None
    