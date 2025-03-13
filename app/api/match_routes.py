from flask import Blueprint, request
from ..models import Match, db

match_bp = Blueprint("matches", __name__)


# GET last tournament number
@match_bp.route('/last_tournament')
def last_tournament():
    matches = Match.query.all()
    # matches.sort(lambda match: match.createdAt)
    print(matches[-1].to_dict()["tournament_num"])

    return matches[-1].to_dict()


# POST new match
@match_bp.route('/new', methods=["POST"])
def new_match():
    r = request.get_json()
    # print("r: ", r)

    new_match = Match(match_num=r["match_num"],
                      tournament_num=r["tournament_num"],
                      player1=r["player1"],
                      player2=r["player2"])
    db.session.add(new_match)
    db.session.commit()
    return new_match.to_dict()

# # DELETE
# # by tournament num
# @match_bp.route('/delete_batch/<int:tourny_num>')
# def delete_batch(tourny_num):
#     pass


# # single match by id
# @match_bp.route('/delete_batch/<int:tourny_num>')
# def delete_batch(tourny_num):
#     pass


# # purge all
# @match_bp.route('/delete_all')
# def delete_all():
#     pass
