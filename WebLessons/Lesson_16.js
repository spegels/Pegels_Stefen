/**
 * Created by pegelss0261 on 4/17/2017.
 */
function text()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    canvas.shadowOffsetX = 4;
    canvas.shadowOffsetY = 4;
    canvas.shadowBlur = 6;
    canvas.shadowColor = "rgba(0, 0, 355, .5";

    canvas.font = "bold 36px Tahoma";
    canvas.textAlign = "end";
    canvas.save();
    canvas.fillText("Canvas", 300, 100);

    canvas.translate(100, 150);
    canvas.fillText("After Translate", 300, 100);

    canvas.rotate(Math.PI);
    canvas.fillText("After Rotate", 0, 0);

    canvas.restore();
    canvas.scale(1.5, 4);
    canvas.fillText("After Scale", 300, 100);

}

window.addEventListener("load", text, false);