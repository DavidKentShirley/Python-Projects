from datetime import datetime, timedelta
from typing import Annotated, Optional
from starlette import status
from starlette.responses import RedirectResponse
from fastapi import Depends, HTTPException, status, APIRouter, Request, Response, Form
from passlib.context import CryptContext  # pip install "passlib[bcrypt]"
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer # pip install python-multipart
from database import SessionLocal
from models import Users
from jose import jwt, JWTError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Router to main.py where the FastAPI app is located
router = APIRouter(
    prefix='/auth', # all endpoints will start with /auth
    tags=['auth'] # Helps seperate docs in swagger all auth endpoints will be seperate from other endpoints
)

SECRET_KEY = 'd6e507c066facf4dac06489fa3fc5964' #Random hex 32, used for JWT
ALGORITHM = 'HS256' # The JWT algo used to encode the user_information

templates = Jinja2Templates(directory="templates")
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto') # Used for password encryption
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token') # used to check the JWT 

class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def create_oauth_form(self):
        form = await self.request.form()
        self.username = form.get("email")
        self.password = form.get("password")

# Basic information to connect to the DataBase
class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    phone_number: Optional[str]
    role: str

# Used to create JWT
class Token(BaseModel):
    access_token: str
    token_type: str

# Used to connect to the DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Used as variable for DB connections in endpoints
db_dependency = Annotated[Session, Depends(get_db)]

# Function to help determin if the username and password entered are correct and in the Database
def authenticate_user(username: str, password:str, db):
    user = db.query(Users).filter(Users.username == username).first() # Looks for username in DB/Will always return first result
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(username: str, user_id:int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        user_role: str = payload.get('role')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
        return {'username': username, 'id': user_id, 'user_role': user_role}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')

@router.get("/", response_class=HTMLResponse)
async def authentication_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/", response_class=HTMLResponse)
async def login(request: Request, db: Session = Depends(get_db)):
    try:
        form = LoginForm(request)
        await form.create_oauth_form()
        response = RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)

        validate_user_cookie = await login_for_access_token(response=response, form_data=form, db=db)

        if not validate_user_cookie:
            msg = "Incorrect Username or Password"
            return templates.TemplateResponse("login.html", {"request": request, "msg": msg})
        return response
    except HTTPException:
        msg = "Unknown Error"
        return templates.TemplateResponse("login.html", {"request": request, "msg": msg})


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        username = create_user_request.username,
        email = create_user_request.email,
        first_name = create_user_request.first_name,
        last_name = create_user_request.last_name,
        phone_number = create_user_request.phone_number,
        role = create_user_request.role,
        hashed_password = bcrypt_context.hash(create_user_request.password),
        is_active = True
    )


    db.add(create_user_model) # Adds information entered to DB
    db.commit() # Commits to the information to permently store entered information to DB


@router.post('/token', response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.')
    
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))
    return {'access_token': token, 'token_type': 'bearer'}