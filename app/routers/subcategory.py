from fastapi import APIRouter, Depends
from app.schemas import SubCategory, ShowCategory
from app.dataBase.db import get_db
from sqlalchemy.orm import Session
from app.dataBase import models
from typing import List
from app.repository import subcategory


router = APIRouter(
    prefix="/subcategory",
    tags=["Subcategories"]
)



@router.get("/", response_model=List[ShowCategory])
def get_subcategories(db:Session = Depends(get_db)):
    data=subcategory.get_subcategories(db)
    return data

@router.get("/{subcategory_name}",response_model=ShowCategory)
def get_subcategory(subcategory_name:str,db:Session = Depends(get_db)):
    acategory = subcategory.get_category(subcategory_name,db)
    return acategory

@router.post("/")
def create_subcategory(mySubCategory: SubCategory,db:Session = Depends(get_db)):
    subcategory.create_subcategory(mySubCategory,db)
    return "subcategory has been created successfully"

@router.delete("/")
def delete_subcategory(subcategory_name: str,db:Session = Depends(get_db)):
    answer = subcategory.delete_subcategory(subcategory_name,db)
    return answer

@router.patch("/{subcategory_name}")
def update_subcategory(subcategory_name:str, updateSubCategory: SubCategory,db:Session = Depends(get_db)):
    subcategoryU = subcategory.update_subcategory(subcategory_name,updateSubCategory,db)
    return subcategoryU
      
    