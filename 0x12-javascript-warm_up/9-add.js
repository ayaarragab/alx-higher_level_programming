#!/usr/bin/node

const args = process.argv;

if (!args[3]) {
  console.log(NaN);
} else {
  add(args[2], args[3]);
}
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
