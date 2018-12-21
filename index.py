from flask import url_for, render_template, request, redirect, Flask
from model import Player, Match, app, db, plays, Team
from datetime import datetime

@app.route('/')
def index(name=None):
    return render_template("welcome.html")

@app.route('/show-players', methods=['GET'])
def show_players():
    """
    We get all of the players and send it to the templates which show them
    """
    players = Player.query.all()
    return render_template("player.html", players=players)

@app.route('/add-player', methods=['POST', 'GET'])
def add_player():
    """
    We create a player with his name and lastname
    """
    name_player = request.form.get("name_player")
    lastname_player = request.form.get("lastname_player")
    player = Player(name=name_player, lastname=lastname_player)
    db.session.add(player)
    db.session.commit()
    return redirect('/show-players')


@app.route('/delete-player/<int:id_player>', methods=['GET'])
def delete_player(id_player):
    """
    We create the player object and delete it 

    :id_player(int) : the player's id
    """
    player = Player.query.filter_by(id=id_player).first()
    db.session.delete(player)
    db.session.commit()
    return redirect('/show-players')

@app.route('/show-matchs', methods=['GET'])
def show_matchs():
    """
    We get all of the matchs and send its to the template
    """
    matchs = Match.query.all()
    players = Player.query.all()
    return render_template("match.html", matchs=matchs, players=players)

@app.route('/add-match', methods=['POST', 'GET'])
def add_match():
    """
    We create a match object, 2 teamps and get the players 
    """
    # Creation object Match
    match = Match()
    
    # Get the players
    team1_players = request.form.getlist("team1-select")
    team2_players = request.form.getlist("team2-select")

    # Get the results of the match
    result1 = request.form.get("result1")
    result2 = request.form.get("result2")

    #Creation of the teams
    team1 = Team(result=result1)
    team2 = Team(result=result2)
    
    # # Cration association object : play for each player in the match
    # team1play1 = Play(result=result1, match_id=match.id)
    # team2play1 = Play(result=result2, match_id=match.id)
    
    # Set the player and add to the match
    team1player1 = Player.query.filter_by(id=int(team1_players[0])).first()
    team2player1 = Player.query.filter_by(id=int(team2_players[0])).first()

    team1.players.append(team1player1)
    team2.players.append(team2player1)

    # Set the second players if they played
    if len(team1_players) > 1:
        team1player2 = Player.query.filter_by(id=int(team1_players[1])).first()
        team1.players.append(team1player2)
    
    if len(team2_players) > 1:
        team2player2 = Player.query.filter_by(id=int(team2_players[1])).first()
        team2.players.append(team2player2)

    # Add the both teams to the matchs
    match.teams.append(team1)
    match.teams.append(team2)

    # Add in the database and commit
    db.session.add(match)
    db.session.commit()

    return redirect("/show-matchs")


@app.route('/delete-match/<int:id_match>', methods=['GET'])
def delete_match(id_match):
    """
    Delete a match

    :id_match(int) : the match id
    """
    #creation object match and all teams of the  match
    match = Match.query.filter_by(id=id_match).first()
    teams = Team.query.filter_by(match_id=id_match).all()

    #for each team, we delete it
    for team in teams:
        match.teams.remove(team)
        db.session.delete(team)

    # delete the match
    db.session.delete(match)
    db.session.commit()
    return redirect('/show-matchs')
