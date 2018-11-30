from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime



db = SQLAlchemy(app)

# plays = db.Table('plays',
#     db.Column('match_id', db.Integer, db.ForeignKey('match.id'), primary_key=True),
#     db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
#     db.Column('result', db.Integer, nullable=False))


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    elo = db.Column(db.Float(), default=2000)
    matchs = db.relationship('Match', secondary="play")

    def _repr_(self):
        return "id : {id}, name : {name} , lastname : {lastname}, elo : {elo} ".format(id=self.id, name=self.name, lastname=self.lastname, elo=self.elo)


class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship('Player', secondary="play")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "id : {id}, date : {date} ".format(id=self.id, date=self.date)


class Play(db.Model):
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    result = db.Column(db.Integer, nullable=False)

    player = db.relationship(Player, backref=db.backref("play"))
    match = db.relationship(Match, backref=db.backref("play"))
