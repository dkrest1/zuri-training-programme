// a simple function to build a
console.log(
  "welcome, this is a simple calculator that perform addition, subtraction, division and multiplication operation"
);

let operation = prompt(
  "please enter the operation you want to perform (+, -, * or /): "
);

// result to be display
let result;

// input your number
let number1 = prompt("enter yoour first number: ");
let number2 = prompt("enter yoour second number: ");

// comdition to carry out operation
if (operation == "+") {
  result = number1 + number2;
} else if (operation == "-") {
  result = number1 - number2;
} else if (operation == "*") {
  result = number1 * number2;
} else {
  result = number1 / number2;
}

// display final result to the console
console.log(`${number1}  ${operation} ${number2} = ${result}`);
