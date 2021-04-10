from flask import Blueprint,render_template,redirect,url_for
from Main import db
# from Main.models import User
from Main.settings.forms import ConfigForm

settings_blueprint = Blueprint('settings',
                             __name__,
                             template_folder='templates/')

@settings_blueprint.route('/', methods=['GET', 'POST'])
def settings():

    form = ConfigForm()
    if form.is_submitted():
        username = form.username.data
        profile_color = form.profile_color.data
        print(profile_color)
        print(username)
        # config = users.query.filter_by(id=session.id)
        # db.session.add(new_user)
        # db.session.commit()

        return redirect('/')
    return render_template('settings.html', form=form)
