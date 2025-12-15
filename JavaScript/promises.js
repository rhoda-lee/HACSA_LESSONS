/*
How Promises are made in Javascripts
    They are made or created using the promise constructor which takes in a single function as an argument.
    That function is called the executor function.
    The executor function is responsible for executing the asynchronous operation.
    The executor function takes in 2 other argumnts and they are called resolve and reject.
    The resolve is called when the asynchronous operation is successful and the reject function is called when the operation fails.
    When the promise is initiated its in the pending state.
*/

// Promise

// let myPromise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//         resolve('Data retrieved successfully')
//     }, 5000)
// })

// // Handling the result of a promise: register a handler: .then() method: this takes a function as an argument
// // which is called when the promise is fulfilled. resolve() works with .then()
// myPromise.then((value) => {
//     console.log(value)
// })

// let promise2 = new Promise((resolve, reject) => {
//     setTimeout( () => {
//         reject('An error occured')
//     }, 2000)
// })

// Handling the results of a failed promise: register handler : .then()

// promise2.then( (value) => {
//     console.log(value)
// }).catch( (error) => {
//     console.log(error)
// })

// A function that has a promise and the function will be successful when 
// the sum has a value greater than ten(10), failing otherwise

// let doSomeMath = (a, b) => {
//     return new Promise( (resolve, reject) => {
//         const result = a + b
//         if (result > 10) {
//             resolve(result)
//         }
//         else {
//             reject('Sum was less than 10')
//         }
//     })
// }
// // Promise Handler

// // doSomeMath(10, 5).then( (result) => {
// //     console.log(result)
// // }).catch( (error) => {
// //     console.log(error)
// // })

// // OR
// doSomeMath(3, 5).then((value) => console.log(value))
// .catch((error) => console.log(error))


// Trad Way
function doTradmath (a, b) {
    return new Promise (function (resolve, reject) {
        const result = a + b
        if (result > 10) {
            resolve(result)
        } else {
            reject('Sum was less than 10!')
        }
    })
}

// // Promise Handler

// // doSomeMath(10, 5).then( (result) => {
// //     console.log(result)
// // }).catch( (error) => {
// //     console.log(error)
// // })

// Create a new promise that regenerates a random number between 0 and 1
// if the number is 0, it is resolved with message 'Resolved successfully'
// If number is 1, it is rejected with message 'Number was not 0'
// Handle this promise gracefully with .then() and .catch

let generateNumber = () => {
    return new Promise( (resolve, reject) => {
        const num = Math.floor(Math.random() * 2)
        console.log(num)
        if (num == 0) {
        resolve('Resolved Successfully!')
        } 
        else if (num == 1) {
            reject('Number was not 0')
        }
        else {
            console.log('You are lost')
        }
    })
}

generateNumber().then( (num) => {
    console.log(num)
}).catch( (error) => {
    console.log(error)
})