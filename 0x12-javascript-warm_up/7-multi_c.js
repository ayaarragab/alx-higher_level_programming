#!/usr/bin/node

const args = process.argv;

if (Number.isInteger(parseInt(args[2]))) {
  for (let index = 0; index < parseInt(args[2]); index++) {
    console.log('C is fun');
  }
} else {
    console.log('Missing number of occurrences');
}
