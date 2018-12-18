$(document).ready(function(){
    $("#AddMatch").hide();
});

function AddMatch(){
    $("#AddMatch").show();
}

function compare2PlayersID(id1, id2) {
    if (id1 === id2){
        return true;
    }
    else{
        return false;
    }
}

$("button").click(function(event){
    event.preventDefault();
    var team1player1 = $("#team1player1-select").val()
    var team1player2 = $("#team1player2-select").val()
    var team2player1 = $("#team2player1-select").val()
    var team2player2 = $("#team2player2-select").val()

    // every compare with teamp1 player1
    if (compare2PlayersID(team1player1, team1player2)){
        alert("Il faut des joueurs différents !")
        event.stopPropagation();
    };
    if (compare2PlayersID(team1player1, team2player1)){
        alert("Il faut des joueurs différents !")
        event.stopPropagation();
    };
    if (compare2PlayersID(team1player1, team2player2)){
        alert("Il faut des joueurs différents !")
        event.stopPropagation();
    };

    // other compare with team1 player2
    if (compare2PlayersID(team1player2, team2player1)){
        alert("Il faut des joueurs différents !")
        event.stopPropagation();
    };

    if (compare2PlayersID(team1player2, team2player2)){
        alert("Il faut des joueurs différents !")
        event.stopPropagation();
    };

    // finish compare with the second team
    if (compare2PlayersID(team2player2, team2player1)){
        alert("Il faut des joueurs différents !")
        event.stopPropagation();
    };

});
