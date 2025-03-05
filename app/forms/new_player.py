from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddNewPlayerForm(FlaskForm):
    strategy = StringField('Strategy', validators=[DataRequired()])
