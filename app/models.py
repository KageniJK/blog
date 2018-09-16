from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    """
    class that defines the users
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True)
    email = db.Column(db.String(255), unique=True, index=True)
    avatar = db.Column(db.String())
    bio = db.Column(db.String(255))
    password_hashed = db.Column(db.String(255))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))
    posts = db.relationship('Post', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hashed = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hashed, password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    """
    Class that defines the roles of the users
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f'User {self.name}'


class Post(db.Model):
    """
    Class that defines the actual blog posts
    """
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    post = db.Column(db.Text)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
