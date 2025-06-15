from sqlalchemy import Column, Integer, Boolean, String, Text, ForeignKey
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship

from ..database import Base


class Order(Base):
    ORDER_STATUSES = (
        ('Pending', 'pending'),
        ('In-Transit', 'in-transit'),
        ('Delivered', 'delivered')
    )

    PIZZA_SIZES = (
			('Small', 'small'),
			('Medium', 'medium'),
			('Large', 'large'),
			('Extra-Large', 'extra-large')
	)

    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    order_status = Column(ChoiceType(choices=ORDER_STATUSES), default="Pending")
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZES), default="Small")
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')

    def __repr__(self):
        return f"<Order {self.id}>"
