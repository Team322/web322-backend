import os
from flask import Flask, session, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_api_key import APIKeyManager

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
apikey_manager = APIKeyManager()


def create_app():
    app = Flask(__name__, static_url_path='', 
            static_folder=os.environ.get("FLASK_STATIC_PATH", "/volume/"))
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SERVICE_WORKER_API_KEY'] = os.environ.get('SERVICE_WORKER_API_KEY')
    app.config["INVOCATION_FILE_PATH"] = os.environ.get('INVOCATION_FILE_PATH')

    login_manager.session_protection = "strong"
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"

    @login_manager.unauthorized_handler
    def dont_redirect():
        return "Unauthorized", 401

    # Invocation files
    @app.route('/download/<path:filename>')
    def custom_static(filename):
        return send_from_directory(app.config["INVOCATION_FILE_PATH"], filename)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .serviceworker import serviceworker as serviceworker_blueprint
    app.register_blueprint(serviceworker_blueprint)
    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    apikey_manager.init_app(app)

    import web322_backend.models
    with app.app_context():
        db.create_all()

    return app

