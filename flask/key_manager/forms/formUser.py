from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length

class FormUser(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=4, max=100)])
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25)])
    email = EmailField("email", validators=[DataRequired(), Length(min=10, max=100)])
    phone = StringField("phone",  validators=[Length(min=9, max=20)])
    password = PasswordField("password", validators=[DataRequired(), Length(min=5, max=100)])
    send = SubmitField("Cadastrar")

class EditPassword(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=4, max=25)])
    confirm_password = PasswordField("confirm_password", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    newpassword = PasswordField("newPassword", validators=[DataRequired()])
    send = SubmitField("Confirmar")

class DelFormUser(FlaskForm):
    account = StringField("Conta", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired()])
    send = SubmitField("Confirmar")