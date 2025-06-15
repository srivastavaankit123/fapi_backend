from typing import Annotated
from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from bcrypt import hashpw, gensalt
from sqlalchemy.orm import Session

from ..schmas import UserSignupModel, BaseUserModel
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