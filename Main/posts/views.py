from flask import Blueprint, render_template, request, Response
from flask.helpers import flash
from flask_login import current_user, login_required
from Main import db
from Main.models import User, Post, Like, Comment

posts_blueprint = Blueprint('posts',
                            __name__,
                            template_folder='templates/')


def process_posts(posts):
    """This function will make the posts into a usable format for the html template

    example usage:

    posts = db.session.query(Post, User).join(User).all()
    return render_template('posts.html', posts=process_posts(posts))

    Args:
        posts: The data from the database

    Returns:
        Any: The data for the template
    """
    posts_json = []

    for post in posts:
        # Get the like count
        likes = db.session.query(Like).filter(
            Like.post_id == post.Post.id).count()

        # Get the like status for the current user
        is_liked = db.session.query(Like).filter(Like.post_id == post.Post.id).filter(
            Like.owner_id == current_user.id).count() == 1

        # Get the comments
        comments_json = []
        comments = db.session.query(Comment, User).join(
            User).filter(Comment.post_id == post.Post.id).all()
        for comment in comments:
            comments_json.append({
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
            'comments': comments_json,
            'id': post.Post.id
        })

    return posts_json


@posts_blueprint.route('/posts', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'GET':
        # Get all the posts
        posts = db.session.query(Post, User).join(User).all()

        return render_template('posts.html', posts=process_posts(posts))
    if request.method == 'POST':
        # Create a new posts
        try:
            post = Post(str(request.form['text']), current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Created post successfully!')
            return 'Saved your post'
        except:
            Response(status=500)
            return 'Couldn\'t save your post'


@posts_blueprint.route('/posts/<post_id>/comment', methods=['POST'])
@login_required
def commment(post_id):
    try:
        commment = Comment(current_user.id, post_id, str(request.form['text']))
        db.session.add(commment)
        db.session.commit()
        flash('Saved your comment')
        return 'Saved your comment'
    except:
        Response(status=500)
        return 'Couldn\'t save your comment'


@posts_blueprint.route('/posts/<post_id>/like', methods=['POST', 'DELETE'])
@login_required
def like(post_id):
    if request.method == 'POST':
        try:
            like = Like(current_user.id, post_id)
            db.session.add(like)
            db.session.commit()
            return 'Saved your like'
        except:
            Response(status=500)
            return 'Couldn\'t save your like'
    if request.method == 'DELETE':
        try:
            like = db.session.query(Like).filter(
                Like.owner_id == current_user.id).filter(Like.post_id == post_id).first()
            db.session.delete(like)
            db.session.commit()
            return 'Removed your like'
        except:
            Response(status=500)
            return 'Couldn\'t remove your like'


@ posts_blueprint.route('/me')
@ login_required
def me():
    # Get all post created by the current user
    posts = db.session.query(Post, User).join(User).filter(
        Post.owner_id == current_user.id).all()

    return render_template('posts.html', posts=process_posts(posts))


@posts_blueprint.route('/liked')
@ login_required
def liked():
    # Get all post liked by the current user
    posts = db.session.query(Like, Post, User).join(Post, Like.post_id == Post.id).join(User, Post.owner_id == User.id).filter(
        Like.owner_id == current_user.id).all()

    return render_template('posts.html', posts=process_posts(posts))
