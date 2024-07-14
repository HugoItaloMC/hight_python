from flask import Blueprint, request, jsonify

from app.api.utils.rjson import to_type
from app.api.schemas.schema_user import Register
from app.api.utils.wrapper import coroutine

bp_user = Blueprint('user', __name__, url_prefix='/user')


@bp_user.route("/register", methods=["GET", "POST"])
@to_type('application/json')
def register(arg):
    try:
        user = Register(name=arg['name'], passwd=arg['passwd'], email=arg['email'])
        coroutine(args=user())  # REGISTRANDO USUÁRIO
        return jsonify({"status-ok": 200, "msg":"OK"})
    except Exception as err:
        if '(psycopg2.errors.UniqueViolation)' in str(err):
            return jsonify({"status-error": 500, 'msg': "ERROR: Dados Já existente, por favor repita as etapas com dados diferentes" % err})
        else:
            return jsonify({"status-error": 400, 'msg': "ERROR %s" % err.args})
