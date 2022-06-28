#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  let count = 0;
  const parsedBody = JSON.parse(body).results;

  for (let i = 0; i < parsedBody.length; i++) {
    const a = parsedBody[i].characters.find((c) => {
      return c.match(/18/);
    });
    if (a !== undefined) {
      count++;
    }
  }

  console.log(count);
});
