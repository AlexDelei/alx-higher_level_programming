#!/usr/bin/node
const arg1 = process.argv[2];
const intValue = parseInt(arg1);
if (!isNaN(intValue)) {
  console.log('My number is ' + intValue);
} else {
  console.log('Not a number');
}
