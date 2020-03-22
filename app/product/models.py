from sqlalchemy import Column, Float, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.base import Base


class Product(Base):
    name = Column(String(50))
    price = Column(Float)
    param_1 = Column(Integer)
    param_2 = Column(Integer)
    param_3 = Column(Boolean)
    avg_rating = Column(Float)
    ratings = relationship('Rating', back_populates='product')


class Rating(Base):
    rate = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='ratings')
    product_id = Column(Integer, ForeignKey('product.id'))
    product = relationship('Product', back_populates='ratings')