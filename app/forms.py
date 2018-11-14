from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, validators
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    names = TextAreaField('Names of Participants', validators=[DataRequired()])
    contact_info = TextAreaField('Phone Numbers', validators=[DataRequired()])
    submit = SubmitField('Generate Secret Santa!')

class SendForm(FlaskForm):
    text = BooleanField('Send Via Text', validators=[validators.AnyOf([True, False])])
    submit = SubmitField('Send em\' out!')
