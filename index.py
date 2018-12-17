from flask import url_for, render_template, request, redirect, Flask
from model import Player, Match, app, db, Play
from datetime import datetime



@app.route('/')
def index(name=None):
    return render_template("welcome.html")

@app.route('/show-players', methods=['GET'])
def show_players():
    players = Player.query.all()
    return render_template("player.html", players=players)

@app.route('/add-player', methods=['POST', 'GET'])
def add_player():
    name_player = request.form.get("name_player")
    lastname_player = request.form.get("lastname_player")
    player = Player(name=name_player, lastname=lastname_player)
    db.session.add(player)
    db.session.commit()
    return redirect('/show-players')


@app.route('/delete-player/<int:id_player>', methods=['GET'])
def delete_player(id_player):
    player = Player.query.filter_by(id=id_player).first()
    db.session.delete(player)
    db.session.commit()
    return redirect('/show-players')

@app.route('/show-matchs', methods=['GET'])
def show_matchs():
    matchs = Match.query.all()
    players = Player.query.all()
    return render_template("match.html", matchs=matchs, players=players)

@app.route('/add-match',  methods=['POST', 'GET'])
def add_match():
    match = Match()
    dict_players = {
        "team1player1": request.form.get("team1player1"),
        "team1player2": request.form.get("team1player2"),
        "team2player1": request.form.get("team2player1"),
        "team2player2": request.form.get("team2player2")
    }
    result1 = request.form.get("result1")
    result2 = request.form.get("result2")
    for clef, player_id in dict_players.items():
        if player_id:
            if "team1" in clef:
                play = Play(result=result1)
            else:
                play = Play(result=result2)
            player = Player.query.filter_by(id=player_id).first()
            match.players.append(play) 
    db.session.add(match)
    db.session.commit()
    return redirect("/show-matchs")
