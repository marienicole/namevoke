from app import app
from flask import render_template, flash, redirect
from .santa_class import SantaGenerator
from app.forms import ContactForm, SendForm
from .message_sender import MessageSender
global names
global contact_info
global sg
global ms

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    global names
    global contact_info

    contact_form = ContactForm()
    if contact_form.validate_on_submit():
        flash('Santa-list generated for {}, with contact {}'.format(contact_form.names.data,
                                                                    contact_form.contact_info.data))
        names = contact_form.names.data
        contact_info = contact_form.contact_info.data
        return redirect('/santa')
    return render_template('index.html', form=contact_form)


@app.route('/santa', methods=['get', 'post'])
def santa():
    global names
    global contact_info
    global sg
    send_form = SendForm()
    if send_form.is_submitted():
        flash('Sending via text?'.format(send_form.text.data))
        am_i_texting = send_form.text.data

        sg = SantaGenerator(names)

        if am_i_texting:
            return redirect('/sent')
        else:
            return redirect('/assignments')
            
    return render_template('santa.html', form=send_form)


@app.route('/assignments')
def assignments():
    global sg
    return render_template('choice.html', namelist=sg.get_assigned())


@app.route('/sent')
def sent():
    global sg
    global ms
    global contact_info
    ms = MessageSender(sg.get_names(), contact_info)
    return render_template('sent.html', message_sender = ms.send_texts())
