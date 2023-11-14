#!/usr/bin/node
exports.callMeMoby = function (number, functionF) {
  for (let index = 0; index < number; index++) {
    functionF();
  }
};
