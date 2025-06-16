from typing import Annotated
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
# from fastapi_jwt_auth import AuthJWT

from ..schmas import UserSignupModel, BaseUserModel, LoginModel
from ..database import SessionLocal, engine, get_db
from ..models import User


auth_router = APIRouter(
    prefix='/user'
)


@auth_router.post('/', response_model=BaseUserModel, status_code=status.HTTP_201_CREATED)
async def create_user(user:UserSignupModel, db: Annotated[Session, Depends(get_db)]):
    db_user = db.query(User).filter(User.email == user.email).first()

    if db_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='User with this email or username already exists.')

    user_data = user.model_dump()
    print('user data::', type(user_data))
    user_data['password'] = hashpw(user_data['password'].encode('utf-8'), salt=gensalt()).decode('utf-8')

    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@auth_router.post('/login', status_code=200)
async def login(user: LoginModel, db: Annotated[Session, Depends(get_db)]):
    db_user = db.query(User).filter(User.username == user.username).first()

    if db_user is None:
        raise HTTPException(status_code=400, detail='No user found with given username.')
    if not checkpw(user.password.encode('utf-8'), db_user.password.encode('utf-8')):
        raise HTTPException(status_code=400, detail='Incorrect password.')

    access_token = db_user.create_access_token()

    return JSONResponse(content={
        'access_token': access_token.decode('utf-8')
    }, status_code=200)