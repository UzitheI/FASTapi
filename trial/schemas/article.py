from typing import Optional
#optional means that the value of the variable can be a None value but at the same time providing the value to the variable is mandatory
from pydantic import BaseModel

class ArticleCategoryBase(BaseModel):
    name:str
    description:str

    class Config:
        from_attributes =True

class ArticleBase(BaseModel):
    title:str
    description:str
    tags:str
    comment:str
    share:bool
    ratings:int
    
    class Config:
        from_attributes=True

class ShowArticleCategory(ArticleCategoryBase):
    id:int
    articles:list[ArticleBase]

class CreateArticle(ArticleBase):
    article_cat_id:int

class ShowArticle(ArticleBase):
    id:int
    article_cat_id:int
    article_category:Optional[ArticleCategoryBase]