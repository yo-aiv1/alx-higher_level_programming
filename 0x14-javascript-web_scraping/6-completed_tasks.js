#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const jsonData = JSON.parse(body);
    const UsersCompletedTasks = {};

    for (let i = 0; i < jsonData.length; i++) {
      const key = jsonData[i].userId;
      if (!(key in UsersCompletedTasks)) {
        UsersCompletedTasks[key] = 0;
      }

      if (jsonData[i].completed === true) {
        UsersCompletedTasks[key]++;
      }
    }
    console.log(UsersCompletedTasks);
  }
});
