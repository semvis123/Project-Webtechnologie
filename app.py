from Main import app
from flask import render_template
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
@login_required
def posts():

    user = {
        'username': 'insecureSalt',
        'icon_color': fake.color(luminosity='dark')
    }
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
    return render_template('posts.html', user=user, posts=posts)


@app.route('/liked')
@login_required
def liked():
    user = {
        'username': 'insecureSalt',
        'icon_color': fake.color(luminosity='dark')
    }
    liked_posts = [
        {
            'owner': 'insecureSalt',
            'icon_color': fake.color(luminosity='dark'),
            'text': 'Welcome to this fantastic post',
            'likes': 5000,
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
    return render_template('posts.html', user=user, posts=liked_posts)


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
