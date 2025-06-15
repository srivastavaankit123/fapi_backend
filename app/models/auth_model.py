from ..database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

from .order_models import Order


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
