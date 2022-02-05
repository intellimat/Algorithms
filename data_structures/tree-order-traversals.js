// Binary tree traversals
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

class Node {
  constructor(key, left_index, right_index) {
    this.key = key;
    this.left_index = left_index;
    this.right_index = right_index;
  }
}

function readInput() {
  let listOfNodes = [];
  let counter = 0;
  let isFirstLine = true;
  readline.on("line", (input) => {
    if (isFirstLine) {
      numOfNextLines = parseInt(input);
      isFirstLine = false;
      return;
    }
    if (counter < numOfNextLines) {
      listOfNodes.push(input);
      counter++;
    }
    if (counter === numOfNextLines) {
      readline.removeAllListeners();
      processInput(listOfNodes);
    }
  });
}

function processInput(listOfNodes) {
  // Parse input
  const parsedListOfNodes = listOfNodes.map((s) => {
    const arr = s.split(" ");
    return new Node(parseInt(arr[0]), parseInt(arr[1]), parseInt(arr[2]));
  });
  printInOrderTreeTraversal(parsedListOfNodes);
  printPreOrderTreeTraversal(parsedListOfNodes);
  printPostOrderTreeTraversal(parsedListOfNodes);
  readline.close();
}

function main() {
  readInput();
}

function printPreOrderTreeTraversal(parsedListOfNodes) {
  function visit(node) {
    readline.write(node.key + " ");

    if (node.left_index !== -1) visit(parsedListOfNodes[node.left_index]);
    if (node.right_index !== -1) visit(parsedListOfNodes[node.right_index]);
  }
  if (parsedListOfNodes.length > 0) visit(parsedListOfNodes[0]);
  readline.write("\n");
}
function printInOrderTreeTraversal(parsedListOfNodes) {
  function visit(node) {
    if (node.left_index !== -1) visit(parsedListOfNodes[node.left_index]);
    readline.write(node.key + " ");
    if (node.right_index !== -1) visit(parsedListOfNodes[node.right_index]);
  }
  if (parsedListOfNodes.length > 0) visit(parsedListOfNodes[0]);
  readline.write("\n");
}
function printPostOrderTreeTraversal(parsedListOfNodes) {
  function visit(node) {
    if (node.left_index !== -1) visit(parsedListOfNodes[node.left_index]);
    if (node.right_index !== -1) visit(parsedListOfNodes[node.right_index]);
    readline.write(node.key + " ");
  }
  if (parsedListOfNodes.length > 0) visit(parsedListOfNodes[0]);
  readline.write("\n");
}

// execute
main();
