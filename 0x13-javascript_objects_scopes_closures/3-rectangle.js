#!/usr/bin/node
module.exports =
  class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }

    print () {
      let pattern = '';
      for (let index = 0; index < this.width; index++) {
        pattern += 'X';
      }
      for (let index = 0; index < this.height; index++) {
        console.log(pattern);
      }
    }
  };
