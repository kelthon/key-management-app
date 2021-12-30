from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired

class ManagerForm(FlaskForm):
    username = SelectField("user", validators=[DataRequired()])
    submit = SubmitField("Promover Usuário")