import sys
sys.path.append("..")

from typing import Optional
from fastapi import Depends, APIRouter, HTTPException
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user
from starlette import status

router = APIRouter(
    prefix='/address', # all endpoints will start with /auth
    tags=['address'] # Helps seperate docs in swagger all auth endpoints will be seperate from other endpoints
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Address(BaseModel):
    address1: str
    address2: Optional[str]
    city: str
    state: str
    country: str
    zipcode: str


@router.post("/")
async def create_address(address: Address, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    address_model = models.Address()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.zipcode = address.zipcode

    db.add(address_model)
    db.flush()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()

    user_model.address_id = address_model.id
    db.add(user_model)
    db.commit()