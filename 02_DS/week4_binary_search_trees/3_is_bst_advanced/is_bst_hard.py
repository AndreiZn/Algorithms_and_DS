#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def InOrderTraverse(keys, left, right, root_idx, stack, fl):

  if root_idx == -1:
    return stack, fl

  stack, fl = InOrderTraverse(keys, left, right, left[root_idx], stack, fl)
  stack.append(keys[root_idx])
  if (keys[root_idx] <= keys[left[root_idx]] and left[root_idx] != -1) or (keys[root_idx] > keys[right[root_idx]] and right[root_idx] != -1):
    #print(root_idx)
    fl = 1
  stack, fl = InOrderTraverse(keys, left, right, right[root_idx], stack, fl)

  return stack, fl

def IsBinarySearchTree(tree):
  # Implement correct algorithm here

  if tree == []:
    return True

  keys, left, right = [tree[i][0] for i in range(len(tree))], [tree[i][1] for i in range(len(tree))], [tree[i][2] for i in range(len(tree))]

  stack, fl = InOrderTraverse(keys, left, right, 0, [], 0)

  cmp = [stack[i+1] >= stack[i] for i in range(len(stack)-1)]

  if cmp.count(False) > 0 or fl == 1:
    return False
  else:
    return True


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
