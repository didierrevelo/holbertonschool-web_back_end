const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
  describe('two arguments', () => {
    it('should return a promise', (done) => {
      getPaymentTokenFromAPI(true)
        .then((res) => {
          expect(res).to.include({ data: 'Successful response from the API' })
          done();
        })
        .catch((err) => {
          done(err);
        });
    });
  });
});
