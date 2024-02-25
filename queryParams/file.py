from fastapi import FastAPI, File,UploadFile
from fastapi import HTTPException,status
from pydantic import BaseModel
from typing import Annotated

app=FastAPI()

@app.get('/model')
async def create_file(file:Annotated[bytes,File()]):
    return {"file_size":len(file)}

@app.post('/uploadfile')
async def create_upload_file(file:UploadFile,filelist:list):
    if file not in filelist:
        raise HTTPException(status_code=404)
    return {"filename":file.filename}