
$(document).ready(function(){
    var audioElement = document.createElement("audio");
    audioElement.src = "https://raw.githubusercontent.com/Aileran/curatorProject/master/static/mp3/labrador-barking-daniel_simon.mp3?token=ASAMGULTC4JZGG2TWYHBYAC72FN66";
    $('#Play_Button').click(function(){
        audioElement.play();
    });
});