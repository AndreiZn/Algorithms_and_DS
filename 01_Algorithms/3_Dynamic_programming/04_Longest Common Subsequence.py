from sys import stdin
import numpy as np

def is_in_str(symbol, str):

    for i in range(len(str)):
        if symbol == str[i]:
            return True

    return True

def LCS(str1, str2):

    # we need to fill in the matrix T
    # vertical dimension is ' word1'
    # horizontal is ' word2'

    m, n = len(str1) + 1, len(str2) + 1
    T = np.empty((m,n), dtype=np.object)
    for i in range(m):
        for j in range(n):
            T[i,j] = []

    # to get from empty to ' word1' takes i insert operations
    #for i in range(m):
    #    T[i, 0] = i
    # to get from ' word2' to empty takes j delete operations
    #for j in range(n):
    #    T[0, j] = j

    # next fill in the matrix T
    for i in range(1, m):
        for j in range(1, n):

            if str1[i-1] != str2[j-1]:
                sub_LCS1 = T[i-1, j]
                sub_LCS2 = T[i, j-1]
                if len(sub_LCS1) > len(sub_LCS2):
                    T[i, j] = sub_LCS1
                else:
                    T[i, j] = sub_LCS2
            else:
                sub_LCS = T[i-1, j-1]
                T[i, j] = list(T[i-1, j-1])
                T[i, j].append(str1[i-1])

    #print(T)
    return T[-1, -1]

def transform_to_str(seq):

    seq = list(map(str, seq))
    s = ''
    for i in range(0, len(seq), 2):
        s += seq[i]

    return s

if __name__ == '__main__':
    n = input()
    seq1 = list(map(int, input().split(sep=' ')))
    m = input()
    seq2 = list(map(int, input().split(sep=' ')))

    res = LCS(seq1, seq2)

    print(len(res))

