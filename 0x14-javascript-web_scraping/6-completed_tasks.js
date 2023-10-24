#!/usr/bin/node

// script that computes the number of tasks completed by user id.

const req = require('request');

const args = process.argv[2];

req(args, (err, res, body) => {
  if (err) {
    console.log(err);
  }

  const dict = JSON.parse(body).reduce((acc, elem) => {
    if (!acc[elem.userId]) {
      if (elem.completed) {
        acc[elem.userId] = 1;
      }
    } else {
      if (elem.completed) {
        acc[elem.userId] += 1;
      }
    }
    return acc;
  }, {});
  console.log(dict);
});
