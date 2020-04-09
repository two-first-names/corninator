#!/usr/bin/env python
import unittest
from crossing import cost_for_crossing, result
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
        self.assertEqual(result(1, 1), 'Your selection of 1 bag(s) and 1 geese will result in NO LOSS at a total cost of: £0.75')

    def test_message_for_two_bags_one_goose(self):
        self.assertEqual(result(2, 1), 'Your selection of 2 bag(s) and 1 geese will result in NO LOSS at a total cost of: £1.75')

    def test_message_for_one_bags_two_geese(self):
        self.assertEqual(result(1, 2), 'Your selection of 1 bag(s) and 2 geese will result in NO LOSS at a total cost of: £1.75')

    def test_message_for_zero_bags_zero_geese(self):
        self.assertEqual(result(0, 0), 'Your selection of 0 bag(s) and 0 geese will result in NO LOSS at a total cost of: £0')

    def test_message_for_three_bags_zero_geese(self):
        self.assertEqual(result(3, 0), 'Your selection of 3 bag(s) and 0 geese will result in NO LOSS at a total cost of: £1.25')

    def test_message_for_one_bags_three_geese(self):
        self.assertEqual(result(1, 3), 'Your selection of 1 bag(s) and 3 geese will result in A LOSS.')

    def test_message_for_four_bags_one_geese(self):
        self.assertEqual(result(4, 1), 'Your selection of 4 bag(s) and 1 geese will result in A LOSS.')

    def test_message_for_two_bags_two_geese(self):
        self.assertEqual(result(2, 2), 'Your selection of 2 bag(s) and 2 geese will result in A LOSS.')




if __name__ == '__main__':
    unittest.main()
