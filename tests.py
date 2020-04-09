import unittest
from crossing import cost_for_crossing


class Tests(unittest.TestCase):
    def test_corn_crossing_price_for_one_bag(self):
        assert cost_for_crossing(1) == 0.25

    def test_corn_crossing_price_for_two_bags(self):
        assert cost_for_crossing(2) == 0.75

    def test_corn_crossing_price_for_three_bags(self):
        assert cost_for_crossing(3) == 1.25
