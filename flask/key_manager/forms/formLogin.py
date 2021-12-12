from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    account = StringField("Conta", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    # remenberMe = BooleanField("remenberMe", false_values=None)
    send = SubmitField("Entrar")