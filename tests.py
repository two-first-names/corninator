import unittest
from crossing import cost_for_crossing
from exceptions import InvalidUsage


class Tests(unittest.TestCase):
    def test_corn_crossing_price_for_minus_one_bag(self):
        with self.assertRaises(InvalidUsage):
            cost_for_crossing(-1)

    def test_corn_crossing_price_for_zero_bag(self):
        self.assertEqual(cost_for_crossing(0), 0)

    def test_corn_crossing_price_for_one_bag(self):
        self.assertEqual(cost_for_crossing(1), 0.25)

    def test_corn_crossing_price_for_two_bags(self):
        self.assertEqual(cost_for_crossing(2), 0.75)

    def test_corn_crossing_price_for_three_bags(self):
        self.assertEqual(cost_for_crossing(3), 1.25)
