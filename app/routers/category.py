from fastapi import APIRouter, Depends
from app.schemas import Category, ShowCategory
from app.dataBase.db import get_db
from sqlalchemy.orm import Session
from app.dataBase import models
from typing import List
from app.repository import category


router = APIRouter(
    prefix="/category",
    tags=["Categories"]
)



@router.get("/", response_model=List[ShowCategory])
def get_categories(db:Session = Depends(get_db)):
    data=category.get_categories(db)
    return data

@router.get("/{category_name}",response_model=ShowCategory)
def get_category(category_name:str,db:Session = Depends(get_db)):
    acategory = category.get_category(category_name,db)
    return acategory

@router.post("/")
def create_category(myCategory: Category,db:Session = Depends(get_db)):
    category.create_category(myCategory,db)
    return "Category has been created successfully"

@router.delete("/")
def delete_category(category_name: str,db:Session = Depends(get_db)):
    answer = category.delete_category(category_name,db)
    return answer

@router.patch("/{category_name}")
def update_category(category_name:str, updateCategory: Category,db:Session = Depends(get_db)):
    categoryU = category.update_category(category_name,updateCategory,db)
    return categoryU
      
    