import numpy as np

def MinMax(op, i, j, mins, Maxs):

    min_val = np.inf
    max_val = -np.inf

    for k in range(i, j):
        if op[k] == '+':
            a = Maxs[i, k] + Maxs[k+1, j]
            b = Maxs[i, k] + mins[k + 1, j]
            c = mins[i, k] + Maxs[k + 1, j]
            e = mins[i, k] + mins[k + 1, j]

            min_val = min(min_val, a, b, c, e)
            max_val = max(max_val, a, b, c, e)

        if op[k] == '-':
            a = Maxs[i, k] - Maxs[k + 1, j]
            b = Maxs[i, k] - mins[k + 1, j]
            c = mins[i, k] - Maxs[k + 1, j]
            e = mins[i, k] - mins[k + 1, j]

            min_val = min(min_val, a, b, c, e)
            max_val = max(max_val, a, b, c, e)

        if op[k] == '*':
            a = Maxs[i, k] * Maxs[k + 1, j]
            b = Maxs[i, k] * mins[k + 1, j]
            c = mins[i, k] * Maxs[k + 1, j]
            e = mins[i, k] * mins[k + 1, j]

            min_val = min(min_val, a, b, c, e)
            max_val = max(max_val, a, b, c, e)

    return min_val, max_val

def MaxVal(d, op):

    n = len(d)

    mins = np.zeros((n, n), dtype=int)
    Maxs = np.zeros((n, n), dtype=int)

    for i in range(n):
        mins[i, i] = d[i]
        Maxs[i, i] = d[i]

    for s in range(1, n):
        for idx in range(0, n-s):

            j = idx + s

            mins[idx, j], Maxs[idx, j] = MinMax(op, idx, j, mins, Maxs)

    #print(mins)
    return Maxs[0, -1]




if __name__ == '__main__':

    s = input()
    d = []
    op = []

    for i in range(len(s)):
        if i % 2 == 0:
            d.append(int(s[i]))
        else:
            op.append(s[i])

    res = MaxVal(d, op)

    print(res)