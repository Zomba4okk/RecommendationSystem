from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.base import Base, SessionContext
from app.product.models import Product, Rating


class User(Base):
    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    ratings = relationship('Rating', back_populates='user')

    def get_ratings(self):
        with SessionContext() as session:
            ratings = session.query(Product). \
                join(Rating, Product.id == Rating.product_id). \
                join(User, self.id == Rating.user_id). \
                all()

        return ratings
