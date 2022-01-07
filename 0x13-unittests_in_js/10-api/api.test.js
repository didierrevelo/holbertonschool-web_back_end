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

  describe('GET /available_payments', () => {
    it('should return 200', (done) => {
      request('http://localhost:7865/available_payments', (err, res, body) => {
        expect(res.statusCode).to.equal(200);
        done();
      });
    });

    it('should return payment methods', (done) => {
      request('http://localhost:7865/available_payments', (err, res, body) => {
        expect(body).to.equal('{"payment_methods":{"credit_cards":true,"paypal":false}}');
        done();
      });
    });

    it('should return payment methods faile 404', (done) => {
      request('http://localhost:7865/availablepayments', (err, res, body) => {
        expect(res.statusCode).to.equal(404);
        done();
      });
    });
  });

  describe('POST /login', () => {
    it('Responds with 200 and correct name Betty', (done) => {
      const form = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          userName: 'Betty',
        },
      };

      request(form, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome Betty');
        done();
      });
    });

    it('Responds with 200 and correct name user', (done) => {    
      const form = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          userName: 'user',
        },
      };

      request(form, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome user');
        done();
      });
    });

    it('Responds with 200 and incorrect userName, undefined', (done) => {
      const form = {
        url: 'http://localhost:7865/login',
        method: 'POST',
        json: {
          username: 'Betty',
        },
      };

      request(form, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome undefined');
        done();
      });
    });

    it('Responds with 404 and incorrect localhost:7865/login/hello', (done) => {
      const form = {
        url: 'http://localhost:7865/login/hello',
        method: 'POST',
        json: {
          userName: 'Betty',
        },
      };

      request(form, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        expect(body).to
        .equal('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>Error</title>\n</head>\n<body>\n<pre>Cannot POST /login/hello</pre>\n</body>\n</html>\n');
        done();
      });
    });

    it('Responds with 404 and incorrect path', (done) => {
      const form = {
        url: 'http://localhost:7865/',
        method: 'POST',
        json: {
          userName: 'Betty',
        },
      };

      request(form, (error, response, body) => {
        expect(response.statusCode).to.equal(404);
        expect(body).to
        .equal('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>Error</title>\n</head>\n<body>\n<pre>Cannot POST /</pre>\n</body>\n</html>\n');
        done();
      });
    });

    it('Responds without json', (done) => {
      const form = {
        url: 'http://localhost:7865/login',
        method: 'POST',
      };

      request(form, (error, response, body) => {
        expect(response.statusCode).to.equal(200);
        expect(body).to
        .equal('Welcome undefined');
        done();
      });
    });
  });
});
