from flask import Blueprint, request
from . import db
from web322_backend.models import Web3Request

main = Blueprint("main", __name__)


@main.route('/profile')
def profile():
    return 'Profile'
