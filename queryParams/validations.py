from typing import Union,List
from fastapi import FastAPI, Query
from typing_extensions import Annotated
#annotated is used to create validations or restrictions in query 

app=FastAPI()

# @app.get('/items/{item_id}')
# def read_items(item_id:int, q:Annotated[Union[str,None],Query(max_length=50)]=None):
#     results={'q':'verstappen'}

#     if q:
#         results.update({'q':q})
#     return results
#i understand it somehow





# @app.get('/items/{item_id}')
# def change(item_id:int, q:Annotated[Union[str,None], Query(max_length=50)]=None):
#     results={'q':'verstappen '}
#     if q:
#         results.update({'q':q})

#     return results    


#default value anything other than None 

# @app.get('/users/base/{item_id}')
# def read_ee(item_id:int, q:Annotated[str,Query(max_length=40,min_length=4,pattern='$homework$')]='$micah$'):
#     #if we are declaring a default value, there is no use of union
#     results={'item_id':item_id,'q':q}
#     if q:   
#         results.update({'q':q})
#     return results

#if we want the value to be required we can simply write q:str or ie 
# Annotated[str, Query=(maxlength-----)]


#if we set the default value to ..., it also becomes required the ... is called elipsis 


#we can also assign list as the type of the query 

@app.get('/items/{item_id}')
def validation(item_id:int, q:Annotated[Union:[List[str],None],Query(max_length=30)]=None):
    query={"q":q}
    return query

