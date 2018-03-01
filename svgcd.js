//the svg
var c = document.getElementById("svg_id");

//clear function
var clear = function (e) {
    // clear nodes
    while(c.hasChildNodes()){
	c.removeChild(c.firstChild);
    }
    //reset variables
    prevx = null;
    prevy = null;
};

//connect clear function to button
cl.addEventListener('click', clear);

//makes svg elements
var make_svg = function(element){
    return document.createElementNS( "http://www.w3.org/2000/svg", element);
};

//add an svg element to the svg html
var add_svg = function(element){
    c.appendChild(element);
};

//variables for previous node
var prevx
var prevy
//draws the dot node + connects to last one if possible
var draw = function (e) {
    //get coordinates with offset
    var x = e.offsetX;
    var y = e.offsetY;
    //get the color
    color = document.getElementById("colors").value;
    //circle
    c1 = make_svg("circle");
    c1.setAttribute("cx", x);
    c1.setAttribute("cy", y);
    c1.setAttribute("r", "25");
    c1.setAttribute("fill", color);
    add_svg(c1);
    if(prevx != null){
	//line to connect
	c2 = make_svg("line");
	console.log(prevx)
	console.log(prevy)
	c2.setAttribute("x1", prevx);
	c2.setAttribute("y1", prevy);
	c2.setAttribute("x2", x);
	c2.setAttribute("y2", y);
	c2.setAttribute("fill", "black");
	add_svg(c2);
    }
    prevx = x;
    prevy = y;
	
};

//connect draw function to click on
c.addEventListener("click", draw);
