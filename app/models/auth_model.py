import jwt
from datetime import datetime, timedelta
from ..database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

from .order_models import Order
from app.secrets import AUTHJWT_SECRET_KEY


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)
    email = Column(String(50), unique=True)
    password = Column(String(100))
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    description = Column(String(10), nullable=True)
    orders = relationship(Order, back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"

    def create_access_token(self):
        payload = {
            'username': self.username,
            'iat': datetime.utcnow(),  # issued at
            'exp': datetime.utcnow() + timedelta(days=1) 
        }
        access_token = jwt.encode(payload, key=AUTHJWT_SECRET_KEY)
        return access_token
