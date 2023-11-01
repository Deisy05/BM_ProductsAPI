from app.dataBase.db import Base
from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__= "category"
    id= Column (Integer, primary_key=True,autoincrement=True)
    name = Column (String)
    state = Column (Boolean, default=True)
    subcategory = relationship("Subcategory",backref="category",cascade="delete,merge")
        
class Subcategory(Base):
    __tablename__="subcategory"
    id= Column (Integer, primary_key=True,autoincrement=True)       
    category_id= Column(Integer, ForeignKey ("category.id",ondelete="CASCADE"))
    name = Column (String)
    category_name=str
    state = Column (Boolean, default=True)
     
class Articles(Base):
    __tablename__="articles"
    id= Column (Integer, primary_key=True,autoincrement=True)       
    subcategory_id= Column(Integer, ForeignKey ("subcategory.id",ondelete="CASCADE"))
    name = Column (String)
    subcategory_name=str
    price = int
    stock = int
    descriptions= str
    state = Column (Boolean, default=True)      