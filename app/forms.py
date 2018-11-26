import os
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, BooleanField, validators
from wtforms import FieldList
from wtforms import FormField
from wtforms_alchemy import PhoneNumberField
from wtforms.validators import DataRequired


class NumParticipantsForm(FlaskForm):
    num_people = IntegerField('Number of Participants', validators=[])
    submit = SubmitField('Input Names and Numbers')


class PhoneEntryForm(FlaskForm):
    phone_number = PhoneNumberField("Phone: ")


class NameEntryForm(FlaskForm):
    name_entry = StringField("Name: ")


class ContactForm(FlaskForm):
    print(os.environ.get("NUM_PPL"))
    names = FieldList(FormField(NameEntryForm), min_entries=3)
    contact_info = FieldList(FormField(PhoneEntryForm), min_entries=3)
    text = BooleanField('Send Via Text', validators=[
                        validators.AnyOf([True, False])])
    submit = SubmitField('Generate Secret Santa!')

class FormView(MethodView):
    def get(self):
        class DynamicForm(wtforms.Form): pass

        dform = main.models.Form.objects.get(name="name2")
        name = dform.name
        for f in dform.fields:
            print(f.label)
            setattr(DynamicForm , f.label, self.getField(f))

        d = DynamicForm() # Dont forget to instantiate your new form before rendering
        for field in d:
            print(field) # you can see html output of fields

        return render_template("santa.html", form=d)

    def getField(self, field):
        if field.fieldtype == "text":
            return TextField(field.label)
        if field.fieldtype == "password":
            return PasswordField(field.label)
        # can extend if clauses at every new fieldtype
