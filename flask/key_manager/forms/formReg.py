from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length


class RegForm(FlaskForm):
    user_id = SelectField("user_id", coerce=int, validators=[DataRequired()])
    key_id = SelectField("key_id",  validators=[DataRequired()])
    holder_name = StringField("holder_name",  validators=[Length(min=9, max=100)])
    holder_email = EmailField("holder_email", validators=[DataRequired(), Length(min=10, max=100)])
    send = SubmitField("Criar Registro")