from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms_components import ColorField
from wtforms.validators import DataRequired


class ConfigForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    profile_color = ColorField('Profile color')
    save = SubmitField('Save')
    cancel = SubmitField('Cancel', render_kw={'formnovalidate': True})
