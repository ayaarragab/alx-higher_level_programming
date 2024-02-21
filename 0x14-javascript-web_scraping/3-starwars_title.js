#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[0];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    try {
      const data = JSON.parse(body);
      console.log(data.title);
    } catch (err) {
      console.log(err);
    }
  }
});
