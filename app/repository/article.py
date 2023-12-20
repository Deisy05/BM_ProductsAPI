from sqlalchemy.orm import Session  
from app.dataBase import models  

  
def create_article(article,db:Session):  
    myarticle = article.model_dump()
    subcategory = db.query(models.Subcategory).filter_by(name=myarticle["subcategory_name"]).first()
    if not subcategory:
        raise Exception(f"subcategory not found")
    new_article = models.Articles(
        name= myarticle["name"],
        state= myarticle["state"],
        price= myarticle["price"],
        stock= myarticle["stock"],
        descriptions= myarticle["descriptions"],
        subcategory_id= subcategory.id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    
def get_article(nameC,db:Session):
    anArticle = db.query(models.Articles).filter(models.Articles.name == nameC).first()
    if not anArticle:
        raise Exception (f"article not found")    
    return anArticle

def get_articles(db:Session):
    data = db.query(models.Articles).all()
    return data

def delete_article(nameC,db:Session):
    article = db.query(models.Articles).filter(models.Articles.name == nameC)
    if not article.first():
        raise Exception (f"article not found")
    article.delete(synchronize_session=False)
    db.commit()
    return "article has been removed successfully"

def update_article(nameC,update,db:Session):
    article = db.query(models.Articles).filter(models.Articles.name == nameC)
    if not article.first():
        raise Exception ( f"article not found")
    article.update(update.model_dump(exclude_unset=True))
    db.commit()
    
    return "article has been updated"  