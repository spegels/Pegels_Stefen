function mouse()
{
    var x = document.getElementById("canvas");
    canvas = x.getContext("2d");

    window.addEventListener("mousemove", icon, false);
}

function icon(e) {
    canvas.clearRect(0, 0, 600, 600);
    var xPos = e.clientX;
    var yPos = e.clientY;
    
    var pic = new Image();
    pic.src = "http://www.bearbiology.com/uploads/pics/Brown-Large_01.jpg";
    canvas.drawImage(pic, xPos-100, yPos-100, 200, 200);

}

window.addEventListener("load", mouse, false);