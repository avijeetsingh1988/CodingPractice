//Assigning values to a variable and printing them out
var b = 'smoothie';
console.log(b);

//Can also change the code on HTML page using javascript

document.getElementById('sometext').innerHTML='Changed this from Javascript';

//also you can get an input from the user and display
var age = prompt('How old are you?')
document.getElementById('sometext').innerHTML = age
// The row 11 will supersede row 7 and just display the output of row 11

//Data types in Javascript

let x= 20 ; // number
let y = 'string'; // string
let z = {first:'Avi',last:'G'}; // this is called an object in Javascript(something similar to to a dicitonary in python)
let truth = false; //boolean
let groceries = ['apple','banana','kiwi']; // this is called an array which is like a list in python
let f; //undefined
let nothing = null // value null

console.log(groceries[3]);