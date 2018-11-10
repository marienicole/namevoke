from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    names = TextAreaField('Names of Participants', validators=[DataRequired()])
    contact_info = TextAreaField('Phone Numbers', validators=[DataRequired()])
    submit = SubmitField('Generate Secret Santa!')

class SendForm(FlaskForm):
    text = BooleanField('Send Via Text')
    email = BooleanField('Send Via Email')
    submit = SubmitField('Send em\' out!')
