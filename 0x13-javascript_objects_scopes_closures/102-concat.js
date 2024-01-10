#!/usr/bin/node
const fs = require('fs');

const FirstFile = fs.readFileSync(process.argv[2]).toString();
const SecondFile = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], FirstFile + SecondFile);
