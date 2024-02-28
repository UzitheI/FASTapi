from typing import Union
from pydantic import BaseModel
'''
'''

#helps create a relationship between our web app and the sqlalchemy model
class ItemBase(BaseModel):
    title:str 
    description:Union[str,None]=None
    #this class is how we define an item and its attributes

class ItemCreate(ItemBase):
    pass
#this class lets us create an item with the specs mentioned in teh ItemBase class

class Item(ItemBase):
    id:int
    owner_id:int
    #this is where we actually create the item where it has a specific id and has a specific owner mentioned to it

    class Config:
        orm_mode:True
        #sub class to item class, this config class has more details about the item class
        #here the orm mode is responsible for seamless communication between our model and schema, normally this can be explained by:

        '''
        we can input data into our database through our web applicaton, for this we input our data through our pydantic model ie schema and then when orm mode is set to true, it gets transformed into sqlalchmey model data effortlessly
        '''
    
class UserBase(BaseModel):
    email:str

class UserCreate(UserBase):
    password:str

class User(UserBase):
    id:int
    is_active:bool
    items:list[Item]=[]

    class Config:
        orm_mode:True

