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

@app.route('/add-match', methods=['POST', 'GET'])
def add_match():

    # Creation object Match
    match = Match()
    db.session.add(match)
    db.session.commit()

    # Get the id of the players
    team1player1_id = request.form.get("team1player1")
    team1player2_id = request.form.get("team1player2")
    team2player1_id = request.form.get("team2player1")
    team2player2_id = request.form.get("team2player2")

    # Get the results of the match
    result1 = request.form.get("result1")
    result2 = request.form.get("result2")
    
    # Cration association object : play for each player in the match
    team1play1 = Play(result=result1, match_id=match.id)
    team2play1 = Play(result=result2, match_id=match.id)
    
    # Set the player and add to the match
    team1play1.player = Player.query.filter_by(id=team1player1_id).first()
    team2play1.player = Player.query.filter_by(id=team2player1_id).first()

    match.plays.append(team1play1)
    match.plays.append(team2play1)

    # Set the second players if they played
    if team1player2_id:
        team1play2 = Play(result=result1)
        team1play2.player = Player.query.filter_by(id=team1player2_id).first()
        match.plays.append(team1play2)
    
    if team2player2_id:
        team2play2 = Play(result=result2)
        team2play2.player = Player.query.filter_by(id=team2player2_id).first()
        match.plays.append(team2play2)
    
    # Add in the database and commit
    db.session.add(match)
    db.session.commit()

    return redirect("/show-matchs")


@app.route('/delete-match/<int:id_match>', methods=['GET'])
def delete_match(id_match):
    plays = Play.query.filter_by(match_id=id_match).all()
    for play in plays:
        db.session.delete(play)
    match = Match.query.filter_by(id=id_match).first()
    db.session.delete(match)
    db.session.commit()
    return redirect('/show-matchs')
