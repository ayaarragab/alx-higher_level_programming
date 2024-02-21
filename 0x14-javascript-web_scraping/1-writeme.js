#!/usr/bin/node
// This is a simple example of reading a file using the fs module.
const fs = require('node:fs');
const args = process.argv;
fs.writeFile(args[2], args[3], 'utf8', err => {
  if (err) {
    console.error(err);
  }
});
