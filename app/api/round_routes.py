from flask import Blueprint, request
from ..models import Round, db

round_bp = Blueprint("rounds", __name__)


# GET all rounds
@round_bp.route('/all')
def get_all_rounds():
    rounds = Round.query.all()
    if rounds:
        return [round.to_dict() for round in rounds]
    else:
        return {"message": "No rounds available yet"}


# GET rounds by match
@round_bp.route('<int:match_id>')
def get_rounds_by_match(match_id):
    rounds = Round.query.filter_by(match_id=match_id).all()

    if rounds:
        return [round.to_dict() for round in rounds]
    else:
        return {"message": "Match Id Not Found"}, 404


# POST new round
@round_bp.route('/new', methods=["POST"])
def new_round():
    r = request.get_json()

    new_round = Round(round=r["round"],
                      move1=r["move1"],
                      move2=r["move2"],
                      match_id=r["match_id"],)

    db.session.add(new_round)
    db.session.commit()

    return new_round.to_dict()
