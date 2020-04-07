# python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
from collections import namedtuple
import os
from time import time

class Stack:
        def __init__(self, n):
                self.p = 0
                self.array = [None for i in range(n)]
        def push(self, arr):
                for i in range(len(arr)):
                        self.array[self.p] = arr[i]
                        self.p += 1
        def pop(self):
                self.p -= 1
                return self.array[self.p]

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height_naive(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            maxHeight = max(maxHeight, height)
        return maxHeight

    def children_nodes(self, p_nodes):
        ch_nodes = [[] for i in range(self.n)]
        for node_idx, p_node in enumerate(p_nodes):
            if p_node == -1:
                root = node_idx
            else:
                ch_nodes[p_node].append(node_idx)
        return root, ch_nodes

    def convert_to_namedtuple(self, arr, h):
        Node = namedtuple('Node', ["key", "height"])
        return [Node(arr[i], h) for i in range(len(arr))]

    def compute_height(self):
        max_h = 1
        t_0 = time()
        root, ch_nodes = self.children_nodes(self.parent)

        self.stack, self.h_stack = Stack(self.n),  Stack(self.n)
        root_children = ch_nodes[root]
        h_array = [2 for idx in range(len(root_children))] # height for root children nodes is 2
        #root_children_tpl = self.convert_to_namedtuple(root_children, h)
        self.stack.push(root_children)
        self.h_stack.push(h_array)

        while self.stack.p != 0:
                node = self.stack.pop()
                h = self.h_stack.pop()
                if ch_nodes[node]:
                        self.stack.push(ch_nodes[node])
                        h_array = [1 + h for idx in range(len(ch_nodes[node]))]
                        self.h_stack.push(h_array)
                else:
                        max_h = max(max_h, h)

        return max_h


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

        # test_dir = '/Users/andreizn/Desktop/Algorithms_and_DS/02_DS/week1_basic_data_structures/2_tree_height/tests/'
        # test_files = sorted(os.listdir(test_dir))
        #
        # for file_id in range(0, len(test_files), 2):
        #     test_filename = test_dir + test_files[file_id]
        #     # print(test_filename)
        #     f = open(test_filename, "r")
        #     text = f.readlines()
        #     tree = TreeHeight()
        #     tree.n = int(text[0])
        #     tree.parent = list(map(int, text[1].split(' ')))
        #     t_0 = time()
        #     naive_ans = tree.compute_height_naive()
        #     t_naive = time() - t_0
        #
        #     t_0 = time()
        #     ans = tree.compute_height()
        #     t = time() - t_0
        #
        #     if  naive_ans != ans:
        #             print(tree.parent)
        #             break
        #     else:
        #             print(file_id)
        #             print('Naive solution time: {}, time: {}'.format(t_naive, t))
        #     #break

threading.Thread(target=main).start()
