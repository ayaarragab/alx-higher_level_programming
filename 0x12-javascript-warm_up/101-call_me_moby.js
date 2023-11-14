#!/usr/bin/node
exports.callMeMoby = function(number, function_f) {
  for (let index = 0; index < number; index++) {
    function_f();
  }
}
