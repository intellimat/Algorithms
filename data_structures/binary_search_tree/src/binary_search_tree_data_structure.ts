export class Node {
    parent: Node | null;
    left: Node | null;
    right: Node | null;
    value: number;

    constructor(value: number, parent = null, left = null, right = null) {
        this.parent = parent;
        this.left = left;
        this.right = right;
        this.value = value;
    }
}

export class BinarySearchTree {
    root: Node | null;

    constructor(root = null) {
        this.root = root;
    }

    getRoot() {
        return this.root;
    }

    getSize(node = this.root): number {
        if (node === null) return 0;
        const leftChildSize = this.getSize(node.left);
        const rightChildSize = this.getSize(node.right);
        return leftChildSize + rightChildSize + 1;
    }

    find(node: Node): Node | null {
        function recursiveFind(node: Node, tree: Node): Node {
            if (node.value === tree.value) return tree;

            if (node.value < tree.value) {
                if (tree.left !== null) return recursiveFind(node, tree.left);
                else return tree;
            } else {
                if (tree.right !== null) return recursiveFind(node, tree.right);
                else return tree;
            }
        }
        if (this.root === null) return this.root;
        else return recursiveFind(node, this.root);
    }

    // Returns the found element or the parent of the node if the node had to be placed
    // @parameter node is of Node type
    // find(node: Node, subtreeRoot = this.root): Node | null {
    //     if (
    //         subtreeRoot === null ||
    //         node === null ||
    //         subtreeRoot.value === node.value
    //     )
    //         return subtreeRoot;
    //     else if (subtreeRoot.value > node.value && subtreeRoot.left !== null)
    //         return this.find(node, subtreeRoot.left);
    //     else if (subtreeRoot.value < node.value && subtreeRoot.right !== null)
    //         return this.find(node, subtreeRoot.right);
    //     else return subtreeRoot;
    // }

    // rangeSearch() {}

    // Add the node to the tree
    // Returns true if the element has been added, false otherwise
    insert(node: Node): boolean {
        let foundNode = this.find(node);
        if (foundNode === null) {
            this.root = node;
            return true;
        } else if (foundNode.value < node.value) {
            foundNode.right = node;
            node.parent = foundNode;
            return true;
        } else if (foundNode.value > node.value) {
            foundNode.left = node;
            node.parent = foundNode;
            return true;
        } else return false;
    }

    _isRoot(node: Node): boolean {
        if (node !== null && node.parent === null) return true;
        return false;
    }

    _hasLeftChild(node: Node): boolean {
        if (node !== null && node.left !== null) return true;
        return false;
    }

    _hasRightChild(node: Node): boolean {
        if (node !== null && node.right !== null) return true;
        return false;
    }

    _isAleaf(node: Node): boolean {
        if (node !== null && node.right === null && node.left === null)
            return true;
        return false;
    }

    // Delete the node from the tree if it's present
    delete(node: Node) {
        if (node === null) return;
        // Search for the node
        const foundNode = this.find(node);
        // if foundNode is not in the tree, return
        if (foundNode === null) return;
        // if foundNode is a leaf, remove it and update parent's pointer
        if (this._isAleaf(foundNode)) {
            // CASE 1
            // if it's also the root then there no other nodes in the tree => we set this.root to null
            if (this._isRoot(foundNode)) {
                this.root = null;
                return;
            }
            // foundNode is not the root => it has a parent
            // update parent pointer; is foundNode left child or right child?
            if (foundNode.parent!.value > foundNode.value)
                // then foundNode it's the left child
                foundNode.parent!.left = null;
            // foundNode is the right child
            else foundNode.parent!.right = null;
            return;
        }
        // If foundNode has only a left child
        if (foundNode.left !== null && foundNode.right === null) {
            // CASE 2
            if (this._isRoot(foundNode)) {
                // CASE 2.1, foundNode is the root
                this.root = foundNode.left;
                foundNode.left.parent = null;

                return;
            }

            // CASE 2.2, foundNode is not the root
            foundNode.left.parent = foundNode.parent;
            if (foundNode.parent!.value > foundNode.value)
                // if foundNode is a left a child
                foundNode.parent!.left = foundNode.left;
            // foundNode is a right child
            else foundNode.parent!.right = foundNode.left;
            return;
        }

        if (foundNode.right !== null) {
            // CASE 3, foundNode has a right child
            const next = this._next(foundNode);
            if (this._getLeftDescendant(foundNode.right) !== foundNode.right) {
                // CASE 3.2a, found.right has a left descendant
                next!.parent!.left = next!.right; // next.right might be null
                if (next!.right !== null) next!.right.parent = next!.parent;
                next!.right = foundNode.right;
                foundNode.right.parent = next;
                if (foundNode.left !== null) {
                    next!.left = foundNode.left;
                    foundNode.left.parent = next;
                }
                next!.parent = foundNode.parent;
                if (foundNode.parent !== null) {
                    if (foundNode.value > foundNode.parent.value)
                        foundNode.parent.right = next;
                    else foundNode.parent.left = next;
                }
                // foundNode is the root
                else this.root = next;
                return;
            }
            // CASE 3.2b, found.right has no left descendant (getLeftDescendant(found.right) returns found.right)
            if (foundNode.left !== null) {
                next!.left = foundNode.left;
                foundNode.left!.parent = next;
            }
            next!.parent = foundNode.parent;
            if (foundNode.parent !== null) {
                if (foundNode.value > foundNode.parent.value)
                    foundNode.parent.right = next;
                else foundNode.parent.left = next;
            } else this.root = next; // foundNode was the root
            return;
        }
    }

    // Returns the height of the tree
    getHeight(subtreeRoot = this.root): number {
        if (subtreeRoot === null) return 0;

        const leftNodeHeight = this.getHeight(subtreeRoot.left);
        const rightNodeHeight = this.getHeight(subtreeRoot.right);

        return Math.max(leftNodeHeight, rightNodeHeight) + 1;
    }

    // Returns true or false
    _isPropertyRespected(node = this.root): boolean {
        function _isPropertyRespected_recursive(
            node: Node,
            lowerRange: number,
            upperRange: number
        ): boolean {
            if (!(lowerRange < node.value && node.value < upperRange))
                return false;
            let leftChildOk = true;
            let rightChildOk = true;
            if (node.left !== null)
                leftChildOk = _isPropertyRespected_recursive(
                    node.left,
                    lowerRange,
                    node.value
                );
            if (node.right !== null)
                rightChildOk = _isPropertyRespected_recursive(
                    node.right,
                    node.value,
                    upperRange
                );
            return leftChildOk && rightChildOk;
        }

        if (node === null || (node.left === null && node.right === null))
            return true;

        let x = true;
        let y = true;

        if (node.left !== null)
            x = _isPropertyRespected_recursive(
                node.left,
                -Infinity,
                node.value
            );
        if (node.right !== null)
            y = _isPropertyRespected_recursive(
                node.right,
                node.value,
                Infinity
            );

        return x && y;
    }

    _getLeftDescendant(node: Node): Node | null {
        if (node === null) return null;
        while (node.left !== null) node = node.left;
        return node;
    }

    _getRightAncestor(node: Node): Node | null {
        if (node === null || node.parent === null) return null;
        if (node.parent.value > node.value) return node.parent;
        else return this._getRightAncestor(node.parent);
    }

    // Returns the smallest bigger node than the node passed as a parameter or null
    _next(node: Node): Node | null {
        if (node === null) return null;
        if (node.right !== null)
            // case 1
            return this._getLeftDescendant(node.right);
        else return this._getRightAncestor(node); // case 2
    }

    _assert(property: boolean) {
        if (property === false) throw new Error();
    }
}
