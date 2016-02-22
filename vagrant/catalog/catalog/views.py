from . import app

import datetime
from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import request
from flask.ext.sqlalchemy import Pagination

from models import Base, engine
from models import Categories, Items
#from forms import PuppyForm

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

PER_PAGE = 20

@app.route('/')
def showHomepage():
    categories = session.query(Categories).order_by('name')
    items = session.query(Items).order_by('date_created desc')
    return render_template('index.html', categories=categories, items=items)

@app.route('/categories')
def showCategories():
    return render_template('index.html')

@app.route('/latest-items')
def showLatestItems():
    return render_template('index.html')

@app.route('/login')
def showLogin():
    return render_template('index.html')

@app.route('/logout')
def userLogout():
    return render_template('index.html')




def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page