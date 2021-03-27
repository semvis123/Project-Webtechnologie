from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('index.html')

@app.route('/liked')
def liked():
    return render_template('index.html')

@app.route('/settings')
def settings():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('index.html')

@app.after_request
def add_header(r):
    """ No need for caching when debugging """
    if app.debug:
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)