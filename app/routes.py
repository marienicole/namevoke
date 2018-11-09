from app import app
from flask import render_template, flash, redirect
from .santa_class import SantaGenerator
from app.forms import ContactForm

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Santa generated for {}, with contact {}'.format(
            form.names.data, form.contact_info.data))
        return redirect('/santa')
    return render_template('index.html', form=form)

@app.route('/santa', methods=['GET', 'POST'])
def santa():
    return render_template('santa.html', namelist==SantaGenerator('../../names.txt'))
