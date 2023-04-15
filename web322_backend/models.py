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


class Web3Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))  # Place on the blockchain
    api_url = db.Column(db.String(300))
    params = db.Column(db.String(500))  # JSON with all params needed for the api call


class Web2Response(db.Model):
    __tablename__ = 'responses'
    # Some combination of things concatenated, tbd
    uid = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    response = db.Column(db.String(500))
    is_encrypted = db.Column(db.Boolean)
    encryption_key = db.Column(db.String(50))
