from flask import Blueprint, render_template, redirect, url_for
from flask.helpers import flash
from flask_login import current_user, login_required
from Main import db
from Main.models import User, Post, Like, Comment
from Main.settings.forms import ConfigForm

posts_blueprint = Blueprint('posts',
                             __name__,
                             template_folder='templates/')

@posts_blueprint.route('/me')
@posts_blueprint.route('/posts')
@posts_blueprint.route('/liked')
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
            comments_json.insert(0, {
                'owner': comment.User.username,
                'icon_color': comment.User.profile_color,
                'text': comment.Comment.message
            })

        # Add the post
        posts_json.insert(0, {
            'owner': post.User.username,
            'icon_color': post.User.profile_color,
            'text': post.Post.text,
            'likes': likes,
            'liked': is_liked,
            'comments': comments_json
        })

    return render_template('posts.html', posts=posts_json)
