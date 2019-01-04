from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost/vincentBaby'
app.config['DEBUG'] = True
app.config['session_options'] = {"autoflush": False}
app.config['SECRET_KEY'] = "coucou"

db = SQLAlchemy(app)

# the table necessary for the join between team and players
plays = db.Table("plays", db.metadata,
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'))
)


class Player(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    elo = db.Column(db.Float(), default=2000)
    teams = db.relationship('Team', secondary=plays, back_populates="")

    def _repr_(self):
        return "id : {id}, name : {name} , lastname : {lastname}, elo : {elo} ".format(id=self.id, name=self.name, lastname=self.lastname, elo=self.elo)
    
    def get_tuple_player(self):
        fullname = "{0} {1}".format(self.name, self.lastname)
        return (self.id, fullname)

class Match(db.Model):
    __tablename__ = "match"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today())
    teams = db.relationship('Team', back_populates="match")

    def __repr__(self):
        return "id : {id}, date : {date} ".format(id=self.id, date=self.date)


class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.Integer, nullable=False, default=0)

    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    match = db.relationship("Match")
    
    players = db.relationship("Player", secondary=plays, back_populates="teams")



# class Play(db.Model):
#     match_id = db.Column(db.Integer, db.ForeignKey('match.id'), primary_key=True)
#     player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
#     result = db.Column(db.Integer, nullable=False, default=0)

#     player = db.relationship(Player, back_populates="plays")
#     match = db.relationship(Match, back_populates="plays")

#     def __repr__(self):
#         return "match_id : {match_id}, player_id : {player_id}, result : {result} ".format(match_id=self.match_id, player_id=self.player_id, result=self.result)
