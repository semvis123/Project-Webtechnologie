from flask import Blueprint,render_template,redirect,url_for
from Main import db
# from Main.models import User
from Main.authentication.forms import LoginForm

authentication_blueprint = Blueprint('authentication',
                             __name__,
                             template_folder='templates/')

@authentication_blueprint.route('/', methods=['GET', 'POST'])
def authenticate():

    form = LoginForm()
    if form.is_submitted():
        print('hmmm')
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(password)
        print(email)

        return redirect('/')
    return render_template('authenticate.html', form=form)
