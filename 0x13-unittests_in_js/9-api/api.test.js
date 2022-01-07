const request = require('request');
const { expect } = require('chai');

describe('api test', () => {
  describe('should return welcome message', () => {
    it('should return welcome message', (done) => {
      request('http://localhost:7865', (err, res, body) => {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });
  });

  describe('should return payment methods for cart id integrer', () => {
    it('should return payment methods for cart 1', (done) => {
      request('http://localhost:7865/cart/1', (err, res, body) => {
        expect(body).to.equal('Payment methods for cart 1');
        done();
      });
    });
  

    it('should return payment methods for cart 2', (done) => {
      request('http://localhost:7865/cart/2', (err, res, body) => {
        expect(body).to.equal('Payment methods for cart 2');
        done();
      });
    });

    it('should return payment methods for cart 3', (done) => {
      request('http://localhost:7865/cart/3', (err, res, body) => {
        expect(body).to.equal('Payment methods for cart 3');
        done();
      });
    });
  });

  describe('GET /cart/string', () => {
    it('should return 404', (done) => {
      request('http://localhost:7865/cart/a12', (err, res, body) => {
        expect(res.statusCode).to.equal(404);
        done();
      });
    });

    it('should return 404', (done) => {
      request('http://localhost:7865/cart/12a', (err, res, body) => {
        expect(res.statusCode).to.equal(404);
        done();
      });
    });

    it('should return 404', (done) => {
      request('http://localhost:7865/cart/12.34', (err, res, body) => {
        expect(res.statusCode).to.equal(404);
        done();
      });
    });
  });
});
