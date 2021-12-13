from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class KeyForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=4, max=100)])
    slug = StringField("slug", validators=[DataRequired(), Length(min=4, max=100)])
    key_category_id = SelectField("key_cat_id", coerce=int, validators=[DataRequired()])
    key_avaliable = SelectField("Disponibilidade", choices=[('True', 'disponível'), ('False', 'indisponível')])
    send = SubmitField("Criar")
