#!/usr/bin/node

const fs = require('fs');

function writeFileToFile(filePath, content) {
    fs.writeFile(filePath, content, 'utf-8', (err) => {
        if (err) {
            console.error(err);
        } else {
            console.log('Successfully written');
        }
    });
}

const filePath = 'my_file.txt';
const content = 'Python is cool';

writeFileToFile(filePath, content);
