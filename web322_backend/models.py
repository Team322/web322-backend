from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"