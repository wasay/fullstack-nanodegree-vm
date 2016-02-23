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
from forms import ItemForm

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

CLIENT_ID = json.loads(
    open('instance/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

PER_PAGE = 20



@app.route('/catalog/categories/JSON')
def viewCategoriesJSON():
    try:
        categories = session.query(Categories).order_by('name')

        return jsonify(Categories=[i.serialize for i in categories])
    except:
        flash('Error')
        return redirect(url_for('showHomepage'))


@app.route('/catalog/<category_name>/items/JSON')
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


@app.route('/')
def showHomepage():
    try:
        categories = session.query(Categories).order_by('name')
        items = session.query(Items).order_by('date_created desc')
    except:
        flash('Error')
    return render_template('index.html', categories=categories, items=items)


@app.route('/catalog/<category_name>/items')
def viewCategoryItems(category_name):
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


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state, CLIENT_ID=CLIENT_ID)


@app.route('/logout')
def showLogout():
    return redirect(url_for('gdisconnect'))


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('''Current user is already
            connected.'''),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: '
    output += '150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;">'
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

    # DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():

    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'),
                                 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = login_session['access_token']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result

    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
        flash('Successfully disconnected')
    else:
        response = make_response(json.dumps('''Failed to revoke token for
            given user.''', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
        flash('Failed to revoke token for given user.')
    return redirect(url_for('showHomepage'))


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)

app.jinja_env.globals['url_for_other_page'] = url_for_other_page
