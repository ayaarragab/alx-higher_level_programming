#!/usr/bin/node
// Write a script that prints all characters of a Star Wars movie:
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const filmId = process.argv.slice(2)[0];

request(url, function (error, _, body) {
  if (error) {
    console.log(error);
  }
  const films = JSON.parse(body).results;
  for (const film of films) {
    if (film.episode_id === Number(filmId)) {
      for (const character of film.characters) {
        request(character, function (error, response, body) {
          if (error) {
            console.log(error);
          }
          console.log(JSON.parse(body).name);
        });
      }
    }
  }
});
