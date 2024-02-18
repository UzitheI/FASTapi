from fastapi import FastAPI
from typing import Union

app=FastAPI()

fake_items_db=[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]

@app.get('/items/')
async def read_item(skip:int =0, limit:int=10):
    return fake_items_db[skip:skip+limit]

#query are everything that comes after ? in a link 

#here there will be the ip code ie 202.23.2.122?skip=0&limit=10


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


from fastapi import FastAPI

app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item

#here unless you are trying within the doc or redoc it is absoutely necessary to proved the value of needy inside the query parameter or else we will recieve an error

fake_items_db=[{"item_name":"Foo"},{"item_name":"Bar"},{"item_name":"Baz"}]
@app.get('/users/{item_id}')
def read_item(item_id:int,q:str,ram:int,skip:int=0,limit:int=10):
    return {"item":item_id,"q":q,"ram":ram},fake_items_db[skip:skip+limit]

