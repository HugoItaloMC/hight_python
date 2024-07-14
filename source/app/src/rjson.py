from flask import request, jsonify
from functools import wraps


def to_type(content_type):
    if 'json' not in content_type:
        return jsonify({"status-error": 400, "msg": "REQUEST NEED BE 'application/json'"})

    def container(args):
        @wraps(args)
        def wrapper(*arg, **kw):
            xstr = lambda ss: ss or ''
            content_json = 'json' in xstr(content_type)

            if request.method == 'POST':
                label = request.get_json(force=True) or request.get_json() or request.form.to_dict()
                fields = request.json if content_json else label
                return args(arg=fields)
            return args(*arg, **kw)
        return wrapper
    return container
