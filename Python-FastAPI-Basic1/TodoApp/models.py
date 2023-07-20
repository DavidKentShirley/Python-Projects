from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# Database model: Used to create/define tables in the database
class Users(Base):
    __tablename__ = 'users' # Names the table in DB

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True) # unique is used to make sure there are no duplicates (cannot be two Billys for example)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    phone_number = Column(String)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=True)
    role = Column(String)

    todos = relationship("Todos", back_populates="owner")
    address = relationship("Address", back_populates="user_address")

# Database model: Used to create/define tables in the database
class Todos(Base):
    __tablename__ = 'todos' # What to name the database
    # Creating colums for the table

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="todos")

class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True, index=True)
    address1 = Column(String)
    address2 = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    zipcode = Column(String)
    
    user_address = relationship("Users", back_populates="address")

