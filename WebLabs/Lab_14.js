var error = 0;
function validate() {
    var x = document.forms.inputform.username.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");

    if(atPos < 1 || dotPos < atPos+2 || dotPos+2 > x.length)
        error = error + 1;
}

function passLength() {
    var y = document.forms.inputform.password.value;
    if(y.length < 6)
        error = error + 2;
}


function both() {
    validate();
    passLength();
    if (error == 0)
        alert("Success");
    else if (error == 3)
        alert("We were unable to process your request. Please correct the following errors: \n" +
            "You did not provide a valid email address \n" +
            "Your password did not meet the minimum requirements");
    else if (error == 1)
        alert("We were unable to process your request. Please correct the following errors: \n" +
            "You did not provide a valid email address");
    else if (error == 2)
        alert("We were unable to process your request. Please correct the following errors: \n" +
            "Your password did not meet the minimum requirements");
}
