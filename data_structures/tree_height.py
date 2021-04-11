# python3

'''

Problem Description

TASK: You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

INPUT FORMAT: The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.

CONSTRAINTS:  1 ≤ 𝑛 ≤ 105.

OUTPUT FORMAT: Output the height of the tree.
'''

import sys
import threading


from collections import namedtuple

Node = namedtuple("Node", ["value", "children"])

def find_height_recursively(root):
    if len(root.children) == 0:
        return 1

    max_height = -1

    for child in root.children:
        curr_height = find_height_recursively(child)
        if curr_height > max_height:
            max_height = curr_height
    
    height = max_height + 1

    return height


def compute_height(n, parents):
    nodes = [ Node(value, []) for value in range(0, n) ]

    # Link the nodes, so that we can form a tree
    for i, p in enumerate(parents):
        if p != -1:
            nodes[p].children.append(nodes[i])
        else:
            root_index = i

    # Compute tree height recursively
    root = nodes[root_index]

    height = find_height_recursively(root)

    return height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
