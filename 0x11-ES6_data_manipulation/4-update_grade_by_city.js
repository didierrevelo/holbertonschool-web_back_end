export default function updateStudentGradeByCity(ListStudents, city, newGrades) {
  if (!Array.isArray(ListStudents)) {
    return [];
  }
  if (!Array.isArray(newGrades)) {
    return [];
  }

  const idCity = ListStudents.filter((student) => student.location === city);

  const studentsGraded = idCity.map((student) => {
    const gradeFilter = newGrades.filter(
      (newGrade) => newGrade.studentId === student.id,
    );

    let grade;

    if (gradeFilter[0]) {
      grade = gradeFilter[0].grade;
    } else {
      grade = 'N/A';
    }

    return {
      ...student,
      grade,
    };
  });

  return studentsGraded;
}
