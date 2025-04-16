from flask import Blueprint, render_template, redirect

# -------------------------

index_bp = Blueprint('index', __name__)

# -------------------------

@index_bp.route('/')
def home():
    return render_template('pages/home.html')

@index_bp.route('/about.html')
def about():
    return render_template('about.html')

@index_bp.route('/projects.html')
def projects():
    return render_template('about.html')

@index_bp.route('/contact.html')
def contact():
    return render_template('contact.html')

@index_bp.route('/instagram')
def instagram():
    return redirect('https://www.instagram.com/robertovicario__')
