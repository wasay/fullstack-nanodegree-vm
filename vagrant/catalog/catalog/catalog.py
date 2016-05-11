from sqlalchemy import *
from . import app

meta = MetaData()

user = Table('user', meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=250), nullable=False),
    Column('email', VARCHAR(length=250), nullable=False),
    Column('picture', VARCHAR(length=250), nullable=True),
)

categories = Table('categories', meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=80), nullable=False),
    Column('date_created', DateTime, nullable=True),
    Column('date_modified', DateTime, nullable=True),
)

items = Table('items', meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=255), nullable=False),
    Column('description', VARCHAR(255), nullable=True),
    Column('date_created', DateTime, nullable=True),
    Column('date_modified', DateTime, nullable=True),
    Column('category_id', Integer, nullable=False),
    Column('user_id', Integer, nullable=False),
)
