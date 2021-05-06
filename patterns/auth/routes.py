from flask import Blueprint, redirect, render_template, request, flash, url_for
from flask_login import login_user, logout_user, current_user
from werkzeug.urls import url_parse
from .forms import Login, SignUp
from patterns import db, login_manager
from patterns.models import User


auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorised():
    """Redirect unauthorised users to login page"""
    return redirect(url_for('auth_bp.login', next=request.endpoint))


@auth_bp.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    """Handles sign up for new users

    GET requests serve sign-up page
    POST requests validate form & user creation,
    and redirect to success
    """
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
            login_user(user)  # check user is logged in
            return redirect(url_for('home_bp.success'))
        flash('Username taken')

    return render_template('sign-up.html', title='Sign Up', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Handles logging in

    GET requests serve login page
    POST requests validate and redirect user to success
    """

    if current_user.is_authenticated:
        return redirect(url_for('home_bp.success'))

    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(password=form.password.data):
            login_user(user)

            next_page = request.args.get('next')  # check redirected
            if not next_page or url_parse(next_page).netloc != '':
                # next_page = url_for('home_bp.success')
                next_page = 'home_bp.success'
            # return redirect(next_page)

            # next_page = request.args.get('next')  # check redirected
            print(next_page)
            print(url_for(next_page))
            return redirect(url_for(next_page) or url_for('home_bp.success'))
        flash('Invalid username or password')
        # return redirect(url_for('auth_bp.login'))

    return render_template('login.html', title='Login', form=form)


@auth_bp.route('/logout')
def logout():
    """User log out logic"""
    logout_user()
    return redirect(url_for('auth_bp.login'))
    # TODO logout when browser is closed
