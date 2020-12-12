from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional

class SignupForm(FlaskForm):

    name = StringField(
        'Name',
        [DataRequired()]
    )

    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email address')),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6,message='Select a stronger password')
        ]
    )
    confirm = PasswordField(
        'Confirm your password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match')
        ]
    )
    submit = SubmitField('Register')

class LoginForm(FlaskForm):

    email = StringField(
        'Email',
        [
            Email(message=('Not a valid email address')),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6,message='Select a stronger password')
        ]
    )

    submit = SubmitField('Log in')