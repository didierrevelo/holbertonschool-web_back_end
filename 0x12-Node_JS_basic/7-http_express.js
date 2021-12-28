const express = require('express');

const args = process.argv.slice(2);
const countStudents = require('./3-read_file_async');

const data = args[0];
const app = express();
const hostname = '127.0.0.1';
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const message = 'This is the list of our students\n';
  try {
    const list = await countStudents(data);
    res.send(`${message}${list.join('\n')}`);
  } catch (error) {
    res.send(`${message}${error.message}`);
  }
});

app.listen(port, hostname, () => {
  // console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;
