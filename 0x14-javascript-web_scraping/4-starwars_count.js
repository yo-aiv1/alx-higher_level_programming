#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const data = JSON.parse(body);

    let count = 0;
    for (let i = 0; i < data.results.length; i++) {
      for (let j = 0; j < data.results[i].characters.length; j++) {
        const character = data.results[i].characters[j];
        if (character.slice(-4) === '/18/') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
