from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db:Session,user_id:int):
    return db.query(models.User).filter(models.User.id == user_id).first()
#session creates an instance with the database, here we are retrieving information on the basis of the id of the user, so we query the database particularly the users table and see if the id that we sent as the function parameter matches with any id that is present in the users table, once the match is found, it returns the first address that is being sent

def get_user_by_email(db:Session,email:str):
    return db.query(models.User).filter(models.User.email==email).first()

def get_users(db:Session,skip:int=0,limit:int=100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db:Session,user:schemas.UserCreate):
    fake_hashed_password= user.password+ 'notreallyhashed'
    db_user = models.User(email=user.email,hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(db:Session,skip:int=0,limit:int=100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(db:Session,item:schemas.ItemCreate,user_id:int):
    db_item=models.Item(**item.dict(),owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

