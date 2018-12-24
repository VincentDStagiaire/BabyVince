$(document).ready(function(){
    $("#AddMatch").hide();
});


function AddMatch(){
    $("#ShowMatchs").hide();
    $("#AddMatch").show();
}

function cancelAddMatch(){
    $("#ShowMatchs").show();
    $("#AddMatch").hide();
}

function compare2PlayersID(id1, id2) {
    if (id1 !== null && id2 !== null && typeof(id1) !== "undefined" && typeof(id2) !== "undefined" ){
        if (id1 === id2 ){
            return true;
        }
        else{
            return false;
        }
    }
}

function refreshMultiSelectPlayers(){
    //deselected all choices
    $("#team1-select option:selected").prop("selected", false);
    $("#team2-select option:selected").prop("selected", false);

}
$("#buttonAddMatch").click(function(event){
    var team1player1 = $("#team1-select").val()[0];
    var team1player2 = $("#team1-select").val()[1];
    var team2player1 = $("#team2-select").val()[0];
    var team2player2 = $("#team2-select").val()[1];

    // every compare with teamp1 player1
    if (compare2PlayersID(team1player1, team1player2)){
        event.preventDefault();
        alert("Il faut des joueurs différents !");
    };
    if (compare2PlayersID(team1player1, team2player1)){
        event.preventDefault();
        alert("Il faut des joueurs différents !");
    };
    if (compare2PlayersID(team1player1, team2player2)){
        event.preventDefault();
        alert("Il faut des joueurs différents !");
    };

    // other compare with team1 player2
    if (compare2PlayersID(team1player2, team2player1)){
        event.preventDefault();
        alert("Il faut des joueurs différents !");
    };

    if (compare2PlayersID(team1player2, team2player2)){
        event.preventDefault();
        alert("Il faut des joueurs différents !");
    };

    // finish compare with the second team
    if (compare2PlayersID(team2player2, team2player1)){
        event.preventDefault();
        alert("Il faut des joueurs différents !");
    };
});

//Checke if a  multi select players got more than 2 players
// and deselected thems if it's true 
$("#team1-select").change(function (event) {
    if ($("#team1-select option:selected").length > 2) {
        alert("Pas plus de 2 joueurs par équipe :P ")
        refreshMultiSelectPlayers();
        
    }
    //Try to remove the option player of the second multi-select but it's complicated : 
    // TO DO : find a way to reload the multi select in case of error choice 
    var saveTeam1 = $("#team1-select").val().slice(-1)[0] 
    $("#team2-select option[value='" + saveTeam1 + "']").remove();
});

//Checke if a  multi select players got more than 2 players
// and deselected thems if it's true 
$("#team2-select").change(function (event) {
    if ($("#team2-select option:selected").length > 2) {
        alert("Pas plus de 2 joueurs par équipe :P ")
        refreshMultiSelectPlayers();
    }
    //Try to remove the option player of the second multi-select but it's complicated : 
    // TO DO : find a way to reload the multi select in case of error choice 
    var saveTeam2 = $("#team2-select").val().slice(-1)[0]
    $("#team1-select option[value='" + saveTeam2 + "']").remove();
});
