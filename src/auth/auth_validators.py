from flask_inputs import Inputs
from wtforms.validators import DataRequired, Email, Length
from wtforms.fields import StringField, PasswordField


class LoginValidator(Inputs):
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])


class RegisterValidator(Inputs):
    username = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    password = PasswordField(validators=[DataRequired(), Length(min=6)])
