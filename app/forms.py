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
    phone_number = PhoneNumberField()


class NameEntryForm(FlaskForm):
    name_entry = StringField()


class ContactForm(FlaskForm):
    names = FieldList(FormField(NameEntryForm), min_entries=4)
    contact_info = FieldList(FormField(PhoneEntryForm), min_entries=4)
    text = BooleanField('Send Via Text', validators=[
                        validators.AnyOf([True, False])])
    submit = SubmitField('Generate Secret Santa!')
