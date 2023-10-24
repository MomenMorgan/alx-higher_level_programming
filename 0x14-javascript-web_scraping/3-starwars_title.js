#!/usr/bin/node

// script that prints the title of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, res) => {
  res = JSON.parse(res);
  const title = res.title;

  console.log(title);
});
