#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (a <= 1 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(parseInt(args[2])));
