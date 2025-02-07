#!/usr/bin/node
const fs = require('fs');
fs.readFile(process.argv[2], (error, paragraph) => {
  if (error) throw error;
  console.log(paragraph.toString());
});
