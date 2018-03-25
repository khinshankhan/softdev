//global variable use with multiple functions
var year;

var data1 = { year: 2018,
              deficit_percent: -2.3,
              deficit_amount: -392,
              gdp: 17.4,
              totalDebt: 18};
var data2 = { year: 2017,
              deficit_percent: -2.6,
              deficit_amount: -443,
              gdp: 17,
              totalDebt: 17.7};

//gets the new year + will run other functions to change graph
var update = function(e){
    year = document.querySelector('input[name="year"]:checked').value;
    console.log(year);
};

//event listener for update
years.addEventListener("click",update);
//run update at the very start
update();
