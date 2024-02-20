#!/usr/bin/node
const request = require('request');

const api = 'https://swapi-api.alx-tools.com/api/films/';
arg = parseInt(process.argv[2])
const MovieId = function () {
  if (arg != 0) {
    return arg - 1;
  } else {
    return 0;
  }
}

request(api, function (err, response, body) {
  if (err == null) {
    const JsonObj = JSON.parse(body)
    const cast = JsonObj.results[MovieId()].characters
    for (let i = 0; i < cast.length; i++) {
      request(cast[i], function (err, response, body) {
        if (err == null) {
          const CharacterObj = JSON.parse(body);
          console.log(CharacterObj.name)
        }
      })
    }

  }
});
