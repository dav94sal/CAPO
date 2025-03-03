from flask import Blueprint
from ..models import Player

players_bp = Blueprint("players", __name__)


@players_bp.route('/')
def all_players():
    players = Player.query.all()
    print(players)
    return [player.to_dict() for player in players]


@players_bp.route('new')
def new_player():
    return "<h1>New Player!</h1>"
