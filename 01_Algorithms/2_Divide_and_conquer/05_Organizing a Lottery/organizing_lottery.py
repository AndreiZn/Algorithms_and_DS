# python3
from sys import stdin
from bisect import bisect_left, bisect_right
from random import randint

def find_lt(a, x):
    'Find rightmost index that corresponds to an element of a less than x'
    i = bisect_left(a, x)
    return i

def find_le(a, x):
    'Find rightmost index that corresponds to an element of a less or equal than x'
    i = bisect_right(a, x)
    return i

def partition3(array, left, right):
    x = array[left]
    j = left

    for i in range(left+1, right+1):
        if array[i] < x:
            j = j + 1
            array[i], array[j] = array[j], array[i]

    array[left], array[j] = array[j], array[left]

    k = j
    for i in range(j+1, right+1):
        if array[i] == x:
            k = k + 1
            array[i], array[k] = array[k], array[i]
    return j, k

def randomized_quick_sort(array, left, right):
    if left >= right:
        return
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]

    m1, m2 = partition3(array, left, right)

    randomized_quick_sort(array, left, m1-1)
    randomized_quick_sort(array, m2 + 1, right)

def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    randomized_quick_sort(starts, 0, len(starts)-1)
    randomized_quick_sort(ends, 0, len(ends) - 1)
    num_segm_per_point = [0 for _ in range(len(points))]

    for i, p in enumerate(points):
        open_left = find_le(starts, p)
        open_right = find_lt(ends, p)
        num_segm_per_point[i] = open_left - open_right

    return num_segm_per_point


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(" ".join(map(str, output_count)))
