import numpy as np

def knapsack_wo_rep(W, v):

    n = len(v) # number of available objects
    value = np.zeros((W+1, n+1), dtype=np.int) # value[i,j] tells what is the max value achievable if the knapsack is limitted by
                                 # the weight i and first j elemetns are used

    for i in range(1,n+1):
        for w in range(1, W+1):
            value[w, i] = value[w, i-1]

            cur_el = v[i-1] # we can try to add this element to the bag
            if cur_el <= w:
                val = value[w-cur_el, i - 1] + cur_el
                if value[w, i] < val:
                    value[w, i] = val

    return value[-1, -1]

if __name__ == '__main__':

    Wn = list(map(int, input().split(sep=' ')))
    W, n = Wn[0], Wn[1]
    v = list(map(int, input().split(sep=' ')))

    res = knapsack_wo_rep(W, v)

    print(res)