import os
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, BooleanField, validators
from wtforms import FieldList, FormField
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
    names = FieldList(FormField(NameEntryForm), min_entries = 1)
    contact_info = FieldList(FormField(PhoneEntryForm), min_entries = 1)
    text = BooleanField('Send Via Text', validators=[
                        validators.AnyOf([True, False])])
    submit = SubmitField('Generate Secret Santa!')
