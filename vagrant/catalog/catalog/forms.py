from . import app

#from wtforms_alchemy import ModelForm

from flask.ext.wtf import Form

from wtforms import BooleanField, StringField, validators
from wtforms import DateField, DateTimeField, TextAreaField
from wtforms import HiddenField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError

from model import Base, engine, Categories, Items, User

# app.config.from_object(__name__)

class CategoryForm(Form):
    name = StringField('Name', [validators.Length(min=2, max=250)])

#class ItemForm(ModelForm):
#    class Meta:
#        model = Items


class ItemForm(Form):
    title = StringField('Title', [validators.Length(min=2, max=250)])
    description = TextAreaField('Description')
    category_id = SelectField('Category', coerce=int)
    user_id = HiddenField('User Id')
