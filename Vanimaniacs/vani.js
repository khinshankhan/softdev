//the svg
var c = document.getElementById("svg_id");

//clear function
var clear = function () {
    // clear nodes
    while(c.hasChildNodes()){
	c.removeChild(c.firstChild);
    }
};


//makes svg elements
var make_svg = function(element){
    return document.createElementNS( "http://www.w3.org/2000/svg", element);
};

//add an svg element to the svg html
var add_svg = function(element){
    c.appendChild(element);
};

//for color
var color;

var id; 
//animation to grow & shrink circle
var animation = function () {
    var radius = 0;
    var action = 1;
    clear();
    //clearInterval(id);
    //console.log("ID: "+id);

    //1 grow, -1 shrink
    var action = 1;

    //grow n shrink circle
    var gs = function () {
	//console.log(radius);
	stopi();
	if(action == -1){
	    clear();
	}
	//sets the color
	color = document.getElementById("colors").value;
	c1 = make_svg("circle");
	c1.setAttribute("cx", 250);
	c1.setAttribute("cy", 250);
	c1.setAttribute("r", radius);
	c1.setAttribute("fill", color);
	c1.setAttribute("stroke", color);
	add_svg(c1);

	//console.log(action)
	if(action == 1){
	    radius++;
	}
	else{
	    radius--;
	}
	if(radius == 0 || radius == 250){
	    //change between grow and shrink
	    if(action == 1){
		action = -1;
	    }
	    else{
		action = 1;
	    }
	}
	
	id = setInterval( gs, 15)
	
    };
    gs();
};

//start animation + save requestID


//stop animation fxn w/o the event
var stopi = function(){
    clearInterval(id);
};

//stop animation fxn
var stopit = function(e){
    clearInterval(id);
};

//connect stop fxn to stop button
var stahp = document.getElementById("stop");
stahp.addEventListener('click', stopit);

//connect animation fxn to reset button, in a sense restarting it
reset.addEventListener('click', animation);


//animation to move like old-timie DVD symbol
var dvda = function () {
    // want it to be 50-450 for both
    var x = Math.floor(Math.random() * (250 - 100)) + 50;
    var y = Math.floor(Math.random() * (250 - 100)) + 50;
    //random pos or neg direction for start
    var dx = Math.random() < 0.5 ? -1 : 1;
    var dy = Math.random() < 0.5 ? -1 : 1;

    console.log("X: "+dx);
    console.log("Y: "+dy);
    
    stopi();
    
    //bounce bounce! like a DVD symbol!
    var bounce = function () {
	clear();
	stopi();
	//sets the color
	color = document.getElementById("colors").value;
	c1 = make_svg("circle");
	c1.setAttribute("cx", x);
	c1.setAttribute("cy", y);
	c1.setAttribute("r", 25);
	c1.setAttribute("fill", color);
	c1.setAttribute("stroke", color);
	add_svg(c1);

	if(x == 25 || x == 500 - 25){
	    dx = dx * -1;
	}
	if(y == 25 || y == 500 - 25){
	    dy = dy * -1;
	}
	
	x += dx;
	y += dy;
		
	id = setInterval( bounce, 10)
	console.log(y);
    };
    bounce();
};

dvd.addEventListener('click', dvda);


animation();
