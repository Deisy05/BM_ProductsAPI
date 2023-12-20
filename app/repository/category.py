from sqlalchemy.orm import Session  
from app.dataBase import models  

  
def create_category(category,db:Session):  
    mycategory = category.model_dump()
    new_category = models.Category(
        name= mycategory["name"],
        state= mycategory["state"]
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    
def get_category(nameC,db:Session):
    acategory = db.query(models.Category).filter(models.Category.name == nameC).first()
    if not acategory:
        return "Category not found"    
    return acategory

def get_categories(db:Session):
    data = db.query(models.Category).all()
    return data

def delete_category(nameC,db:Session):
    category = db.query(models.Category).filter(models.Category.name == nameC)
    if not category.first():
        return "Category not found"
    category.delete(synchronize_session=False)
    db.commit()
    return "Category has been removed successfully"

def update_category(nameC,updateCategory,db:Session):
    category = db.query(models.Category).filter(models.Category.name == nameC)
    if not category.first():
        return "Category not found"
    category.update(updateCategory.model_dump(exclude_unset=True))
    db.commit()
    
    return "Category has been updated"  