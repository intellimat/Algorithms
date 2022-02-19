#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(2*10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  def isBinarySearchTreeRecursive(node, lowerRange, upperRange):
    # this function has access to <tree>
    key = node[0]
    leftIndex = node[1]
    rightIndex = node[2]

    if lowerRange < key < upperRange:
      pass
    else:
      return False

    leftChildOk = True
    rightChildOk = True

    if leftIndex != -1:
      leftChildOk = isBinarySearchTreeRecursive(tree[leftIndex], lowerRange, key)
    if rightIndex != -1:
      rightChildOk = isBinarySearchTreeRecursive(tree[rightIndex], key, upperRange)

    return leftChildOk and rightChildOk
  
  l = len(tree)
  if l == 0 or l == 1:
    return True

  root = tree[0]

  x = True
  y = True

  if root[1] != -1:
    x = isBinarySearchTreeRecursive(tree[root[1]], float('-inf'), root[0])

  if root[2] != -1:
    y = isBinarySearchTreeRecursive(tree[root[2]], root[0], float('inf'))
  
  return x and y


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
