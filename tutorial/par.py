from typing import Union
from enum import Enum 

from fastapi import FastAPI

app=FastAPI()

from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:int
    forSale:Union[bool,None]=None

@app.get('/files/{file_path}')
async def read_file(file_path:str):
    return {'file_path':file_path}

@app.put('/files/{item_id}')
async def update_item(item_id:int, item:Item):
    return {'item_name':item.name,'item_price':item.price,'forSale':item.forSale}