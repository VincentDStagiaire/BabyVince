$(document).ready(function(){
    $("#AddMatch").hide();
    // document.multiselect('#team1-select');
    // document.multiselect('#team2-select');
});

function AddMatch(){
    $("#ShowMatchs").hide();
    $("#AddMatch").show();
}

function cancelAddMatch(){
    $("#ShowMatchs").show();
    $("#AddMatch").hide();
}

// function compare2PlayersID(id1, id2) {
//     if (id1 !== null && id2 !== null){
//         if (id1 === id2 ){
//             return true;
//         }
//         else{
//             return false;
//         }
//     }
// }

// $("#buttonAddMatch").click(function(event){
//     var team1player1 = $("#team1player1-select").val();
//     var team1player2 = $("#team1player2-select").val();
//     var team2player1 = $("#team2player1-select").val();
//     var team2player2 = $("#team2player2-select").val();

//     // every compare with teamp1 player1
//     if (compare2PlayersID(team1player1, team1player2)){
//         event.preventDefault();
//         alert("Il faut des joueurs différents !");
//     };
//     if (compare2PlayersID(team1player1, team2player1)){
//         event.preventDefault();
//         alert("Il faut des joueurs différents !");
//     };
//     if (compare2PlayersID(team1player1, team2player2)){
//         event.preventDefault();
//         alert("Il faut des joueurs différents !");
//     };

//     // other compare with team1 player2
//     if (compare2PlayersID(team1player2, team2player1)){
//         event.preventDefault();
//         alert("Il faut des joueurs différents !");
//     };

//     if (compare2PlayersID(team1player2, team2player2)){
//         event.preventDefault();
//         alert("Il faut des joueurs différents !");
//     };

//     // finish compare with the second team
//     if (compare2PlayersID(team2player2, team2player1)){
//         event.preventDefault();
//         alert("Il faut des joueurs différents !");
//     };
// });

$("team2-select").change(function (event) {
    if($("select option:selected").length > 2) {
        alert("Si c'est marqué important, c'est qu'il faut lire :P ");
        event.preventDefault();
    }
});

$("#team1-select").change(function (event) {
    if($("select option:selected").length > 2) {
        alert("Si c'est marqué important, c'est qu'il faut lire :P ");
        event.preventDefault();
    }
});
