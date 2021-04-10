from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms_components import ColorField

class ConfigForm(FlaskForm):
    username = StringField('Username')
    profile_color = ColorField('Profile color')
    save = SubmitField('Save')
    cancel = SubmitField('Cancel', render_kw={'formnovalidate': True})
