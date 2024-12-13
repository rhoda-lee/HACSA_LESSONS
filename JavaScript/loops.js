// For Loops
/* Allows for more control over the iteration process
With the for loop, we can add conditions and directly manipulate elements in an array rather
than returning a new array.
Three parts of a for loop:
    1. The initialization:
    This where we declare a value and set it to a starting value

    2. The Condition:
    This is a boolean expression that determines the number of times that a loop will run and when it stops.
    Without a condition the loop runs indefinitely

    3. Final Expression:
    This is where we increment or decrement the final variable
*/

// Loop through with a for loop
let numbers = [1, 2, 3, 4, 5, 6]

for (let i = 0; i < numbers.length; i++) {
    numbers[i] *= 2
}

console.log(numbers)


// Write a for loop to return a squared number of any number in the numbers list
let numbers2 = [1, 2, 3, 4, 5, 6]

for (let i = 0; i < numbers2.length; i++) {
    numbers2[i] *= numbers2[i]
}

console.log(numbers2)

// continue and break keywords

for (let i = 0; i <= 10; i++) {
    if (i === 5) {
        continue
    }
    console.log(i)
}

for (let i = 0; i <= 10; i++) {
    if (i === 5) {
        break
    }
    console.log(i)
}


// in operator/keyword: Mostly used for Objects
/* Used to check if a specified property is in an object */

let student = {
    name: 'Talatu',
    age: 19,
    class: 'Backend Class'
}

if ('Talatu' in student) {
    console.log('There is a name property in student')
}

for (let key in student) {
    console.log(`${key}: ${student[key]}`)
}

for (let j of numbers) {
    j *= j
    console.log(j)
}

// while loops
let dieRoll = 0

while (dieRoll != 6) {
    dieRoll = Math.ceil(Math.random() * 6)
    console.log(`You rolled ${dieRoll}`)
}


