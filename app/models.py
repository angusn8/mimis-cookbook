from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from hashlib import md5

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    full_name = db.Column(db.String(150))

    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile", backref="profile_id")

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)

    bio = db.Column(db.String(255), default="")
    subscribers = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    num_reviews = db.Column(db.Integer, default=0)

class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer)
    username = db.Column(db.String(255))
    title = db.Column(db.String(255))
    time = db.Column(db.String(255))
    servings = db.Column(db.String(255))
    ingredients = db.Column(db.String(255))
    directions = db.Column(db.String(10000))
    photo_path = db.Column(db.String(255))

