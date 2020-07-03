from sys import stdin

def prim_calc(n):
    # primitive calculator can multiply a number by 2 and by 3, or add 1 to the number

    n_steps = [0] * (n+1)
    interm = [] # going back from n to 1, we will save how we got to each i (from which number - from i+1 or 2*i or 3*i)

    for i in range(n-1, 0, -1):  # from n-1 down to 1

        vals = [1e7] * 3

        for j in range(3):
            # subtract 1
            if j == 0:
                vals[j] = n_steps[i+1] + 1

            # divide by 2
            if j == 1 and i * 2 <= n:
                vals[j] = n_steps[i*2] + 1

            # divide by 3
            if j == 2 and i * 3 <= n:
                vals[j] = n_steps[i*3] + 1

        n_steps[i] = min(vals)
        j = vals.index(n_steps[i])
        if j == 0:
            interm.append(i + 1)
        elif j == 1:
            interm.append(i * 2)
        else:
            interm.append(i * 3)

    interm.append(1)
    interm = interm[::-1]
    #print(interm)
    opt_num_steps = n_steps[1]
    seq = [1, ]  # any sequence starts with 1
    idx = 1 # how to get to 1 (from 2, 2 or 3?)

    while idx < n:
        next_item = interm[idx]
        seq.append(next_item)
        idx = next_item

    return opt_num_steps, seq

if __name__ == '__main__':
    n = int(input())

    min_num_operations, sequence = prim_calc(n)

    print(min_num_operations)
    print(*sequence, sep=' ')

