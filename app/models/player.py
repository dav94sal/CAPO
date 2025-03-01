from .db import db

class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    strategy = db.Column(db.String)

    matches = db.relationship("Match", cascade="all, delete-orphan")
