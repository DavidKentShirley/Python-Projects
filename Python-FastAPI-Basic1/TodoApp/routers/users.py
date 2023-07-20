from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from database import SessionLocal
from sqlalchemy.orm import Session
from starlette import status
from .auth import get_current_user
from passlib.context import CryptContext
from models import Users

import models

router = APIRouter(
    prefix='/user', # all endpoints will start with /auth
    tags=['user'] # Helps seperate docs in swagger all auth endpoints will be seperate from other endpoints
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependecy = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto') # Used for password encryption

@router.get('/', status_code=status.HTTP_200_OK)
async def get_user(user: user_dependecy, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authenication Failed')
    return db.query(Users).filter(Users.get('id')).first()



@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(user: user_dependecy, db: db_dependency, user_verification: UserVerification):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Failed")
    user_model = db.query(Users).filter(Users.id == user.get('id')).first()
    if not bcrypt_context.verify(user_verification.password, user_model.hashed_password):
        raise HTTPException(status_code=401, detail="Password incorect")
    
    user_model.hashed_password = bcrypt_context.hash(user_verification.new_password)
    db.add(user_model)
    db.commit()