from flask import Blueprint, render_template
from main import app

views = Blueprint('views', __name__)

@app.route('/')
def home():
    return render_template('home.html')