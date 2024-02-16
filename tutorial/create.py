from pydantic import BaseModel
from fastapi import FastAPI
from typing import Union
app=FastAPI()

# class Item(BaseModel):
#     item_id:int
#     item_name:str
#     forSale:Union[bool,None]=None
@app.get('/')
def root():
    return {"hello":"hell0"}

# @app.get('/items/{item_id}')
# def root_id(id:int,q=Union[str,None]=None):
#     return {"item-id":id,"query":q}

# @app.put('/items/{item_id}')
# def update():

#order matters in fast api which means that if we have a user defined route, we have to write it before the get request where we can pass custom route

@app.get('/items/me')
async def get_me():
    return {'mssg':'This is the current user'}


@app.get("/items/{item_id}")
def read_item(item_id:Union[str,int,None]=None):
    if item_id is None:
        return {'msg':'no id present'}
    #this is invalid code because why would the id be empty
    else:
        return {'item_id':item_id}


#
