from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/me')
@app.route('/posts')
def posts():
    def random_iconcolor(): return "#%06x" % random.randint(0, 0xFFFFFF)
    posts = [
        {
            'owner': 'insecureSalt',
            'icon_color': random_iconcolor(),
            'text': 'Welcome to this fantastic post',
            'likes': 122,
            'comments': [
                {
                    'owner': 'shyTomatoe',
                    'icon_color': random_iconcolor(),
                    'text': 'Good post'
                },
                {
                    'owner': 'debonairDinosaur',
                    'icon_color': random_iconcolor(),
                    'text': 'Good post'
                }
            ]
        } for i in range(10)
    ]
    return render_template('posts.html', posts=posts)


@app.route('/liked')
def liked():
    def random_iconcolor(): return "#%06x" % random.randint(0, 0xFFFFFF)
    liked_posts = [
        {
            'owner': 'insecureSalt',
            'icon_color': random_iconcolor(),
            'text': 'Welcome to this fantastic post',
            'likes': 122,
            'comments': [
                {
                    'owner': 'shyTomatoe',
                    'icon_color': random_iconcolor(),
                    'text': 'Good post'
                },
                {
                    'owner': 'debonairDinosaur',
                    'icon_color': random_iconcolor(),
                    'text': 'Good post'
                }
            ]
        } for i in range(10)
    ]
    return render_template('posts.html', posts=liked_posts)


@app.route('/settings')
def settings():
    return render_template('landing.html')


@app.route('/profile')
def profile():
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
    app.run(debug=True)
