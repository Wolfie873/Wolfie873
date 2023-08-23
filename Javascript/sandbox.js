/* Chapter 1

//Variables can be let and const, as well as var. Var is the older way that is still supported but being phased out in modern javascript. Older browsers do notsuppor let and const
let age = 31;
let year = 1991;
 
//Console logs wll only write information visible to the console
console.log(age, year);

//
age = 339;

console.log(age,year);

const points = 2293389;

console.log(points);

var score = 32;

console.log(score);

let fullName = "JorgeOertizDiaz";

console.log(fullName);

console.log(fullName.length);
console.log(fullName.toUpperCase());

// $age - yes
// 5age - no

// Javascript data types:

// String
// Number
// Boolean
// null
// undefined
// Object
// Symbol
*/

/* Chapter 2 Strings
//string concatenation

let firstName = 'Jorge';
let lastName = 'Ortiz';

let fullName = firstName + ' ' + lastName;

console.log(fullName);

//getting characters
console.log(fullName[3]);

//string length
console.log(fullName.length);

//string methods
console.log(fullName.toUpperCase());
let result = fullName.toLowerCase();
*/

/* Chapter 3 Numbers

// math operators +, -, *, /, **, %
let radius = 10;
const pi = 3.14;

console.log(10/2);
let result = radius % 3;

console.log(result);

//order of operations - B I D M A S / PEMDAS español

let like = 10;

likes = like + 1;
console.log(likes);

likes++;
console.log(likes);

likes += 10;
console.log(likes);

likes -= 15;
console.log(likes);

//NaN - not a number
//concatenate numbers

let resultC = "the blog has " + likes + " likes!";

console.log(resultC);

//template strings
const title = "Best reads of 2019";
const author = "Mario";
const likesw = 30;


let resultw = `The blog called ${title} by ${author} has ${likesw} likes`;
console.log(resultw);
*/

/* Chapter 4 Arays*/

let ninjas = ['shaun', 'ryu', 'chun-lee'];

console.log(ninjas[1])