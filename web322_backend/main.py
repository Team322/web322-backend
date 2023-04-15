import os
from flask import Blueprint, request
from . import db
from web322_backend.models import Web3Request
from flask import send_from_directory

main = Blueprint("main", __name__)


@main.route('/profile')
def profile():
    return 'Profile'

@main.route('/')
def index():
    return send_from_directory(os.environ.get("FLASK_STATIC_PATH", "/volume/"), 'index.html')

# @main.route('/<path:path>')
# def send_report(path):
#     return send_from_directory('/volume/', path)