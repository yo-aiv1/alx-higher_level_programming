#!/usr/bin/node

const list = require('./100-data').list;
console.log(list);
const NewList = list.map((num, i) => i * num);
console.log(NewList);
