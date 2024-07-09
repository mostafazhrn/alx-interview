#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieID}/`;

request(url, async (error, repond, body) => {
  if (error) {
    console.log(error);
  }
  for (const character of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(character, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
