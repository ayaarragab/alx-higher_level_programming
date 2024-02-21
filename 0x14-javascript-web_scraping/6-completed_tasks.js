#!/usr/bin/node
// This script lists all tasks that are completed

request = require("request");
args = process.argv.slice(2);
empty = {};


request(args[0], function(error, response, body){
    if (error) {
	console.log(error);
    }
    for (let i = 0; i < JSON.parse(body).length; i++) 
        if (JSON.parse(body)[i].completed == 'true') {
        empty[i] = JSON.parse(body)[i].userId;
    }    
});
console.log(empty);
