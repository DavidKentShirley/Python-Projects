from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # Creates local db in desired location
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234!@localhost/TodoApplicationDatabase' # Connect to external db

# Creates/ defines the DB engine ,, connect_args={'check_same_thread': False} -- SLQlite only
engine = create_engine(SQLALCHEMY_DATABASE_URL) 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
