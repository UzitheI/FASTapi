from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
#api router is for routering, httpexcetion is to create exception or show error in your code to the user, status, to set status code and depends is used for security(authentication and authorization)

from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session

from schemas.article import ShowArticle, CreateArticle

from models.article import Article

