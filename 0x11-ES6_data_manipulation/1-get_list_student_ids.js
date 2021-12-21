export default function getListStudentIds(ListStudents) {
  if (!Array.isArray(ListStudents)) {
    return [];
  }
  const id = ListStudents.map((student) => student.id);
  return id;
}
