// Declaring a string

let punjabi_greeting ='Hello paaji kiddan?';
let english_greeting='Hello, how are you?;'

//string manipulation

console.log(punjabi_greeting.charAt(7)); //returns the location of the character mentioned
console.log(punjabi_greeting.slice(1,4)); //slices the string and return the characters between the index mentioned
console.log(english_greeting.split(',')); //splits the characters w.r.t the conditon passed and returns a object(list)
console.log(english_greeting.split('')); //
console.log(english_greeting.length); //returns the length of the string
console.log(english_greeting.toUpperCase()); //returns the same string but in uppercase
console.log(english_greeting.concat(punjabi_greeting)); //concatenates the two string (str1 +str2)