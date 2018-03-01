//the svg
var c = document.getElementById("svg_id");

//clear function
var clear = function () {
    // clear nodes
    while(c.hasChildNodes()){
	c.removeChild(c.firstChild);
    }
    //reset variables
    
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

//1 grow, -1 shrink
var action = 1;
//change between grow and shrink
var toggle = function () {
    action = action * -1;
};

//animation to grow & shrink circle
var animation = function () {
    var radius = 50;
    action = 1;

    clearInterval(id);
    
    //grow n shrink circle
    var gs = function () {
	clear();
	//sets the color
	color = document.getElementById("colors").value;
	c1 = make_svg("circle");
	c1.setAttribute("cx", c.width/2+"");
	c1.setAttribute("cy", c.height/2+"");
	c1.setAttribute("r", radius+"");
	c1.setAttribute("fill", color);
	c1.setAttribute("stroke", color);
	add_svg(c1);
	/*
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
	id = setInterval( gs, 15)
	*/
    };
    gs();
};

//start animation + save requestID
id = setInterval( animation, 15)

//stop animation fxn
var stopit = function(e){
    clearInterval(id);
};

//connect stop fxn to stop button
var stahp = document.getElementById("stop");
stahp.addEventListener('click', stopit);

//connect animation fxn to reset button, in a sense restarting it
reset.addEventListener('click', animation);
