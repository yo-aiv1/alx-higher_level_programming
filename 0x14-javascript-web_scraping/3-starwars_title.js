#!/usr/bin/node
const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
request(api, function (err, response, body) {
  if (err == null) {
    const jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
