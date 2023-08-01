function displayTime(){
    var dateTime = new Date();
    var hrs = dateTime.getHours();
    var mins = dateTime.getMinutes();
    var secs = dateTime.getSeconds();

    document.getElementById("hr").innerHTML = hrs;
    document.getElementById("min").innerHTML = mins;
    document.getElementById("sec").innerHTML = secs;
}

setInterval(displayTime,10);