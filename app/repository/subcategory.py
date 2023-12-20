from sqlalchemy.orm import Session  
from app.dataBase import models  

  
def create_subcategory(subcategory,db:Session):  
    mysubcategory = subcategory.model_dump()
    category = db.query(models.Category).filter_by(name=mysubcategory["category_name"]).first()
    if not category:
        raise Exception(f"Category not found")
    new_subcategory = models.Subcategory(
        name= mysubcategory["name"],
        state= mysubcategory["state"],
        category_id= category.id
    )
    db.add(new_subcategory)
    db.commit()
    db.refresh(new_subcategory)
    
def get_subcategory(nameC,db:Session):
    asubcategory = db.query(models.Subcategory).filter(models.Subcategory.name == nameC).first()
    if not asubcategory:
        raise Exception (f"subcategory not found")    
    return asubcategory

def get_subcategories(db:Session):
    data = db.query(models.Subcategory).all()
    return data

def delete_subcategory(nameC,db:Session):
    subcategory = db.query(models.Subcategory).filter(models.Subcategory.name == nameC)
    if not subcategory.first():
        raise Exception (f"subcategory not found")
    subcategory.delete(synchronize_session=False)
    db.commit()
    return "subcategory has been removed successfully"

def update_subcategory(nameC,update,db:Session):
    subcategory = db.query(models.Subcategory).filter(models.Subcategory.name == nameC)
    if not subcategory.first():
        raise Exception ( f"subcategory not found")
    subcategory.update(update.model_dump(exclude_unset=True))
    db.commit()
    
    return "subcategory has been updated"  