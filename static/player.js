$(document).ready(function(){
    $("#AddPlayer").hide();
});

function AddPlayer(){
    $("#ShowPlayers").hide();
    $("#AddPlayer").show();
}

function CancelAddPlayer(){
    $("#ShowPlayers").show();
    $("#AddPlayer").hide();
}
