from fastapi import FastAPI
from routers import auth, todos, admin, users, address
from starlette.staticfiles import StaticFiles

# Creates the FastAPI app, routers are used in other files to connect to this app
# Will always run this app to start server
app = FastAPI() 

# models.Base.metadata.create_all(bind=engine) # Used to create local DB
# Can only work on first run of server or if you delete the og Data Base [For Local DB only]

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(auth.router)  # Adds the routers to this file [EX: auth.py]
app.include_router(todos.router)  # Adds the routers to this file
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(address.router)
