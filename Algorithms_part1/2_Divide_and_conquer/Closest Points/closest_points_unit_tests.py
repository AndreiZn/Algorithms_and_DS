import unittest
from closest_points import minimum_distance_squared, minimum_distance_squared_naive, Point
from random import randint


class ClosestPoints(unittest.TestCase):
    def test_small(self):
        for points in (
            [Point(4, 4), Point(-2, -2), Point(-3, -4), Point(-1, 3), Point(2, 3), Point(-4, 0),
             Point(1, 1), Point(-1, -1), Point(3, -1), Point(-4, 2), Point(-2, 4)],

        ):
            self.assertAlmostEqual(minimum_distance_squared(points),
                                   minimum_distance_squared_naive(points),
                                   delta=1e-03)

    def test_random(self):
        for n in [2, 5, 10, 100]:
            for max_value in [1, 2, 3, 1000]:
                points = []
                for _ in range(n):
                    x = randint(-max_value, max_value)
                    y = randint(-max_value, max_value)
                    points.append(Point(x, y))
                self.assertAlmostEqual(minimum_distance_squared(points),
                                       minimum_distance_squared_naive(points),
                                       delta=1e-03)



if __name__ == '__main__':
    unittest.main()
