from flask import Blueprint

match_bp = Blueprint("matches", __name__)


@match_bp.route('new')
def new_match():
    return '<h1>New Match!</h1>'
