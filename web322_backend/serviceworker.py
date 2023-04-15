from flask import Blueprint, jsonify, request
from wtforms import StringField, PasswordField, validators, Form
from . import db, login_manager
from .models import User
from .auth import require_apikey
from flask_api_key import api_key_required

serviceworker = Blueprint("serviceworker", __name__)


@serviceworker.route("/getapiparams", methods=["GET"])
def getapiparams():
    pass


@serviceworker.route("/storeinvocation", methods=["POST"])
def storeinvocation():
    pass
