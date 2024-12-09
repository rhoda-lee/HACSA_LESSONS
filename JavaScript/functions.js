// Create a function that takes in a number and divides it by 2

function division(num) {
    let result = num / 2;
    return result
}

console.log(division(6))


// Write a function that adds two numbers and returns the sum

function add(num1, num2) {
    let result = num1 + num2;
    return result
}

console.log(add(3, 5))

// Using isNan

function multiplyByTwo(num) {
    if (isNaN(num)) {
        return 'Value must be a number'
    }
    const result = num * 2
    return result
}

// Anonymous funtions: They are funtions without names. To call them, store them in a variable
// This is a function expression: storing the nameless function in a variable
const anonymous = function () {
    console.log('I am a function and I am anonymous')
}
console.log(anonymous())
// This returns undefined because it does not have a return statement

// Write an anonymous function to do anything

const greeting = function (name, isDay) {
    if (isDay == 'True') {
        return `Hello ${name}, good morning`
    }
    return `Hello ${name}, good evening`
}

console.log(greeting('Rhoda', 'False'))

/* Arrow functions are also called fat arrow or lambda funtions
Short hand way of writing funtion expressions in JavaScript. */

// Traditional Way of Functions
function squaredNumber(num) {
    return num * num
}

console.log(squaredNumber(10))

// An Arrow Function
const sqrNumber = (num) => num * num;

console.log(sqrNumber(3))

// Also
const sqrNumberArrow = (num) => {
    return num * num
}

console.log(sqrNumberArrow(2))

// They are a build up for callback functions

// Write an arrow function that adds two numbers

const addNumbers = (num1, num2) => num1 + num2
console.log(addNumbers(3, 7))


// Write an arrow function to divide a number by 2
const divideByTwo = (num) => {
    return num / 2
}
console.log(divideByTwo(68))

/* They are useful when yu need to write a function to take another function as a parameter. 
When another function is taken as a parameter is called a call back 
and the parent that takes a function as a parameter is a Higher Order Function 
They are mostly used to manipulate arrays and implement higher order tasks*/

/* 
.map()
This is a higher order function we can use that takes in a callback function as an argument.
The callback function is applied to each element in the array.
After, the map function returns a new array with the result of the callback function
applied to each element in the array.
*/

// Map() Function
const numbers = [1, 4, 5, 6, 7]

const squaredArray = numbers.map(
    (number) => number * number
)

const words = ['this', 'is', 'a', 'great', 'day']

const capitalizeWords = words.map(
    (word) => word.toUpperCase()
)

console.log(squaredArray)
console.log(capitalizeWords)

// Map() Function to divide number in array by 2

const numArray = [2, 4, 56, 22, 67, 90]

const divByTwo = numArray.map(
    (num) => num / 2
)
console.log(divByTwo)
