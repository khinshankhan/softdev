//the svg + some attributes
var c = document.getElementById("svg_id");
var width = c.getAttribute("width");
var height = c.getAttribute("height");

//clear function
var clear = function () {
    // clear nodes
    while(c.hasChildNodes()){
	c.removeChild(c.firstChild);
    }
};
//connect clear fxn to button
cl.addEventListener('click', clear);

//makes svg elements
var make_svg = function(element){
    return document.createElementNS( "http://www.w3.org/2000/svg", element);
};

//add an svg element to the svg html
var add_svg = function(element){
    c.appendChild(element);
};

//remove an svg element to the svg html
var delete_svg = function(element){
    c.removeChild(element);
};

var make_circle = function(e) {
    var elem = make_svg("circle");
    var cx = elem.setAttribute("cx", e.offsetX);
    var cy = elem.setAttribute("cy", e.offsetY);
    elem.setAttribute("r", 25);
    elem.setAttribute("fill", "#800000");
    //console.log("x "+cx+" y "+cy);
    elem.addEventListener("click", change_colors, true);
    add_svg(elem);
};

var change_colors = function(e) {
  this.setAttribute("fill", "#00ACAC");
  this.addEventListener("click", delete_circle, true);
  e.stopPropagation();
};

var delete_circle = function(e) {
    delete_svg(e.target);
    var elem = make_svg("circle");
    var randcx = Math.floor(Math.random() * (width - 100)) + 50;
    var randcy = Math.floor(Math.random() * (height - 100)) + 50;
    elem.setAttribute("cx", randcx);
    elem.setAttribute("cy", randcy);
    elem.setAttribute("r", 25);
    elem.setAttribute("fill", "#800000");
    elem.addEventListener("click", change_colors, true);
    add_svg(elem);
};

c.addEventListener("click", make_circle);
