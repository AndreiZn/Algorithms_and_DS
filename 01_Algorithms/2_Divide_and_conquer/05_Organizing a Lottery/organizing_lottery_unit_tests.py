import unittest
from organizing_lottery import points_cover, points_cover_naive


class PointsAndSegments(unittest.TestCase):
    def test_small(self):
        for starts, ends, points in [
            ([0, 7], [5, 10], [1, 6, 11]),
            ([-10], [10], [-100, 100, 0])
        ]:
            self.assertEqual(points_cover(list(starts), list(ends), list(points)),
                             points_cover_naive(starts, ends, points))

    #def test_random(self):


    def test_large(self):
        for (starts, ends, points, answer) in [
            ([0] * 50000, [1] * 50000, list(range(2,40002)), [0]*40000)
        ]:
            self.assertEqual(
                points_cover(list(starts), list(ends), list(points)),
                answer
            )


if __name__ == '__main__':
    unittest.main()
