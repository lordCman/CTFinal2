from functools import wraps
from flask import request

from .models import User


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][7:]
        else:
            return {
                'status': 'not ok',
                'message': 'Missing header, please add "Authorization" to your headers'
            }
        if not token:
            return {
                'status': 'not ok',
                'message': 'Missing auth token. Please lopg in to a user that has a valid token'
            }
        user = User.query.filter_by(apitoken = token).first()
        if not user:
            return {
                 'status': 'not ok',
                 'message': 'that token does not belong to a valid user'
            }
        return func(user = user, *args, **kwargs)
    return decorated

