#!/usr/bin/node

const req = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode !== 200) {
    console.log(`Ooops: ${response.statusCode}`);
  } else {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
