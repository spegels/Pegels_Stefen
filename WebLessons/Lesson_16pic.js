/**
 * Created by pegelss0261 on 4/17/2017.
 */
function text()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    var pic = new Image();
    pic.src = "http://www.bearbiology.com/uploads/pics/Brown-Large_01.jpg";

    pic.addEventListener("load", function() { canvas.drawImage(pic, 0, 0, 600, 400)}, false);
}

window.addEventListener("load", text, false);