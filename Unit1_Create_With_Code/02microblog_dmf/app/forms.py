from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])  # StringField is a class that represents a text field
    password = PasswordField('Password', validators=[DataRequired()])  # PasswordField is a class that represents a password field
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')