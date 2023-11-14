#!/usr/bin/node

const args = process.argv.slice(2); // Exclude the first two elements (node and script name)

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(Number); // Convert arguments to numbers
  const sortedNumbers = numbers.sort((a, b) => b - a); // Sort numbers in descending order
  console.log(sortedNumbers[1]); // Print the second element, which is the second biggest number
}
