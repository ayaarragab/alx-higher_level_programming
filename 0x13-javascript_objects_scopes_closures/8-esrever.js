#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  let j = 0;
  for (let index = list.length - 1; index >= 0; index--) {
    arr[j] = list[index];
    j += 1;
  }
  return arr;
};
