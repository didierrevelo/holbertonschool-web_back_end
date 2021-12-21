export default function getStudentIdsSum(listStudent) {
  if (!Array.isArray(listStudent)) {
    return [];
  }
  const id = listStudent.map((student) => student.id);
  return id.reduce((acc, cur) => acc + cur, 0);
}
