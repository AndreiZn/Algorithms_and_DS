# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    stop_flag = 1
    k = 1

    while stop_flag:

        k_new = k + 1
        n_new = n - k
        if n_new <= k:
            stop_flag = 0
            summands.append(n)
        else:
            summands.append(k)
            k = k_new
            n = n_new

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(" ".join(map(str, output_summands)))
