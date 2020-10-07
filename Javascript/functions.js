// This is how we create a funciton in js

function fun() {
    console.log("you created a function");
}

//calling a function

fun()

//Passing arguments in the functions

function greeting(yourName) {
    var result = 'Hello ' + yourName; // This is called string concatenation
    console.log(result);
}
var name = prompt('What is your name?');
greeting(name)