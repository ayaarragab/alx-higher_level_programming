#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');
const url = process.argv.slice(2)[0];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  }
  const films = JSON.parse(body).results;
  let count = 0;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.endsWith('/18/')) {
        count++;
      }
    }
  }
  console.log(count);
}
);
