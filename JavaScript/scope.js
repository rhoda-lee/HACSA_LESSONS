/* 
let, var, const
Used to create local variables but can be used to create global variables

Global and Local variables
A local variable is a variable that is accessible withing the scope or block of code it was declared
A global variable is accessible outside the scope of ots declaration

declare variables with let instead of var
var is an old way of declaring variables and is not as efficient

const
This is used to create variables whose values can not be changed again
*/



//DATA TYPES

//String
let myString = 'This is my string value'
console.log(myString)

// Integer
let myInt = 7
console.log(myInt)

// BigInt : They are valuable addition to js that is meant to handle numbers that exceep what the number data type can handle
const bigNumber = 456n
console.log(typeof(bigNumber))

// Float
const PI = 3.14
console.log(PI)

// Undefined variables
let user 
console.log(user)   // should return undefined
console.log(typeof(user))

//Null
const job = null
console.log(job)

/* Complex structures and hold more sophisticated values that primitive data type
they are immutable */
//Arrays





// Objects
const person = {
    firstName: 'Habiba',
    lastName: 'Adam',
    age: 24
}
console.log(typeof(person))

// It is comples because inside the object can be different datatypes and the 