from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    pwd = db.Column(db.String(300), nullable=False)
    request_config = db.relationship('Web3Request', backref='users')

    def __init__(self, username, pwd):
        self.username = username
        self.pwd = generate_password_hash(pwd)

    def verify_password(self, pwd):
        return check_password_hash(self.pwd, pwd)

    def __repr__(self):
        return f"User('{self.username}')"


class Web3Request(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    responses = db.relationship('Web2Response', backref='requests')
    calling_contract_chain = db.Column(db.String(256))  # Address and chain for the contract that can call our api
    calling_contract_addr = db.Column(db.String(256))
    api_url = db.Column(db.String(300))
    params = db.Column(db.String(1024))  # JSON with all params needed for the api call
    encryption_key = db.Column(db.String(64), nullable=True)  # Key to encrypt the response with


class Web2Response(db.Model):
    __tablename__ = 'responses'
    # Some combination of things concatenated, tbd
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey('requests.id'))
    calling_contract_chain = db.Column(db.String(256))  # Address and chain for the contract that can call our api
    calling_contract_addr = db.Column(db.String(256))
    api_url = db.Column(db.String(300))
    uid = db.Column(db.String(256), nullable=False)
    response = db.Column(db.LargeBinary, nullable=False)
