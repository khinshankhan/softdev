//global variables use with multiple functions
var names = ["Deficit Percent", "Deficit Amount", "GDP", "Total Debt"];
var chart = d3.select(".chart");
var bar = chart.selectAll("div");
var barUpdate = bar.data(names);
var barEnter = barUpdate.enter().append("div");

var year;

//2018
var data1 = { deficit_percent: -2.3,
              deficit_amount: -392,
              gdp: 17.4,
              totalDebt: 18};
//2017
var data2 = { deficit_percent: -2.6,
              deficit_amount: -443,
              gdp: 17,
              totalDebt: 17.7};

//initialize set up
var initial = function(e){
    year = null;
    //get graph ready
    barEnter.text(function(d) { return d; });
    update();
};

//gets the new year + will run other functions to change graph
var update = function(e){
    //rewrote without query
    //year = document.querySelector('input[name="year"]:checked').value;
    var radios = document.getElementsByName('year');
    var BreakException = {};
    try {
	radios.forEach(function(elem) {
	    if (elem.checked){
		year = elem.value;
		throw BreakException;
	    }
	});
    } catch (e) {
	if (e !== BreakException) throw e;
    }
    
    graphBind(year);
};

//redo the graph
var graphBind = function(y){
    datawanted = null;
    //set data based on radio button
    switch(y) {
    case '2018':
        datawanted = data1;
        break;
    case '2017':
        datawanted = data2;
        break;
    }
    //gets just the nums needed
    var data = [];
    
    for (var key in datawanted) {
	if (datawanted.hasOwnProperty(key)) {           
            //console.log(key, datawanted[key]);
	    data.push(datawanted[key]);
	}
    }
    //console.log(data);
    changeGraph(data);
};

var changeGraph = function(data){
    i = -1;
    //transition in 3 sec
    barEnter.transition().duration(3000).style("width", function(d) {
	i += 1;
	//console.log(data[i]);
	return data[i] * 40 + "px"; });
};

//event listener for update
years.addEventListener("click",update);
//run setup at the very start
initial();
