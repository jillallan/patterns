from flask.helpers import url_for
from patterns.auth.forms import SignUp
from flask import Blueprint, redirect, render_template

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
        return redirect(url_for('home_bp.success'))

    return render_template('sign-up.html', form=form)
