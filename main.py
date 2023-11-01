from fastapi import FastAPI
import uvicorn
from app.routers import category,subcategory,article
from app.dataBase.db import Base,engine

def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()


app = FastAPI()
app.include_router(category.router)
app.include_router(subcategory.router)
app.include_router(article.router)

@app.get("/")
def root():
    return "Que más pues"
    


if __name__ == '__main__':
    uvicorn.run("main:app",port=8686)






