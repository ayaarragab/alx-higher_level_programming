#!/usr/bin/node
/**
 * Write a script that gets the contents of a webpage and stores it in a file.
The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module request
*/

const request = require('request');
const url = process.argv.slice(2)[0];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const fs = require('fs');
  const filePath = process.argv.slice(2)[1];
  fs.writeFile(filePath, body, 'utf8', function (err) {
    if (err) {
      console.error(err);
    }
  }
  );
});
