from sqlalchemy import text
from .db import db

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    match_num = db.Column(db.Integer, nullable=False)
    tournament_num = db.Column(db.Integer, nullable=False)
    player1 = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    player2 = db.Column(db.Integer, db.ForeignKey("players.id"), nullable=False)
    createdAt = db.Column(db.DateTime, server_default=text('CURRENT_TIMESTAMP'))

    rounds = db.relationship("Round", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "match_num": self.match_num,
            "tournament_num": self.tournament_num,
            "player1": self.player1,
            "player2": self.player2,
            "createdAt": self.createdAt,
        }
