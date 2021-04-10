from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash
from wtforms import StringField, SubmitField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired, Email, ValidationError
from Main.models import User
import safe

def loginValidator(form, _element):
    if form.login.data:
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            raise ValidationError('This combination of email and password does not exist.')
        if not check_password_hash(user.password_hash, form.password.data):
            raise ValidationError('This combination of email and password does not exist.')


def registerValidator(form, _element):
    if form.register.data:
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            raise ValidationError('Email is already in use.')
        if not bool(safe.check(form.password.data)):
            raise ValidationError('Password is too weak.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login', validators=[loginValidator])
    register = SubmitField('Register', validators=[registerValidator])
