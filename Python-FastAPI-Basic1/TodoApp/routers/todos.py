from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

import models
from database import SessionLocal

from .auth import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependecy = Annotated[dict, Depends(get_current_user)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@router.get("/test")
async def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get('/', status_code=status.HTTP_200_OK)
async def read_all(user: user_dependecy, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    return db.query(models.Todos).filter(models.Todos.owner_id == user.get('id')).all()

@router.get('/{todo_id}', status_code=status.HTTP_200_OK)
async def read_todo(user: user_dependecy, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get('id')).first()
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404, detail='Todo not found')

@router.post('/', status_code= status.HTTP_201_CREATED)
async def create_todo(user: user_dependecy, db: db_dependency, todo_request: TodoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    
    todo_model = models.Todos(**todo_request.model_dump(), owner_id=user.get('id'))

    db.add(todo_model)
    db.commit()

@router.put('/{todo_id}', status_code= status.HTTP_204_NO_CONTENT)
async def update_todo(user: user_dependecy, db: db_dependency, todo_request: TodoRequest, todo_id: int = Path(gt=0)): # Anything dealing with path has to come last
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete('/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(user: user_dependecy, db: db_dependency, todo_id: int = Path(gt=0)):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get('id')).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')
    db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get('id')).delete()

    db.commit()

