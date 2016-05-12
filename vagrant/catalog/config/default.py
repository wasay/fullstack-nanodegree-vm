# #############################################
# values are overwritten in instance\config.py
# #############################################

DEBUG = False
SQLALCHEMY_ECHO = False

"""
Initialize keys with values
Overwrite these values in excluded instance folder config.py
"""
SECRET_KEY = 'some_seckret_key'
STRIPE_API_KEY = 'some_api_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///itemcatalog.db'

# BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension
# MAIL_FROM_EMAIL = "catalog@example.com" # For use in application emails
