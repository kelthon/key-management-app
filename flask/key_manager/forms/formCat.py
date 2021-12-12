from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class CatForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(), Length(min=4, max=100)])
    slug = StringField("slug", validators=[DataRequired(), Length(min=4, max=100)])
    submit = SubmitField("Criar")