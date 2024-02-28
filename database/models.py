#now we will create the sql database app which is the model
from sqlalchemy import Boolean, Column, ForeignKey, Integer,String

from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__='users'

    id=Column(Integer,primary_key=True)
    email=Column(String,unique=True,index=True)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)

    items=relationship('Item',back_populates='owner')
    #every class is basically a seperate table, the relationship functon allows to build a communication with 2 different tables, here the items is related to owner, which basically means that every item has an owner or multiple owners, for user, every user can own an item or multiple items, this is how we create a sqlalchemy model, now this needs to communicate with the pydantic model for it to be effectively used by our web application
    

class Item(Base):
    __tablename__='items'
    id=Column(Integer, primary_key=True)
    title=Column(String,index=True)
    description=Column(String,index=True)
    owner_id=Column(Integer,ForeignKey('users.id'))

    owner=relationship('User',back_populates='items')



