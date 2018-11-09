from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ContactForm(FlaskForm):
    names = StringField('Names of Participants', validators=[DataRequired()])
    contact_info = StringField('Phone Numbers', validators=[DataRequired()])
    submit = SubmitField('Generate Secret Santa!')
