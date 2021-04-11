from flask import Blueprint, render_template, redirect
from flask.helpers import flash
from flask_login import current_user, login_required
from Main import db
from Main.models import User
from Main.settings.forms import ConfigForm

settings_blueprint = Blueprint('settings',
                               __name__,
                               template_folder='templates/')


@settings_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def settings():
    """This function will save the user's settings
    """
    form = ConfigForm()
    if form.validate_on_submit():
        if form.save.data:
            username = form.username.data
            profile_color = form.profile_color.data
            user = User.query.filter_by(id=current_user.id).first()
            user.username = username
            # This will make sure the hex color is correct
            hex_color = profile_color.hex
            if len(hex_color) == 4:
                user.profile_color = '#' + \
                    ''.join([x + x for x in hex_color[1:]])
            else:
                user.profile_color = hex_color
            # This will save the changes
            db.session.add(user)
            db.session.commit()
            flash('Settings updated!')
        return redirect('/')
    return render_template('settings.html', form=form)
