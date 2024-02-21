#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv.slice(2)[0];

request(url, function (error, _, body) {
  if (error) {
    console.log(error);
  }
  for (const character of JSON.parse(body).characters) {
    request(character, function (error, response, body) {
      if (error) {
        console.log(error);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
