from Main.models import User
from flask import Blueprint, render_template, redirect, flash, request, url_for
from flask_login import login_user, login_required, logout_user
from Main import db
from Main.authentication.forms import LoginForm

authentication_blueprint = Blueprint('authentication',
                             __name__,
                             template_folder='templates/')


@authentication_blueprint.route('/', methods=['GET', 'POST'])
def authenticate():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        register = form.register.data
        login = form.login.data
        if login:
            user = User.query.filter_by(email=email).first()
            if user:
                # User password is already checked
                login_user(user)
                flash('Succesvol ingelogd.')
                next = request.args.get('next')
                if next == None or not next[0]=='/':
                    next = url_for('welkom')
                    return redirect(next)
            raise 'unexpected error occurred'
        if register:
            if User.query.filter_by(email=email).first():
                raise

            user = User(email, password)
            db.session.add(user)

        return redirect('/')
    return render_template('authenticate.html', form=form)
