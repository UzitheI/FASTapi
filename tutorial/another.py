from typing import Union
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class Model(str, Enum):
    alexnet='finance'
    micah='gym'
    homie='class'

@app.get('/items/{model_name}')
def get_model(model_name:Model):
        if model_name is Model.alexnet:
            return {"model_name":model_name,'mssg':'humanoid'}
        if model_name.value == 'gym ':
            return {"model_name":model_name,'mssg':'answer should be gym'}
        return {'model_name':model_name,'mssg':'answer should be the third one'}

