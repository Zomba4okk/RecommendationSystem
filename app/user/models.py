from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.base import Base


class User(Base):
    username = Column(String(50), unique=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    ratings = relationship('Rating', back_populates='user')