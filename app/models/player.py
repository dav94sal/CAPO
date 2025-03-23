from .db import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    strategy = db.Column(db.String)

    p1_matches = db.relationship("Match", foreign_keys="[Match.player1]", cascade="all, delete-orphan")
    p2_matches = db.relationship("Match", foreign_keys="[Match.player2]", cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "strategy": self.strategy,
        }
