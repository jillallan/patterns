from flask import Blueprint, render_template
from flask_login import login_required

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
    )


@home_bp.route('/')
def hello():
    return render_template('index.html', title='home', text='Hello world')


@home_bp.route('/success')
@login_required
def success():
    return render_template('success.html')
    # ?url=[name-of-route]


@home_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
    # ?url=[name-of-route]
