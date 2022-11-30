#!/usr/bin/node

function add (x, y) {
  return parseInt(x) + parseInt(y);
}

console.log(add(process.argv[2], process.argv[3]));
