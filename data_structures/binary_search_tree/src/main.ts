import { BinarySearchTree, Node } from './binary_search_tree_data_structure';
// Make sure that upperRange - lowerRange >> numOfInsertions
// Otherwise we cannot find enough different values to insert in the tree
const numOfInsertions = parseInt(process.argv[2] ? process.argv[2] : '400');
const lowerRange = parseInt(process.argv[3] ? process.argv[3] : '0');
const upperRange = parseInt(process.argv[4] ? process.argv[4] : '1000000');

let insertedNodes: Node[] = [];
let bst: BinarySearchTree = new BinarySearchTree();

function main() {
    test_insertions_and_deletions();
    // test_get_size();
}

function test_get_size() {
    // reset bst and insertedNodes list
    bst = new BinarySearchTree();
    insertedNodes = [];
    _populateBST();
    if (bst.getSize() === numOfInsertions) console.log('Size test SUCCESS');
    else console.log('Size test FAILED');
}

function _populateBST() {
    let j = 0;
    while (j < numOfInsertions) {
        const initialSize = bst.getSize();
        let node = new Node(getRandomIntInclusive(lowerRange, upperRange));
        const inserted = bst.insert(node);
        if (inserted) {
            checkBSTproperty();
            const nextExpectedSize = initialSize + 1;
            checkBSTsize(nextExpectedSize);
            insertedNodes.push(node);
            console.log('Insertion ' + j + ' SUCCESS');
            j++;
        }
    }
}

function _deleteInsertedNodes() {
    let i = 0;
    // TODO: shuffle insertedNodes with Fisher-Yates algorithm
    for (const node of insertedNodes) {
        const initialSize = bst.getSize();
        bst.delete(node);
        const nextExpectedSize = initialSize - 1;
        checkBSTsize(nextExpectedSize);
        checkBSTproperty();
        console.log(
            'Deletion  ' + i + '/' + (insertedNodes.length - 1) + ' SUCCESS'
        );
        i++;
    }
}

function test_insertions_and_deletions() {
    // reset bst and insertedNodes list
    bst = new BinarySearchTree();
    insertedNodes = [];

    _populateBST();
    console.log('BREAKPOINT - INSERTED ALL NODES ');
    _deleteInsertedNodes();
    console.log('SUCCESS - ALL TESTS PASSED. ');
}

function test_find() {
    const insertedNodes: Node[] = [];
    const bst = new BinarySearchTree();

    for (let i = 0; i < 10000; i++) {
        let node = new Node(getRandomIntInclusive(lowerRange, upperRange));
        bst.insert(node);
        checkBSTproperty();
        insertedNodes.push(node);
    }

    for (let i = 0; i < 10000; i++) {
        const node = insertedNodes[i];
        const foundNode = bst.find(node);
        if (foundNode === null || foundNode.value !== node.value)
            throw (
                'test failed, foundNode.value = ' +
                foundNode?.value +
                'and node.value = ' +
                node.value
            );
    }
    console.log('TESTS PASSED');
}

function getRandomIntInclusive(min: number, max: number): number {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1) + min); //The maximum is inclusive and the minimum is inclusive
}

function checkBSTproperty() {
    if (!bst._isPropertyRespected()) {
        console.log('TEST FAILED. ');
        throw new Error('BST property violated.');
    }
}

function checkBSTsize(expectedSize: number) {
    const actualSize = bst.getSize();
    if (actualSize !== expectedSize) {
        console.log('TEST FAILED. ');
        throw new Error(
            `Expected size: ${expectedSize} but actual size is ${actualSize}`
        );
    }
}

// Execution
main();
