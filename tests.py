#!/usr/bin/env python
import unittest
from crossing import cost_for_crossing, result, journey
from exceptions import InvalidUsage

class Tests(unittest.TestCase):
    def test_result_for_minus_one_bag(self):
        with self.assertRaises(InvalidUsage):
            result(-1, 0)

    def test_result_for_minus_one_geese(self):
        with self.assertRaises(InvalidUsage):
            result(0, -1)
    
    def test_message_for_one_bag_one_goose(self):
        self.assertEqual(result(1, 1), 'Your selection of 1 bag(s) and 1 geese will result in NO LOSS at a total cost of: £0.75')

    def test_message_for_two_bags_one_goose(self):
        self.assertEqual(result(2, 1), 'Your selection of 2 bag(s) and 1 geese will result in NO LOSS at a total cost of: £1.75')

    def test_message_for_one_bags_two_geese(self):
        self.assertEqual(result(1, 2), 'Your selection of 1 bag(s) and 2 geese will result in NO LOSS at a total cost of: £1.75')

    def test_message_for_zero_bags_zero_geese(self):
        self.assertEqual(result(0, 0), 'Your selection of 0 bag(s) and 0 geese will result in NO LOSS at a total cost of: £0.00')

    def test_message_for_three_bags_zero_geese(self):
        self.assertEqual(result(3, 0), 'Your selection of 3 bag(s) and 0 geese will result in NO LOSS at a total cost of: £1.25')

    def test_message_for_one_bags_three_geese(self):
        self.assertEqual(result(1, 3), 'Your selection of 1 bag(s) and 3 geese will result in A LOSS.')

    def test_message_for_four_bags_one_geese(self):
        self.assertEqual(result(4, 1), 'Your selection of 4 bag(s) and 1 geese will result in A LOSS.')

    def test_message_for_two_bags_two_geese(self):
        self.assertEqual(result(2, 2), 'Your selection of 2 bag(s) and 2 geese will result in A LOSS.')

    def test_journey_for_one_bag_one_geese(self):
        self.assertEqual(journey(1,1), 'Take bag across, return, take goose across')

    def test_journey_for_two_bags_one_geese(self):
        self.assertEqual(journey(2, 1), 'Take goose across, return, take bag across, return with goose, take bag across, return, take goose across')

    def test_journey_for_one_bag_two_geese(self):
        self.assertEqual(journey(1, 2), 'Take bag across, return, take goose across, return with bag, take geese across, return, take bag across')
    
    def test_journey_for_zero_bags_zero_geese(self):
        self.assertEqual(journey(0, 0), 'No journey taken')

    def test_journey_for_3_bags_zero_geese(self):
        self.assertEqual(journey(3, 0), 'Take bag across, return, take bag across, return, take bag across')

    def test_journey_for_4_bags_zero_geese(self):
        self.assertEqual(journey(4, 0), 'Take bag across, return, take bag across, return, take bag across, return, take bag across')

    def test_journey_for_1_bags_three_geese(self):
        self.assertEqual(journey(1, 3), 'No journey taken')












if __name__ == '__main__':
    unittest.main()
