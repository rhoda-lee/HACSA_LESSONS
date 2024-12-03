/* Arrays are denoted by square brackets []
*/
const fruits = ['Banana', 'Mango', 'Apple', 'Pear']

// Array indexing
console.log(fruits[3])

const movies = []
movies[0] = 'John Wick'
movies[1] = 'What happened to Monday'
movies[2] = 'Dungeons and Dragons'

console.log(movies)

// New Array
const series = new Array('YOU', 'The 100', 'Arcane', 'Merlin')
console.log(series)

series[3] = 'Vikings'
console.log(series)


// Array methods
// .length: return length or sixe of an array (like len() in python)
console.log(fruits.length)

// .toString(): converts an array to a string
console.log(fruits.toString())

// print element based on its index
console.log(fruits.at(2))

// sort(): sorts in alhabetical or ascending order of magnitude. This modifies the original array
console.log(fruits.sort())
console.log(fruits)

// toSorted: does not modify the original array
console.log(fruits.toSorted())

// .reverse(): Used to reverse an array bottom up
console.log(series.reverse())

// .join: Converts array to string and specify the delimeter or seperator
console.log(fruits.join('-'))

// .pop()
const popped = movies.pop()
console.log(movies)

// .shift(): removes the first element of an array
movies.shift()
console.log(movies)

// .unshift(): Adds an element at the beginning of an array and shifts the older element
series.unshift('Avatar')
console.log(series)

// .flat() flatening an array means to reduce the dimentionality of an array
const myArray = [[1, 2], [3, 4], [5, 6]]
const flattendArr = myArray.flat()
// console.log(flattendArr)

// push(): adds element to end of an array
movies.push('Squid Games')
console.log(movies)

// Array.isArray('Array-name) : Check type of an array
console.log(Array.isArray(movies))

//.concat(): concatenates two arrays
const myGirls = ['Cecilie', 'Lone']
const myBoys = ['Emil', 'Tobias', 'Linus']

const myKids = myGirls.concat(myBoys)
console.log(myKids)



