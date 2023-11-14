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

    rotate () {
      const temp = this.height;
      this.height = this.width;
      this.width = temp;
    }

    double () {
      this.width = this.width * 2;
      this.height = this.height * 2;
    }
  };
