# python3

from collections import namedtuple
from sys import stdin
import numpy as np

Segment = namedtuple('Segment', 'start end')

# Choose the segment with the leftmost right coordinate and then remove segments that are to the left from the current "leftmost right" segment. Also, remove these segments from
# the right coordinates sorted by ascending order. Then, continue the algorithm on the subproblem.
def compute_optimal_points(segments):
    n = len(segments)
    l_c, r_c = np.array([segments[i][0] for i in range(n)]), np.array([segments[i][1] for i in range(n)])
    l_ind_asc, r_ind_asc = np.argsort(l_c), np.argsort(r_c)
    output_set = np.array([], dtype=np.int)
    r_asc_idx_remove = np.array([], dtype=np.int)
    l_ind = 0
    leftmost_right = r_c[r_ind_asc[0]]

    while l_ind <= n-1:
        output_set = np.append(output_set, leftmost_right)
        l_ind = l_ind + 1
        while l_ind <= n-1 and l_c[l_ind_asc[l_ind]] <= leftmost_right:
            l_ind = l_ind + 1

        abs_seg_ind_remove = l_ind_asc[:l_ind]
        for j in range(np.size(abs_seg_ind_remove)):
            r_asc_idx_remove = np.append(r_asc_idx_remove, np.where(r_ind_asc == abs_seg_ind_remove[j]))

        r_ind_asc[r_asc_idx_remove] = -1
        new_leftmost_right_idx = np.where(r_ind_asc >= 0)

        if l_ind <= n-1 and np.size(new_leftmost_right_idx) > 0:
            new_leftmost_right_idx = r_ind_asc[new_leftmost_right_idx[0][0]]
            leftmost_right = r_c[new_leftmost_right_idx]

    return np.unique(output_set)

if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(" ".join(map(str, output_points)))
