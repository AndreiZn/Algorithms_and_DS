from sys import stdin

def money_split(money, denominations):
    #print(money)
    arr = [0] * (money + 1)
    for i in range(1, money+1):
        vals = [1e5] * len(denominations)
        for j, d in enumerate(denominations):
            if i >= d:
                vals[j] = arr[i-d] + 1
        arr[i] = min(vals)

    return arr[-1]

if __name__ == '__main__':
    money = int(input())

    min_num_coins = money_split(money, [1,3,4])

    print(min_num_coins)

