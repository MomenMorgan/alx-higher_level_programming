#!/usr/bin/node

// script that writes a string to a file.

const write = require('fs');

const file = process.argv[2];
const text = process.argv[3];

write.writeFile(file, text, 'utf8', (err) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log('sucess');
});
