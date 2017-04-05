function shapes()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");
    var g = canvas.createLinearGradient(380, 140, 640, 390);
    g.addColorStop(0, "green");
    g.addColorStop(0.5, "aquamarine");
    g.addColorStop(1, "blue");
    canvas.fillStyle = g;

    canvas.beginPath();
    canvas.moveTo(510, 90);
    canvas.lineTo(540, 200);
    canvas.lineTo(640, 140);
    canvas.lineTo(580, 240);
    canvas.lineTo(700, 265);
    canvas.lineTo(580, 290);
    canvas.lineTo(640, 390);
    canvas.lineTo(540, 330);
    canvas.lineTo(510, 440);
    canvas.lineTo(480, 330);
    canvas.lineTo(380, 390);
    canvas.lineTo(440, 290);
    canvas.lineTo(320, 265);
    canvas.lineTo(440, 240);
    canvas.lineTo(380, 140);
    canvas.lineTo(480, 200);
    canvas.closePath();
    canvas.stroke();
    canvas.fill();


}


window.addEventListener("load", shapes, false);
