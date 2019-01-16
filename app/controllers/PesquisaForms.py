from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import validators

class pesquisaForm(FlaskForm):
    buscaData = StringField("buscaData", validators=[DataRequired(), validators.length(min=4, max=4)])

