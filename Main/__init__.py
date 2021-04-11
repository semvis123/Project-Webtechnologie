import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = '\x8e\x82\x99o^\xfd\xf8s\xd7\xf76\xab'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = "authentication.authenticate"


from Main.settings.views import settings_blueprint
from Main.authentication.views import authentication_blueprint
from Main.posts.views import posts_blueprint

app.register_blueprint(settings_blueprint, url_prefix="/settings")
app.register_blueprint(authentication_blueprint, url_prefix="/authenticate")
app.register_blueprint(posts_blueprint)
