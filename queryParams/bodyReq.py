from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    item_id:int
    price:float
    description:Union[str,None]=None

@app.get('/')
def read():
    return {'mssg':'this is the main page'}

@app.get('/item/{item_id}')
def read_item(price:str):
    return{'mssg':'The item is {item_id} with the price {price}'}

@app.put('/item/{item_id}')
def write_item(item:Item,item_id:int):
    item_id=item.item_id
    item_price=item.price
    item_des=item.description
    return {'mssg':'The item id is {item_id} and the price is {item.price} and the description ={item.description}'}