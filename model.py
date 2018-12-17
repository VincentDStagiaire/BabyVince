from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/vincentBaby'
app.config['DEBUG'] = True

db = SQLAlchemy(app)

# plays = db.Table("plays", db.metadata,
#     db.Column('result', db.Integer, nullable=False),
#     db.Column('match_id', db.Integer, db.ForeignKey('match.id')),
#     db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
# )


class Player(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    elo = db.Column(db.Float(), default=2000)
    matchs = db.relationship('Play', back_populates="player")

    def _repr_(self):
        return "id : {id}, name : {name} , lastname : {lastname}, elo : {elo} ".format(id=self.id, name=self.name, lastname=self.lastname, elo=self.elo)


class Match(db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship('Play', back_populates="match")
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return "id : {id}, date : {date} ".format(id=self.id, date=self.date)


class Play(db.Model):
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    result = db.Column(db.Integer, nullable=False, default=0)

    player = db.relationship(Player, back_populates="matchs")
    match = db.relationship(Match, back_populates="players")
