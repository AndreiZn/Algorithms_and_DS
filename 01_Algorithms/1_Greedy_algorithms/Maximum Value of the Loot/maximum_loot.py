# python3

from sys import stdin
import numpy as np

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    prices_per_pound = [prices[i]/weights[i] for i in range(len(prices))]
    ind = np.argsort(prices_per_pound)
    capacity_left = capacity
    i = np.size(ind, 0) - 1
    total_price = 0

    while capacity_left > 0 and i >= 0:
        cur_idx = ind[i]
        cur_price = prices_per_pound[cur_idx]
        cur_weight = weights[cur_idx]

        if cur_weight < capacity_left:
            capacity_left = capacity_left - cur_weight
            total_price = total_price + cur_weight * cur_price
        else:
            total_price = total_price + capacity_left * cur_price
            capacity_left = 0


        i = i - 1

    return total_price

if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
