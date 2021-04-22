from flask import Blueprint, redirect, render_template
from flask.helpers import flash, url_for
from .forms import Login, SignUp
from patterns import db
from patterns.models import User


auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    """Handles sign up for new users"""
    form = SignUp()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user = User(
                email=form.email.data,
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('home_bp.success'))
        flash('Username taken')

    return render_template('sign-up.html', title='Sign Up', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in"""
    form = Login()
    if form.validate_on_submit():
        return redirect(url_for('home_bp.success'))

    return render_template('login.html', title='Login', form=form)
