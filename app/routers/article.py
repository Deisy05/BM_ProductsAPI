from fastapi import APIRouter, Depends
from app.schemas import Articles, ShowArticle
from app.dataBase.db import get_db
from sqlalchemy.orm import Session
from app.dataBase import models
from typing import List
from app.repository import article


router = APIRouter(
    prefix="/article",
    tags=["Articles"]
)



@router.get("/", response_model=List[ShowArticle])
def get_articles(db:Session = Depends(get_db)):
    data=article.get_articles(db)
    return data

@router.get("/{article_name}",response_model=ShowArticle)
def get_article(article_name:str,db:Session = Depends(get_db)):
    anArticle = article.get_article(article_name,db)
    return anArticle

@router.post("/")
def create_article(myArticle: Articles,db:Session = Depends(get_db)):
    article.create_article(myArticle,db)
    return "article has been created successfully"

@router.delete("/")
def delete_article(article_name: str,db:Session = Depends(get_db)):
    answer = article.delete_article(article_name,db)
    return answer

@router.patch("/{article_name}")
def update_article(article_name:str, updateArticle: Articles,db:Session = Depends(get_db)):
    articleU = article.update_article(article_name,updateArticle,db)
    return articleU
      
    