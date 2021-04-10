from Main import app
from flask import render_template, redirect, flash
from flask_login import login_user, login_required, logout_user
from Main.models import User
from faker import Faker
fake = Faker()


@app.route('/')
@login_required
def landing():
    return render_template('landing.html')


@app.route('/me')
@app.route('/posts')
@app.route('/liked')
@login_required
def posts():
    posts = [
        {
            'owner': 'insecureSalt',
            'icon_color': fake.color(luminosity='dark'),
            'text': 'Welcome to this fantastic post',
            'likes': 122,
            'liked': True,
            'comments': [
                {
                    'owner': 'shyTomatoe',
                    'icon_color': fake.color(luminosity='dark'),
                    'text': 'Good post'
                },
                {
                    'owner': 'debonairDinosaur',
                    'icon_color': fake.color(luminosity='dark'),
                    'text': 'Good post'
                }
            ]
        } for i in range(10)
    ]
    return render_template('posts.html', posts=posts)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Log out successful!')
    return redirect('/authenticate')


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
    app.run(debug=True)
