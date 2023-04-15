from flask import Blueprint
from . import db

main = Blueprint("main", __name__)

@main.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@main.route('/profile')
def profile():
    return 'Profile'
