#several arguments can be passed in our decorator which are called path operation configuration 

#response status code 

from typing import Union, Annotated,Optional,List
from fastapi import FastAPI,HTTPException,status
from pydantic import BaseModel

app=FastAPI()

class Item(BaseModel):
    item_name:str
    item_id:Union[int,None]=None
    price:float
    tax:Union[float,None]=None
    tags:List[str]=set()

@app.post('/items/',response_model=Item,status_code=status.HTTP_201_CREATED)
async def create_item(item:Item):
    return item

