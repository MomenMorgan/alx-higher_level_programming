#!/usr/bin/node

// script to recive word and print it

const file = require('fs');
const args = process.argv[2];

// fetch the content
file.readFile(args, 'utf8', (error, data) => {
  if (error) {
    console.log(error);
    return;
  }

  console.log(data);
});
