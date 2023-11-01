from pydantic import BaseModel
from typing import Optional

#category_model
class Category(BaseModel):
    name: str
    state: Optional[bool] = None


class ShowCategory(BaseModel):
    name:str
    state: bool
    class config():
        orm_mode =True
        
        
#subcategory_model        
class SubCategory(BaseModel):
    name: str
    category_name: str
    state: Optional[bool] = None
 
    
#articles_model
class Articles(BaseModel):
    name: str
    subcategory_name: str
    price:int
    stock: int
    descriptions: str
    state: Optional[bool] = None   

class ShowArticle(BaseModel):
    name:str
    state: bool
    price: int
    stock: int
    descriptions: str
    class config():
        orm_mode =True       