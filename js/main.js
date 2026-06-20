// const age = 21;
// {
//   console.log(`I am ${age}!`);
// }

// const greetUser = (cName) => {
//   return `Hello ${cName}!`;
// };

// greetUser("Adrian");

// const multiply = (num1, num2) => {
//   return num1 * num2;
// };

// multiply(6, 7);

// const isAdult = (age) => {
//   if (age >= 18) return true;
//   else return false;
// };

// isAdult(16);

// const sumArray = (numbers) => {
//   total = 0;
//   for (const number of numbers) {
//     total += number;
//   }
//   return total;
// };
// sumArray([1, 2, 3, 4, 5]);

// const getLastItem = (item) => {
//   const lastItem = item.at(-1);
//   return lastItem;
// };

// getLastItem(["one", "two", "three"]);

// const reverseString = (reversed) => {
//   const reverseWord = reversed.split("").reverse().join("");
//   return reverseWord;
// };

// reverseString("HELLO");

// const btn = document.querySelector("#btn");

// const greetUser = (uName) => {
//   return `Hello ${uName}!`;
// };

// greetUser("Adrian");

// const multiply = (num1, num2) => {
//   return num1 * num2;
// };

// console.log(multiply(6, 7));

// const isAdult = (age) => {
//   if (age >= 18) return true;
//   else return false;
// };

// console.log(isAdult(12));

// const sumArray = (numbers) => {
//   let total = 0;
//   for (const number of numbers) total += number;
//   return total;
// };

// console.log(sumArray([1, 2, 3, 4, 5]));

// const getLastItem = (numbers) => {
//   const lastNumber = numbers.at(-1);
//   return lastNumber;
// };

// console.log(getLastItem(["one", "two", "three"]));

// const reverseString = (word) => {
//   const reversedWord = word.split("").reverse().join("");
//   return reversedWord;
// };

// console.log(reverseString("HELLO"));

// const log = document.getElementById("log");
// const outer = document.getElementById("outer");
// const inner = document.getElementById("inner");
// const button = document.getElementById("btn-propagate");

// const outerClick = (e) => {
//   log.textContent += " Outer clicked | ";
//   //   e.stopPropagation();
// };
// const innerClick = () => {
//   log.textContent += " Inner clicked | ";
// };

// const buttonClick = (e) => {
//   log.textContent += " Button clicked |";
//   //   e.stopPropagation();
// };
// outer.addEventListener("click", outerClick, { capture: true });
// inner.addEventListener("click", innerClick);
// button.addEventListener("click", buttonClick);
