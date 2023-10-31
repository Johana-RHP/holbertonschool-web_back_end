import Currency from "./3-currency.js";

class Pricing {
  constructor(amount, currency) {
    this._amount = 0;
    this._currency = new Currency("", "");

    this.amount = amount;
    this.currency = currency;
  }

  // Getter and setter for 'amount'
  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value === "number") {
      this._amount = value;
    } else {
      throw new TypeError("Amount must be a number");
    }
  }

  // Getter and setter for 'currency'
  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (value instanceof Currency) {
      this._currency = value;
    } else {
      throw new TypeError("Currency must be an instance of the Currency class");
    }
  }

  // Method to display the full price
  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  // Static method to convert the price using a conversion rate
  static convertPrice(amount, conversionRate) {
    if (typeof amount === "number" && typeof conversionRate === "number") {
      return amount * conversionRate;
    } else {
      throw new TypeError("Amount and conversionRate must be numbers");
    }
  }
}

export default Pricing;

