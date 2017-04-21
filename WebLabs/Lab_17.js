/**
 * Created by pegelss0261 on 4/20/2017.
 */
function drag() {
    bear = document.getElementById("bear");
    leftbox = document.getElementById("leftBox");

    bear.addEventListener("dragstart", startDrag, false);
    bear.addEventListener("dragend", endDrag, false);

    leftbox.addEventListener("dragenter", dragEnter, false);
    leftbox.addEventListener("dragleave", dragLeave, false);
    leftbox.addEventListener("dragover", function(e){e.preventDefault()}, false);
    leftbox.addEventListener("drop", drop, false);
}

function startDrag(e){
    var pic = '<img id = "bear" src = "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQz-wyviyl8QCzg0QTPRLbrOj5GevYnzoernqiZ0JsHQ9pnRQCX">';
    e.dataTransfer.setData('Picture', pic);
}

function dragEnter(e){
    e.preventDefault();
    leftbox.style.background = "aquamarine";
    leftbox.style.border = "2px solid gray";
}

function dragLeave(e){
    e.preventDefault();
    leftbox.style.background = "white";
    leftbox.style.border = "2px solid gray";
}

function drop(e) {
    e.preventDefault();
    leftBox.innerHTML = e.dataTransfer.getData('Picture');
}

function endDrag(e){
    pic = e.target;
    pic.style.visibility = "hidden";
}
window.addEventListener("load", drag, false);