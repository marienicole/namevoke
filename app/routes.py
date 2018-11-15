from app import app
from flask import render_template, flash, redirect
from .santa_class import SantaGenerator
from app.forms import ContactForm, NumParticipantsForm
from .message_sender import MessageSender
global names
global contact_info
global sg
global ms

@app.route('/', methods=['get', 'post'])
@app.route('/index', methods=['get', 'post'])
def index():
    global num_ppl
    ppl_form = NumParticipantsForm()
    if ppl_form.validate_on_submit():
        flash("Generating page for {} participants".format(ppl_form.num_people.data))
        num_ppl = ppl_form.num_people.data
        return redirect('/santa')
    return render_template('index.html', form=ppl_form)


@app.route('/santa', methods=['get', 'post'])
def santa():
    global names
    global contact_info
    global sg
    global num_ppl

    contact_form = ContactForm()

    if contact_form.is_submitted():
        flash('Santa-list generated for {}, with contact {}'.format(contact_form.names.data,
                                                                    contact_form.contact_info.data))
        names = contact_form.names.data
        contact_info = contact_form.contact_info.data

        print(names)
        print(contact_info)
        flash('Sending via text?'.format(contact_form.text.data))
        am_i_texting = contact_form.text.data

        sg = SantaGenerator(names)

        if am_i_texting:
            return redirect('/sent')
        else:
            return redirect('/assignments')

    return render_template('santa.html', form=contact_form)


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
