//get canvas
var c = document.getElementById("slate");
//canvas contextualized
var ctx = c.getContext("2d");

//to stop
var requestID;

//clears canvas
var clear = function () {
    ctx.clearRect(0, 0, 500, 500);
};

//for color
var color;

//1 grow, -1 shrink
var action = 1;
//change between grow and shrink
var toggle = function () {
    action = action * -1;
};

//animation to grow & shrink circle
var animation = function () {
    var radius = 0;
    action = 1;
    
    var circle = function () {
	clear();
	ctx.beginPath();
	ctx.arc(c.width/2, c.height/2, radius, 0, 2*Math.PI);
	//sets the color
	color = document.getElementById("colors").value;
	ctx.strokeStyle = color;
	ctx.stroke();
	ctx.fillStyle = color;
	ctx.fill();
	if(action == 1){
	    radius++;
	}
	else{
	    radius--;
	}
	if(radius == 0 || radius == c.height/2){
	    toggle();
	}
	console.log(requestID);
	requestID = window.requestAnimationFrame(circle);
    };
    circle();
};

//start animation + save requestID
requestID = window.requestAnimationFrame(animation);

//stop animation fxn
var stopit = function(e){
    //console.log("Stop "+requestID);
    window.cancelAnimationFrame(requestID);
};

//connect stop fxn to stop button
var stahp = document.getElementById("stop");
stahp.addEventListener('click', stopit);

//connect animation fxn to reset button, in a sense restarting it
reset.addEventListener('click', animation);

