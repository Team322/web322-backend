from flask import Blueprint, jsonify, request
from wtforms import StringField, PasswordField, validators, Form
from . import db, login_manager
from .models import User

serviceworker = Blueprint("serviceworker", __name__)


@serviceworker.route("/getapiparams", methods=["GET"])
def getapiparams():
    pass


@serviceworker.route("/storeinvocation", methods=["POST"])
def storeinvocation():
    pass
