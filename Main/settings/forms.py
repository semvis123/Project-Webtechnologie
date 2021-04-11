from Main.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms_components import ColorField
from wtforms.validators import DataRequired, ValidationError
from flask_login import current_user


def usernameValidator(form, _element):
    """This function will check if the email, username and password are valid

    Args:
        form: The data from the form
    """
    username = User.query.filter_by(username=form.username.data).first()
    if current_user.username != form.username.data and username:
        raise ValidationError('Username is already in use.')


class ConfigForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), usernameValidator])
    profile_color = ColorField('Profile color')
    save = SubmitField('Save')
    cancel = SubmitField('Cancel', render_kw={'formnovalidate': True})
