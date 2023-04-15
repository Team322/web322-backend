from flask import Blueprint, request
from . import db
from web322_backend.models import Web3Request

main = Blueprint("main", __name__)

@main.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@main.route('/profile')
def profile():
    return 'Profile'


@main.route('/web3request', methods=['POST'])
def add_request():
    rq = request.get_json()

    w3r = Web3Request()
    w3r.id = rq['id']
    w3r.user = rq['user']
    w3r.api_url = rq['api_url']
    w3r.params = rq['params']

    db.session.add(w3r)
    db.session.commit()


@main.route('/web2response')
def get_response():
    return "kekw"