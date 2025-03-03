from flask import Blueprint

round_bp = Blueprint("rounds", __name__)


@round_bp.route('new')
def new_round():
    return '<h1>New Round!</h1>'
