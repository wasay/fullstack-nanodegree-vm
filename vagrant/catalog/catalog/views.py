from . import app

import datetime
import random
import string
import httplib2
import json
import requests

from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
from flask import session as login_session
from flask import abort, make_response

from urlparse import urljoin

from flask.ext.sqlalchemy import Pagination

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, engine
from models import Categories, Items, User

from forms import ItemForm

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

from werkzeug.contrib.atom import AtomFeed


APPLICATION_NAME = "Catalog App"

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

PER_PAGE = 20


@app.route('/')
@app.route('/catalog/')
def showHomepage():
    try:
        categories = session.query(Categories).order_by('name')
        items = session.query(Items).order_by('date_created desc')
    except:
        flash('Error')
    return render_template('catalog.html', categories=categories, items=items)


@app.route('/catalog/<category_name>/items')
def viewCategoryItems(category_name):
    """
    viewCategoryItems: display items related to category name
    Args:
        category_name (data type: str): category name to filter items
    Returns:
        return view of items for the category
    """
    try:
        categories = session.query(Categories).order_by('name')

        category = session.query(Categories).filter_by(name=category_name).\
            one()
        items = session.query(Items).filter_by(category_id=category.id).\
            order_by('title')

    except:
        flash('Error')
    return render_template('viewcategory.html', categories=categories,
                           category=category, items=items)


@app.route('/catalog/<category_name>/<item_title>/')
def viewLatestItems(category_name, item_title):
    try:
        item = session.query(Items).filter_by(title=item_title).one()
        return render_template('viewitem.html', item=item)
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))


@app.route('/catalog/item/new', methods=['GET', 'POST'])
def newItem():
    try:
        form = ItemForm()
        form.category_id.choices = [(0, 'Select')]
        form.category_id.choices += [(category.id, category.name) for category
                                     in session.query(Categories).
                                     order_by('name')]
        print form.errors

        if form.validate_on_submit():
            title = form.title.data
            category_id = form.category_id.data

            newItem = Items(title=title, category_id=category_id)

            session.add(newItem)
            session.commit()
            flash("New Item Created")
        else:
            return render_template('newitem.html', form=form)
    except:
        flash('Error')
    return redirect(url_for('showHomepage'))


@app.route('/catalog/<category_name>/<item_title>/edit',
           methods=['GET', 'POST'])
def editItem(category_name, item_title):
    try:
        item = session.query(Items).filter_by(title=item_title).one()

        form = ItemForm(obj=item)

        categories = session.query(Categories).order_by('name')

        form.category_id.choices = [(0, 'Select')]
        form.category_id.choices += [(category.id, category.name) for
                                     category in categories]
        print form.errors

        if form.validate_on_submit():
            # form.populate_obj(post)

            title = form.title.data
            category_id = form.category_id.data

            newItem = Items(title=title, category_id=category_id)

            session.add(newItem)
            session.commit()
            flash("Item Successfully Edited")
            return redirect(url_for('showHomepage'))
        else:
            return render_template('edititem.html', form=form, item=item)
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))


@app.route('/catalog/<category_name>/<item_title>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_name, item_title):

    item = session.query(Items).filter_by(title=item_title).one()

    if item:

        if request.method == 'POST':
            session.delete(item)
            session.commit()
            flash("Item Successfully Deleted")
            return redirect(url_for('showHomepage'))
        else:
            return render_template(
                'deleteitem.html', item=item)
    else:
        flash("Unable to locate Item")
        return redirect(url_for('showHomepage'))


def make_external(url):
    return urljoin(request.url_root, url)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page
