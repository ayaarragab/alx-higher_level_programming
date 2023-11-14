#!/usr/bin/node

const Square2 = require('./5-square.js');

module.exports = class Square extends Square2 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let pattern = '';
      for (let index = 0; index < this.width; index++) {
        pattern += c;
      }
      for (let index = 0; index < this.height; index++) {
        console.log(pattern);
      }
    } else {
      super.print();
    }
  }
};
