#!/usr/bin/node

// script that display the status code of a GET request.

const req = require('request');

const url = process.argv[2];

req(url, (_err, res) => {
  console.log('code:', res.statusCode);
});
