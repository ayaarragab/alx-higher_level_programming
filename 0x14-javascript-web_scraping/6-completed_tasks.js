#!/usr/bin/node
// This script lists all tasks that are completed

request = require("request");
args = process.argv.slice(2);

request(args[0], function(error, response, body){
    if (error) {
	console.log(error);
    }
    console.log(body);
})
