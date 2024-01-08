#!/usr/bin/node

const arglen = process.argv.length - 2;

if (arglen >= 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

