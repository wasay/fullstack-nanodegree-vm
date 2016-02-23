from . import app

from flask.ext.wtf import Form

from wtforms import BooleanField, StringField, validators
from wtforms import DateField, DateTimeField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError

class CategoryForm(Form):
    name = StringField('Name', [validators.Length(min=2, max=250)])

class ItemForm(Form):
    title = StringField('Title', [validators.Length(min=2, max=250)])
    description = TextAreaField('Description')
    category_id = SelectField('Category', coerce=int)