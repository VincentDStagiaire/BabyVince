from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/vincentBaby'
app.config['DEBUG'] = True
app.config['session_options'] = {"autoflush": False}

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
    plays = db.relationship('Play', back_populates="player")

    def _repr_(self):
        return "id : {id}, name : {name} , lastname : {lastname}, elo : {elo} ".format(id=self.id, name=self.name, lastname=self.lastname, elo=self.elo)


class Match(db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, primary_key=True)
    plays = db.relationship('Play', back_populates="match")
    date = db.Column(db.Date, nullable=False, default=date.today())

    def __repr__(self):
        return "id : {id}, date : {date} ".format(id=self.id, date=self.date)


class Play(db.Model):
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    result = db.Column(db.Integer, nullable=False, default=0)

    player = db.relationship(Player, back_populates="plays")
    match = db.relationship(Match, back_populates="plays")

    def __repr__(self):
        return "match_id : {match_id}, player_id : {player_id}, result : {result} ".format(match_id=self.match_id, player_id=self.player_id, result=self.result)
