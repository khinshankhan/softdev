var head;

//adds new item to list when button is pressed
var add = function(e){
    var ol = document.getElementById("thelist");
    var li = document.createElement("li");
    var num = ol.getElementsByTagName("li").length;
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
    var ol = document.getElementById("thelist");
    var num = ol.getElementsByTagName("li").length;
    var list = ol.getElementsByTagName("li");
    for(var i = 0; i < num; i++){ 
	//console.log(list[i]);
	addlisteners(list[i]);
    }
};

//gets nth fibonacci number
var fibonacci = function(n){
    if (n==0) return 0;
    if (n<2) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
};

var fib = function(e){
    var ol = document.getElementById("list2");
    var li = document.createElement("li");
    var num = ol.getElementsByTagName("li").length;
    console.log(num);
    li.innerHTML = fibonacci(num);
    ol.appendChild(li);
};

//connects fib_b button to fibonacci
var button2 = fib_b.addEventListener('click', fib);

var golden = function(n){
    return fibonacci(n+2) + "/" + fibonacci(n+1);
};

var goldList = function(e){
    var ol = document.getElementById("listy");
    var li = document.createElement("li");
    var num = ol.getElementsByTagName("li").length;
    li.innerHTML = golden(num);
    ol.appendChild(li);
};

var button3 = goldenboi.addEventListener('click', goldList);

console.log(golden(0));
console.log(golden(1));
console.log(golden(2));
console.log(golden(3)); 

listenerstolist();
