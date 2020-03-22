from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker

from config.config import SQLALCHEMY_DATABASE_URI

engine = create_engine(SQLALCHEMY_DATABASE_URI)
base = declarative_base()
Session = sessionmaker()
Session.configure(bing=engine)


@declarative_base
class Base(base):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)


class SessionContext:
    def __init__(self):
        self.session = Session()

    def __enter__(self):
        yield self.session
        self.session.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self.session.rollback()
            raise
        self.session.close()
