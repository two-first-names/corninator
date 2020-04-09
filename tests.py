#!/usr/bin/env python
import unittest
from crossing import cost_for_crossing, can_cross, result
from exceptions import InvalidUsage

class Tests(unittest.TestCase):
    def test_corn_crossing_price_for_minus_one_bag(self):
        with self.assertRaises(InvalidUsage):
            cost_for_crossing(-1)

    def test_corn_crossing_price_for_zero_bags(self):
        self.assertEqual(cost_for_crossing(0), 0)

    def test_corn_crossing_price_for_one_bag(self):
        self.assertEqual(cost_for_crossing(1), 0.25)

    def test_corn_crossing_price_for_two_bags(self):
        self.assertEqual(cost_for_crossing(2), 0.75)

    def test_corn_crossing_price_for_three_bags(self):
        self.assertEqual(cost_for_crossing(3), 1.25)
    
    def test_message_for_one_bag_one_goose(self):
        self.assertEqual(result(1, 1), 'Your selection of 1 goose and 1 bag will result in NO LOSS at a total cost of: £0.75')

    def test_message_for_two_bags_one_goose(self):
        self.assertEqual(result(2, 1), 'Your selection of 1 goose and 2 bags will result in NO LOSS at a total cost of: £1.75')

    def test_message_for_one_bags_two_geese(self):
        self.assertEqual(result(1, 2), 'Your selection of 2 geese and 1 bag will result in NO LOSS at a total cost of: £1.75')

    def test_message_for_zero_bags_zero_geese(self):
        self.assertEqual(result(0, 0), 'Your selection of 0 geese and 0 bag(s) will result in NO LOSS at a total cost of: £0')

    def test_message_for_three_bags_zero_geese(self):
        self.assertEqual(result(3, 0), 'Your selection of 0 geese and 3 bag will result in NO LOSS at a total cost of: £1.25')

    def test_message_for_one_bags_three_geese(self):
        self.assertEqual(result(1, 3), 'Your selection of 1 bag and 3 geese will result in A LOSS.')


if __name__ == '__main__':
    unittest.main()
