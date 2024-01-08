#!/usr/bin/node

let args = [...process.argv];
args.splice(0, 2);
args.sort();

console.log(args[args.length - 2]);
