from .db import db

class Round(db.Model):
    __tablename__ = 'rounds'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    round = db.Column(db.Integer, nullable=False)
    move1 = db.Column(db.String(1), nullable=False)
    move2 = db.Column(db.String(1), nullable=False)
    match_id = db.Column(db.Integer, db.ForeignKey("matches.id"), nullable=False)

    match = db.relationship("Match", overlaps="rounds")
