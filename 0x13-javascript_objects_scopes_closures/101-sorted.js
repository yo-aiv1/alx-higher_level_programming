#!/usr/bin/node

const dict = require('./101-data').dict;

const NewDict = {};
for (const key in dict) {
  if (dict.hasOwnProperty(key)) {
    const value = dict[key];
    if (NewDict.hasOwnProperty(value)) {
      NewDict[value].push(key);
    } else {
      NewDict[value] = [key];
    }
  }
}

console.log(NewDict);
