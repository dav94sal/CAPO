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


# POST rounds by match
@round_bp.route('/new', methods=["POST"])
def new_round():
    r = request.get_json()
    match_rounds = [r[o] for o in r]

    for round in match_rounds:
        new_round = Round(round=round["round"],
                        move1=round["move1"],
                        move2=round["move2"],
                        match_id=round["match_id"],)
        db.session.add(new_round)

    db.session.commit()

    return new_round.to_dict()


@round_bp.route('/delete_all', methods=["DELETE"])
def delete_all():
    all_rounds = Round.query.all()

    if all_rounds:
        for r in all_rounds:
            db.session.delete(r)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
    else:
        return {"message": "No rounds in database"}, 404
