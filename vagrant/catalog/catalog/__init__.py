from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# Load the default configuration
app.config.from_object('config.default')

# Load the configuration from the instance folder
app.config.from_pyfile('config.py')


"""
    import files into the application
    catalog: class mapping to database objects
    forms: database add/update forms
    model: database model
    views: all views
    webapi: JSON Calls
"""
import catalog
import forms
import model
import views
import webapi
