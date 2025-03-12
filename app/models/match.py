from .db import db

class Match(db.Model):
    __tablename__ = 'matches'

    id = db.Column(db.Integer, primary_key=True)
    match_num = db.Column(db.Integer)
    tournament_num = db.Column(db.Integer, autoincrement=True)
    player1 = db.Column(db.Integer, db.ForeignKey("players.id"))
    player2 = db.Column(db.Integer, db.ForeignKey("players.id"))

    rounds = db.relationship("Round", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "match_num": self.match_num,
            "tournament_num": self.tournament_num,
            "player1": self.player1,
            "player2": self.player2,
        }
