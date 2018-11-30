from flask import Flask, render_template, flash, redirect
from simplesanta.santa_class import SantaGenerator
from simplesanta.forms import NumParticipantsForm, ContactForm
from simplesanta.message_sender import MessageSender

application = Flask(__name__)
application.config['SECRET_KEY'] = 'any secret string'

@application.route('/', methods=['get', 'post'])
@application.route('/index', methods=['get', 'post'])
def index():
    global num_ppl
    ppl_form = NumParticipantsForm()
    if ppl_form.validate_on_submit():
        flash("Generating page for {} participants".format(ppl_form.num_people.data))
        num_ppl = str(ppl_form.num_people.data)
        return redirect('/santa')
    return render_template('index.html', form=ppl_form)


@application.route('/santa', methods=['get', 'post'])
def santa():
    global names
    global contact_info
    global sg
    global num_ppl

    contact_form = ContactForm()
    for i in range(int(num_ppl)-1):
        contact_form.names.append_entry()
        contact_form.contact_info.append_entry()

    if contact_form.is_submitted():
        flash('Santa-list generated for {}, with contact {}'.format(contact_form.names.data,
                                                                    contact_form.contact_info.data))
        names = contact_form.names.data
        contact_info = contact_form.contact_info.data

        flash('Sending via text?'.format(contact_form.text.data))
        am_i_texting = contact_form.text.data

        sg = SantaGenerator(names)

        if am_i_texting:
            return redirect('/sent')
        else:
            return redirect('/assignments')

    return render_template('santa.html', form=contact_form)


@application.route('/assignments')
def assignments():
    global sg
    return render_template('choice.html', namelist=sg.get_assigned())


@application.route('/sent')
def sent():
    global sg
    global ms
    global contact_info
    ms = MessageSender(sg.get_names(), contact_info)
    return render_template('sent.html', message_sender = ms.send_texts(sg.get_assigned()))

if __name__ == "__main__":
    application.run(threaded=True)
