/* Asynchronous Javascript
1.JS timing methods:
They are higher order functions that allow us to schedule execution of functions at a 
later time or at regular intervals

Examples
a. SetTimeOut:
Allow us to shcedule the execution of a function after a sepcified number of miliseconds.
It takes in 2 arguments ie: 
the function to be executed and the num of miliseconds to wait before executing the function
It retruns a timer id it assigns to every timer.This id can be used to clear or cancel times

*/

// setTimeout expample. Definig a function
// const displayMessage = () => {
//     console.log('Welocome to Async Javascript')
// }
// setTimeout(displayMessage, 2000)


// // Using the setTimeout as an Anonymous func.This is the normal way
// setTimeout(() => {
//     console.log('This is a setTimeout as a higher order func')
// }, 5000)




// b. clearTimeOut: It return a

console.log('Start')
const timerId = setTimeout(() => {
    console.log('Welcome to Async JavaScript')
}, 5000)
// clearTimeOut
// clearTimeout(timerId)
console.log('End')


/* c. SetInterval:
Allows us to schedule the execution of a function at regular intervals.
Just like the setTimeOut() the setInterval takes in 2 args,
the function to be executed and the interval time in miliseconds

It also returns a timer id.
The id can be given to the clearInterval(): works like the clearTimeOut
*/

// setInterval()
// const intTimer = setInterval(() => {
//     console.log('Running every second')
// }, 1000)

// clearInterval(intTimer)


/* Asynchronous
Async JavaScript is an essential concept in mordern web development.
In traditional JavaScript, code runs syncromously,
meaming each line of code is executed one after the other, from top to bottom.
While this is okay for simple tasks, it becomes inefficient for long running operations like
querying a database, calling external APIs or reading or writing to files.

If such files were run synchronously, the event loop in node js would be blocked,
preventing it from handling incoming requests.
This could severely degrade the performance of a backend server,
especially in environents where multiple users make requests simultaneously.

The term asynchronous refers to a programming pattern where multiple tasks 
can be executed simultaneously without blocking each other
This is necessary for mordern web applications which is often needed to perform
multiple tasks at the same time.

The Event loop is a mechanism in JavaScript and other programming environments that allows
a program to handle asynchronous operations, while remaining single threaded
*/

/* Asynchronous code is handled with:
Callbacks, Promises and Async/Await
*/

/*
Promises
A promise is an object that represents the eventual completion or failure of an asynchronous operation.
It is like a placeholder for a value that wwill become available in the future or not.
A promise has 3 states:
    1. Pending
    It is the initial state of the promise specifying that the value is not yet available.

    2. Fulfilled
    It is the stae of the promise representing a successful operation,
    meaning the value is now available.

    3. Rejected
    The state of the promise representing a failed operation.

How Promises are made in Javascripts
    They are made or created using the promise constructor which takes in a single function as an argument.
    That function is called the executor function.
    The executor function is responsible for executing the asynchronous operation.
    The executor function takes in 2 other argumnts and they are called resolve and reject.
    The resolve is called when the asynchronous operation is successful and the reject function is called when the operation fails.
    When the promise is initiated its in the pending state.
*/