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

// Rest Parameters
/* Rest Parameters allow us to pass an infinite amount arguments during function calls
They bundle the arguments into an array, hence returning an array
*/

function doSomething(num1, ...otherNums) {
    console.log(num1);
    console.log(otherNums);
}

doSomething(3, 4, 5, 6, 7, 8, 9)

function restParam (...arg) {
    // console.log(arg);
    for (const num of arg) {
        console.log(num * 2)
    }
}

restParam(1, 2, 3, 4, 5, 6, 7, 8, 9);

// Rest Parameter in an anonymous function
const anonymousRest = function (...arg) {
    for (const num of arg) {
        console.log(num * 3);
    }
}
anonymousRest(3, 6, 9, 12, 15);

const arrowRest = (...arg) => {
    for (const num of arg) {
        console.log(num + 2);
    }
}
arrowRest(1, 2, 3, 4, 5, 6, 7, 8);

const randomArrow = (num) => num * num
const res = randomArrow(10)
console.log(res)

// Nested Functions
/* Functions within a function */
function outer() {
    console.log("Outer");
    function inner() {
        console.log("Inner");
    }
    inner();
}
outer();


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

/* forEach() function
This is an array function that executes a callback function onn each of its array elements
Unlike the map function, the forEach function does not return a new array and 
does not modify the original array either
Instead it iterates through the elements of an array and performs an operation on each of them
*/

// forEach()
// const namesOfPeople = ['prissy', 'rhoda', 'jedidah', 'saida', 'delicious']
// const names = namesOfPeople.forEach(
//     (name) => console.log(name)
// )
// console.log(names)

// Modifying Array with forEach()
const names = ['prissy', 'rhoda', 'jedidah', 'saida', 'delicious']
let upperNames = []

names.forEach(
    (name) => {
        const upper = name.toUpperCase()
        upperNames.push(upper)
    }
)
console.log(upperNames)

// filter() Function
// It is an arry method used to filter off methods that meet a condition

const countries = ['Ghana', 'Nigeria', 'UK', 'Netherlands', 'USA', 'Norway', 'Uruguay', 'Uganda']
const countWithNorU = countries.filter(
    (country) => {
        return country.startsWith('N') || country.startsWith('U')
    }
)
console.log(countWithNorU)

// Countries that start with 'U'
const countries2 = ['Ghana', 'Nigeria', 'UK', 'Netherlands', 'USA', 'Norway', 'Uruguay', 'Uganda']
const countWithU = countries2.filter(
    (country) => country.startsWith('U')

)
console.log(countWithU)

// Reduce()
/* This reduces an array to a single value/ 
It iterates through an array, performs a function on each element and returns a single value. 
The method takes a callback function with two parameters representing 2 elements in the array.
The callback function then performs an action starting from the first element in the array.
Say you have an array of points for variouss participants:
*/

const participantPoints = [10, 20, 30, 40, 50]

const sumOfPoints = participantPoints.reduce(
    (a, b) => a + b
)

console.log(sumOfPoints)

const sentence = ['this', 'is', 'the', 'backend', 'class']

const fullSentence = sentence.reduce(
    (a, b) => a + ' ' + b
)
console.log(fullSentence)

const sentence2 = ['this', 'is', 'the', 'backend', 'class']

const fullSentence2 = sentence2.reduce(
    (a, b) => {
        return sentence2.join(' ')
    }
)
console.log(fullSentence2)

// find()
// It returns the first element in an array that meets a condition

const findPrissy = names.find(
    (name) => name === 'prissy'
)

console.log(findPrissy)

/* research on:
some()
includes()
findIndex()
every() */