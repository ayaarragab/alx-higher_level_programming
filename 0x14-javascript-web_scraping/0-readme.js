#!/usr/bin/node
// This is a simple example of reading a file using the fs module.
const fs = require('node:fs');
const args = process.argv;
fs.readFile(args[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
