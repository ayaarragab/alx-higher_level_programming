#!/usr/bin/node

const args = process.argv;
let x = '';
if (Number.isInteger(parseInt(args[2]))) {
  for (let index = 0; index < parseInt(args[2]); index++) {
    x += 'X';
  }
  for (let index = 0; index < parseInt(args[2]); index++) {
    console.log(x);
  }
} else {
  console.log('Missing number size');
}
