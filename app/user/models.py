from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.base import Base, Session
from app.product.models import Product, Rating


class User(Base):
    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    ratings = relationship('Rating', back_populates='user')

    @classmethod
    def get_ratings(cls, id=None):
        session = Session()

        query = session.query(cls) \
            .join(Rating, cls.id == Rating.user_id) \
            .join(Product, Product.id == Rating.product_id)
        if id is not None:
            query = query.filter(cls.id == id)

        ratings = query \
            .with_entities(
                cls.id.label('user_id'),
                Product.id.label('product_id'),
                Rating.rate.label('rate')) \
            .all()

        return ratings
