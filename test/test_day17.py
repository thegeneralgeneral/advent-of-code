import unittest
from day17 import get_all_combinations, PUZZLE_CONTAINERS, get_all_combinations_of_min_length

class Day17_getAllCombinationsTests(unittest.TestCase):
    
    def test_base(self):
        example_containers = [10, 5, 5]
        amount = 10
        result = list(get_all_combinations(example_containers, amount))
        self.assertEqual([[10], [5, 5]], result)
    
    def test_example(self):
        example_containers = [20, 15, 10, 5, 5]
        expected_results = [
            [15, 10], [20, 5], [20, 5], [15, 5, 5]
        ]
        amount = 25
        result = list(get_all_combinations(example_containers, 25))
        self.assertEqual(4, len(result))
        self.assertTrue(all([i in result for i in expected_results]))
    
    def test_puzzle(self):
        containers = PUZZLE_CONTAINERS
        amount = 150
        result = list(get_all_combinations(containers, amount))
        # print len(result)
        self.assertEqual(654, len(result))

class Day17_getCombinationsOfMinLengthTests(unittest.TestCase):
    
    def test_example(self):
        example_containers = [20, 15, 10, 5, 5]
        expected_results = [
            [15, 10], [20, 5], [20, 5]
        ]
        amount = 25
        result = list(get_all_combinations_of_min_length(example_containers, 25))
        print result
        self.assertEqual(3, len(result))
        self.assertTrue(all([i in result for i in expected_results]))
    
    def test_puzzle(self):
        combs = get_all_combinations_of_min_length(PUZZLE_CONTAINERS, 150)
        self.assertEqual(57, len(combs))