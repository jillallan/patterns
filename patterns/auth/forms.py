from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class SignUp(FlaskForm):
    """Sign up form"""

    email = StringField(
        'Email Address',
        [
            DataRequired(message='Please provide an email'),
            Email(message='Please provide a valid email address')
        ]
    )

    password = PasswordField(
        'Password',
        [
            DataRequired(message='Please provide a password'),
            Length(
                min=8, max=8,
                message='Passwords must be between 8 and 25 characters'
            )
        ]
    )

    confirm = PasswordField(
        'Confirm Password',
        [
            DataRequired(message='Please confirm your password'),
            EqualTo('password', message='Passwords must match')
        ]
    )

    submit = SubmitField('Sign Up')
