#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
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
