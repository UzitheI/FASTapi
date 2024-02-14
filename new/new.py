#fast api handles asynchronous communication between apis for that it uses a model called asgi which is counterpart to wsgi(synchronous)
#fast api depends on starlette and pydant for communication
#it also requires a asgi server for which i installed uvicorn standard version 

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def read_root():
    return {"hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id:int,q:Union[str,None]=None):
    return {"item_id":item_id,"q":q}
