from Main import db, login_manager
from faker import Faker
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

fake = Faker()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password_hash = db.Column(db.String(128))
    profile_color = db.Column(db.String)

    def __init__(self, email, password):
        self.email = email
        self.password_hash = generate_password_hash(password)
        # create a random config first, user can change it later
        self.username = fake.user_name()
        self.profile_color = fake.color(luminosity='dark')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "user({},{},{},{})".format(self.id, self.username, self.email, self.profile_color)


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    message = db.Column(db.String)

    def __init__(self, owner_id, post_id, message):
        self.owner_id = owner_id
        self.post_id = post_id
        self.message = message

    def __repr__(self):
        return "comment({},{},{},{})".format(self.id, self.owner_id, self.post_id, self.message)


class Like(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __init__(self, owner_id, post_id):
        self.owner_id = owner_id
        self.post_id = post_id

    def __repr__(self):
        return "like({},{},{})".format(self.id, self.owner_id, self.post_id)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    text = db.Column(db.Text)

    def __init__(self, text, owner_id):
        self.text = text
        self.owner_id = owner_id

    def __repr__(self):
        return "post({}, {}, {})".format(self.id, self.owner_id, self.text)
