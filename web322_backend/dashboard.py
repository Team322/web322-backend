from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

from .models import Web3Request, Web2Response
from . import db

dashboard = Blueprint("dashboard", __name__)


@dashboard.route('/web3request', methods=['POST'])
@login_required
def add_request():
    rq = request.get_json()

    w3r = Web3Request()
    w3r.id = rq['id']
    w3r.user = current_user.id
    w3r.api_url = rq['api_url']
    w3r.params = rq['params']

    db.session.add(w3r)
    db.session.commit()


@dashboard.route('/dashboard_data', methods=['GET'])
@login_required
def dashboard_data():
    reqs = Web3Request.query.filter_by(user_id=current_user.id).all()
    name_map = dict(calling_contract_addr="contract_address", calling_contract_chain="contract_chain",
                    api_url="api_url", params="params", encryption_key="encryption_key")
    return_data = {}
    return_data["apiEndpoints"] = [{v: getattr(req, k) for k, v in name_map.items()} for req in reqs]
    reps = Web2Response.query.filter_by(user_id=current_user.id).all()

    name_map = dict(calling_contract_addr="contract_address", calling_contract_chain="contract_chain",
                    api_url="api_url", uid="uid")
    return_data["apiCalls"] = [{v: getattr(rep, k) for k, v in name_map.items()} for rep in reps]
    return_data["username"] = current_user.username

    return jsonify(return_data), 200


@dashboard.route('/web2response')
def get_response():
    return "kekw"
