import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() {
    return this._amount;
  }

  set amount(amount) {
    if (typeof amount === 'number') {
      this._amount = amount;
    } else {
      throw new TypeError('Amount must be a number');
    }
  }

  get currency() {
    return this._currency;
  }

  set currency(currency) {
    if (currency instanceof Currency) {
      this._currency = currency;
    } else {
      throw new TypeError('Currency must be a Currency object');
    }
  }

  static convertPrice(amount, conversionRate) {
    return (amount * conversionRate);
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }
}
