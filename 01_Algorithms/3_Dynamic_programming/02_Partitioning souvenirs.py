import numpy as np

def three_partitioning(seq):

    total = sum(seq)
    n = len(seq)

    if n < 3:
        return 0

    if total % 3 != 0:
        return 0

    m = int(total / 3)

    sums = np.zeros((n+1, m+1, m+1), dtype=bool) # sums[p, i,j] tells whether it's possible to reach sum i in the first subset

                                                # and j in the second one using first p symbols from the seq
    #sums[0, 1:, 1:] = 0
    #sums[0, 0, 0] = 1
    sums[:, 0, :] = 1 # we can always, trivially, arrive at a target sum of 0
    sums[:, :, 0] = 1

    for p in range(1, n+1): # sums[0, 1:, 1:] = 0, because it's not possible to reach any sum without taking any elements
        for i in range(1, m+1):
            for j in range(1, m+1):
                if sums[p-1, i, j] == 1:
                    sums[p, i, j] = 1 # if we are able to attain a particular sum with a subset of the elements
                                      # that we have presently, we can also attain that sum with our current
                                      # set of elements — by simply not using the extra elements

                else:
                    # required sums should be achieved using the current element
                    cur_el = seq[p-1]
                    fl_1, fl_2 = False, False
                    if cur_el <= j:
                        fl_1 = sums[p-1, i, j-cur_el]

                    if cur_el <= i:
                        fl_2 = sums[p-1, i-cur_el, j]

                    if fl_1 or fl_2:
                        sums[p, i, j] = True

    return sums[n, m, m]


if __name__ == '__main__':

    n = input()
    seq = list(map(int, input().split(sep=' ')))

    res = three_partitioning(seq)

    print(int(res))