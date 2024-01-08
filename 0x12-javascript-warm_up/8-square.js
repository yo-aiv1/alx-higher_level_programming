#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (Number.isNaN(num)) {
  console.log('Missing size');
} else {
  let str = "";
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      str += 'X'
    }
    if (i != (num - 1)) {
    str += '\n'
    }
  }
  console.log(str);
}

