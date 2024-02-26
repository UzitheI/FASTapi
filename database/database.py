#a common way to talk to database is by using orms object relational mapping 

from typing import Union, List,Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL='sqlite:///./sql_app.db'
#this is the main link that we have to change if we want change our database

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False},
    echo=True
)
SessionLocal= sessionmaker(autocommit=False, autflush=False, bind=engine)

Base=declarative_base()


