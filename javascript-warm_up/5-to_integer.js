#!/usr/bin/node
const input = process.argv[2];
const parsedInput = parseInt(input);

if (!isNaN(parsedInput)) {
    console.log(`My number: ${parsedInput}`);
} else {
    console.log('Not a number');
}
