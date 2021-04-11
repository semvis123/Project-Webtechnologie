from Main import app
from flask import render_template
from flask_login import login_required
from faker import Faker
fake = Faker()


@app.route('/')
@login_required
def landing():
    return render_template('landing.html')


@app.after_request
def add_header(r):
    """ Adds headers to request """

    # No need for caching when debugging
    if app.debug:
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
