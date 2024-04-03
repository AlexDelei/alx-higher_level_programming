#!/usr/bin/node

const req = require('request');

function countMovies (apiUrl) {
  const charId = 18;
  let cnt = 0;

  req(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    const data = JSON.parse(body);
    data.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)) {
        cnt++;
      }
    });
    console.log(cnt);
  });
}

function main () {
  const apiUrl = process.argv[2];
  if (!apiUrl) {
    console.error('Please provide the API url');
    process.exit(1);
  }
  countMovies(apiUrl);
}

main();
