#!/usr/bin/node
exports.callMeMobby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
