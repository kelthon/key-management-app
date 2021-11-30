from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class formUser(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    username = PasswordField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    phone = PasswordField("phone", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    usertype = PasswordField("level", validators=[DataRequired()])
    send = SubmitField("Entrar")