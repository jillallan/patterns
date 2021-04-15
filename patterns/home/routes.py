from flask import Blueprint, render_template

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static'
    )

@home_bp.route('/')
def hello():
    return render_template('index.html', title='home', text='Hello world')