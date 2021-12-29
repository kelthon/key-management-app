from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class NewsForm(FlaskForm):
    title = StringField("title", validators=[DataRequired(), Length(min=20, max=150)])
    content = TextAreaField("content", validators=[DataRequired(), Length(min=5, max=2000)])
    send = SubmitField("Confirmar")