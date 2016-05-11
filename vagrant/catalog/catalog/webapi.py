from . import app

from flask import Flask
from flask import render_template
from flask import request, redirect, jsonify
from flask import url_for, flash

import httplib2, json, requests, random, string
import pycurl, urllib, StringIO
from pyatom import AtomFeed
from array import array

from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, engine

from model import Categories, Items, User

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# ######################################
# JSON APIs to view Restaurant Information
# ######################################

@app.route('/webapi')
def showWebApi():
    return render_template('webapi.html', login_session=login_session)

# ######################################
# Get Categories in JSON Format
# ######################################
@app.route('/catalog/categories/JSON/')
def viewCategoriesJSON():
    try:
        categories = session.query(Categories).order_by('name')

        return jsonify(Categories=[i.serialize for i in categories])
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))

# ######################################
# Get Categories in ATOM Format
# ######################################
@app.route('/catalog/categories/ATOM')
def viewCategoriesATOM():
    try:

        feed = AtomFeed('Categories',
                        feed_url=request.url, url=request.url_root)
        categories = session.query(Categories).order_by('name')

        for category in categories:
            feed.add(category.name, unicode(category.name),
                 content_type='html',
                 author=category.name,
                 url='',
                 updated=category.date_modified,
                 published=category.date_created)
        return feed.get_response()
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))


# ######################################
# Get Categories in XML Format
# ######################################
@app.route('/catalog/categories/XML')
def viewCategoriesXML():
    try:
        categories = session.query(Categories).order_by('name')

        response.headers["Content-Type"] = "application/xml"

        return jsonify(Categories=[i.serialize for i in categories])
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))


# ######################################
# Get Categories in RSS Format
# ######################################
@app.route('/catalog/categories/RSS')
def viewCategoriesRSS():
    try:
        categories = session.query(Categories).order_by('name')

        return rss(Categories=[i.serialize for i in categories])
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))


# ######################################
# Get Category Items in JSON Format
# ######################################
@app.route('/catalog/<category_name>/JSON')
def viewCategoryItemsJSON(category_name):
    try:
        categories = session.query(Categories).order_by('name')

        category = session.query(Categories).filter_by(name=category_name).\
            one()
        items = session.query(Items).filter_by(category_id=category.id).\
            order_by('title')

        return jsonify(Items=[i.serialize for i in items])
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))