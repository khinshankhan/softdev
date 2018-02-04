//get canvas
var c = document.getElementById("slate");
//canvas contextualized
var ctx = c.getContext("2d");

//toggling option shape
// 1 square, -1 circle
var shape = 1;

//for color
var color = "red";

//clear function
var clear = function (e) {
    ctx.clearRect(0, 0, 500, 500);
};

//connect clear function to button
var button = cl.addEventListener('click', clear);

//switches the shape
var change = function (e) {
    shape = shape * -1;
};

//connect toggle/change function to button
var button = toggle.addEventListener('click', change);

//draws the right shape
var draw = function (e) {
    //get coordinates
    //math for getting it closer to the click
    var x = e.clientX - 7;
    var y = e.clientY - 77;
    //console.log("X: " + x);
    //console.log("Y: " + y);

    //sets the color
    color = document.getElementById("colors").value;
    ctx.strokeStyle = color;
    ctx.beginPath();
    if(shape == 1){
	//center into square
	x = x - 25;
	y = y - 25;
	ctx.rect(x,y,50,50);
    }
    else{
	ctx.arc(x, y, 25, 0, 2*Math.PI);
    }
    ctx.stroke();
    ctx.fillStyle = color;
    ctx.fill();
};

//connect draw function to click on canvas
slate.addEventListener("click", draw);
