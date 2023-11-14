#!/usr/bin/node
const args = process.argv;
function factorial (a) {
  if (a <= 1 || !a) {
    return 1;
  }
  return a * factorial(a - 1);
}
if (parseInt(args[2])) {
  console.log(factorial(parseInt(args[2])));
}
