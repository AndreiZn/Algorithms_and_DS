# python3

import math
import numpy as np

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query, l, r):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 10 ** 4

    if r < l:
        return -1

    m = math.ceil(l + (r - l) / 2)

    if keys[m] == query:
        return m
    elif query > keys[m]:
        return binary_search(keys, query, m+1, r)
    else:
        return binary_search(keys, query, l, m-1)

if __name__ == '__main__':
    input_keys = np.array(list(map(int, input().split())))
    input_n, input_keys = input_keys[0], input_keys[1:]
    input_queries = np.array(list(map(int, input().split())))
    input_m, input_queries = input_queries[0], input_queries[1:]

    for q in input_queries:
        print(binary_search(input_keys, q, 0, len(input_keys)-1), end=' ')
