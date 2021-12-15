from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class ManagerForm(FlaskForm):
    username = StringField("search-username")
    search = SubmitField("Search")