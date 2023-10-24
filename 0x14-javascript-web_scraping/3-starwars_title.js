#!/usr/bin/node

// script that prints the title of a Star Wars movie

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, res) => {
  if (err) {
    console.log(err);
    return;
  }

  const body = JSON.parse(res.body);
  const title = body.title;

  console.log(title);
});
