var head;

//adds new item to list when button is pressed
var add = function(e){
    var ol = document.getElementById("thelist");
    var li = document.createElement("li");
    var num = document.getElementsByTagName("li").length;
    li.innerHTML = "item " + num;
    ol.appendChild(li);
    listenerstolist();
};

//connects add to button
var button = b.addEventListener('click', add);

//changes the heading to be list item
var change = function() {
    var h = document.getElementById("h");
    h.innerHTML = this.innerHTML;
};

//reverts heading back to original
var revert = function() {
    var h = document.getElementById("h");
    h.innerHTML = head;
};

//removes item from list
var remove = function() {
    this.remove();
    revert();
};

//add all the listeners needed to each item
var addlisteners = function (item){
    var h = document.getElementById("h");
    if(head == (undefined || null)){
	//console.log(h);
	head = h.innerHTML;
    }
    item.addEventListener( "mouseover", change);
    item.addEventListener( "mouseleave", revert);
    item.addEventListener( "click", remove);
};

//goes over the list to add the listners
var listenerstolist = function(){
    var num = document.getElementsByTagName("li").length;
    var list = document.getElementsByTagName("li");
    for(var i = 0; i < num; i++){ 
	//console.log(list[i]);
	addlisteners(list[i]);
    }
};

listenerstolist();
