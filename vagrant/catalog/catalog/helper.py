
# ######################################
# User Helper Functions
# ######################################

# ######################################
# Create User from login_session
# ######################################
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# ######################################
# Get User Info
# ######################################
# param (int) user_id
def getUserInfo(user_id):
    try:
        user = session.query(User).filter_by(id=user_id).one()
        return user
    except:
        return None


# ######################################
# Get User Id
# ######################################
# param (string) email
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None