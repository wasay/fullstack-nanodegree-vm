from . import app

from flask import Flask
from flask import render_template
from flask import request, redirect, jsonify
from flask import url_for, flash

import httplib2, json, requests, random, string
import pycurl, urllib, StringIO
from array import array

from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from flask import make_response


# ######################################
# Create anti-forgery state token
# ######################################
def getReqState():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state


# ######################################
# Website Authentication
# ######################################

@app.route('/login')
def showLogin():
    getReqState()

    AMZ_CLIENT_ID = json.loads(open('instance/amz_client_secrets.json', 'r').read())[
        'web']['client_id']

    FB_APP_ID = json.loads(open('instance/fb_client_secrets.json', 'r').read())[
        'web']['app_id']

    G_CLIENT_ID = json.loads(open('instance/g_client_secrets.json', 'r').read())[
        'web']['client_id']

    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=login_session['state'], AMZ_CLIENT_ID=AMZ_CLIENT_ID, FB_APP_ID=FB_APP_ID, G_CLIENT_ID=G_CLIENT_ID)


# ######################################
# FB and Google Authentication
# ######################################
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('instance/fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('instance/fb_client_secrets.json', 'r').read())['web']['app_secret']

    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.4/me"
    # strip expire tag from access token
    token = result.split("&")[0]


    url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result

    # if error is
    # API calls from the server require an appsecret_proof argument
    # http://stackoverflow.com/questions/22359611/api-calls-from-the-server-require-an-appsecret-proof-argument

    data = json.loads(result)

    login_session['provider'] = 'facebook'

    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout, let's strip out the information before the equals sign in our token
    stored_token = token.split("=")[1]
    login_session['access_token'] = stored_token

    # Get user picture
    url = 'https://graph.facebook.com/v2.4/me/picture?%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id,access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


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
        G_CLIENT_ID = json.loads(open('instance/g_client_secrets.json', 'r').read())[
            'web']['client_id']

        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('instance/g_client_secrets.json', scope='')
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
    if result['issued_to'] != G_CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
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
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] != '200':
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# ######################################
# Amazon Connect
# ######################################
# Route with Method: POST
@app.route('/amzconnect', methods=['GET', 'POST'])
def amzconnect():
    if request.args.get('state') != login_session['state']:
        response = 'Invalid state parameter.'
        response = make_response(json.dumps(response), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    access_token = request.data

    app_id = json.loads(open('instance/amz_client_secrets.json', 'r').read())[
        'web']['app_id']
    client_id = json.loads(open('instance/amz_client_secrets.json', 'r').read())[
        'web']['client_id']
    client_secret = json.loads(
        open('instance/amz_client_secrets.json', 'r').read())['web']['client_secret']

    b = StringIO.StringIO()

    # verify that the access token belongs to us
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "https://api.amazon.com/auth/o2/tokeninfo?access_token=" + urllib.quote_plus(access_token))
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.WRITEFUNCTION, b.write)

    c.perform()
    d = json.loads(b.getvalue())

    if d['aud'] != client_id :
        # the access token does not belong to us
        raise BaseException("Invalid Token")

    stored_token = d['aud']

    # exchange the access token for user profile
    b = StringIO.StringIO()

    c = pycurl.Curl()
    c.setopt(pycurl.URL, "https://api.amazon.com/user/profile")
    c.setopt(pycurl.HTTPHEADER, ["Authorization: bearer " + access_token])
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.WRITEFUNCTION, b.write)

    c.perform()
    data = json.loads(b.getvalue())

    login_session['provider'] = 'amazon'
    login_session['username'] = data['name']
    login_session['email'] = data['email']
    login_session['amazon_id'] = data['user_id']

    login_session['access_token'] = stored_token

    login_session['picture'] = ''

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# ######################################
# Amazon Disconnect
# ######################################
# Route with Method: GET
@app.route('/amzdisconnect')
def amzdisconnect():
    amazon_id = login_session['amazon_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://api.amazon.com/auth/o2/tokeninfo?access_token=%s' % (access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]


# #########################################################################
# DISCONNECT - Revoke a current user's token and reset their login_session
# #########################################################################

# Route with Method: GET
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            # del login_session['credentials']

        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']

        if login_session['provider'] == 'amazon':
            amzdisconnect()
            del login_session['amazon_id']

        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']

        flash("You have successfully been logged out.")

    else:
        flash("You were not logged in to begin with!")

    return redirect(url_for('showHomepage'))
