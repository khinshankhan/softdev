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

    window.cancelAnimationFrame(requestID);
    
    //grow n shrink circle
    var gs = function () {
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
	//console.log(requestID);
	requestID = window.requestAnimationFrame(gs);
    };
    gs();
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

//animation to move like old-timie DVD symbol
var dvda = function () {
    // want it to be 50-450 for both
    var x = Math.floor(Math.random() * (c.width - 100)) + 50;
    var y = Math.floor(Math.random() * (c.height - 100)) + 50;
    //random pos or neg direction for start
    var dx = Math.random() < 0.5 ? -1 : 1;
    var dy = Math.random() < 0.5 ? -1 : 1;

    console.log("X: "+dx);
    console.log("Y: "+dy);
    
    window.cancelAnimationFrame(requestID);
    
    //bounce bounce! like a DVD symbol!
    var bounce = function () {
	clear();
	ctx.beginPath();
	ctx.arc(x, y, 25, 0, 2*Math.PI);
	//sets the color
	color = document.getElementById("colors").value;
	ctx.strokeStyle = color;
	ctx.stroke();
	ctx.fillStyle = color;
	ctx.fill();

	if(x == 25 || x == c.width - 25){
	    dx = dx * -1;
	}
	if(y == 25 || y == c.height - 25){
	    dy = dy * -1;
	}
	
	x += dx;
	y += dy;

	
	//console.log(requestID);
	requestID = window.requestAnimationFrame(bounce);
    };
    bounce();
};

dvd.addEventListener('click', dvda);
