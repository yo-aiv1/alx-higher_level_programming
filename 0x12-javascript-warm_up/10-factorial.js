#!/usr/bin/node

const size = parseInt(process.argv[2]);

function factorial (num) {
  if ((Number.isNaN(num)) || (num == 1)) {
    return 1;
  }
  return factorial(num - 1) * num;
}

console.log(factorial(size));
