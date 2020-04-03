# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    n_10 = money // 10
    n_5 = (money % 10) // 5
    n_1 = (money % 10) % 5
    return n_10 + n_5 + n_1

if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
