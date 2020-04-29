//global variables use with multiple functions
var names = ["$1 Trillion -- (for scale)", "Deficit", "GDP", "Total Debt"];
var chart = d3.select(".chart");
var pres = document.getElementById("pres");
var bar = chart.selectAll("div");
var barUpdate = bar.data(names);
var barEnter = barUpdate.enter().append("div");

var year;

var data1 = { year: 2018,
              president: 'Donald J. Trump',
              deficitAmount: 392,
              gdp: 17400,
              totalDebt: 18000};

var data2 = { year: 2017,
              president: 'Donald J. Trump',
              deficitAmount: 443,
              gdp: 17000,
              totalDebt: 17700};

var data3 = { year: 1991,
              president: 'George H. W. Bush',
              deficitAmount: 392,
              gdp: 8900,
              totalDebt: 5240};

var data4 = { year: 1945,
              president: 'Harry S. Truman',
              deficitAmount: 467,
              gdp: 2200,
              totalDebt: 2550};


//initialize set up
var initial = function(e){
  year = null;
  //get graph ready
  barEnter.text(function(d) { return d; });
  update();
};

//gets the new year + will run other functions to change graph
var update = function(e){
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
    if (e != BreakException) throw e;
  }

  graphBind(year);
};

//redo the graph
var graphBind = function(y){
  var datawanted = null;
  //set data based on radio button
  switch(y) {
  case '2018':
    datawanted = data1;
    break;
  case '2017':
    datawanted = data2;
    break;
  case '1991':
    datawanted = data3;
    break;
  case '1945':
    datawanted = data4;
    break;
  }
  //gets just the nums needed
  var data = [];

  data.push(1000);
  data.push(datawanted.deficitAmount);
  data.push(datawanted.gdp);
  data.push(datawanted.totalDebt);
  pres.innerHTML = datawanted.president;

  changeGraph(data);
};

var changeGraph = function(data){
  console.log(data);
  var i = -1;
  //transition in 2 sec
  barEnter.transition().duration(2000).style("width", function(d) {
    i += 1;
    return data[i] / 15 + "px";
  });
};

//event listener for update
years.addEventListener("click",update);
//run setup at the very start
initial();
