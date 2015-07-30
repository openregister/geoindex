from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class PostcodeForm(Form):
    postcode = StringField('Postcode', validators=[DataRequired()])
