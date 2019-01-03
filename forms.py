from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class Form_add_players(FlaskForm):
    name = StringField('Nom', validators=[DataRequired()])
    last_name = StringField('Prénom', validators=[DataRequired()])
