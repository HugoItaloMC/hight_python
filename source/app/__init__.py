import secrets
import os

from flask import Flask
from flask_jwt_extended import JWTManager
from werkzeug.middleware.proxy_fix import ProxyFix

from app.api.schemas.schema_auth import UserID


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'default_secret_key')

    from app.db import init_app
    with app.app_context():
        init_app(app)
        app.secret_key = secrets.token_hex(16)
        jwt = JWTManager(app)

        @jwt.user_identity_loader
        def user_identity_lookup(user):
            """
                Registra uma funcão de callback que registra uma identidade JWT
              serializado como objeto JSON
            :param user: Usuário registrado no JWT
            :return: Usuário registrado
            """
            return user

        @jwt.user_lookup_loader
        def user_lookup_callback(_jwt_header, jwt_data):
            """
                Uma funcão de callback para retornar um usuário do banco de dados
               em rotas protegidas
            :return: Um usuário do banco de dados
            """
            identity = jwt_data["sub"]
            return UserID(id=identity)

        from app.api.routes.auth import bp_auth

        app.register_blueprint(bp_auth)

        # Para aplicacão se comportar como proxys no WSGI
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

    return app
