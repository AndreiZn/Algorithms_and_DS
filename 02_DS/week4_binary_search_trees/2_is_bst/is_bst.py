#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def InOrderTraverse(keys, left, right, root_idx, stack):

  if root_idx == -1:
    return stack

  # stack will keep the entries of the tree in the InOrderTraverse
  stack = InOrderTraverse(keys, left, right, left[root_idx], stack)
  stack.append(keys[root_idx])
  stack = InOrderTraverse(keys, left, right, right[root_idx], stack)

  return stack

def IsBinarySearchTree(tree):
  # Implement correct algorithm here

  # an empty tree is considered to be a binary search tree
  if tree == []:
    return True

  # unpack the tree to have separate info on keys, left nodes and right nodes
  keys, left, right = [tree[i][0] for i in range(len(tree))], [tree[i][1] for i in range(len(tree))], [tree[i][2] for i in range(len(tree))]

  # get the InOrderTraverse path
  stack = InOrderTraverse(keys, left, right, 0, [])

  # analyze the obtained stack array (if the entries are in the ascending order, then the tree is a binary search tree)
  cmp = [stack[i+1] > stack[i] for i in range(len(stack)-1)]

  # check the condition described above
  if cmp.count(False) > 0:
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




### Alternative solution (narrow the feasible interval after considering each node) ###

# def isBST(node, min_val, max_val):
#   key, left, right = node[0], node[1], node[2]
#   if key < min_val or key > max_val:
#     return False
#   else:
#     return True
#
# def IsBinarySearchTree(tree, root_idx, min_val, max_val):
#   # Implement correct algorithm here
#
#   if tree == []:
#     return True
#
#   if not isBST(tree[root_idx], min_val, max_val):
#     #print('case 1')
#     return False
#
#   root_key, l_idx, r_idx = tree[root_idx][0], tree[root_idx][1], tree[root_idx][2]
#
#   # deal with the left sub-tree
#   if  l_idx != -1:
#     #l_tree = tree[l_idx]
#     res = IsBinarySearchTree(tree, l_idx, min_val, root_key-1)
#     if not res:
#       #print('case 2')
#       return False
#
#   if  r_idx != -1:
#     #r_tree = tree[r_idx]
#     res = IsBinarySearchTree(tree, r_idx, root_key+1, max_val)
#     if not res:
#       #print('case 3')
#       return False
#
#   return True
