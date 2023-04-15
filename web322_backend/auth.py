from flask import Blueprint, jsonify, request
from flask_login import login_user
from wtforms import StringField, PasswordField, validators, Form
from . import db, login_manager
from .models import User

auth = Blueprint("auth", __name__)


class LoginForm(Form):
    class Meta:
        csrf=False
    username = StringField("username", [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField("password", [validators.DataRequired()])

    def __init__(self, json_data):
        super().__init__()
        self.username.data = json_data.get("username", None)
        self.password.data = json_data.get("password", None)

    def __repr__(self):
        return f"LoginForm('{self.username.data}', '{self.password.data}')"


class SignupForm(Form):
    class Meta:
        csrf=False
    username = StringField("New username", [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField("New Password", [validators.DataRequired()])

    def __init__(self, form_data):
        super().__init__()
        self.username.data = form_data.get("username", None)
        self.password.data = form_data.get("password", None)

    def __repr__(self):
        return f"SignupForm('{self.username.data}', '{self.password.data}')"


@auth.route("/login", methods=["POST"])
def login():
    form = LoginForm(request.get_json())
    if form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user)
            return jsonify({"message": "User logged in successfully"}), 200
        else:
            return jsonify({"message": "Invalid username or password"}), 401
    return jsonify({"message": "invalid form data"}), 403


@auth.route("/signup", methods=["POST"])
def signup():
    form = SignupForm(request.get_json())
    if form.validate():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            return jsonify({"message": "Username already exists"}), 403
        user = User(username=form.username.data, pwd=form.password.data)
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User created successfully"}), 200
    return jsonify({"message": "invalid form data"}), 403


@auth.route("/logout")
def logout():
    return "Logout"
