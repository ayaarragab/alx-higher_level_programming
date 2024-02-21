#!/usr/bin/node
// This script lists all tasks that are completed

const request = require('request');
const args = process.argv.slice(2);
const empty = {};

request(args[0], function (error, _, body) {
  if (error) {
    console.log(error);
  }
  const tasks = JSON.parse(body);
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed === true) {
      if (empty[tasks[i].userId]) {
        empty[tasks[i].userId]++;
      } else {
        empty[tasks[i].userId] = 1;
      }
    }
  }
  console.log(empty);
});
