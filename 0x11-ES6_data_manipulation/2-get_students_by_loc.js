export default function getStudentsByLocation(ListStudents, Location) {
  if (!Array.isArray(ListStudents)) {
    return [];
  }
  const id = ListStudents.filter((student) => student.location === Location);
  return id;
}
