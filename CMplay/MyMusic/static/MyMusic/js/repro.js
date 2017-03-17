$(document).ready(function(){
    audio();
});

function audio() {
    $("#audioPlayer")[0].src = $("#list_can .tdcan a")[0];
    //$("#audioPlayer")[0].play();
    var cancion_actual=0;
    $("#list_can .tdcan a").click(function (e) {
        e.preventDefault();
        $("#audioPlayer")[0].src=this;
        $("#audioPlayer")[0].play();
        cancion_actual=$(this).parent().parent().index();


    });

    $("#audioPlayer")[0].addEventListener("ended",function () {
       cancion_actual++;
        var tan= $("#list_can .tdcan").length;
       if (cancion_actual== tan){
            cancion_actual=0;
            $("#audioPlayer")[0].src = $("#list_can .tdcan a")[cancion_actual];
       }
       else {
           $("#audioPlayer")[0].src = $("#list_can .tdcan a")[cancion_actual];
           $("#audioPlayer")[0].play();
       }

    });
}
