# python3

from itertools import permutations
import numpy as np

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):

    numbers = np.array(numbers, dtype=np.int)
    truncate_len = len(str(np.max(numbers))) + 1
    aux_array = np.zeros(np.size(numbers))
    for i in range(np.size(numbers)):
        k = str(numbers[i])*truncate_len
        aux_array[i] = k[:truncate_len]
    sort_idx = np.argsort(aux_array)
    sort_idx = sort_idx[::-1]

    s = "".join(list(map(str, numbers[sort_idx])))

    return int(s)


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    #assert len(input_numbers) == n
    print(largest_number(input_numbers))
