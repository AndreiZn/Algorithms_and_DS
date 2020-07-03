from sys import stdin
import numpy as np

def edit_distance(str1, str2):

    # we need to fill in the matrix T
    # vertical dimension is ' word1'
    # horizontal is ' word2'

    m, n = len(str1) + 1, len(str2) + 1
    T = np.zeros((m, n), dtype=np.int)

    # to get from empty to ' word1' takes i insert operations
    for i in range(m):
        T[i, 0] = i
    # to get from ' word2' to empty takes j delete operations
    for j in range(n):
        T[0, j] = j

    # next fill in the matrix T
    # check if it is necessary to insert, delete, dismatch or match i, j-th symbols (str1[cur_idx] == str2[cur_idx] ?)
    # then, select the optimal movement
    for i in range(1, m):
        for j in range(1,n):
            if str1[i-1] != str2[j-1]:
                choices = [0] * 3
                choices[0] = T[i-1, j] + 1
                choices[1] = T[i, j-1] + 1
                choices[2] = T[i-1, j-1] + 1

                T[i, j] = min(choices)
            else:
                T[i, j] = T[i-1, j-1]

    return T[-1, -1]

if __name__ == '__main__':
    str1 = input()
    str2 = input()

    ed = edit_distance(str1, str2)

    print(ed)

