$(document).ready(function(){
    initWelcome();
});

function ShowPlayers(){
    LeaveWelcome();
    $("#ShowPlayers").show();
    $("#ComeBackWelcome").show();
}

function ShowMatchs(){
    LeaveWelcome();
    $("#ShowMatchs").show();
    $("#ComeBackWelcome").show();
}

function LeaveWelcome(){
    $("#buttonSPlayers").hide();
    $("#buttonAMatch").hide();
    $("#buttonSMatchs").hide();
    $("#buttonAPlayer").hide();
}
function AddMatch(){
    LeaveWelcome();
    $("#AddMatch").show();
    $("#ComeBackWelcome").show();
}
function ComeBackWelcome(){
    //$("#ShowPlayers").hide();
    //$("#AddPlayer").hide();
    //$("#ShowMatchs").hide();
    //$("#AddMatch").hide();
    //$("#ComeBackWelcome").hide();
    initWelcome();
    $("#buttonSPlayers").show();
    $("#buttonAMatch").show();
    $("#buttonSMatchs").show();
    $("#buttonAPlayer").show();
}

function initWelcome(){
    $("#ShowPlayers").hide();
    $("#AddPlayer").hide();
    $("#ShowMatchs").hide();
    $("#AddMatch").hide();
    $("#ComeBackWelcome").hide();
}
