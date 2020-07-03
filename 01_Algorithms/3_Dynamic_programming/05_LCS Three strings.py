from sys import stdin
import numpy as np

def num_els(seq):
    for idx in range(len(seq)):
        if seq[idx] > 1e9:
            res = idx
            break
    return res

def LCS3(str1, str2, str3):

    # we need to fill in the matrix T
    # vertical dimension is ' word1'
    # horizontal is ' word2'

    m, n, p = len(str1) + 1, len(str2) + 1, len(str3) + 1
    max_len = max([m,n,p])
    T = np.empty((m,n,p), dtype=np.object)
    for i in range(m):
        for j in range(n):
            for k in range(p):
                T[i, j, k] = [int(1e10)]*max_len

    # next fill in the matrix T
    for i in range(1, m):
        for j in range(1, n):
            for k in range(1,p):
                if str1[i-1] != str2[j-1] or str1[i-1] != str3[k-1] or str2[j-1] != str3[k-1]:
                    sub_LCS1 = T[i-1, j, k]
                    sub_LCS2 = T[i, j-1, k]
                    sub_LCS3 = T[i, j, k-1]
                    sub_LCS = [sub_LCS1, sub_LCS2, sub_LCS3]
                    sub_LCS_len = [num_els(sub_LCS1), num_els(sub_LCS2), num_els(sub_LCS3)]
                    idx_max = np.argmax(sub_LCS_len)
                    T[i, j, k] = sub_LCS[idx_max]
                else:
                    T[i, j, k] = list(T[i-1, j-1, k-1])
                    write_idx = num_els(T[i, j, k])

                    T[i, j, k][write_idx] = str1[i-1]

    #print(T)
    return T[-1, -1, -1]

if __name__ == '__main__':
    n = input()
    seq1 = list(map(int, input().split(sep=' ')))
    m = input()
    seq2 = list(map(int, input().split(sep=' ')))
    p = input()
    seq3 = list(map(int, input().split(sep=' ')))

    res = LCS3(seq1, seq2, seq3)
    #print(res)
    print(num_els(res))