from flask import Blueprint, jsonify, request
from wtforms import StringField, PasswordField, validators, Form
from . import db, login_manager
from .models import User, Web3Request, Web2Response
from .auth import require_apikey
from flask_api_key import api_key_required

serviceworker = Blueprint("serviceworker", __name__)


@serviceworker.route("/getapiparams", methods=["POST"])
@require_apikey
def getapiparams():
    req_params = request.get_json()
    contract_address, contract_chain, api_url = req_params["contract_address"], req_params["contract_chain"], \
    req_params["api_url"]
    print(f'contract_address: {contract_address}, contract_chain: {contract_chain}, api_url: {api_url}')

    resp_data = Web3Request.query.filter_by(calling_contract_addr=contract_address,
                                            calling_contract_chain=contract_chain, api_url=api_url).first()
    if resp_data is None:
        return jsonify({"error": "No such request found"}), 404
    return jsonify({"params": resp_data.params, "encryption_key": resp_data.encryption_key}), 200


@serviceworker.route("/storeinvocation", methods=["POST"])
@require_apikey
def storeinvocation():
    # We get the response and uid and calling contract address and calling contract chain from the request,
    # and store it in the database
    req_params = request.get_json()
    contract_address, contract_chain, api_url, uid, response = req_params["contract_address"], req_params[
        "contract_chain"], req_params["api_url"], req_params["uid"], req_params["response"]

    used_request_config = Web3Request.query.filter_by(calling_contract_addr=contract_address,
                                            calling_contract_chain=contract_chain, api_url=api_url).first()
    if used_request_config is None:
        return jsonify({"error": "No such request found"}), 404

    # Insert the response into the database
    resp_data = Web2Response(calling_contract_addr=contract_address, calling_contract_chain=contract_chain,
                             api_url=api_url, uid=uid, request_id=used_request_config.id)
    db.session.add(resp_data)
    db.session.commit()
    return jsonify({"success": "Response stored"}), 200
