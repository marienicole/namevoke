from app import app
from flask import render_template, flash, redirect
from .santa_class import SantaGenerator
from app.forms import ContactForm

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    form = ContactForm()
    global names
    global contact_info
    if form.validate_on_submit():
        flash('Santa-list generated for {}, with contact {}'.format(form.names.data, form.contact_info.data))
        names = form.names.data
        contact_info = form.contact_info.data
        return redirect('/santa')
    return render_template('index.html', form=form)

@app.route('/santa', methods=['get', 'post'])
def santa():
    return render_template('santa.html', namelist=SantaGenerator(names, contact_info).get_assigned())
