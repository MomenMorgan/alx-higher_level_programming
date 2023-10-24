#!/usr/bin/node

// script that prints the title of a Star Wars movie

const Id = process.argv[2];

const req = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/'.concat(Id);

req(url, (_err, res, body) => {
  body = JSON.parse(body);

  console.log(body.title);
});
