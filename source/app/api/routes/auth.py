from time import time

from flask import Blueprint, jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.src.rjson import to_type
from app.api.schemas.schema_auth import RegisterUser, LoginUser
from app.src.wrapper import ContainerCoroutine

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route("/register", methods=["GET", "POST"])
@to_type('application/json')
def register(arg):
    try:
        user = RegisterUser(name=arg['name'], passwd=generate_password_hash(arg['passwd']), email=arg['email'])
        ContainerCoroutine(args=user())  # REGISTRANDO USUÁRIO

        return jsonify({"status-ok": 200, "msg":"OK"})
    except Exception as err:
        if '(psycopg2.errors.UniqueViolation)' in str(err):
            return jsonify({"status-error": 500, 'msg': "ERROR: Dados Já existente, por favor repita as etapas com dados diferentes" % err})
        else:
            return jsonify({"status-error": 400, 'msg': "ERROR %s" % err.args})


@bp_auth.route('/login', methods=['GET', 'POST'])
@to_type('application/json')
def login(arg):
    try:
        login_user = LoginUser(name=arg['name'], passwd=arg['passwd'], email=arg['email'])
        ContainerCoroutine(args=login_user())
        return jsonify(access_token=login_user.token)
    except Exception as err:
        return jsonify({"status-error":500, "msg": "ERROR %s" % err})


@bp_auth.route('/update', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()

    return jsonify(user_logged=current_user)

