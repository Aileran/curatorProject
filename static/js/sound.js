
$(document).ready(function(){
    var audioElement = document.createElement("audio");
    audioElement.src = "https://raw.githubusercontent.com/Metastruct/garrysmod-chatsounds/master/sound/chatsounds/autoadd/snoop_dogg/hold%20up%20wait.ogg";
    $('#Play_Button').click(function(){
        audioElement.play();
    });
});