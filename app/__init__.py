from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix


def create_app():
    app = Flask(__name__, instance_relative_config=False)

    from api.db import init_app
    from api.utils.base_model import db
    with app.app_context():
        init_app(app)
        db.init_app(app)

        from api.routes.user import bp_user

        app.register_blueprint(bp_user)

        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

    return app
