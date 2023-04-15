from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from flask_login import login_required, current_user

from . import db
from .models import Web3Request, Web2Response

dashboard = Blueprint("dashboard", __name__)


@dashboard.route('/save', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def add_request():
    rq = request.get_json()

    fe_index = rq["index"]
    w3r = Web3Request.query.filter_by(user_id=current_user.id, frontend_index=fe_index).first()
    existed = w3r is not None
    if not existed:
        w3r = Web3Request()
        print("here1")
    w3r.user_id = current_user.id
    w3r.api_url = rq['url']
    w3r.params = rq['jsonParameters']
    w3r.calling_contract_addr = rq['contractAddress']
    w3r.calling_contract_chain = rq['chainOption']
    w3r.encryption_key = rq['encryptionKey']
    w3r.frontend_index = fe_index
    print("here2")

    # Either update existing entry or add a new one
    if existed:
        db.session.commit()
        print("here3")
        return jsonify({"success": "Endpoint updated"}), 200
    db.session.add(w3r)
    db.session.commit()
    print("here4")
    return jsonify({"success": "Endpoint added"}), 200


@dashboard.route('/delete', methods=['POST'])
@cross_origin(supports_credentials=True)
@login_required
def delete_request():
    rq = request.get_json()
    fe_index = rq["index"]

    w3r = Web3Request.query.filter_by(user_id=current_user.id, frontend_index=fe_index).first()
    if w3r is None:
        return jsonify({"error": "No such endpoint found"}), 404

    db.session.delete(w3r)
    db.session.commit()
    return jsonify({"success": "Endpoint deleted"}), 200


@dashboard.route('/dashboard_data', methods=['GET'])
@cross_origin(supports_credentials=True)
@login_required
def dashboard_data():
    reqs = Web3Request.query.filter_by(user_id=current_user.id).all()
    name_map = dict(calling_contract_addr="contractAddress", calling_contract_chain="chainOption",
                    api_url="url", params="jsonParameters", encryption_key="encryptionKey", frontend_index="index")
    return_data = {}
    return_data["apiEndpoints"] = [{v: getattr(req, k) for k, v in name_map.items()} for req in reqs]
    # Get all web2response objects that have a request id from the reqs list
    reps = Web2Response.query.filter(Web2Response.request_id.in_([req.id for req in reqs])).all()

    name_map = dict(calling_contract_addr="contractAddress", calling_contract_chain="chainOption",
                    api_url="url", uid="uid", timestamp="timestamp")
    return_data["apiCalls"] = [{v: getattr(rep, k) for k, v in name_map.items()} for rep in reps]
    return_data["username"] = current_user.username

    return jsonify(return_data), 200


@dashboard.route('/web2response')
@cross_origin(supports_credentials=True)
def get_response():
    return "kekw"
