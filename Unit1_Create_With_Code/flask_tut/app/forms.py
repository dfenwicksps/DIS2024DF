from flask_wtf import FlaskForm  # FlaskForm is a class that represents a form, and it is a subclass of Form class
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # StringField is a class that represents a text field
from wtforms.validators import DataRequired  # DataRequired is a class that represents a validator that checks if the field is empty


class LoginForm(FlaskForm):  # LoginForm is a class that represents a form
    username = StringField('Username', validators=[DataRequired()])  # username is an instance of StringField class, which represents a text field
    password = PasswordField('Password', validators=[DataRequired()])  # password is an instance of PasswordField class, which represents a password field
    remember_me = BooleanField('Remember Me')  # remember_me is an instance of BooleanField class, which represents a checkbox
    submit = SubmitField('Sign In')  # submit is an instance of SubmitField class, which represents a submit button
