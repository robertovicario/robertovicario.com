from flask import Blueprint, render_template

# -------------------------

index_bp = Blueprint('index', __name__)

# -------------------------

@index_bp.route('/')
def home():
    return render_template('home.html')

@index_bp.route('/about.html')
def about():
    return render_template('about.html')
