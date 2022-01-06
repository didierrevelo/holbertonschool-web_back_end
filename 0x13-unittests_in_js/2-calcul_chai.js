module.exports = function calculateNumber(type, a, b) {
  const aRound = Math.round(a);
  const bRound = Math.round(b);

  if (type === 'SUM') {
    return aRound + bRound;
  } else if (type === 'SUBTRACT') {
    return aRound - bRound;
  } else if (type === 'DIVIDE') {
    if (bRound === 0) {
      return 'Error';
    }
    return aRound / bRound;
  }
}
