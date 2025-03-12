from flask import Blueprint, request
from ..models import Match, db

match_bp = Blueprint("matches", __name__)


# POST new match
@match_bp.route('/new', methods=["POST"])
def new_match():
    r = request.get_json()
    print("r: ", r)

    new_match = Match(match_num=r["match_num"],
                      tournament_num=r["tournament_num"],
                      player1=r["player1"],
                      player2=r["player2"])
    db.session.add(new_match)
    db.session.commit()
    return new_match.to_dict()
