import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy import String, Date, Numeric, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# from . import app

Base = declarative_base()

# engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
engine = create_engine('sqlite:///itemcatalog.db')


Base.metadata.create_all(engine)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    picture = Column(String)


class Categories(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_modified = Column(DateTime, default=datetime.datetime.utcnow)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Items(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('categories.id'))
    categories = relationship(Categories)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_modified = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category_id': self.category_id,
        }


Base.metadata.create_all(engine)