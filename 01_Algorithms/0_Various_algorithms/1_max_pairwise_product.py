# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    idx_1 = 1
    for j in range(2, n):
        if numbers[j] > numbers[idx_1]:
            idx_1 = j

    if idx_1 == 0:
        idx_2 = 1
    else:
        idx_2 = 0

    for j in range(1, n):
        if numbers[j] > numbers[idx_2] and j != idx_1:
            idx_2 = j
            
    max_product = max(max_product,
             numbers[idx_1] * numbers[idx_2])

    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
