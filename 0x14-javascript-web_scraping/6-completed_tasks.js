#!/usr/bin/node
const request = require('request');

const url = process.argv[2] || '';
const storage = {};
let tmp = '';

request(url, (err, res, body) => {
  if (err) {
    return console.log(err);
  }

  const parsedBody = JSON.parse(body);

  for (let i = 0; i < parsedBody.length; i++) {
    tmp = parsedBody[i].userId;
    if (parsedBody[i].completed) {
      storage[tmp] = (storage[tmp] || 0) + 1;
    }
  }

  console.log(storage);
});
