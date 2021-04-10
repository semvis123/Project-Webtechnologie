from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from Main.models import User


def loginValidator(form, _element):
    user = User.query.filter_by(email=form.email.data).first()
    if not user:
        raise ValidationError('De combinatie van het email en wachtwoord is niet gevonden.')
    if check_password_hash(user.password_hash, form.password.data):
        raise ValidationError('De combinatie van het email en wachtwoord is niet gevonden.')

def registerValidator(form, _element):
    


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    login = SubmitField('Login', validators=[loginValidator])
    register = SubmitField('Register')
