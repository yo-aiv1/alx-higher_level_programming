const request = require('request');

request(process.argv[2], function (err, response) {
  if (err == null) {
    console.log('code: %d', response.statusCode);
  }
});
