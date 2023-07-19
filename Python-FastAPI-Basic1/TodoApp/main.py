from fastapi import FastAPI
from database import engine
from routers import auth, todos

import models

app = FastAPI() # Creates the FastAPI app, routers are used in other files to connect to this app///will always run this app to start server

models.Base.metadata.create_all(bind=engine) # Used to create local DB,,, Can only work on first run of server or if you delete the og Data Base [For Local DB only]

app.include_router(auth.router) # Adds the routers to this file [EX: auth.py]
app.include_router(todos.router) # Adds the routers to this file

