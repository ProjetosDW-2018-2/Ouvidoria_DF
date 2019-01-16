from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, InputRequired
from wtforms import validators
from wtforms.fields.html5 import EmailField
from wtforms.fields.html5 import TelField


class LoginForm(FlaskForm):
    mail = EmailField('email', [validators.DataRequired(), validators.Email()])
    password = PasswordField("password", validators=[DataRequired()])
