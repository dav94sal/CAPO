from flask import Blueprint, request
from ..models import Player, db
# from ..forms import AddNewPlayerForm

players_bp = Blueprint("players", __name__)


# GET two players
@players_bp.route('/<int:player1_id>/<int:player2_id>')
def get_two_players(player1_id, player2_id):
    player1 = Player.query.get(player1_id)
    player2 = Player.query.get(player2_id)
    

# GET all players
@players_bp.route('/all')
def all_players():
    players = Player.query.all()
    # print(players)
    return [player.to_dict() for player in players]


# POST new player
@players_bp.route('/new', methods=["POST"])
def new_player():
    r = request.get_json()
    # print("Hit the backend!", r)
    player = Player(strategy=r["strategy"])

    db.session.add(player)
    db.session.commit()
    return player.to_dict()
    # return form.errors, 401
