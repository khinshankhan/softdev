//the svg
var c = document.getElementById("svg_id");

//clear function
var clear = function (e) {
    while(c.hasChildNodes()){
	c.removeChild(c.firstChild);
    }
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

//draws the dot node + connects to last one if possible]
var draw = function (e) {
    //get coordinates with offset
    var x = e.offsetX;
    var y = e.offsetY;
    //get the color
    color = document.getElementById("colors").value;
    c1 = make_svg("circle");
    c1.setAttribute("cx", x);
    c1.setAttribute("cy", y);
    c1.setAttribute("r", "50");
    add_svg(c1);
};
