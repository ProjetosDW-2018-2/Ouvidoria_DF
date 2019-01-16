from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms import validators, TextAreaField
from wtforms.fields.html5 import EmailField

class ContatoForm(FlaskForm):
    nome = StringField("Nome: *", validators=[DataRequired(), validators.length(min=3, max=35)])
    email = EmailField('email', [validators.DataRequired(), validators.Email(), validators.length(min=10, max=40)])
    entidade = StringField("Tipo de Entidade", validators=[DataRequired(), validators.InputRequired(), validators.length(min=0, max=1)])
    mensagem = TextAreaField("Mensagem",  validators=[DataRequired(), validators.length(min=0, max=250),
                                                           validators.input_required()])
