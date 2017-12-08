var add = function(e){
    var ol = document.getElementById("thelist");
    var li = document.createElement("li");
    var num = document.getElementsByTagName("li").length;
    li.innerHTML = "item " + num;
    ol.appendChild(li);
};

var button = b.addEventListener('click', add);

var change = function(e){
    var position = this;
    console.log(position);
};

var head = ol.addEventListener('hover', change);
