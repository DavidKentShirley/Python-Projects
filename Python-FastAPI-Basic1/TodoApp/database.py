from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # Creates local db in desired location

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) # Creates/ defines the DB engine

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
