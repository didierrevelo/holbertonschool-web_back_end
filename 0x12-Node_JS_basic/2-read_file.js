const fs = require('fs');

module.exports = function countStudents(database) {
  let file;
  try {
    file = fs.readFileSync(database, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }
  const lines = file.toString().split('\n');
  let students = lines.filter((line) => line);
  students = students.map((item) => item.split(','));
  const NUMBER_OF_STUDENTS = students.length ? students.length - 1 : 0;
  console.log(`Number of students: ${NUMBER_OF_STUDENTS}`);

  const fields = {};
  for (const i in students) {
    if (i !== 0) {
      if (!fields[students[i][3]]) fields[students[i][3]] = [];

      fields[students[i][3]].push(students[i][0]);
    }
  }

  delete fields.field;

  for (const key of Object.keys(fields)) {
    console.log(
      `Number of students in ${key}: ${fields[key].length}. List: ${fields[
        key
      ].join(', ')}`,
    );
  }
};
