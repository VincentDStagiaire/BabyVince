from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, IntegerField, validators
from wtforms.validators import DataRequired


class Form_add_players(FlaskForm):
    name_player = StringField('Nom', validators=[DataRequired()]  )
    last_name_player = StringField('Prénom', validators=[DataRequired()])
    csrf = True
    csrf_secret = "coucou"


class Form_add_match(FlaskForm):
    team1_select = SelectMultipleField("Équipe 1")
    team2_select = SelectMultipleField("Équipe 2")
    result1 = IntegerField(" - ", [validators.required(), validators.length(max=10)])
    result2 = IntegerField([validators.required(), validators.length(max=10)])
    csrf = True
    csrf_secret = "coucou"
