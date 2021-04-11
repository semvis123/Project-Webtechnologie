from Main import app, db
from flask import render_template, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from Main.models import Comment, Post, User, Like
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
    posts = db.session.query(Post, User).join(User).all()
    posts_json = []

    for post in posts:
        # Get the like count
        likes = db.session.query(Like).filter(
            Like.post_id == post.Post.id).count()
        # Get the like status for the current user
        is_liked = db.session.query(Like).filter(
            Like.post_id == post.Post.id).filter(Like.owner_id == current_user.id).count() == 1
        comments_json = []

        # Get the comments
        comments = db.session.query(Comment, User).join(User).filter(
            Comment.post_id == post.Post.id).all()

        for comment in comments:
            comments_json.append({
                'owner': comment.User.username,
                'icon_color': comment.User.profile_color,
                'text': comment.Comment.message
            })

        # Add the post
        posts_json.append({
            'owner': post.User.username,
            'icon_color': post.User.profile_color,
            'text': post.Post.text,
            'likes': likes,
            'liked': is_liked,
            'comments': comments_json
        })

    return render_template('posts.html', posts=posts_json)


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
