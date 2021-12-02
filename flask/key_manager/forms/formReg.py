from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length


class RegForm(FlaskForm):
    id = StringField("id", validators=[DataRequired(), Length(min=4, max=100)])
    user_id = StringField("user_id", validators=[DataRequired(), Length(min=4, max=25)])
    key_loan_date = StringField("key_loan_date", validators=[DataRequired(), Length(min=4, max=25)])
    key_return_date = StringField("key_return_date",  validators=[Length(min=9, max=20)])
    key_id = StringField("key_id",  validators=[Length(min=9, max=20)])
    holder_name = StringField("holder_name",  validators=[Length(min=9, max=20)])
    holder_email = EmailField("email", validators=[DataRequired(), Length(min=10, max=100)])
    send = SubmitField("Criar Registro")