from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    full_name = db.Column(db.String(150))

    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
    profile = db.relationship("Profile", backref="profile_id")

class Profile(db.Model):
    __tablename__ = 'profile'
    id = db.Column(db.Integer, primary_key=True)

    bio = db.Column(db.String(255), default="")
    subscribers = db.Column(db.Integer, default=0)
    rating = db.Column(db.Float, default=0.0)
    num_reviews = db.Column(db.Integer, default=0)

