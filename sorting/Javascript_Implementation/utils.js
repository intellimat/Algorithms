const readline = require('readline');

function swap(array, i, j){
    if (i >= 0 && j >= 0 && i < array.length && j < array.length){
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    } else console.log('\nCannot swap, indeces out of range.\n')
}

function getRandomInteger(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max + 1 - min) + min)
}


function ask(query) {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
      });

      return new Promise(resolve => rl.question(query, (answer) => {
          rl.close();
          resolve(answer);
      }));
}

module.exports.getRandomInteger = getRandomInteger;
module.exports.ask = ask;
module.exports.swap = swap;