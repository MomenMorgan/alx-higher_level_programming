#!/usr/bin/node

// script that prints the number of movies where
// the character “Wedge Antilles” is present.

const req = require('request');

const args = process.argv[2];

req(args, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  body = JSON.parse(body).results.filter((elem) => {
    return elem.characters.filter((url) => { return url.includes('18'); }).length;
  }).length;
  console.log(body);
});
