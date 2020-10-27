let fruits = ['apple','kiwi','banana'];
let vegetables = ['brocoli','kale','asparagus'];
console.log(fruits);
console.log(fruits.join(' * ')); // joins the valur of the strings with the condition passed
console.log(fruits.toString()); // converts the array into a string
fruits.pop(); // removes the last value in the array
console.log(fruits);
fruits.push('Banana');// adds the value given to the last in the array
console.log(fruits);
console.log(fruits[2]); // returns the value on the given index
fruits[3] = 'orange';
console.log(fruits);
fruits.shift(); // removes first item
fruits.unshift('Apple'); // add item to the first index

let all_groceries = fruits.concat(vegetables); // concates two arrays
console.log(all_groceries);

let some_numbers = [34,2,3,56,23,6,8,3,4,3,9];
console.log(some_numbers.sort()); // this does not sort as you want for numbers but for strings it does 
console.log(some_numbers.sort(function(a,b) {return a-b})); // sorting in ascending order
console.log(some_numbers.sort(function(a,b) {return b-a})); // sorting in descending order

let empty_array = [] ;
// or you can also pass an empty array as following
let emptyArray = new Array();

for(let num =0; num < 10; num++){ 
    emptyArray.push(num);
}
console.log(emptyArray);

