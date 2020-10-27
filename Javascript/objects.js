// Objects in JS are like dictionary in Python

let student = {
    first:'Avijeet',
    last:'Singh',
    age:32, 
    height:173, 
    studentinfo: function(){                
        return this.first + '\n' + this.last;
    }
};

console.log(student);
console.log(student.first); // to access the first values pass the first key with dot notation
console.log(student["last"]); // or you can use this
student.first = 'Avi';
console.log(student);
student.age++; // increments the age by 1
console.log(student.studentinfo());
