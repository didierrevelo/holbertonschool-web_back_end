const chai = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function () {
  describe('two integrer', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 2, 4)).to.equal(6);
    });
  });

  describe('two round', () => {
    it('should return 8', () => {
      chai.expect(calculateNumber('SUM', 2.5, 4.5)).to.equal(8);
    });
  });

  describe('one round', () => {
    it('should return 7', () => {
      chai.expect(calculateNumber('SUM', 2.5, 4)).to.equal(7);
    });
  });

  describe('one round2', () => {
    it('should return 7', () => {
      chai.expect(calculateNumber('SUM', 2, 4.5)).to.equal(7);
    });
  });

  describe('one round floor', () => {
    it('should return 6', () => {
      chai.expect(calculateNumber('SUM', 2.3, 4)).to.equal(6);
    });
  } );

  describe('Two round reversed', function () {
    it('should return 5', function () {
      chai.expect(calculateNumber('SUM', 3.7, 1.2)).to.equal(5);
    });
  });

  describe('Two round again floor both', function () {
    it('should return 3', function () {
      chai.expect(calculateNumber('SUM', 1.2, 2.1)).to.equal(3);
    });
  });

  describe('Two round again floor first', function () {
    it('should return 3', function () {
      chai.expect(calculateNumber('SUM', 1.2, 2)).to.equal(3);
    });
  });

  describe('Two round again floor second', function () {
    it('should return 4', function () {
      chai.expect(calculateNumber('SUM', 2, 2.1)).to.equal(4);
    });
  });

  describe('round top', function () {
    it('should return 18', function () {
      chai.expect(calculateNumber('SUM', 15.5, 2)).to.equal(18);
    });
  });

  describe('two integrer', function () {
    it('should return 6', function () {
      chai.expect(calculateNumber("SUM", 2, 4)).to.equal(6);
    });
  });

  describe('two round', function () {
    it('should return 8', function () {
      chai.expect(calculateNumber("SUM", 2.5, 4.5)).to.equal(8);
    });
  });

  describe('one round', function () {
    it('should return 7', function () {
      chai.expect(calculateNumber("SUM", 2.5, 4)).to.equal(7);
    });
  });

  describe('one round2', function () {
    it('should return 7', function () {
      chai.expect(calculateNumber("SUM", 2, 4.5)).to.equal(7);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.5', function () {
      chai.expect(calculateNumber("DIVIDE", 2, 4)).to.equal(0.5);
    });
  });

  describe('DIVIDE', function () {
    it('should return Error', function () {
      chai.expect(calculateNumber("DIVIDE", 2, 0)).to.equal('Error');
    });
  });

  describe('DIVIDE', function () {  // 
    it('should return 0.6', function () {
      chai.expect(calculateNumber("DIVIDE", 2.5, 4.5)).to.equal(0.6);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.75', function () {
      chai.expect(calculateNumber("DIVIDE", 2.5, 4)).to.equal(0.75);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -2', function () {
      chai.expect(calculateNumber("SUBTRACT", 2, 4)).to.equal(-2);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -2', function () {
      chai.expect(calculateNumber("SUBTRACT", 2.5, 4.5)).to.equal(-2);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -1', function () {
      chai.expect(calculateNumber("SUBTRACT", 2.5, 4)).to.equal(-1);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -7', function () {
      chai.expect(calculateNumber("SUBTRACT", -2, 4.5)).to.equal(-7);
    });
  });
});