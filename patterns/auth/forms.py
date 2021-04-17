from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class Test(FlaskForm):
    name = StringField(
        'Name',
    )

    submit = SubmitField('Submit')


class SignUp(FlaskForm):
    """Sign up form"""

    email = StringField(
        'Email Address',
        [
            Email(message='Please provide a valid email address'),
            DataRequired(message='Please provide an email')
        ]
    )  # Test for invalid email

    password = StringField(
        'Password',
        [
            Length(
                min=4, max=25,
                message='Password length must be between 4 and 25 characters'),
            DataRequired(message='Please provide a password')
        ]
    )  # Test for passowrd that is too long and password that is too short
    # might need to disable javascript validation

    confirm = StringField(
        'Confirm Your Password',
        [
            EqualTo('password', message='Passwords must match'),
            DataRequired(message='Please confirm your password')
        ]
    )  # Test for matching and mis-matching passwords

    submit = SubmitField('Sign Up')
