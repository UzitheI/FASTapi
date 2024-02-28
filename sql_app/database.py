#a common way to talk to database is by using orms object relational mapping 

from typing import Union, List,Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL='sqlite:///./sql_app.db'
#this is the main link that we have to change if we want change our database, here this particular link creates a database within our ram which means that it is volatile, this can be replaced with our cloud based sql database

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False},
    echo=True
    #echo console logs the data that is being created
    #the connect args are a set of underlying mechanism that are assosciated with teh created database, it accepts a dictionary, here checksamethread when set to false makes sure that multiple people can communicate with our database
)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engine)
#sessionmaker is like a manager which makes sure that every user gets their turn with the database without having to fight for it, the autocommit=false argument here makes sure that the changes we make with data in real time are not being saved permanently, autoflush argument sets whether we are going to keep checking the database for changes, when we set it to false, we will tell the database if we are dont playing with the data

Base=declarative_base()
#blueprint for our data


