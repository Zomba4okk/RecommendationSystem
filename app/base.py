from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker, scoped_session

from config.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    @classmethod
    def count(cls):
        session = Session()

        return session.query(cls).count()
