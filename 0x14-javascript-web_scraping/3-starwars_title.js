#!/usr/bin/node

// script that prints the title of a Star Wars movie

const request = require('request');
const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsUri, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
