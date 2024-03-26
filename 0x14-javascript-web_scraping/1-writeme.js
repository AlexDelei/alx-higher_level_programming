#!/usr/bin/node

const fs = require('fs');
const [, , fileTo, stringTo] = process.argv;

fs.writeFile(fileTo, stringTo, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
