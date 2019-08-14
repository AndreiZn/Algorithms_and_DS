# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    s, i = 0, 1
    n = len(stops)

    t = list(stops)
    stops = [0 for _ in range(n+2)]
    stops[1:n+1] = t
    stops[n+1] = d

    while i <= n:

        [l, r] = [stops[i-1], stops[i-1] + m]

        if stops[i] > r:
            return -1

        while i<=n and stops[i]<=r:
            i = i + 1

        if stops[i] > r:
            s = s + 1

    if stops[n+1] - stops[n] >  m:
        return -1

    return s


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
