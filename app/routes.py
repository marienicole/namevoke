from app import app
from flask import render_template
from .santa_class import SantaGenerator
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', namelist=SantaGenerator('names.txt').assignments)
