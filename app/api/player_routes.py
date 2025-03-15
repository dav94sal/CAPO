from flask import Blueprint, request
from ..models import Player, db
# from ..forms import AddNewPlayerForm

players_bp = Blueprint("players", __name__)


# GET all players
@players_bp.route('/all')
def all_players():
    players = Player.query.all()
    print(players)
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


# DELETE
# # One player
@players_bp.route('/delete/<int:player_id>', methods=["DELETE"])
def delete_one(player_id):
    player = Player.query.get(player_id)

    if player:
        db.session.delete(player)
        db.session.commit()
        return {"message": "Successfully Deleted"}
    else:
        return {"message": "Player Not Found"}, 404
