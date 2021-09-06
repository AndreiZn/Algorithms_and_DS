# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge(b,c):
    n = len(b)+len(c)
    out = [0 for _ in range(n)]
    i = 0
    b_idx, c_idx = 0, 0

    n_inv = 0

    while i < n:

        if b_idx < len(b) and c_idx < len(c):

            if b[b_idx] <= c[c_idx]:
                out[i] = b[b_idx]
                b_idx = b_idx + 1
            else:
                n_inv = n_inv + len(b) - b_idx
                out[i] = c[c_idx]
                c_idx = c_idx + 1

        elif b_idx >= len(b):
            out[i] = c[c_idx]
            c_idx = c_idx + 1
        else:
            out[i] = b[b_idx]
            b_idx = b_idx + 1

        i = i + 1
    return n_inv, out


def mergesort(a):
    n_el = len(a)
    if n_el == 1:
        return 0, [a[0]]

    m = int(n_el/2)
    b, c = a[:m], a[m:]

    n_inv_b, b_sorted = mergesort(b)
    n_inv_c, c_sorted = mergesort(c)
    n_inv_merge, a_sorted = merge(b_sorted, c_sorted)
    n_inv = n_inv_b + n_inv_c + n_inv_merge

    return n_inv, a_sorted

def compute_inversions(a):
    return mergesort(a)[0]


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))