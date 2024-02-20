#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const jsonData = JSON.parse(body);
    const UsersCompletedTasks = {};

    for (let i = 0; i < jsonData.length; i++) {
      const key = jsonData[i].userId;

      if (jsonData[i].completed === true) {
        if (!(key in UsersCompletedTasks)) {
          UsersCompletedTasks[key] = 1;
        } else {
          UsersCompletedTasks[key]++;
        }
      }
    }
    console.log(UsersCompletedTasks);
  }
});
