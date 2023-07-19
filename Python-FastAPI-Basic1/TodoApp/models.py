from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
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
    role = Column(String)

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




