# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt, inf


Point = namedtuple('Point', 'x y')


def distance(first_point, second_point):
    return sqrt((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance(p, q))

    return min_distance_squared


def get_sec_coord(p):
    return p.y


def minimum_distance_squared(points):

    num_points = len(points)
    if num_points < 4:
        return minimum_distance_squared_naive(points)

    sorted_points_by_x = sorted(points)
    m = int(num_points / 2)
    next_el_idx, next_el = m-1, sorted_points_by_x[m-1].x
    while next_el == sorted_points_by_x[m-1].x and next_el_idx < num_points:
        next_el = sorted_points_by_x[next_el_idx].x
        next_el_idx = next_el_idx + 1
    sep_point_x = sorted_points_by_x[next_el_idx-1].x + 0.5*(next_el - sorted_points_by_x[next_el_idx-1].x)

    points_sorted_left, points_sorted_right =  sorted_points_by_x[:m], sorted_points_by_x[m:]
    if len(points_sorted_left) < 2:
        points_sorted_left, points_sorted_right =  sorted_points_by_x[:m+1], sorted_points_by_x[m+1:]
    if len(points_sorted_right) < 2:
        points_sorted_left, points_sorted_right =  sorted_points_by_x[:m-1], sorted_points_by_x[m-1:]

    d1, d2 = minimum_distance_squared(points_sorted_left), minimum_distance_squared(points_sorted_right)
    d = min([d1, d2])
    stripe = [points[i] for i in range(num_points) if abs(points[i].x - sep_point_x) <= d]
    stripe_sorted = sorted(stripe, key = get_sec_coord)
    d3 = inf
    n_points_in_stripe = len(stripe)

    for idx in range(n_points_in_stripe):
        # furthest point's idx to check:
        f_idx = min([idx+7, n_points_in_stripe-1])
        for j in range(idx+1, f_idx+1):
            p_1, p_2 = stripe_sorted[idx], stripe_sorted[j]
            cur_d = distance(p_1, p_2)
            if cur_d < d3:
                d3 = cur_d

    return min([d, d3])

if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(minimum_distance_squared(input_points)))
