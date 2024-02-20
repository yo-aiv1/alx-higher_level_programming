#!/usr/bin/node
const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
request(api, function (err, response, body) {
  if (err == null) {
    const JsonObj = JSON.parse(body);
    for (let i = 0; i < JsonObj.characters.length; i++) {
      request(JsonObj.characters[i], function (err, response, body) {
        if (err == null) {
          const cast = JSON.parse(body);
          console.log(cast.name);
        }
      });
    }
  }
});
